---
name: scientific-paper-figures
description: Use when planning, designing, reproducing, generating, revising, or auditing figures and tables for research papers, theses, dissertations, preprints, and journal submissions, including figure storyboards, reference-figure analysis, architecture diagrams, data plots, multi-panel figures, captions, and publication artwork QA.
---

# Scientific Paper Figures

## Core principle

Build the visual argument from claims and evidence before choosing a renderer. A figure is ready only when its scientific meaning, provenance, editable source, final-size legibility, and exported file have all been checked.

## Classify every rule

Use these labels in plans, specifications, audits, and recommendations:

- 【文献/官方标准】: directly supported by a linked paper, publisher, journal, or authoritative body. State its scope; a Nature rule is not universal.
- 【Skill 归纳规则】: an operational heuristic synthesized for this skill. Never call it a submission requirement.
- 【领域模板】: a starting pattern for a research domain. Adapt it to the manuscript and evidence.

Every normative list, table, or numeric recommendation must sit under one of these labeled headings or carry an explicit `rule_class` field. A provenance legend by itself is not enough. Do not mix official requirements and heuristics in one unlabeled block.

If a numeric or venue-specific requirement matters, verify the current official page for the exact journal, article type, figure type, and submission stage. If those are unknown, label the choice provisional.

## Route the request

Run only the layers needed by the user's requested scope:

1. **Paper Figure Planner** — for whole-paper planning, figure/table decisions, ordering, or Main/Appendix placement. Read [planner.md](references/planner.md).
2. **Figure Designer** — for a single figure, a reference figure, structure/layout, multi-panel composition, formulas, arrows, captions, or visual critique. Read [designer.md](references/designer.md).
3. **Figure Renderer** — when files or code must be generated, revised, exported, or audited. Read [renderer.md](references/renderer.md).

For cross-layer work, pass structured artifacts forward rather than silently reinterpreting them. Read [artifact-contracts.md](references/artifact-contracts.md) and use the examples in `assets/`.

Read [standards-and-sources.md](references/standards-and-sources.md) when citing standards or setting journal-facing parameters. Read [domain-templates.md](references/domain-templates.md) only for a matching field. Read [reference-skills.md](references/reference-skills.md) when maintaining or extending this skill.

## Non-negotiable gates

- Do not invent data, sample sizes, uncertainty, methods, modules, results, citations, licences, or journal requirements.
- Preserve raw data/images and record filters, exclusions, transformations, smoothing, aggregation, normalization, seeds, and image adjustments.
- If required evidence is missing, deliver a provisional plan/specification plus a missing-input manifest; do not stop at a generic refusal and do not render publishable-looking fake evidence.
- A supplied reference image is evidence about design, not authority for the user's science. Separate content, relationships, and appearance; check licence/permission before reuse or close adaptation.
- Do not claim “publication-ready”, “accessible”, or “journal-compliant” from DPI, a palette, or an automated check alone.
- Preserve the user's requested backend and output scope when feasible. Do not generate files when the user asked only for planning or critique.

## Completion contract

Return the artifacts relevant to the requested layer:

- Planner: Claim–Evidence Map, Figure Inventory, Storyboard, Main/Appendix decisions, evidence gaps, and journal-dependent items.
- Designer: Figure Card, reference-use decision when applicable, layout/arrow/formula/panel specification, caption draft, and visual-system tokens.
- Renderer: editable source, requested exports, data/provenance record, rendered QA report, and unresolved issues.

Validate structured JSON with:

```powershell
python scripts/validate_figure_artifact.py <artifact.json>
```

## Final check

Before declaring completion, inspect the actual rendered output at intended size. Verify scientific accuracy, scales and uncertainty, missingness/exclusions, label and notation consistency, reading order, contrast without color alone, overlaps/clipping, font embedding/editability, physical dimensions, file format, and source traceability.
