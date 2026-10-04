# Dr. Mashirito categorized art

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `ds_b_02`, `ds_b_02_4`, `ds_b_02_5`, `ds_b_02_6`, `ds_b_02_7`, `ds_b_03`, `ds_b_03_8`, `ds_s_02`, `ds_s_02_2`, `ds_s_02_3`, `ds_s_03`, `ds_s_03_2`.

Categories: `attacks_heavy` (12), `attacks_light` (10), `attacks_special` (38), `generics` (27), `hitstun` (30), `misc` (58), `panels` (8), `supports` (24), `taunt` (2). Total: 209 selected assets, including 8 source extras.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 155 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 35 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- Caramel Man ds_b_03 is an alternate native family; its 8k special pieces are separate from ds_b_02 robot summon bodies.
- No ds_s_03_3 archive exists. Color/palette alternates and source compound transform sequence selection remain unresolved.

Gold `ds_b_03` / `ds_s_03` art is a **native-only alternate-form candidate**. The corrected idle source pixel probe found no match (0%); this form has no source-confirmed rectangle and contributes no source-sheet coverage claim.
