import importlib.util
import sys
import tempfile
import textwrap
import unittest
from datetime import date
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "content_quality_audit.py"
SPEC = importlib.util.spec_from_file_location("content_quality_audit", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {MODULE_PATH}")
content_quality_audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = content_quality_audit
SPEC.loader.exec_module(content_quality_audit)


class ContentQualityAuditTests(unittest.TestCase):
    def write_article(self, body: str) -> Path:
        temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(temporary_directory.cleanup)
        article = Path(temporary_directory.name) / "article.md"
        article.write_text(textwrap.dedent("\n" + body).lstrip(), encoding="utf-8")
        return article

    def test_flags_future_material_claim_and_missing_sources(self):
        article = self.write_article(
            """---
            title: \"Future rate claim\"
            date: 2026-08-20
            ---

            Rates rose 12.5% in December 2026.
            """
        )

        result = content_quality_audit.audit_file(article, today=date(2026, 8, 23))

        self.assertIn("future_claim", result.issue_codes)
        self.assertIn("missing_sources", result.issue_codes)

    def test_accepts_visible_source_list_for_supported_quantitative_guide(self):
        article = self.write_article(
            """---
            title: \"Supported guide\"
            date: 2026-08-20
            sources:
              - https://www.eia.gov/electricity/monthly/
            ---

            This worked example uses 900 kWh at $0.15 per kWh.

            ## Sources
            - [U.S. Energy Information Administration](https://www.eia.gov/electricity/monthly/)
            """
        )

        result = content_quality_audit.audit_file(article, today=date(2026, 8, 23))

        self.assertNotIn("missing_sources", result.issue_codes)
        self.assertNotIn("future_claim", result.issue_codes)


if __name__ == "__main__":
    unittest.main()
