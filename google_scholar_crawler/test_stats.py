import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from main import parse_stats, update_stats


PROFILE = """
<table><tr><td>Citations</td><td>99999</td></tr></table>
<table id="gsc_rsb_st">
  <thead><tr><th></th><th>All</th><th>Since 2021</th></tr></thead>
  <tbody>
    <tr><td><a>Citations</a></td><td>2,601</td><td>2565</td></tr>
    <tr><td><a>h-index</a></td><td>18</td><td>17</td></tr>
    <tr><td><a>i10-index</a></td><td>22</td><td>20</td></tr>
  </tbody>
</table>
"""


class StatsTests(unittest.TestCase):
    def test_all_time_column_and_correct_table(self):
        self.assertEqual(parse_stats(PROFILE), {"citedby": 2601, "hindex": 18, "i10index": 22})

    def test_invalid_responses_are_rejected(self):
        for html in (
            "<html>Please complete the CAPTCHA</html>",
            PROFILE.replace("i10-index", "other"),
            PROFILE.replace("2,601", ""),
            PROFILE.replace("2,601", "1,,000"),
            PROFILE.replace("2,601", "-1"),
            PROFILE.replace("2,601", "1"),
        ):
            with self.subTest(html=html), self.assertRaises(ValueError):
                parse_stats(html)

    def test_zero_is_valid(self):
        html = PROFILE.replace("2,601", "0").replace("<td>18</td>", "<td>0</td>")
        html = html.replace("<td>22</td>", "<td>0</td>")
        self.assertEqual(parse_stats(html), {"citedby": 0, "hindex": 0, "i10index": 0})

    def test_failed_fetch_preserves_previous_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "stats.json"
            output.write_text('{"previous": true}\n', encoding="utf-8")
            with patch("main.fetch_profile", side_effect=RuntimeError("Network unavailable")):
                with self.assertRaises(RuntimeError):
                    update_stats("yprv7EsAAAAJ", output)
            self.assertEqual(output.read_text(), '{"previous": true}\n')
            with patch("main.fetch_profile", return_value="CAPTCHA"):
                with self.assertRaises(ValueError):
                    update_stats("yprv7EsAAAAJ", output)
            self.assertEqual(output.read_text(), '{"previous": true}\n')

    def test_successful_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "stats.json"
            with patch("main.fetch_profile", return_value=PROFILE):
                stats = update_stats("yprv7EsAAAAJ", output)
            self.assertEqual(json.loads(output.read_text()), stats)
            self.assertEqual(stats["scholar_id"], "yprv7EsAAAAJ")
            self.assertEqual(stats["citedby"], 2601)
            self.assertTrue(stats["updated"].endswith("Z"))
            self.assertEqual(stats["source"], "https://scholar.google.com/citations?user=yprv7EsAAAAJ&hl=en")


if __name__ == "__main__":
    unittest.main()
