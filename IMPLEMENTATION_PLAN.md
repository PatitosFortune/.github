# Patitos Fortune — GitHub identity implementation plan

## Scope and approval gates

M0 planning foundation, prepared 2026-09-30; M0 approved and M1 core work authorized by the user. M1 implementation notes are recorded below. The approved identity board is the primary visual source; this is a translation into a reusable system, not a redesign. Only this repository is in scope. Each milestone ends with an updated `STATUS.md`, a deliverable/validation report, and an explicit user approval gate. No commits or pushes without separate explicit approval.

The public identity is **Patitos Fortune / Creative Software Lab**: a small, independent software lab exploring curious ideas and turning them into useful software. Use broad categories of work, never private project names or inferred business details.

## Inspection and reference interpretation

- Repository inspected: empty working tree containing only `.git`, no commits, initially on unborn `main`. Configured origin is `https://github.com/PatitosFortune/.github.git`. Remote contents were not fetched or verified. No applicable `AGENTS.md` found in the workspace or its parent chain.
- Working branch: `brand/github-identity-v01`, also unborn until an approved first commit.
- Approved reference: `PatitosFortune-identity1.png`, supplied in the conversation. It shows cream paper, deep ink, a faceted duck, institutional typography, round seals, rectangular labels, and thin drafting lines.
- Preserve the duck's left-pointing angular tail, low polygonal body, upright bent neck, small head and right-facing beak. Broad colored planes provide the character; texture and drafting detail are secondary.
- The board contains differing duck proportions and facets. Proposed master reference: the large standalone duck at the far right of section A. Reuse its silhouette and plane relationships throughout; do not merge incompatible versions into new anatomy.
- Round seals and rectangular labels contribute structure. The PF monogram is subordinate. Stars, circles, grids and construction marks are optional annotations, never compulsory decoration.
- Do not reproduce the board's sample repository names or implied project claims. The user has confirmed **EST. 2025** for secondary institutional/stamp treatments. Keep the date out of the primary geometric duck.

## Canonical identity hierarchy

All five marks are complementary members of the final identity family. Both round and rectangular stamps remain required, including their ink and restrained ochre-detail treatments. The hierarchy assigns roles; it is not a selection/elimination process.

1. **Geometric Impossible Duck:** primary symbol, default cream avatar, shared source geometry.
2. **Round Lab Stamp:** institutional seal for larger archival/research contexts.
3. **Rectangular Lab Label:** organization header and documentation identity.
4. **PF monogram:** compact secondary typographic mark; never replaces the duck as the default avatar.
5. **Technical line duck:** diagrammatic derivative of the same geometry for experimental contexts.

## Approved palette direction

These working values were selected from the board's visual relationships, not transcribed from its printed HEX labels or claimed as pixel samples. M1 retains all eight values after flat-color browser rendering and contrast measurement. The canonical tokens and restrictions are now in `brand/palette/palette.json` and `brand/palette/PALETTE.md`.

| Role | Token | HEX | Intended use |
| --- | --- | --- | --- |
| Primary | Ink | `#102A36` | Text, outlines, dark fields, primary dark facets |
| Primary | Paper | `#F5F0E6` | Default background and reverse text |
| Secondary | Sage | `#628580` | Duck planes and controlled project fields |
| Secondary | Mist | `#AFBDB5` | Pale planes and quiet diagram fields |
| Accent | Ochre | `#C49449` | Small annotations, stamp detail, warm facets |
| Accent | Rust | `#BA6041` | Small contrasting facets and project accents |
| Neutral | Slate | `#52616A` | Supporting text on paper; one cool neck plane |
| Neutral | Rule | `#C7CBC5` | Nonessential separators and drafting grids |

Normalize the board's paper texture to a flat cream and its shaded ink to a single navy; do not create a new swatch for every raster shade. Retain muted warm/cool balance and avoid metallic effects. Ink on paper and paper on ink are the default text pairings. Use ink labels on light palette chips. Ochre, rust, sage and mist are graphical colors until their specific text/background pairing passes contrast checks. Low-contrast drafting lines must carry no essential information.

## Typography and composition

- Editorial/institutional headings: `Georgia, 'Times New Roman', serif`.
- Technical labels and supporting copy: `'Segoe UI', Arial, Helvetica, sans-serif`.
- Coordinates or specimen metadata, only when useful: `Consolas, 'Liberation Mono', monospace`.
- No font binaries, proprietary font dependency or remote font loading. GitHub body typography remains native; designed typography belongs in a small number of image assets.
- Use spaced uppercase for short labels, sentence case for explanatory text. Avoid wide tracking at tiny sizes.
- Construct on an 8-unit spacing rhythm. Establish clear space from one eighth of the master mark's bounding-box width; validate optical adjustments in M1. Keep one visual focus per composition.
- Editable templates may retain text and documented fallback stacks. Fixed wordmarks may use outlined glyphs if a reproducible conversion is available; preserve editable text upstream. Validate fallback rendering before deciding. Accessible titles/alt text remain necessary when lettering is outlined.

## Proposed final structure and asset inventory

