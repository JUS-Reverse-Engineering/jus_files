# The freeze-fix A/B, 2026-09-28

The experiment behind `cpu-ai-levels.md` §3.25. One emulator session, stock ROM, the savestate
`pc-kakashi-npc-jotaro-fightcpu` loaded fresh before each arm, 3400 frames, the same 23-watch
set. Both patches are RAM pokes at the ov11 virtual address, so the stock ROM is also the
treatment ROM and reloading the savestate reverts each arm.

Driver: `/private/tmp/freeze-ab/run_ab.py` (ephemeral).

## Files

| file | what |
|---|---|
| `ab_control.jsonl` | arm 1, no poke. 3420 rows, fc 32575–35994. |
| `ab_data.jsonl` | arm 2, the two-byte guard-table patch. 3420 rows, fc 32615–36034. |
| `ab_code.jsonl` | arm 3, the four-byte NOP. 3420 rows, fc 32595–36014. |
| `ab.specs.json` | the watch order and the pointers resolved at capture time. |
| `ab.summary.json` | the driver's per-arm summary. |

Column order is in `ab.specs.json` — read it before indexing. `AI+0x39` is `(ai_act >> 8) & 0xFF`,
`AI+0x3A` is `(ai_act >> 16) & 0xFF`. Positions are 8.8 fixed point: divide by 256.

## Result

- **control**: unchanged. `+0x39 == 1` on all 2486 post-latch frames, `+0x3E` saturates at 255,
  own state 0 everywhere, no movement.
- **data**: the freeze is gone — the phase cycles, 834 attack frames, 478 x-changes, and the
  opponent enters `8/23/24/25` (hit and launched).
- **code**: inert, bit-identical to control.

**The control is bit-identical to `../ai-phase-machine-2026-09-28/cap1.jsonl` on all 23 watched
fields across 3400 shared frames — 0 differences.** That is the determinism proof that makes the
treatment comparison attributable to the poke.

## The correction this run forced

`AI+0x39` never reaches 9 or 0xA in **any** arm, including healthy stock play. Those are the only
values the finalizer writes, so the finalizer's write path is never taken and it is **not** the
freeze's escape hatch. The data patch works through the guard's other 16 callers — first
divergence at **fc 32760**, 749 frames before the latch. See §3.25.
