# Reference Skill architecture review

This skill was designed independently after reviewing the following public Skill architectures. The useful ideas are recorded at the pattern level; wording, schemas, scripts, and asset libraries were not copied.

Snapshot review date: 2026-09-11.

| Reference Skill | Architecture idea retained | Deliberate difference in this Skill |
|---|---|---|
| [research-paper-figures](https://github.com/CDUTAKL/research-workflow-kit/tree/main/skills/research-paper-figures) | claim-linked inventory; explicit editable-source/export/QA handoff; missing data yields a spec | generalized beyond one thesis workflow and avoids mandatory Image Gen/draw.io defaults |
| [academic-figure-paper-analyzer lineage](https://github.com/Azhi-ss/academic-figure-skills/tree/main/academic-figure-draft-analyzer) | paper-to-Figure Plan separation; completeness and missing-evidence tracking | integrates Claim–Evidence Map, Main/Appendix, and venue-pending logic into one Planner contract; current upstream folder is `academic-figure-draft-analyzer` |
| [scientific-visualization](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-visualization) | scientific integrity before aesthetics; live journal verification; metadata/render inspection | adds whole-paper planning and reference-figure redesign rather than focusing on data plots |
| [visualization-strategy-and-critique](https://github.com/openai/plugins/blob/main/plugins/build-web-data-visualization/skills/visualization-strategy-and-critique/SKILL.md) | claim-first visual choice; critique lenses; references as principle studies | narrows the scope to scholarly static figures and manuscript evidence chains |
| [Academic Figure Skill](https://github.com/TingxiYu/academic-figure-skill) | figure contract, progressive references, automated QA utilities, final-size inspection | does not bundle a large chart-template atlas or advertise a generic “Nature style” as compliance |
| [academic-figure-workflow](https://github.com/CuiMuxuan/academic-codex-skills/tree/main/skills/academic-figure-workflow) | method routing by figure type; evidence trace; editable source and rendered QA | makes the Planner/Designer/Renderer boundaries and rule provenance classes explicit |
| [paper-figure](https://github.com/wbopan/paper-figure) | explicit grid/edge anchors; actual-render inspection loop; paper-context sizing | treats D3/HTML as one optional renderer rather than the universal backend |

## Reviewed revisions

- `research-workflow-kit`: `d386f1a7320c934d771c6ed22b019185ad370151`
- `scientific-agent-skills`: `15e77e6215425bd9a498ca54e049a06176277189`
- `academic-figure-skills`: `3e38b08f562ce85edeb8a5fce2e447fcd0f5267b`
- `academic-codex-skills`: `ec860d410117061a7e03f5ac134df9b5930fd313`
- `academic-figure-skill`: `1df9940dd01ac939f072b12fe28d6353b79b90f9`
- `paper-figure`: `03dbef935d2b84c6e8a184e3074193a4da9dea3a`

Commit hashes are provenance snapshots, not endorsements. Re-check upstream content and licences before copying code or assets in future revisions.