This is a target inventory, not permission to generate files before their milestone. Create directories only when their contents are needed.

```text
README.md                              # M5: navigation and recommended assets
IMPLEMENTATION_PLAN.md                 # M0: approved scope and approach
STATUS.md                              # Every milestone: durable handoff
GITHUB_SETUP_CHECKLIST.md               # M5: exact manual upload instructions
profile/
  README.md                            # M3: public organization profile
  assets/
    lab-header.svg                     # M3: restrained notebook/lab-label header
brand/
  BRAND_GUIDE.md                       # M1 foundation; expand through M5
  source/
    geometric-duck.svg                 # M1: transparent canonical polygon mark
    technical-line-duck.svg            # M1: shared geometry, if legible
    round-stamp.svg                    # M2: ink master
    rectangular-stamp.svg              # M2: ink master
    pf-monogram.svg                    # M2: secondary mark
  palette/
    PALETTE.md                        # M1: locked values, pairings, contrast
  stamps/
    round-stamp-ochre.svg              # M2: ink structure, restrained ochre detail
    rectangular-stamp-ochre.svg        # M2: ink structure, restrained ochre detail
  avatars/
    duck-cream.svg / .png              # M2: recommended default
    duck-ink.svg / .png                # M2: light facets adjusted for dark field
    duck-ochre.svg / .png              # M2: controlled warm emphasis
    duck-sage.svg / .png               # M2: controlled cool emphasis
    duck-line.svg / .png               # M2: simplified technical candidate
    duck-seal.svg / .png               # M2: text-free seal, only if legible
  social/
    social-preview-template.svg       # M4: editable 1280 × 640 template
    example-number-puzzle.svg / .png  # M4: fictional puzzle specimen
    example-game-companion.svg / .png # M4: fictional Ink specimen
    example-data-tool.svg / .png      # M4: fictional Sage specimen
    example-simulation-lab.svg / .png # M4: fictional Rust specimen
```

Ink stamp masters live in `source/`; do not duplicate them under `stamps/`. Avatar PNGs are planned at 512 × 512 for upload, with smaller QA renders kept temporary. Add a header PNG only if rendering evidence shows it is useful. Any generation/validation helper added later must serve reproducibility and be documented, not introduce unnecessary tooling.

## SVG construction strategy

Manually reconstruct a clean polygon master from the selected reference duck. Preserve its proportions and visual character; avoid automatic tracing of raster noise. Use a square `viewBox` with a consistent coordinate system and named palette values. Derive the line duck from the same vertices and edges, removing redundant seams as needed for legibility.

Use standalone SVGs with no external references, scripts, embedded raster images or remote fonts. Keep polygons, paths and groups readable; use local definitions only. Compositions reuse the approved master geometry, with a documented derivation process to prevent facet drift. Do not introduce image generation for this vector reconstruction.

M1 should prove the silhouette before stamp development. A tiny-size simplification may remove the eye, very narrow facets or secondary seams, but must preserve tail/body/neck/beak proportions. A mathematical impossibility is not a requirement to invent a new optical illusion: preserve the approved abstract construction.

## GitHub profile strategy (M3)

Build `profile/README.md` around one shallow cream research-label header, the exact public lab description, and a short text treatment of puzzles, simulations, tools, games and experiments. Keep content readable without images using descriptive alt text and real Markdown copy. Avoid hardcoding unverified repository links or pinned-project recommendations.

Verify image paths for GitHub's organization-profile context, light/dark appearance and narrow layouts. Give the designed header an explicit paper background so its ink does not disappear in dark mode. Use broadly supported Markdown/HTML, no custom CSS or interactive dependencies. Avoid reproducing the entire reference board as a large poster.

## Repository social-preview strategy (M4)

One 1280 × 640 composition with a 64 px safe margin, consistent lab signature, short project descriptor, and separate project motif area. Start with a left title/descriptor area of roughly 60% and a right motif area of roughly 40%; protect the lab signature at the bottom. Fit long titles by controlled line wrapping and documented limits, not indefinite shrinking.

The M4 authorization supersedes the initial two-example proposal: use at least four explicitly fictional specimens (Number Puzzle, Game Companion, Data Tool and Simulation Lab). Include Paper and Ink fields, controlled Ochre/Sage/Rust accents and project-specific study diagrams. Keep the primary colorful duck as a small laboratory attribution. Export 1280 x 640 PNGs. Document fixed/variable rules, structured inputs and restrained repository README use. No application repository changes or automatic GitHub uploads.

## Validation approach

