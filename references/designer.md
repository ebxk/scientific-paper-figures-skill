# Figure Designer

Use this layer to turn one planned figure into a precise, original, evidence-grounded design.

## 1. Create a Figure Card

Record:

- figure ID and manuscript location;
- reader question and one-sentence claim;
- evidence/source IDs and status;
- figure function: framework, data pipeline, model architecture, algorithm flow, mechanism, experimental design, quantitative result, distribution, sensitivity, or graphical summary;
- target medium, width, and language;
- panel jobs and reading order;
- caption draft;
- renderer, editable source, and exports;
- journal rules pending verification.

The function taxonomy is 【Skill 归纳规则】, not a universal standard.

## 2. Analyze a reference figure

Do not start by tracing pixels. Build a Reference Figure Card:

1. paper title, figure number, caption, DOI/URL, screenshot/local path;
2. licence, copyright holder, permission status, and intended reuse type;
3. **Content**: scientific entities, labels, values, and claims;
4. **Structure**: groups, hierarchy, topology, reading path, panel roles, and visual encodings;
5. **Appearance**: typography, palette roles, strokes, shapes, spacing, icon style, and emphasis;
6. transferable principles;
7. elements that must not be copied or inferred;
8. planned transformation and attribution.

### Reuse decision

- **Reuse**: use the original image only when the licence/permission and required attribution permit it.
- **Adapt**: when recognizable expression remains, verify permission/licence and use the required credit language.
- **Independent redesign**: retain only abstract design principles; rebuild composition, labels, assets, and visual expression from the user's evidence.
- **Do not proceed**: if requested reuse would violate rights or attribution requirements.

【文献/官方标准】Open access does not mean attribution-free. Springer Nature states that qualifying OA figure reuse requires correct authorship/citation and publisher identification; subscription content may require formal permission. See [OA figure reuse](https://support.springernature.com/en/support/solutions/articles/6000217050-use-of-an-open-access-figure-or-table) and [author copyright information](https://support.springernature.com/en/support/solutions/articles/6000080095-author-copyrights-information).

## 3. Choose the layout grammar

【Skill 归纳规则】Match layout to the real relationship:

| Logic | Default layout |
|---|---|
| Linear stages, time, input→output | left-to-right when width permits |
| Narrow column, long labels, hierarchy | top-to-bottom |
| Methods/conditions compared | parallel aligned lanes |
| True feedback or iteration | loop with an explicit return edge |
| One core with several inputs/outputs | hub-and-spoke only when centrality is meaningful |
| Containment or scale | nested regions |

Do not draw a loop, hierarchy, or hub merely for visual drama.

### Module hierarchy

【Skill 归纳规则】Try 3–6 primary groups as a first-pass readability heuristic, never as a standard. Prefer two visible hierarchy levels. If more are necessary, use panels or an overview-plus-detail pair.

### Grid and spacing

- align peers to a shared grid;
- make repeated relationships use repeated gaps;
- reserve whitespace to separate groups, not to decorate;
- size regions around their contents;
- judge balance at the final insertion width.

## 4. Define arrow semantics before drawing

Create a small arrow legend when more than one meaning is used. A stable default is:

- solid single arrow = data/computation/causal direction as explicitly defined;
- dashed arrow = optional, conditional, supervisory, or auxiliary relation;
- double arrow = genuine two-way exchange only;
- loop-back arrow = feedback/iteration with a named returned object.

Connect from consistent box-edge anchors. Minimize crossings by changing grouping or placement before adding connector bends. Never let one arrow style silently represent different relations.

## 5. Place formulas and notation

Use a formula inside a module only when it identifies that module or states its core transformation in one short line. Put long derivations in the manuscript or caption. Preserve variable italics, operators, superscripts, subscripts, and symbol definitions across manuscript and figure.

【文献/官方标准】For general mathematical typography principles, see [Ten Simple Rules for Typographically Appealing Scientific Texts](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008458). Apply the target venue's own style when it differs.

## 6. Compose multi-panel figures

Combine panels only when they jointly answer one reader question. Give every panel a job in the evidence chain. Use one dominant panel when the evidence has a dominant claim; equal-sized grids are not mandatory.

【文献/官方标准】Nature's own production guide asks for neat, space-efficient panel arrangement and alphabetical order where possible, with panel sizes driven by content and legibility. This is Nature-specific. See [Building and exporting figure panels](https://research-figure-guide.nature.com/figures/building-and-exporting-figure-panels/).

## 7. Use a restrained scientific visual system

【Skill 归纳规则】Start from:

- white or transparent background;
- one type family;
- consistent stroke and corner treatment;
- neutral context plus 1–3 semantic accents;
- direct labels near evidence;
- no gradient, glow, 3D boxes, heavy shadow, decorative stock icons, banner title, or one-color-per-box styling unless the scientific meaning requires it.

Use color redundantly with labels, shapes, patterns, or line styles. Test the exported result in grayscale and at intended size, while recognizing that grayscale is not a complete accessibility test.

## 8. Caption contract

The caption identifies the question/claim, panels, encodings, units, uncertainty, sample/replicate meaning, abbreviations, and necessary conditions. It must not introduce unsupported results.

【文献/官方标准】PLOS treats captions as essential to explaining how to read a figure. See [Ten Simple Rules for Better Figures](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833).

## Designer output

Deliver the Figure Card, any Reference Figure Card and reuse decision, a panel/layout specification, visual tokens, caption draft, evidence gaps, and journal rules still pending. For rendering, emit a `figure_spec` JSON following [artifact-contracts.md](artifact-contracts.md).
