# Google Scholar statistics

The `Sync Google Scholar statistics` GitHub Actions workflow fetches the public
profile every hour at minute 23 (UTC). GitHub may delay scheduled jobs. It also
runs when the crawler or workflow changes, and supports **Run workflow** in the
Actions tab for an immediate refresh.

The crawler reads the **All** column for citations, h-index, and i10-index, validates
the complete response, and publishes `gs_data.json` to the `google-scholar-stats`
branch. It uses the workflow's repository token; no API key is needed. A failed
fetch leaves the previous snapshot intact and marks the workflow as failed.

The homepage fetches this snapshot on each visit. `_data/scholar_stats.json`
provides the initial values before JavaScript loads; the browser also caches the
latest successful snapshot for network failures. Update timestamps are kept
internally for freshness checks, with no cutoff date displayed on the homepage.

Run locally with Python 3.9 or later (standard library only):

```sh
python3 -m unittest discover -s google_scholar_crawler -p 'test_*.py'
python3 google_scholar_crawler/main.py --scholar-id yprv7EsAAAAJ
```

To refresh the initial values committed with the site, add
`--output _data/scholar_stats.json`. Scholar access errors or changes to its HTML
will appear in the workflow logs; they must not replace metrics with zeroes.
