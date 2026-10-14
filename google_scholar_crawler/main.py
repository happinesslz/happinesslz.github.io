"""Fetch the public Google Scholar profile's All-time citation metrics."""

import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class StatsTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.rows = []
        self.row = None
        self.cell = None

    def handle_starttag(self, tag, attrs):
        if tag == "table" and dict(attrs).get("id") == "gsc_rsb_st":
            self.in_table = True
        if not self.in_table:
            return
        if tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self.cell = []

    def handle_data(self, data):
        if self.in_table and self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if not self.in_table:
            return
        if tag in ("td", "th") and self.cell is not None:
            if self.row is not None:
                self.row.append(" ".join("".join(self.cell).split()))
            self.cell = None
        elif tag == "tr" and self.row is not None:
            self.rows.append(self.row)
            self.row = None
        elif tag == "table":
            self.in_table = False


def parse_stats(html):
    parser = StatsTableParser()
    parser.feed(html)
    rows = parser.rows
    if not rows or "All" not in rows[0]:
        raise ValueError("Google Scholar's All-time statistics table is missing")
    column = rows[0].index("All")
    labels = {"Citations": "citedby", "h-index": "hindex", "i10-index": "i10index"}
    stats = {}
    for row in rows[1:]:
        if not row or row[0] not in labels:
            continue
        key = labels[row[0]]
        if key in stats or len(row) <= column:
            raise ValueError("Duplicate or incomplete Google Scholar metric")
        value = row[column]
        if not re.fullmatch(r"(?:[0-9]+|[0-9]{1,3}(?:,[0-9]{3})+)", value):
            raise ValueError("Invalid Google Scholar metric: " + key)
        stats[key] = int(value.replace(",", ""))
    if set(stats) != set(labels.values()):
        raise ValueError("Google Scholar did not return all three metrics")
    if stats["hindex"] > stats["citedby"] or stats["i10index"] > stats["citedby"]:
        raise ValueError("Inconsistent Google Scholar metrics")
    return stats


def fetch_profile(url):
    request = Request(url, headers={
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
    })
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                encoding = response.headers.get_content_charset() or "utf-8"
                return response.read().decode(encoding, errors="replace")
        except (HTTPError, URLError, TimeoutError) as error:
            # Do not retry access restrictions or rate limits.
            if attempt == 2 or (isinstance(error, HTTPError) and error.code < 500):
                raise
            time.sleep(2 ** attempt)


def update_stats(scholar_id, output):
    if not re.fullmatch(r"[A-Za-z0-9_-]{6,64}", scholar_id):
        raise ValueError("Invalid Google Scholar profile ID")
    source = "https://scholar.google.com/citations?user=" + scholar_id + "&hl=en"
    stats = parse_stats(fetch_profile(source))
    snapshot = {
        "schema_version": 1,
        "scholar_id": scholar_id,
        **stats,
        "source": source,
        "updated": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
    }
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Publish only complete, validated snapshots; failures preserve the old file.
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=output.parent,
                                         prefix=".scholar-", delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(snapshot, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
        temporary.replace(output)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    return snapshot


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scholar-id", default=os.environ.get("GOOGLE_SCHOLAR_ID"))
    parser.add_argument("--output", default="results/gs_data.json")
    args = parser.parse_args()
    if not args.scholar_id:
        parser.error("Set GOOGLE_SCHOLAR_ID or supply --scholar-id")
    stats = update_stats(args.scholar_id, args.output)
    print("Google Scholar: {citedby} citations, h-index {hindex}, i10-index {i10index}".format(**stats))


if __name__ == "__main__":
    main()
