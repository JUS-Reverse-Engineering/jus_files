# Toshirō Hitsugaya categorized art

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `bl_b_05`, `bl_b_05_4`, `bl_b_05_5`, `bl_b_05_6`, `bl_s_05`, `bl_s_05_2`, `bl_s_05_3`.

Categories: `attacks_heavy` (6), `attacks_light` (5), `attacks_special` (33), `generics` (14), `hitstun` (15), `misc` (30), `panels` (6), `supports` (13), `taunt` (1). Total: 123 selected assets, including 6 source extras.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 64 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 39 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- 5k/6k ice arcs, dragon body and ice-field source compositions require independent transforms.
