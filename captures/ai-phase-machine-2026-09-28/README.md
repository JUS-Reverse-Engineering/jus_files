# The freeze fixture capture, 2026-09-28

The run behind `cpu-ai-levels.md` §3.24. One bridge-only capture of
`pc-kakashi-npc-jotaro-fightcpu`, stock ROM, savestate load, no input, 3400 frames.

- **3420 rows, fc 32595–36014, 0 gaps, 0 dropped**, latch confirmed at **fc 33509**.
- Watch spec: **23 watches / 510 bytes** of the bridge's 512-byte budget.
- Driver: `/private/tmp/jus-phase-capture/run_capture.py` (full raw log
  originally `/private/tmp/jus-phase-capture/cap1.jsonl`; now tracked here as `cap1.jsonl`).

## Files

| file | what |
|---|---|
| `decisive.tsv` | the 16 decisive columns, one row per frame, 3420 rows. Tab-separated, header row. |
| `specs.json` | the watch spec and the pointers resolved at capture time. |
| `analysis.json` | the driver's own summary (latch, per-field histograms, consistency checks). |

`decisive.tsv` columns: `fc`, `a38` `a39` `a3a` (`AI+0x38/+0x39/+0x3A`), `a3e` (`+0x3E`),
`a40` (`+0x40`), `a105` (`+0x105`), `ai20` (`[AI+0x20]`), `opp18` (`[[AI+0x20]+0x18]`),
`ai24` (`[AI+0x24]`), `movptr` (`[[AI+0x24]+8]`), `mov180` (`[[AI+0x24]+8]+0x180`),
`st1` `st2` (both fighters' state codes), `p1x` `p2x`.

## What it shows, and how to check it without the emulator

1. **`a39 == 1` and `a3e` climbs to 255** — the signature of the `0x0217B410` route, and the
   refutation of the knockdown exit `0x0217B41C` (which returns before the increment).
2. **`a40 == 0` on every frame** — so the dispatcher's second table takes index 0, the
   finalizer `0x0217A968`.
3. **`opp18` is 0 (2550 frames) / 1 (42)** — the CPU's *own* state, and neither is in the guard
   table `{9,10,11,12,26}` at `0x021813CC`. Hence the guard fails and the finalizer writes
   nothing.
4. **`mov180 == 0x001E00A8` and `movptr == 0x022606A0`, constant** — the object the step-1
   handler actually tests is *not* `objA`/`objB` (0x02260AC0 / 0x0225F020); it agreed with
   them on 0 of 3420 frames.

## The reaction weights (same run)

`[AI+0x2C]` = `0x0239ED10`, constant. `[AI+0x2C]+0x38` (the roll source) takes **all 256
values** over the run. The 13 weight bytes at `[AI+0x2C]+8+15..+8+27` are **constant**:

```
[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 15, 21]
```

Mapped through the entry list in `ai-behaviour-taxonomy.md` §4.4 (weight index 15..27 in
entry order):

| cumulative | entry | id | class |
|---:|---|---:|---:|
| 0–219 | entries 0–10 | 1,2,3,4,5,6,1,1,7,8,11 | 0,1,0,1,0,1,2,3,5,6,17 |
| **220–249** | **entries 11–12** | **13, 14** | **4** |
| 250–255 | entry 13 | 127 (sentinel) | 18 |

Total 271, but the roll is `(x>>1) & 0xFF` so only 0–255 is reachable. So the punish band
(ids 13/14) has a **30/256 ≈ 11.7 %** share and the sentinel ~2.3 %. The punish band is
therefore **not** unreachable for lack of weight or roll range — see
`jus-ai-reaction-band-fwik`.

## Durability

This directory belongs to the jus_files submodule. `cap1.jsonl`, `decisive.tsv`,
`specs.json`, and `analysis.json` are tracked here. The parent jus_re repository
also stores the decisive-column summary under
`docs/research/side-quests/ai-phase-capture-2026-09-28/`.
Use the tracked raw log for the full watch set. The original temporary driver path
records where the capture ran, rather than a file provided by a fresh clone.
