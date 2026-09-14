"""Acquire the user-selected source formats without transforming raw data.

Run from any directory. Existing downloads are checksum-verified and skipped.
A failed transfer leaves no final dataset file. No GIS analysis is performed.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import zipfile

import requests

ROOT = Path(__file__).resolve().parents[1]
VANCOUVER = ['poles', 'conduits', 'junction-boxes', 'service-panels', 'abandoned-conduits']
DNV = ['LgtStreetLightPoles', 'LgtStreetLightConduit', 'LgtStreetLightFittings']


def checksum(path):
    with path.open('rb') as stream:
        digest = hashlib.sha256()
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
        return digest.hexdigest()


def acquire(municipality, identifier, url, suffix, params=None):
    directory = ROOT / 'data' / 'raw' / municipality
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / (identifier + suffix)
    record = directory / (target.name + '.acquisition.json')
    if target.exists():
        if not record.exists() or json.loads(record.read_text())['sha256'] != checksum(target):
            raise RuntimeError(f'Existing file lacks matching acquisition evidence: {target}')
        print(f'Verified existing download: {target.name}', flush=True)
        return
    partial = target.with_name(target.name + '.part')
    if partial.exists() or record.exists():
        raise RuntimeError(f'Incomplete prior acquisition requires review: {target}')
    try:
        with requests.get(url, params=params, stream=True, timeout=(20, 180)) as response:
            response.raise_for_status()
            evidence = {
                'source_id': identifier, 'municipality': municipality,
                'requested_url': response.request.url, 'final_url': response.url,
                'redirects': [{'url': h.url, 'status': h.status_code} for h in response.history],
                'parameters': params or {}, 'http_status': response.status_code,
                'response_headers': {key: response.headers.get(key) for key in
                                     ['Content-Type', 'Content-Length', 'ETag', 'Last-Modified']},
                'filters': 'None', 'pagination': 'None; complete export/archive request',
                'requested_crs': 'EPSG:4326' if municipality == 'vancouver' else 'Original FGDB CRS; not selected or changed',
                'local_path': str(target.relative_to(ROOT)),
            }
            with partial.open('xb') as stream:
                for chunk in response.iter_content(1024 * 1024):
                    stream.write(chunk)
        if municipality == 'vancouver':
            with partial.open() as stream:
                content = json.load(stream)
            if content.get('type') != 'FeatureCollection' or not isinstance(content.get('features'), list):
                raise ValueError('Response is not a GeoJSON FeatureCollection')
            evidence['feature_count'] = len(content['features'])
            evidence['declared_crs'] = content.get('crs')
        else:
            with zipfile.ZipFile(partial) as archive:
                if archive.testzip() is not None:
                    raise ValueError('ZIP integrity check failed')
                members = archive.namelist()
                if not any('.gdb/' in n.lower() for n in members):
                    raise ValueError('ZIP contains no FGDB directory')
                evidence['archive_members'] = members
        evidence.update(downloaded_at_utc=datetime.now(timezone.utc).isoformat(),
                        bytes=partial.stat().st_size, sha256=checksum(partial))
        partial.rename(target)
        record.write_text(json.dumps(evidence, indent=2) + '\n')
        print(f'Downloaded {target.name}: {evidence["bytes"]:,} bytes', flush=True)
    finally:
        if partial.exists():
            partial.unlink()


def main():
    for category in VANCOUVER:
        identifier = 'street-lighting-' + category
        acquire('vancouver', identifier,
                f'https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/{identifier}/exports/geojson',
                '.geojson', {'epsg': '4326'})
    for identifier in DNV:
        acquire('dnv', identifier,
                f'https://geoweb.dnv.org/Products/Data/FGDB/{identifier}_fgdb.zip', '_fgdb.zip')


if __name__ == '__main__':
    main()
