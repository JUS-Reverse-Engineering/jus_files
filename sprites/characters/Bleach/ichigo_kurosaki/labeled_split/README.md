# Ichigo Kurosaki categorized art

Native body poses, components and supports are exported separately from the immutable source sheet. `art.json` records authored animation IDs, exact archive/texture/cell ownership, frame bounds/origins, source pieces and uncertain branches. Files retain authored facing.

Native origins: `bl_b_01`, `bl_b_01_4`, `bl_b_01_5`, `bl_b_01_6`, `bl_b_02`, `bl_b_02_7`, `bl_b_02_8`, `bl_s_01`, `bl_s_01_2`, `bl_s_01_3`.

Categories: `attacks_heavy` (12), `attacks_light` (10), `attacks_special` (39), `generics` (28), `hitstun` (30), `misc` (44), `panels` (8), `supports` (12), `taunt` (2). Total: 185 selected assets, including 10 source extras.

Body and component strips are separate assets. Base support `_s_` speech/SFX/graphics are `support_component`; actual main-body support nodes are `support_actor`. `misc/native_cells` preserves canonical unused cells and palettes as well as referenced cells. Deck art in `panels` uses reviewed source pieces; touching printed layouts are separate `misc/source_references` crops. Portrait/HUD references also live in `misc`.

Visual review covered all full source sheet tile overviews, crop candidates and outputs, and native first/last-cell category contacts. The DSIGv2 allocation repair changed 162 canonical cells; before/after contacts were inspected for every affected asset. Native cells and composed source outputs pass exact regeneration verification. Review does not certify gameplay playback, transforms, branch selection or state duration.

Source coverage remains separate from native archive coverage: 143 bounded source row groups are retained as reference dispositions for compound examples, source-only poses, repeat guides and attribution. They do not assert one-to-one native correspondence or a selected runtime asset for every source pixel.

Residuals:

- Normal and Bankai source UNUSED SPRITE rows remain source-only candidates; engine selection is unresolved.
- Bankai 7k VERSION 1 / VERSION 2 source compound effects require branch and transform composition; native pieces are preserved independently.
