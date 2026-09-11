# Structured artifact contracts

These contracts make Planner → Designer → Renderer handoffs explicit. Use JSON for multi-figure or file-producing tasks; concise Markdown is sufficient for a small planning-only request.

## Shared rules

Every artifact includes:

- `artifact_type` and `version`;
- `provenance.rule_classes` containing exactly the three supported rule classes;
- `provenance.official_sources`, each with title, HTTPS URL, and scope;
- explicit open questions or unresolved issues;
- no invented values disguised as observations.

When a field encodes a normative decision rather than a factual claim, give the containing object a `rule_class` value or document the class in an adjacent machine-readable policy field. Official and heuristic values must not share an unlabeled object.

The required rule-class strings are:

```json
["文献/官方标准", "Skill 归纳规则", "领域模板"]
```

## `figure_plan` v1.0

Required top-level fields:

```text
artifact_type, version, paper_profile, claims, figures,
storyboard, open_questions, provenance
```

Each claim contains `id`, `text`, `evidence_ids`, and `status`.

Each figure contains:

```text
id, question, claim_ids, medium, placement, status,
required_inputs, caption_claim
```

Recommended optional fields: `panels`, `width`, `aspect_ratio`, `reference_assets`, `journal_rules_pending`, and `reason`.

## `figure_spec` v1.0

Required top-level fields:

```text
artifact_type, version, figure_id, claim, evidence_sources,
layout, panels, visual_system, renderer, outputs,
open_questions, provenance
```

For data-backed panels, include `variables`, `units`, `sample_unit`, `uncertainty`, `missingness`, `transformations`, `scales`, and `forbidden_claims` where applicable.

For schematic panels, include `nodes`, typed `edges`, reading order, formula placement, and source-of-truth references.

## `qa_report` v1.0

Required top-level fields:

```text
artifact_type, version, figure_id, checks, unresolved,
verdict, provenance
```

Each check contains `category`, `name`, `status`, and `evidence`. Use `pass`, `fail`, `pending`, or `not_applicable`.

Allowed verdicts:

- `ready_for_requested_use`;
- `provisional`;
- `blocked`.

An automated validator may establish structural validity; it cannot by itself set `ready_for_requested_use` without rendered inspection and scientific review.

## Examples

- `assets/figure-plan.example.json`
- `assets/figure-spec.example.json`
- `assets/qa-report.example.json`

Validate any artifact with:

```powershell
python scripts/validate_figure_artifact.py path/to/artifact.json
```
