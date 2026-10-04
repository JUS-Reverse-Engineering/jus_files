# Killua Zoldyck categorized art

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `hh_b_02`, `hh_b_02_4`, `hh_b_02_5`, `hh_s_02`, `hh_s_02_2`, `hh_s_02_3`.

Categories: `attacks_heavy` (6), `attacks_light` (5), `attacks_special` (18), `generics` (14), `hitstun` (15), `misc` (22), `panels` (4), `supports` (11), `taunt` (1). Total: 96 selected assets, including 4 source extras.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 53 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 32 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- 3k die tiles are components, not panel artwork; source 3k panel crop explicitly excludes neighboring die art.
- 2k/5k lightning/speed poses require native keyed transforms and runtime selection.
