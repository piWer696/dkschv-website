#!/usr/bin/env python3
"""Prüft lokale Paket-Slugs und öffentliche DKSchV-Linkziele rein lesend."""
from __future__ import annotations
import argparse
import csv
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent


def metadata(text: str) -> dict[str, str]:
    end = text.find('\n---\n', 4)
    if not text.startswith('---\n') or end < 0:
        return {}
    result = {}
    for line in text[4:end].splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def check_path(item: tuple[str, list[str], bool]) -> dict[str, str]:
    path, sources, locally_present = item
    url = 'https://www.dkschv.ch' + path
    request = Request(url, headers={'User-Agent': 'DKSchV-Content-QA/1.0 (+manual review)'})
    try:
        with urlopen(request, timeout=15) as response:
            response.read(512)
            code = str(response.status)
            final_url = response.url
    except HTTPError as exc:
        code, final_url = str(exc.code), exc.url
    except (URLError, TimeoutError, OSError) as exc:
        code, final_url = 'ERROR: ' + str(exc)[:130], url
    return {'path': path, 'public_status': code, 'final_url': final_url,
            'paket_slug_existiert': 'ja' if locally_present else 'nein',
            'verlinkt_von': '; '.join(sorted(sources))}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    files = sorted((ROOT / 'articles').glob('*.md')) + sorted((ROOT / 'resources').glob('*.md'))
    slugs = {metadata(path.read_text(encoding='utf-8')).get('slug', '') for path in files}
    paths: dict[str, set[str]] = {}
    for file in files:
        text = file.read_text(encoding='utf-8')
        own_slug = metadata(text).get('slug', '')
        if own_slug:
            paths.setdefault(own_slug, set()).add(file.relative_to(ROOT).as_posix() + ' (eigener Slug)')
        for target in re.findall(r'\]\((/[^)\s#]+)', text):
            paths.setdefault(target, set()).add(file.relative_to(ROOT).as_posix())
    items = [(p, sorted(s), p in slugs) for p, s in sorted(paths.items())]
    with ThreadPoolExecutor(max_workers=5) as pool:
        rows = list(pool.map(check_path, items))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=['path', 'public_status', 'final_url',
                                                    'paket_slug_existiert', 'verlinkt_von'])
        writer.writeheader()
        writer.writerows(rows)
    summary: dict[str, int] = {}
    for row in rows:
        summary[row['public_status']] = summary.get(row['public_status'], 0) + 1
    print(f'{len(rows)} eindeutige DKSchV-Pfade geprüft; Statusverteilung: {summary}; Bericht: {args.output}')


if __name__ == '__main__':
    main()
