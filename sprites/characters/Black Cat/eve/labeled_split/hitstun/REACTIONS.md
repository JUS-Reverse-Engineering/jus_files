# Hit-reaction sprite labels

The attack's reaction type selects these poses. The numbers are engine reaction IDs, not damage tiers or hit order.

| Current filename | Native animation | Typical trigger |
|---|---|---|
| `hit_type_0` | `0x0B` | Reaction type 0, such as Eve or Train's grounded B |
| `hit_type_1` | `0x0A` | Reaction type 1, such as Kakashi or Yusuke's grounded B |
| `hit_type_2` | `0x0C` | Reaction type 2, such as Kakashi's up+B |
| `surprised` | `0x0D` | Reaction type 7 |

Kakashi retains `_left` and `_right` variants. Other characters retain their existing facing convention.

Type 3 also starts animation `0x0C`. Type 4 starts `0x0C` and then plays the knockdown animation. Types 13, 14, and 15 reuse `0x0B`, `0x0A`, and `0x0A`, respectively.

A hit's alternate selector value 2 replaces the ordinary type-0, type-1, type-2, or type-7 pose with animation `0x0E`. Those bright outlined animation cells are separate assets. Being airborne does not itself select the alternate pose.

Multihit attacks can author different reaction types for successive contacts. Kakashi's side+B uses types 1 then 2. There is no general light/medium alternation rule. A late combo has a separate reaction override that can lead to knockdown.

The four-frame native tracks hold their final cell for the rest of hitstun. They do not imply four frames of hitstun.

## Filename changes on 2026-10-04

| Previous filename | Current filename | Animation | Native cell |
|---|---|---|---|
| `light.png` | `hit_type_1.png` | `0x0A` | 27 |
| `light_2?.png` | `hit_type_0.png` | `0x0B` | 26 |
| `medium?.png` | `hit_type_2.png` | `0x0C` | 28 |

Source evidence is recorded in `jus_re/docs/research/findings/hit-pose-selection-2026-10-04.md` and its capture directory. Images were matched to decoded native cells; relabeling did not change PNG bytes.
