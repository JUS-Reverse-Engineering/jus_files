# Jaguar categorized art

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `pj_b_01`, `pj_b_01_4`, `pj_b_01_5`, `pj_b_01_6`, `pj_s_01`, `pj_s_01_2`, `pj_s_01_3`.

Categories: `attacks_heavy` (6), `attacks_light` (5), `attacks_special` (37), `generics` (14), `hitstun` (15), `misc` (26), `panels` (4), `supports` (13), `taunt` (1). Total: 121 selected assets, including 4 source extras.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 80 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 46 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- Source musician helpers, SFX, and special compound strips require transforms and runtime branch selection.
- Source UNUSED pose remains reference-only.
