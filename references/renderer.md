# Figure Renderer

Use this layer only when the user asks to create, edit, export, or audit files.

## 1. Inspect before choosing tools

Inspect the project, data, existing figure sources, installed runtimes, and target outputs. Reuse the project's established Python or R stack when it can produce the required figure reliably. Do not rewrite a working analysis pipeline solely to match a preference in this skill.

## 2. Route by figure and source of truth

| Task | Preferred route | Use another route when |
|---|---|---|
| Data-backed statistical figure | Python or R already used by the project | user specifies the other language or a required library exists there |
| Framework, pipeline, ordinary architecture | editable SVG or draw.io | a code-defined layout is materially easier to maintain |
| Mathematics-native diagram | TikZ/PGF | collaborators need draw.io/SVG editability |
| CNN/U-Net/encoder-decoder layer view | PlotNeuralNet or SVG/TikZ | the figure is a method pipeline rather than a layer diagram |
| Highly customized vector/data composition | SVG/D3 | a normal Python/R plot is simpler and equally reproducible |
| Bitmap illustration | image generation only with explicit user intent | scientific topology, text, or data must be exact—then redraw as vector |

[Skill-Derived Heuristic] Renderer choice follows evidence, editability, reproducibility, collaborator tooling, and final venue—not a universal software hierarchy.

## 3. Data truthfulness gate

Before plotting, record:

- source path/identifier and version;
- variable meanings, units, sample/replicate structure;
- missing/censored values and exclusions;
- estimator and uncertainty definition;
- filtering, aggregation, normalization, smoothing, bins, transformations, and random seeds;
- intended comparison and direction of “better.”

Do not silently connect missing observations, suppress inconvenient points, interpolate measured data, or smooth a curve to strengthen a conclusion. Synthetic data is allowed only for an explicitly labeled demonstration that cannot be mistaken for evidence.

[Literature/Official Standard] PLOS warns against misleading scales/encodings and emphasizes choosing a simple form that communicates the message. See [Ten Simple Rules for Better Figures](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003833). For scientific images, the US Office of Research Integrity recommends preserving originals and documenting manipulations; see [image-processing guidelines](https://ori.hhs.gov/education/products/RIandImages/guidelines/list.html).

## 4. Build from an explicit specification

Use a validated `figure_spec` containing:

- claim and evidence sources;
- panel jobs and encodings;
- scales, limits, units, uncertainty, and missing-data treatment;
- layout and final dimensions;
- visual-system tokens;
- renderer and editable-source format;
- output formats;
- official rules with scope and checked date;
- unresolved items and forbidden claims.

If inputs are missing, return this specification and a required-input manifest instead of generating publishable-looking placeholders.

## 5. Produce editable source and exports

- Keep plotting code beside a machine-readable input/spec or clearly documented parameters.
- Preserve `.drawio`, `.svg`, `.tex`, `.py`, `.R`, or HTML/D3 source as appropriate.
- Prefer vector PDF/SVG/EPS for line art when the target accepts it.
- Use PNG/TIFF/JPEG only when required or when the content is intrinsically raster.
- Embed or retain editable text/fonts when supported.
- Keep a raster preview for inspection even when vector is the primary deliverable.

Do not convert a low-resolution raster into a vector container and call it vector artwork.

## 6. Rendered QA loop

Every generated or revised figure follows:

1. render/export;
2. inspect the actual output, not only source code;
3. check at 100% and intended physical width;
4. record failures by element/location;
5. fix source, re-export, and re-inspect;
6. stop when a full pass finds no new blocking issue or report unresolved blockers.

### Scientific QA

- every mark traces to data, code, manuscript, or author-approved concept;
- scales, baselines, units, uncertainty, `n`, and replicate unit are explicit;
- missingness, exclusions, transformations, and image adjustments are disclosed;
- comparisons use consistent samples/scales where the claim requires them;
- labels and formulas match manuscript terminology.

### Visual and accessibility QA

- reading order and panel hierarchy are obvious;
- no overlaps, clipping, broken arrows, ambiguous arrow meanings, or detached labels;
- text remains readable at final size;
- contrast is sufficient and meaning is not carried by color alone;
- direct labels/keys are close to the evidence;
- alt text or a data alternative is supplied when required by the medium.

### File QA

- physical dimensions, aspect ratio, page box, DPI/effective DPI, color mode, transparency, and file size are checked;
- fonts and vector elements are embedded/editable as required;
- file opens in the intended downstream application;
- editable source and output filenames are stable and traceable;
- target-journal requirements have a current official link and correct scope.

## 7. Compliance wording

Use:

- `verified against <official guide>, checked YYYY-MM-DD` when every applicable item was inspected;
- `general publication-quality baseline; venue rules pending` when the venue or stage is unknown;
- `automated checks passed; scientific and human visual review still required` for script-only validation.

Never use “Nature-compliant” as a synonym for “89 mm wide” or “300 dpi.”

## Renderer output

Return editable source, requested exports, source-data/provenance record, a `qa_report` JSON, and unresolved issues. Validate structured artifacts with `scripts/validate_figure_artifact.py`.
