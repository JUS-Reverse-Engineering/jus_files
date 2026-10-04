# Sanji art authoring package

104 visible categorized strips/panels, including 6 source comic panels; 0 transparent native tracks retained as provenance. 717 canonical native cell PNGs preserve decoded body, support and effect banks.

`art.json` records category, authored animation ID, archive member, texture owner, node, frame bounds, anchors and hashes. The category directories contain review strips. `misc/native_cells/` contains the original-size decoded cells.

Native archives: `op_b_03`, `op_b_03_4`, `op_b_03_5`, `op_b_03_6`, `op_s_03`, `op_s_03_2`, `op_s_03_3`.

Native pixels retain full origin-relative bounds, full palette indices, index-zero transparency, authored flips and DSIGv2 two-tile segment alignment. Sheet panels use explicit source rectangles and occupied-cell masks. No poses are synthesized by mirroring.

`fighter_body` and `support_actor` identify primary tracks; effect, text, summon and child-node art remains separate components. A native actor may be a helper rather than this fighter. Empty tracks are marked `empty_native_track` and excluded from the visible count.

Strips show distinct native cells in their first occurrence order. Repeated holds and complete key tracks remain in the manifest; these strips are not a runtime playback specification. All runtime candidates remain false until timing, facing, gameplay selection and composition are reconciled.

The original source, every categorized overview, corrected alignment tracks and panel selections were visually inspected. Verification checks source/archive hashes and regenerates canonical pixels and strips. 91 nodes with no cell track, 0 unresolved-node records and 0 unsupported-texture records remain explicit.

Source coverage remains `reviewed_reference_unreconciled`: coordinate bands in `dispositions` document reviewed reference regions, not proven pose matches or complete extraction. Comic panels have exact piece provenance. Native art has exact archive provenance; native-to-sheet pose coverage is still incomplete.

Remaining character-specific work: Heart/target-dependent poses, flame components and speech rows require hit/miss and target branches.

Verify from the research repo with `scripts/analysis/cast_art.py verify --source <character-directory> --stage <character-directory> --repo-root <research-repo>`. The package is an authoring artifact; the normalized runtime library contract is unchanged.
