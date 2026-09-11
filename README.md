# Scientific Paper Figures

English | [中文](README_CN.md)

An evidence-first Codex skill for planning, designing, rendering, revising, and auditing scholarly figures and tables.

It helps turn scientific claims and evidence into clear visual arguments while preserving provenance, editability, final-size legibility, and journal-specific constraints.

## What it does

- Plans figure and table sets for papers, theses, dissertations, preprints, and journal submissions.
- Designs individual figures, multi-panel layouts, architecture diagrams, data plots, captions, and visual systems.
- Produces or revises editable artwork and exported files when rendering is requested.
- Audits scientific accuracy, visual clarity, accessibility, traceability, and delivery requirements.
- Analyzes reference figures without treating their scientific content as authority for a new manuscript.

## Workflow

The skill routes each request through only the layers it needs:

1. **Paper Figure Planner** — maps claims to evidence, decides which results need figures or tables, and organizes the main-text and appendix story.
2. **Figure Designer** — specifies the structure, panels, arrows, formulas, labels, caption, and visual system for a figure.
3. **Figure Renderer** — generates, revises, exports, or audits the actual files and records the associated data provenance.

Structured artifacts pass between layers so later stages do not silently reinterpret earlier decisions.

## Evidence and quality rules

The skill distinguishes three kinds of guidance:

- `[Literature/Official Standard]` — requirements or guidance supported by a cited paper, publisher, journal, or authoritative body.
- `[Skill-Derived Heuristic]` — operational heuristics synthesized for this skill.
- `[Domain Template]` — domain-specific starting patterns that must be adapted to the manuscript and evidence.

It does not invent data, methods, results, citations, licences, sample sizes, uncertainty, or journal requirements. When evidence is missing, it returns a provisional plan plus a missing-input manifest rather than creating publication-looking fictional evidence.

## Installation

Clone the repository into your Codex skills directory:

```powershell
git clone https://github.com/ebxk/scientific-paper-figures-skill.git "$env:USERPROFILE\.codex\skills\scientific-paper-figures"
```

## Usage

Invoke the skill explicitly in Codex:

```text
Use $scientific-paper-figures to plan the figures for my paper from this manuscript and dataset.
```

Other example requests:

```text
Use $scientific-paper-figures to redesign Figure 2 while preserving the underlying data and claims.
```

```text
Use $scientific-paper-figures to audit these exported figures at their intended publication size.
```

## Structured artifact validation

Example planner, figure-specification, and QA artifacts are provided in [`assets/`](assets/). Validate a structured JSON artifact with:

```powershell
python scripts/validate_figure_artifact.py <artifact.json>
```

## Repository structure

```text
scientific-paper-figures/
├── SKILL.md                  # Skill entry point and routing rules
├── agents/openai.yaml        # Codex interface metadata
├── assets/                   # Example structured artifacts
├── references/               # Planner, designer, renderer, and standards guidance
├── scripts/                  # Artifact validation utility
└── tests/                    # Validator tests
```

## Licence

Released under the [MIT License](https://github.com/ebxk/scientific-paper-figures-skill/blob/main/LICENSE).
