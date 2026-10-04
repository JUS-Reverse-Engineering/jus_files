# Naruto categorized art

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `na_b_01`, `na_b_01_4`, `na_b_01_5`, `na_b_01_6`, `na_b_05`, `na_b_05_7`, `na_b_05_8`, `na_s_01`, `na_s_01_2`, `na_s_01_3`.

Categories: `attacks_heavy` (12), `attacks_light` (10), `attacks_special` (63), `generics` (28), `hitstun` (30), `misc` (24), `panels` (9), `supports` (15), `taunt` (2). Total: 193 selected assets, including 11 source extras.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 155 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 139 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- 2k Sexy Jutsu heart compounds and Kyuubi 7k/8k aura/beam composites retain source reference rows; node composition and branch timing remain unresolved.
- Normal and Kyuubi UNUSED SPRITES are not certified runtime states.
