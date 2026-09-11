# Paper Figure Planner

Use this layer to decide what the paper should show before designing individual figures.

## Intake and evidence status

Record only what has been inspected:

- manuscript or supplied sections;
- research question and claimed contributions;
- methods, datasets, experiments, and available results;
- target audience, venue, article type, stage, page/figure limits;
- existing figures/tables and source-data paths;
- requested scope: outline, full plan, or downstream rendering.

Assign each input one status: `verified`, `author-stated`, `inferred`, or `missing`. An inference may guide a provisional plan but cannot become a factual figure label.

## 1. Classify the paper

[Skill-Derived Heuristic] Choose the closest logic, allowing hybrids:

| Paper logic | Typical evidence chain |
|---|---|
| Method/model | problem → method → primary comparison → mechanism/ablation → robustness |
| Empirical/observational | setting/data → descriptive pattern → identification/model → estimate → heterogeneity/robustness |
| Experimental | hypothesis → design → manipulation/check → primary outcome → mechanism/replication |
| Resource/dataset/tool | need → construction → quality/coverage → benchmark/use case → limitations |
| Review/conceptual | scope → taxonomy/framework → evidence landscape → gaps/agenda |

This classification is a planning lens, not a journal taxonomy.

## 2. Build a Claim–Evidence Map

[Literature/Official Standard] Start from the message and audience before drawing; PLOS frames these as the first two figure-design decisions. See [Ten Simple Rules for Better Figures](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833).

[Skill-Derived Heuristic] Create one row per claim:

| Claim ID | Claim | Required evidence | Available evidence | Status | Candidate medium |
|---|---|---|---|---|---|
| C1 | Testable sentence | result/method needed | inspected source | supported/partial/missing | text/table/figure |

Do not create a figure merely because a result exists. Every candidate visual must either support a claim or clarify a method needed to assess one.

## 3. Decide Text vs Table vs Figure

[Skill-Derived Heuristic] Use:

- **Text** for a few values or a simple fact without a pattern to inspect.
- **Table** when exact values, many fields, or lookup/comparison precision is primary.
- **Figure** when shape, trend, distribution, relationship, spatial structure, uncertainty, mechanism, or workflow is primary.
- **Both** only when the figure exposes a pattern and the table supplies necessary exact values without duplicating the same reading task.

## 4. Create the Figure Inventory

For every candidate record:

- ID and one-sentence reader question;
- supported claim IDs;
- evidence/source-data IDs and evidence status;
- visual type and why it fits the comparison;
- planned panels;
- caption claim;
- Main/Appendix/omit status with reason;
- target width/aspect ratio if known;
- required inputs and unresolved decisions.

[Skill-Derived Heuristic] Do not prescribe a universal figure count. Generate enough candidates to cover the claim map, then merge, move, or remove them.

## 5. Main text vs Appendix

Place in **Main** when the item is needed to understand the contribution, evaluate the primary evidence, or test a central alternative explanation.

Place in **Appendix/Supplement** when it provides implementation detail, extended diagnostics, secondary subgroups, full grids, additional examples, or robustness that supports but does not carry the main argument.

Omit or merge when removing the item does not weaken the paper's argument, the visual duplicates another item, or its evidence is too weak for the claimed role.

Venue limits override these heuristics only after the exact official instruction is verified.

## 6. Build the Figure Storyboard

[Literature/Official Standard] The American Physiological Society manuscript-development tutorial recommends organizing potential figures/tables around their main messages and reordering them into a coherent scientific story. See [Publishing Particulars, Part 2](https://journals.physiology.org/doi/full/10.1152/ajpregu.00267.2022).

[Skill-Derived Heuristic] Order items by dependency, not by the time analyses were run. A common sequence is:

1. orientation or essential setup;
2. primary evidence;
3. decisive comparison;
4. mechanism or ablation;
5. robustness, boundary conditions, or generalization.

Run the caption-only test: reading figure IDs, claim titles, and captions in sequence should reveal the paper's research object, method, central evidence, and credibility checks.

## Missing information policy

When the manuscript, data, or venue is incomplete:

1. produce the strongest provisional Claim–Evidence Map supported by supplied material;
2. mark all inferred or missing evidence explicitly;
3. avoid fixed counts and venue-specific dimensions unless labeled provisional;
4. return a prioritized missing-input manifest;
5. stop at planning if rendering would require invented evidence.

## Planner output

Deliver a concise human-readable plan and, for multi-figure work, a `figure_plan` JSON that follows [artifact-contracts.md](artifact-contracts.md). Validate it before handoff.
