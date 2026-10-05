# Renji Abarai categorized art

<!-- current-art-summary:start -->
Character package: 129 assets, 128 visible strips/panels and 1 transparent native tracks. 392 referenced canonical native cell PNGs. [Attack map](ATTACKS.md) contains 50 action groups.

Native diagnostics in the current manifest: 66 nodes without cell tracks, 0 unresolved-node records and 0 unsupported-texture records. These diagnostics describe decoding; gameplay selection and composition remain separate review items.
<!-- current-art-summary:end -->

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `bl_b_04`, `bl_b_04_4`, `bl_b_04_5`, `bl_b_04_6`, `bl_s_04`, `bl_s_04_2`, `bl_s_04_3`.

Categories: `attacks_heavy` (14), `attacks_light` (10), `attacks_special` (42), `generics` (18), `hitstun` (15), `misc` (2), `panels` (6), `supports` (19), `taunt` (3). Total: 129 selected assets.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 59 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 60 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- 6k giant serpent parts and source repeat brackets require keyed transforms/composition, not sheet row order.
