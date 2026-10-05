# Yugi art authoring package

<!-- current-art-summary:start -->
Character package: 158 assets, 150 visible strips/panels and 8 transparent native tracks. 556 referenced canonical native cell PNGs. [Attack map](ATTACKS.md) contains 50 action groups.

Native diagnostics in the current manifest: 138 nodes without cell tracks, 0 unresolved-node records and 0 unsupported-texture records. These diagnostics describe decoding; gameplay selection and composition remain separate review items.
<!-- current-art-summary:end -->

`art.json` records category, authored animation ID, archive member, texture owner, node, frame bounds, anchors and hashes. The category directories contain review strips. `misc/native_cells/` contains the original-size decoded cells.

Native archives: `yo_b_01`, `yo_b_01_4`, `yo_b_01_5`, `yo_b_01_6`, `yo_s_01`, `yo_s_01_2`, `yo_s_01_3`.

Native pixels retain full origin-relative bounds, full palette indices, index-zero transparency, authored flips and DSIGv2 two-tile segment alignment. Sheet panels use explicit source rectangles and occupied-cell masks. No poses are synthesized by mirroring.

`fighter_body` and `support_actor` identify primary tracks; effect, text, summon and child-node art remains separate components. A native actor may be a helper rather than this fighter. Empty tracks are marked `empty_native_track` and excluded from the visible count.

Strips show distinct native cells in their first occurrence order. Repeated holds and complete key tracks remain in the manifest; these strips are not a runtime playback specification. All runtime candidates remain false until timing, facing, gameplay selection and composition are reconciled.

The original source, every categorized overview, corrected alignment tracks and panel selections were visually inspected. Verification checks source/archive hashes and regenerates canonical pixels and strips. Current native diagnostics appear in the package summary above.

Source coverage remains `reviewed_reference_unreconciled`: coordinate bands in `dispositions` document reviewed reference regions, not proven pose matches or complete extraction. Comic panels have exact piece provenance. Native art has exact archive provenance; native-to-sheet pose coverage is still incomplete.

Remaining character-specific work: Shared body poses are reused for specials; summons and cards remain separate. Source instructional text is reference evidence, not animation art. Interior green key replaces the dark border sample.

Verify from the research repo with `scripts/analysis/cast_art.py verify --source <character-directory> --stage <character-directory> --repo-root <research-repo>`. The package is an authoring artifact; the normalized runtime library contract is unchanged.

## Attack associations

[Attack map](ATTACKS.md) groups body animation, actors and effects by input.
`art.json.attack_art` contains stable links and evidence; `asset_labels` preserves
semantic labels across native re-export. Browse the same groups in `ART_REVIEW.html`.
