#!/usr/bin/env python3
"""Validate structured handoff artifacts used by scientific-paper-figures."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


RULE_CLASSES = {"文献/官方标准", "Skill 归纳规则", "领域模板"}
REQUIRED_FIELDS = {
    "figure_plan": {
        "artifact_type",
        "version",
        "paper_profile",
        "claims",
        "figures",
        "storyboard",
        "open_questions",
        "provenance",
    },
    "figure_spec": {
        "artifact_type",
        "version",
        "figure_id",
        "claim",
        "evidence_sources",
        "layout",
        "panels",
        "visual_system",
        "renderer",
        "outputs",
        "open_questions",
        "provenance",
    },
    "qa_report": {
        "artifact_type",
        "version",
        "figure_id",
        "checks",
        "unresolved",
        "verdict",
        "provenance",
    },
}


def require_fields(value: Any, fields: set[str], path: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        errors.append(f"{path} must be an object")
        return
    missing = sorted(fields - value.keys())
    if missing:
        errors.append(f"{path} missing fields: {', '.join(missing)}")


def require_list(value: Any, path: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list):
        errors.append(f"{path} must be a list")
        return []
    return value


def validate_provenance(value: Any, errors: list[str]) -> None:
    require_fields(value, {"rule_classes", "official_sources"}, "provenance", errors)
    if not isinstance(value, dict):
        return

    classes = require_list(value.get("rule_classes"), "provenance.rule_classes", errors)
    if set(classes) != RULE_CLASSES or len(classes) != len(RULE_CLASSES):
        errors.append(
            "provenance.rule_classes must contain exactly: "
            + ", ".join(sorted(RULE_CLASSES))
        )

    for index, source in enumerate(
        require_list(value.get("official_sources"), "provenance.official_sources", errors)
    ):
        path = f"provenance.official_sources[{index}]"
        require_fields(source, {"title", "url", "scope"}, path, errors)
        if not isinstance(source, dict):
            continue
        url = source.get("url")
        if not isinstance(url, str) or not url.startswith("https://"):
            errors.append(f"{path}.url must be an https URL")
        for field in ("title", "scope"):
            if not isinstance(source.get(field), str) or not source[field].strip():
                errors.append(f"{path}.{field} must be a non-empty string")


def validate_rule_classes(value: Any, path: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        if "rule_class" in value and value["rule_class"] not in RULE_CLASSES:
            errors.append(
                f"{path}.rule_class must be one of: {', '.join(sorted(RULE_CLASSES))}"
            )
        for key, child in value.items():
            validate_rule_classes(child, f"{path}.{key}", errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            validate_rule_classes(child, f"{path}[{index}]", errors)


def validate_plan(data: dict[str, Any], errors: list[str]) -> None:
    claims = require_list(data.get("claims"), "claims", errors)
    figures = require_list(data.get("figures"), "figures", errors)
    require_list(data.get("storyboard"), "storyboard", errors)
    require_list(data.get("open_questions"), "open_questions", errors)

    claim_ids: set[str] = set()
    for index, claim in enumerate(claims):
        path = f"claims[{index}]"
        require_fields(claim, {"id", "text", "evidence_ids", "status"}, path, errors)
        if isinstance(claim, dict) and isinstance(claim.get("id"), str):
            claim_ids.add(claim["id"])
        if isinstance(claim, dict):
            require_list(claim.get("evidence_ids"), f"{path}.evidence_ids", errors)

    figure_ids: set[str] = set()
    for index, figure in enumerate(figures):
        path = f"figures[{index}]"
        require_fields(
            figure,
            {
                "id",
                "question",
                "claim_ids",
                "medium",
                "placement",
                "status",
                "required_inputs",
                "caption_claim",
            },
            path,
            errors,
        )
        if not isinstance(figure, dict):
            continue
        figure_id = figure.get("id")
        if isinstance(figure_id, str):
            if figure_id in figure_ids:
                errors.append(f"duplicate figure id: {figure_id}")
            figure_ids.add(figure_id)
        linked_claims = require_list(figure.get("claim_ids"), f"{path}.claim_ids", errors)
        for claim_id in linked_claims:
            if claim_id not in claim_ids:
                errors.append(f"{path}.claim_ids references unknown claim: {claim_id}")
        require_list(figure.get("required_inputs"), f"{path}.required_inputs", errors)


def validate_spec(data: dict[str, Any], errors: list[str]) -> None:
    require_list(data.get("evidence_sources"), "evidence_sources", errors)
    require_list(data.get("panels"), "panels", errors)
    require_list(data.get("outputs"), "outputs", errors)
    require_list(data.get("open_questions"), "open_questions", errors)
    for field in ("layout", "visual_system", "renderer"):
        if not isinstance(data.get(field), dict):
            errors.append(f"{field} must be an object")


def validate_qa(data: dict[str, Any], errors: list[str]) -> None:
    checks = require_list(data.get("checks"), "checks", errors)
    require_list(data.get("unresolved"), "unresolved", errors)
    allowed_statuses = {"pass", "fail", "pending", "not_applicable"}
    for index, check in enumerate(checks):
        path = f"checks[{index}]"
        require_fields(check, {"category", "name", "status", "evidence"}, path, errors)
        if isinstance(check, dict) and check.get("status") not in allowed_statuses:
            errors.append(f"{path}.status must be one of {sorted(allowed_statuses)}")
    if data.get("verdict") not in {
        "ready_for_requested_use",
        "provisional",
        "blocked",
    }:
        errors.append("verdict must be ready_for_requested_use, provisional, or blocked")


def validate(data: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["artifact root must be an object"]

    artifact_type = data.get("artifact_type")
    if artifact_type not in REQUIRED_FIELDS:
        return [
            "artifact_type must be one of: " + ", ".join(sorted(REQUIRED_FIELDS))
        ]

    require_fields(data, REQUIRED_FIELDS[artifact_type], "artifact", errors)
    validate_provenance(data.get("provenance"), errors)
    validate_rule_classes(data, "artifact", errors)

    if artifact_type == "figure_plan":
        validate_plan(data, errors)
    elif artifact_type == "figure_spec":
        validate_spec(data, errors)
    else:
        validate_qa(data, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path, help="Path to a JSON artifact")
    args = parser.parse_args()

    try:
        data = json.loads(args.artifact.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read valid JSON: {exc}")
        return 1

    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: valid {data['artifact_type']} v{data['version']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
