# Rukia Kuchiki categorized art

<!-- current-art-summary:start -->
Character package: 111 assets, 111 visible strips/panels and 0 transparent native tracks. 338 referenced canonical native cell PNGs. [Attack map](ATTACKS.md) contains 50 action groups.

Native diagnostics in the current manifest: 185 nodes without cell tracks, 0 unresolved-node records and 0 unsupported-texture records. These diagnostics describe decoding; gameplay selection and composition remain separate review items.
<!-- current-art-summary:end -->

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `bl_b_03`, `bl_b_03_4`, `bl_b_03_5`, `bl_b_03_6`, `bl_s_03`, `bl_s_03_2`, `bl_s_03_3`.

Categories: `attacks_heavy` (19), `attacks_light` (5), `attacks_special` (34), `generics` (15), `hitstun` (15), `misc` (2), `panels` (5), `supports` (14), `taunt` (2). Total: 111 selected assets.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 34 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 44 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- Source 5k Flip the effects to fit / Example at y2490 remains composition guidance; no universal facing rule is inferred.
