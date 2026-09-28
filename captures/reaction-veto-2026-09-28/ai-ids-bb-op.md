# CPU AI behaviour ids 7-23 — static read of two `_b_ files
Method: parser logic reused from `scripts/analysis/aipm_slot_matrix.py` (DSCP
decompress, `AIPM` magic, 23-entry slot array at +0x08). Files chosen:
`bb_b_01.bin` (the file the brief's sample sub-record came from) and
`op_b_03.bin` (the live-fixture file named in the data-layout doc). No
emulator, no patching, no repo edits. All readings below are hypotheses.

## bb_b_01.bin  (payload 3676 bytes)

| id | slot | rec off | +0x04 | +0x0C raw | count | size | sub-records (hex, first 3 if >3) |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0x64 | 0 | 0x00000001 | 1 | 0xBC | 1400e2ff10001000010000000a000000000000000c0010000301000000000000 |
| 2 | 1 | 0x120 | 1 | 0x00000001 | 1 | 0xBC | 2400dcff17002200010000001300000000000000100014000302000000000000 |
| 3 | 2 | 0x1DC | 2 | 0x00000001 | 1 | 0xBC | 2a00dcff2e0018000100000009000000000000000a001a000307000000000000 |
| 4 | 3 | 0x298 | 3 | 0x00000001 | 1 | 0xBC | 5500bfff3b00270001000000140000000000000013001f000302000000000000 |
| 5 | 4 | 0x354 | 4 | 0x00000001 | 1 | 0xBC | 1000dfff10001500010000000a000000000000000a000c000307000000000000 |
| 6 | 5 | 0x410 | 5 | 0x00000001 | 1 | 0xBC | 2400d3ff1d002a00010000001400000000000000110017000307000000000000 |
| 7 | 6 | 0x4CC | 6 | 0x00000001 | 1 | 0xBC | 2300e7ff17001300010000000300000000000000340038000307000000000000 |
| 8 | 7 | 0x588 | 7 | 0x00000001 | 1 | 0xBC | 3a00e8ff1d001800010000000a0000000000000026002c000302000001000000 |
| 9 | 8 | 0x644 | 8 | 0x00000001 | 1 | 0xBC | 1600d4ff1c001700010000000a0000000000000008000e000305000000000000 |
| 10 | 9 | 0x700 | 9 | 0x00000001 | 1 | 0xBC | fdffdbff3f001100010000001400000000000000100013000302000000000000 |
| 11 | 10 | 0x7BC | 10 | 0x00000101 | 1 | 0xBC | 2000f8ff10000800000100000000000000000000100090000000000000000000 |
| 12 | 11 | 0x878 | 11 | 0x00000001 | 1 | 0xBC | 3000dcff28001800010000000a000000000000000c001c000302000000000000 |
| 13 | 12 | 0x934 | 12 | 0x00000001 | 1 | 0xBC | 3c00d0ff44002c00010000001000000000000000300032000505000000000000 |
| 14 | 13 | 0x9F0 | 13 | 0x00000003 | 3 | 0xFC | 2500e1ff0c000c000401000004000000000000001e0036000402e00000000000 4d0009000c000c000411000004000000000000001e0036000402e00000000000 71002d000c000c000421000004000000000000001e0036000402e00000000000 |
| 15 | 14 | 0xAEC | 14 | 0x00000001 | 1 | 0xBC | ad00e4ff890020000001000014000000000000002e0056000402000000000000 |
| 16 | 15 | 0xBA8 | 15 | 0x00000001 | 1 | 0xBC | 2d00daff2d002100010000002800000000000000100044000505000000000000 |
| 17 | 16 | 0xC64 | 16 | 0x00000101 | 1 | 0xBC | 6500eaff260015000100000008000000000000004d0050000505000000000000 |
| 18 | 17 | 0xD20 | 17 | 0x00000005 | 5 | 0x13C | 1600e8ff0c000c000701000007000000000000004b0073000405000000000000 3300f4ff0c000c000711000007000000000000004b0073000405000000000000 500000000c000c000721000007000000000000004b0073000405000000000000  (+2 more) |
| 19-23 | 18-22 | — | — | — | absent | — | array entries 0xFFFFFFFF |
### bb_b_01.bin: first-sub-record word matrix (id x 8 LE u32)

| id | w0 | w1 | w2 | w3 | w4 | w5 | w6 | w7 |
|---|---|---|---|---|---|---|---|---|
| 1 | 0xFFE20014 | 0x00100010 | 0x00000001 | 0x0000000A | 0 | 0x0010000C | 0x00000103 | 0 |
| 2 | 0xFFDC0024 | 0x00220017 | 0x00000001 | 0x00000013 | 0 | 0x00140010 | 0x00000203 | 0 |
| 3 | 0xFFDC002A | 0x0018002E | 0x00000001 | 0x00000009 | 0 | 0x001A000A | 0x00000703 | 0 |
| 4 | 0xFFBF0055 | 0x0027003B | 0x00000001 | 0x00000014 | 0 | 0x001F0013 | 0x00000203 | 0 |
| 5 | 0xFFDF0010 | 0x00150010 | 0x00000001 | 0x0000000A | 0 | 0x000C000A | 0x00000703 | 0 |
| 6 | 0xFFD30024 | 0x002A001D | 0x00000001 | 0x00000014 | 0 | 0x00170011 | 0x00000703 | 0 |
| 7 | 0xFFE70023 | 0x00130017 | 0x00000001 | 0x00000003 | 0 | 0x00380034 | 0x00000703 | 0 |
| 8 | 0xFFE8003A | 0x0018001D | 0x00000001 | 0x0000000A | 0 | 0x002C0026 | 0x00000203 | 0x00000001 |
| 9 | 0xFFD40016 | 0x0017001C | 0x00000001 | 0x0000000A | 0 | 0x000E0008 | 0x00000503 | 0 |
| 10 | 0xFFDBFFFD | 0x0011003F | 0x00000001 | 0x00000014 | 0 | 0x00130010 | 0x00000203 | 0 |
| 11 | 0xFFF80020 | 0x00080010 | 0x00000100 | 0 | 0 | 0x00900010 | 0 | 0 |
| 12 | 0xFFDC0030 | 0x00180028 | 0x00000001 | 0x0000000A | 0 | 0x001C000C | 0x00000203 | 0 |
| 13 | 0xFFD0003C | 0x002C0044 | 0x00000001 | 0x00000010 | 0 | 0x00320030 | 0x00000505 | 0 |
| 14 | 0xFFE10025 | 0x000C000C | 0x00000104 | 0x00000004 | 0 | 0x0036001E | 0x00E00204 | 0 |
| 15 | 0xFFE400AD | 0x00200089 | 0x00000100 | 0x00000014 | 0 | 0x0056002E | 0x00000204 | 0 |
| 16 | 0xFFDA002D | 0x0021002D | 0x00000001 | 0x00000028 | 0 | 0x00440010 | 0x00000505 | 0 |
| 17 | 0xFFEA0065 | 0x00150026 | 0x00000001 | 0x00000008 | 0 | 0x0050004D | 0x00000505 | 0 |
| 18 | 0xFFE80016 | 0x000C000C | 0x00000107 | 0x00000007 | 0 | 0x0073004B | 0x00000504 | 0 |
| 19-23 | — | — | — | — | — | — | — | — |
### bb_b_01.bin: distinct values per word position

| word | n_ids | distinct values |
|---|---|---|
| w0 | 18 | 0xFFBF0055, 0xFFD0003C, 0xFFD30024, 0xFFD40016, 0xFFDA002D, 0xFFDBFFFD, 0xFFDC0024, 0xFFDC002A, 0xFFDC0030, 0xFFDF0010, 0xFFE10025, 0xFFE20014, … (18 total) |
| w1 | 17 | 0x00080010, 0x000C000C, 0x00100010, 0x0011003F, 0x00130017, 0x00150010, 0x00150026, 0x0017001C, 0x0018001D, 0x00180028, 0x0018002E, 0x00200089, … (17 total) |
| w2 | 4 | 0x00000001, 0x00000100, 0x00000104, 0x00000107 |
| w3 | 11 | 0, 3, 4, 7, 8, 9, 0x0A, 0x10, 0x13, 0x14, 0x28 |
| w4 | 1 | 0 (constant) |
| w5 | 18 | 0x000C000A, 0x000E0008, 0x0010000C, 0x00130010, 0x00140010, 0x00170011, 0x001A000A, 0x001C000C, 0x001F0013, 0x002C0026, 0x00320030, 0x0036001E, … (18 total) |
| w6 | 9 | 0, 0x00000103, 0x00000203, 0x00000204, 0x00000503, 0x00000504, 0x00000505, 0x00000703, 0x00E00204 |
| w7 | 2 | 0, 1 |
## op_b_03.bin  (payload 3484 bytes)
| id | slot | rec off | +0x04 | +0x0C raw | count | size | sub-records (hex, first 3 if >3) |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0x64 | 0 | 0x00000001 | 1 | 0xBC | 1700dcff0f00140001000000070000000000000007000b000300000000000000 |
| 2 | 1 | 0x120 | 1 | 0x00000101 | 1 | 0xBC | 1e00d4ff280010000100000001000000000000001b001d000300000000000000 |
| 3 | 2 | 0x1DC | 2 | 0x00000001 | 1 | 0xBC | 3000ebff2f000c00000100000700000000000000080018000200000000000000 |
| 4 | 3 | 0x298 | 3 | 0x00000001 | 1 | 0xBC | 6600e2ff1400100001000000080000000000000019001d000305000000000000 |
| 5 | 4 | 0x354 | 4 | 0x00000001 | 1 | 0xBC | 0200dbff0f001b0001000000070000000000000008000b000301000000000000 |
| 6 | 5 | 0x410 | 5 | 0x00000001 | 1 | 0xBC | 1500c9ff12002300010000000f00000000000000110014000302000000000000 |
| 7 | 6 | 0x4CC | 6 | 0x00000001 | 1 | 0xBC | 4000e5ff12001b000100000004000000000000002d0030000300000000000000 |
| 8 | 7 | 0x588 | 7 | 0x00000001 | 1 | 0xBC | 1500e7ff18001100010000000e000000000000002c002f000305000001000000 |
| 9 | 8 | 0x644 | 8 | 0x00000001 | 1 | 0xBC | 1600dbff130011000100000007000000000000000b001f000302000000000000 |
| 10 | 9 | 0x700 | 9 | 0x00000001 | 1 | 0xBC | 0c00e2ff11001100010000000200000000000000170019000300000000000000 |
| 11 | 10 | 0x7BC | 10 | 0x00000000 | 0 | 0xBC | (empty record) |
| 12 | 11 | 0x878 | 11 | 0x00000001 | 1 | 0xBC | 2600d4ff28001000010000000200000000000000170019000300000000000000 |
| 13 | 12 | 0x934 | 12 | 0x00000001 | 1 | 0xBC | d800dcff19001900020000000a000000000000006a006e000506000000000000 |
| 14 | 13 | 0x9F0 | 13 | 0x00000001 | 1 | 0xBC | 340077ff1a003300010000000a0000000000000027002b000506000000000000 |
| 15 | 14 | 0xAAC | 14 | 0x00000001 | 1 | 0xBC | ad00e4ff1a001400010000000c000000000000007f0081000506000000000000 |
| 16 | 15 | 0xB68 | 15 | 0x00000001 | 1 | 0xBC | 0800e3ff21001b000100000000000000640000000c005b000507000000000000 |
| 17 | 16 | 0xC24 | 16 | 0x00000001 | 1 | 0xBC | 3a00e1ff17001900010000000400000000000000080027000500000000000000 |
| 18 | 17 | 0xCE0 | 17 | 0x00000000 | 0 | 0xBC | (empty record) |
| 19-23 | 18-22 | — | — | — | absent | — | array entries 0xFFFFFFFF |
### op_b_03.bin: first-sub-record word matrix (id x 8 LE u32)

| id | w0 | w1 | w2 | w3 | w4 | w5 | w6 | w7 |
|---|---|---|---|---|---|---|---|---|
| 1 | 0xFFDC0017 | 0x0014000F | 0x00000001 | 0x00000007 | 0 | 0x000B0007 | 0x00000003 | 0 |
| 2 | 0xFFD4001E | 0x00100028 | 0x00000001 | 0x00000001 | 0 | 0x001D001B | 0x00000003 | 0 |
| 3 | 0xFFEB0030 | 0x000C002F | 0x00000100 | 0x00000007 | 0 | 0x00180008 | 0x00000002 | 0 |
| 4 | 0xFFE20066 | 0x00100014 | 0x00000001 | 0x00000008 | 0 | 0x001D0019 | 0x00000503 | 0 |
| 5 | 0xFFDB0002 | 0x001B000F | 0x00000001 | 0x00000007 | 0 | 0x000B0008 | 0x00000103 | 0 |
| 6 | 0xFFC90015 | 0x00230012 | 0x00000001 | 0x0000000F | 0 | 0x00140011 | 0x00000203 | 0 |
| 7 | 0xFFE50040 | 0x001B0012 | 0x00000001 | 0x00000004 | 0 | 0x0030002D | 0x00000003 | 0 |
| 8 | 0xFFE70015 | 0x00110018 | 0x00000001 | 0x0000000E | 0 | 0x002F002C | 0x00000503 | 0x00000001 |
| 9 | 0xFFDB0016 | 0x00110013 | 0x00000001 | 0x00000007 | 0 | 0x001F000B | 0x00000203 | 0 |
| 10 | 0xFFE2000C | 0x00110011 | 0x00000001 | 0x00000002 | 0 | 0x00190017 | 0x00000003 | 0 |
| 11 | — | — | — | — | — | — | — | — |
| 12 | 0xFFD40026 | 0x00100028 | 0x00000001 | 0x00000002 | 0 | 0x00190017 | 0x00000003 | 0 |
| 13 | 0xFFDC00D8 | 0x00190019 | 0x00000002 | 0x0000000A | 0 | 0x006E006A | 0x00000605 | 0 |
| 14 | 0xFF770034 | 0x0033001A | 0x00000001 | 0x0000000A | 0 | 0x002B0027 | 0x00000605 | 0 |
| 15 | 0xFFE400AD | 0x0014001A | 0x00000001 | 0x0000000C | 0 | 0x0081007F | 0x00000605 | 0 |
| 16 | 0xFFE30008 | 0x001B0021 | 0x00000001 | 0 | 0x00000064 | 0x005B000C | 0x00000705 | 0 |
| 17 | 0xFFE1003A | 0x00190017 | 0x00000001 | 0x00000004 | 0 | 0x00270008 | 0x00000005 | 0 |
| 18-23 | — | — | — | — | — | — | — | — |
### op_b_03.bin: distinct values per word position

| word | n_ids | distinct values |
|---|---|---|
| w0 | 16 | 0xFF770034, 0xFFC90015, 0xFFD4001E, 0xFFD40026, 0xFFDB0002, 0xFFDB0016, 0xFFDC0017, 0xFFDC00D8, 0xFFE1003A, 0xFFE2000C, 0xFFE20066, 0xFFE30008, … (16 total) |
| w1 | 15 | 0x000C002F, 0x00100014, 0x00100028, 0x00110011, 0x00110013, 0x00110018, 0x0014000F, 0x0014001A, 0x00190017, 0x00190019, 0x001B000F, 0x001B0012, … (15 total) |
| w2 | 3 | 0x00000001, 0x00000002, 0x00000100 |
| w3 | 10 | 0, 1, 2, 4, 7, 8, 0x0A, 0x0C, 0x0E, 0x0F |
| w4 | 2 | 0, 0x64 |
| w5 | 15 | 0x000B0007, 0x000B0008, 0x00140011, 0x00180008, 0x00190017, 0x001D0019, 0x001D001B, 0x001F000B, 0x00270008, 0x002B0027, 0x002F002C, 0x0030002D, … (15 total) |
| w6 | 8 | 0x00000002, 0x00000003, 0x00000005, 0x00000103, 0x00000203, 0x00000503, 0x00000605, 0x00000705 |
| w7 | 2 | 0, 1 |
## The 8 word positions (step 4)
Words map to the doc's sub-record field table (+0x00..+0x1F):

- **w0** = s16 pair at +0x00/+0x02 — varies across nearly all ids (18/17 distinct).
  Candidate parameter; signed with both signs occurring, consistent with the
  doc's coordinate hypothesis. Units not established by these bytes.
- **w1** = u16 pair at +0x04/+0x06 — varies (18/15 distinct). Candidate
  parameter; the doc's extents/sizes reading is plausible, not proven.
- **w2** = u32 at +0x08 — **not a semantic parameter**: low u16 is constant
  within a record, high u16 is the sub-record index (bb id 14: 0x104 ->
  0x1104 -> 0x2104; bb id 18: 0x107 -> 0x1107 -> 0x2107). An ordering key.
- **w3** = s32 at +0x0C — varies (0..40). Candidate parameter, constant
  within a record.
- **w4** = s32 at +0x10 — constant 0 in 17 of 18 records; only op id 16
  sets it (100). Optional modifier.
- **w5** = u16 pair at +0x14/+0x16 — varies; ordered (lower < upper) per the
  doc. Candidate parameter, a range.
- **w6** = bytes +0x18..+0x1B — low byte is the **class byte** (ids 1-12 ->
  {2,3}, ids 13+ -> {4,5}, 0 = near-empty record); +0x19 small enum; +0x1A
  signed param; +0x1B flag.
- **w7** = bytes +0x1C..+0x1F — +0x1C flag (set only by id 8 in both files);
  +0x1D..+0x1F reserved/zero.
## Per-id readings (step 5) — all hypotheses
- **id 7**: single sub-record, class 3, small w3 (3-4) and a tight w5 range
  (52-56 / 45-48) — a low-magnitude single-step behaviour; the bytes do not
  name it. **Unresolved.**
- **id 8**: the only id in either file with sub-record byte +0x1C = 1 (w7=1) —
  a unique flag distinguishing it from every other id; what the flag triggers
  is not in the data. **Unresolved beyond the flag.**
- **id 9**: single sub-record, class 3, w3 = 0x0A/0x07 — no distinguishing
  bytes. **Unresolved.**
- **id 10**: bb w0 = (-3,-5), the only both-negative coordinate pair in
  bb_b_01; op w0 = (12,-30). **Unresolved.**
- **id 11**: bb's record is near-empty (class byte +0x18 = 0, w3 = 0) and
  op's slot 10 is entirely empty (+0x0C = 0) — consistent with the doc's
  "0 = empty or near-empty record"; id 11 carries no usable behaviour for
  these two characters. **Unresolved.**
- **id 12**: the only code-anchored name — the doc ties +0x3A == 0xC to the
  phase-8 branch; the data itself is an ordinary single sub-record, class 3.
- **id 13**: first id of the 13+ family (class byte 5 in both files) and the
  first id the remap at 0x02174ED4 tests (`cmp r5,#0xd`); op's w0 =
  (216,-36) is the largest coordinate magnitude in either file. Hypothesis:
  base of the opponent-state family. Semantics beyond the class boundary
  **unresolved**.
- **id 14**: count=3 in bb — three sub-records sharing w1/w3/w5/class and
  differing only in w0 and the w2 index: a 3-step positional sequence with
  identical parameters. op has a single sub-record with the most negative
  coordinate (-137). Hypothesis: multi-step sequence. **Unresolved.**
- **id 15**: w0 = (173,-28) is byte-identical in bb_b_01 and op_b_03 — the
  only id whose coordinate pair is shared across these two characters,
  suggesting a fixed game-space anchor rather than per-character tuning.
  **Unresolved beyond that.**
- **id 16**: op's record is the only one in either file with nonzero w4
  (+0x10 = 100); bb's has the largest w3 in bb (40). **Unresolved.**
- **id 17**: single sub-record, class 5, no distinguishing bytes. **Unresolved.**
- **id 18**: count=5 in bb — five sub-records sharing w1/w3/w5/class with w0's
  x running 22, 51, 80, ... (arithmetic +29 per step): a 5-step sweep at
  fixed parameters; op's slot 17 is empty. Hypothesis: multi-step sweep.
  **Unresolved.**
- **ids 19-23**: no record in either file (array entries 0xFFFFFFFF). Per the
  doc's corpus table, slots 18-21 are populated in only 16/16/11/11 files
  and slot 22 in none — resolving these needs a character that populates them
  (`aipm_slot_matrix.py who 18..22`). **Unresolved.**

## Remap note
The brief said ids 13-18 are remapped; the doc's disassembly at
0x02174ED4-0x02174EF0 shows the rewrite branch is entered only when the
incoming id is 13 or 14 (`cmp r5,#0xd; sub r0,r5,#0xd; cmp r0,#1`), delta
2*(signed byte off ctx). Ids 15-18 are not rewritten there — discrepancy
between the brief and the measured code, flagged as stated.

## Consistency checks (parse validation)

- Record chain tiles both payloads exactly (bb ends 0xE5C = 3676, op 0xD9C =
  3484); every record offset + size = next offset.
- +0x04 self-index matches the slot for all 34 present records.
- w2 steps by exactly 0x1000 within multi-sub-record records; class byte
  partitions at id 13 in both files, matching the doc.
