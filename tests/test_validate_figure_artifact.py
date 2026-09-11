import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = SKILL_ROOT / "scripts" / "validate_figure_artifact.py"


def run_validator(payload: dict) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as tmp:
        artifact = Path(tmp) / "artifact.json"
        artifact.write_text(json.dumps(payload), encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(artifact)],
            text=True,
            capture_output=True,
            check=False,
        )


class ValidateFigureArtifactTests(unittest.TestCase):
    def test_accepts_english_rule_classes(self) -> None:
        payload = {
            "artifact_type": "figure_plan",
            "version": "1.0",
            "paper_profile": {},
            "claims": [],
            "figures": [],
            "storyboard": [],
            "open_questions": [],
            "provenance": {
                "rule_classes": [
                    "Literature/Official Standard",
                    "Skill-Derived Heuristic",
                    "Domain Template",
                ],
                "official_sources": [],
            },
        }
        result = run_validator(payload)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_legacy_chinese_rule_classes(self) -> None:
        payload = {
            "artifact_type": "figure_plan",
            "version": "1.0",
            "paper_profile": {},
            "claims": [],
            "figures": [],
            "storyboard": [],
            "open_questions": [],
            "provenance": {
                "rule_classes": [
                    "\u6587\u732e/\u5b98\u65b9\u6807\u51c6",
                    "Skill \u5f52\u7eb3\u89c4\u5219",
                    "\u9886\u57df\u6a21\u677f",
                ],
                "official_sources": [],
            },
        }
        result = run_validator(payload)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("rule_classes", result.stdout)

    def test_accepts_valid_example_artifacts(self) -> None:
        for name in (
            "figure-plan.example.json",
            "figure-spec.example.json",
            "qa-report.example.json",
        ):
            with self.subTest(name=name):
                payload = json.loads(
                    (SKILL_ROOT / "assets" / name).read_text(encoding="utf-8")
                )
                result = run_validator(payload)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_rejects_unknown_artifact_type(self) -> None:
        result = run_validator({"artifact_type": "unknown", "version": "1.0"})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("artifact_type", result.stdout)

    def test_requires_all_three_rule_classes(self) -> None:
        payload = {
            "artifact_type": "figure_plan",
            "version": "1.0",
            "paper_profile": {},
            "claims": [],
            "figures": [],
            "storyboard": [],
            "open_questions": [],
            "provenance": {
                "rule_classes": ["Skill-Derived Heuristic"],
                "official_sources": [],
            },
        }
        result = run_validator(payload)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("rule_classes", result.stdout)

    def test_rejects_official_source_without_https_url(self) -> None:
        payload = {
            "artifact_type": "figure_plan",
            "version": "1.0",
            "paper_profile": {},
            "claims": [],
            "figures": [],
            "storyboard": [],
            "open_questions": [],
            "provenance": {
                "rule_classes": [
                    "Literature/Official Standard",
                    "Skill-Derived Heuristic",
                    "Domain Template",
                ],
                "official_sources": [
                    {"title": "Example", "url": "http://example.com", "scope": "test"}
                ],
            },
        }
        result = run_validator(payload)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("https", result.stdout)

    def test_rejects_unknown_nested_rule_class(self) -> None:
        payload = json.loads(
            (SKILL_ROOT / "assets" / "figure-spec.example.json").read_text(
                encoding="utf-8"
            )
        )
        payload["visual_system"]["rule_class"] = "journal standard"
        result = run_validator(payload)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("rule_class", result.stdout)


if __name__ == "__main__":
    unittest.main()