- **Reference fidelity:** compare the master silhouette and facets against section A, then compare the family for shared proportions and hierarchy.
- **Vector integrity:** parse SVG XML, verify dimensions/viewBoxes, inspect for missing references and external dependencies, and render in a standard browser. Confirm no clipped text or accidental seams.
- **Small sizes:** render the duck at 16, 24, 32, 48, 64 and 128 px; inspect actual pixels. Test each avatar in square and circular crops at 32/48/64 px. Keep beak and tail inside crop-safe bounds. Stamps are not expected to retain fine text at avatar sizes.
- **Color:** measure contrast for documented text pairings; target 4.5:1 for normal text, 3:1 for large text, and 3:1 for essential non-text indicators. Record values and any changes in `PALETTE.md`. Decorative planes need separate perceptual review.
- **Typography:** check installed fonts and renderer support before exports; inspect substitutions, tracking and line breaks. No font installation is assumed.
- **Exports:** verify PNG dimensions, transparency/background intent and visual agreement with source SVGs. Inspect social examples at reduced preview size.
- **Profile/docs:** check links, local paths, alt text, image loading assumptions and light/dark presentation. Distinguish a local preview from a verified live GitHub rendering.
- **Public safety/scope:** inspect generated text for private names, unsupported claims and local personal paths. Ensure only this repository changed. Review `git diff --check` and the complete untracked-file inventory before each checkpoint.
- **M0 only:** confirm branch, scope, the two planning files, and milestone gates; no logo validation can be claimed yet.

## Milestones and expected work

| Milestone | Scope | Exit evidence / approval gate |
| --- | --- | --- |
| M0 | Inspect and plan; two Markdown files only | Present proposed system; update status; stop |
| M1 | Lock palette, duck master, useful line derivative, typography and guide foundation | Render and inspect size ladder; SVG and contrast checks; stop |
| M2 | Two stamp families, PF monogram, six purposeful avatar candidates and upload exports | Compare family, small circles and PNGs; stop |
| M3 | Organization profile and required header asset | Check copy, links and rendering assumptions; stop |
| M4 | Reusable social template, four fictional examples, repository visual rules | Check dimensions, title limits and palette variation; stop |
| M5 | Full QA, inventory, root README and setup checklist | Report complete handoff; no commit/push; stop |

M1 estimate: one focused milestone with three work blocks: (1) palette/coordinate construction, (2) master and line-variant review at actual sizes, (3) typography/guide documentation and validation. Allow roughly 60–120 minutes of implementation and visual QA as a planning allowance, depending on renderer readiness and how closely the silhouette needs refinement. One consolidated review checkpoint; no stamp, avatar family, profile or social-card production in M1. Revisions that materially change the approved direction require a scope checkpoint.

## Risks and unresolved decisions

- The board is raster artwork, not an exact vector specification. The approved anchor is section A's far-right duck; M1 interprets its silhouette, proportions and facets with clean deterministic geometry rather than mechanical tracing.
- Printed HEX labels, shading and paper texture do not define stable colors. M1 measurements retain the approved palette direction with explicit text-pairing restrictions.
- The eye, narrow facets and drafting seams may fail at 16–24 px. Prefer justified simplification over thicker outlines everywhere.
- System font metrics vary. Fixed compositions need rendering checks and possibly outlined final lettering; editable templates need explicit font guidance.
- Fine circular seal text cannot serve small avatars; the seal candidate should use only a duck and restrained rings.
- Founding date resolved by the user: use `EST. 2025` only as secondary institutional metadata.
- M1 browser rendering and PNG dimensions are validated locally. Live GitHub rendering remains unverified; the board's mock GitHub UI is not a layout guarantee.
- Avatar upload, social-preview upload and organization configuration are manual handoff actions. No organization-wide changes are authorized.

M0 and M1 are approved. The corrected R3-B treatment has been canonicalized and validated. M2 is complete and approved; M3 is complete and approved. M4 is complete and approved; M5 is complete and Brand System v1 is approved for publication. Approval to continue a milestone does not authorize committing or pushing.

## M1 implementation additions

`brand/palette/palette.json` provides reusable exact tokens. `brand/tools/validate-core.py` checks core SVG geometry, references and color pairings; `brand/tools/render-core.cjs` regenerates browser review sheets and native-size PNGs into an explicitly chosen directory outside the repository. `brand/VALIDATION.md` records results and limitations. These focused helpers support reproducibility without creating later-milestone assets. QA PNGs are review artifacts, not production avatar exports.


## Approved M1 treatment and authorized M2 emphasis

The corrected R3-B technical PA duck is canonical: complete Ochre A legs and counter, shared lower-body P, and an Ochre-filled bill with Ink head/eye/construction. Geometry and proportions remain unchanged. This secondary mark does not replace the primary colorful faceted duck.

M2 must preserve both expressions of the merged B+C board. Develop both round and rectangular Lab Stamp/Label forms in Ink and restrained Ochre detail, plus PF monogram and six avatar candidates: colorful Paper, Ink, Ochre and Sage; technical PA; and a seal derivative where legible. Use Ink, Sage, Mist, Ochre and Rust relationships across the colorful family. Keep the filled master unchanged and adapt dark-background derivative facets deliberately. Produce the family review sheet before declaring variants final. Signature-wing exploration is parked.

M1 and M2 are complete. The user approved the full M2 family and final expressive treatments. M3 is approved. M4 is complete and approved, including four fictional samples and the reusable project-identity/social-preview system. M5 is complete and Brand System v1 is approved for publication. Preserve M1–M4. Commit/push/PR publication is authorized; no merge, new project rollout, website implementation or asset uploads.
