# Momotaro categorized art

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `oj_b_02`, `oj_b_02_4`, `oj_b_02_5`, `oj_b_02_6`, `oj_s_02`, `oj_s_02_2`, `oj_s_02_3`.

Categories: `attacks_heavy` (6), `attacks_light` (5), `attacks_special` (36), `generics` (14), `hitstun` (15), `misc` (26), `panels` (5), `supports` (10), `taunt` (1). Total: 118 selected assets, including 5 source extras.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 110 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 37 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- Dialogue cut-in portraits at source x1258+ y2312+ are special components, not deck koma.
- 5k/6k ice-dragon/afterimage compounds require transforms and branch selection.
