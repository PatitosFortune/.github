# Reproduce Brand System v1

Run from the repository root. No original chat, reference raster or external historical baseline is required. The two hand-authored M1 SVG masters and `palette/palette.json` are inputs, not outputs to recreate from a screenshot. Keep them intact.

## Runtime

Use Python 3.10+ with assertions enabled, Node.js with `playwright` and `marked` resolvable, and a Chromium-family browser executable. Generation and validation use the Python standard library; Pillow is optional for pixel audits. No fonts are downloaded or bundled. The supported type stacks and fallback checks are in [BRAND_GUIDE.md](BRAND_GUIDE.md#typography).

M5 was run with Python 3.14, Node 24.21 and Edge/Chromium 154.0.4258.48 using the already available dependencies. No installation was needed. On another machine, provision these prerequisites through its normal environment before running the commands. If Node modules are in a shared runtime, set `NODE_PATH` to that runtime's `node_modules` directory; do not copy a personal machine path into the repository.

## Preserve the approved baseline

The [v1 integrity manifest](review/V1_INTEGRITY.json) records approved visual/input hashes. Before rebuilding, keep a separate backup of the working files or use a separately authorized checkout. The renderers for family and social previews overwrite their production PNG exports. HTML, detailed samples and reports go to the explicit review directory.

Never refresh approval hashes merely to silence a failure. Check whether it is a permitted documentation change, a real artwork change, or raster variation. SVG generation is deterministic. PNG encoding/rasterization may vary even between runs of a browser; compare the saved approved bytes and visible pixels. During M5, one transient Ink-avatar PNG mismatch returned to the approved hash on a repeat render. All final PNG hashes match the pre-M5 files.

The milestone manifests are rebuilt from current upstream inputs; they alone do not prove preservation. Compare with the separate v1 integrity manifest before and after work:

```powershell
@'
import hashlib, json
from pathlib import Path
m = json.loads(Path('brand/review/V1_INTEGRITY.json').read_text(encoding='utf-8'))
for name, expected in m['files'].items():
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest() == expected, name
print('Approved v1 visual/input hashes match.')
'@ | python -
```

## Build in dependency order

This PowerShell sequence stops on a failed native command:

```powershell
$ErrorActionPreference = 'Stop'
foreach ($suite in @('family', 'expressive', 'profile', 'social')) {
    python "brand/tools/build-$suite.py"
    if ($LASTEXITCODE -ne 0) { throw "Build failed: $suite" }
}
```

- Family derives clean round/rectangular stamps, PF, Ochre counterparts and avatars from M1 sources.
- Expressive derives aged impressions and construction presentations from the clean family; wear uses seed `20251001`.
- Profile derives the two header layouts; the approved README is maintained separately.
- Social derives the anatomy template and four fictional examples from `brand/social/examples.json`.

These builders do not export PNGs. Existing approved PNGs are supplied in the repository. When creating a genuinely new family without those exports, render the family immediately after building it and before the downstream manifest-producing builders.

To verify determinism, record hashes of all generated SVGs and manifests, repeat the same four builders, and compare the hashes. M5 performed that check; no timestamp or random seed changes appear in generated SVGs/manifests.

## Render and validate

Use a writable review directory outside the repository. These Windows defaults can be replaced with the local equivalents:

```powershell
$qa = Join-Path $env:TEMP 'patitos-fortune-v1-qa'
$browser = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
foreach ($suite in @('core', 'family', 'expressive', 'profile', 'social')) {
    $suiteOutput = Join-Path $qa $suite
    node "brand/tools/render-$suite.cjs" $suiteOutput $browser
    if ($LASTEXITCODE -ne 0) { throw "Render failed: $suite" }
    python "brand/tools/validate-$suite.py" --renders $suiteOutput
    if ($LASTEXITCODE -ne 0) { throw "Validation failed: $suite" }
}
```

Run the integrity check again afterward. Inspect `core-review.png`, the size ladder, the family and expressive review sheets, `m3-profile-review.png` and `m4-social-review.png` in their respective output folders. This is visual QA, not a publication command. Browser helpers block remote page requests and use local artwork.

For a fast structural pass without fresh browser evidence:

```powershell
foreach ($suite in @('core', 'family', 'expressive', 'profile', 'social')) {
    python "brand/tools/validate-$suite.py"
    if ($LASTEXITCODE -ne 0) { throw "Validation failed: $suite" }
}
```

Do not describe that shorter command as a fresh render check. `--renders` verifies current source hashes against the saved report and checks the expected dimensions/layout records. The profile's optional historical `m2-approved-hashes.json` and expressive before/after directory add historical comparison only; the repository manifests suffice for a clean reproduction.

## New project inputs

Follow the [structured contract and examples](REPOSITORY_VISUALS.md#structured-input-contract). Supply a separate JSON file and output directory using `build-social.py --input ... --output-dir ...`; pass that same directory as the renderer's third positional argument and validator's `--source-dir`. Custom projects retain pending-review status. Do not overwrite the approved fictional fixtures for a real repository rollout.

The current generator supports four local motif presets and an empty study field. Arbitrary project SVG/icon imports and additional output aspect ratios are not implemented. Extend them only under a later scoped request and rerun the relevant checks.
