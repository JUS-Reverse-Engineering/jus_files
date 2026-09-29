# jus_files

Private reference data for Jump Ultimate Stars research. [jus_re](https://github.com/drj613/jus_re)
uses this repository as its `jus_files/` submodule. JUSToolkit also consumes it.
The separate [bound-fullbleed](https://github.com/drj613/bound-fullbleed) game repository
copies selected proof-of-concept assets into `game/assets/poc_jus/`.

## Get the reference files

Clone jus_re with `git clone --recurse-submodules git@github.com:drj613/jus_re.git`.
You need access to both private repositories. From an existing jus_re checkout,
run `git submodule update --init --recursive` to get its pinned data revision.

All files present here are versioned, including generated sprite splits, captures,
local metadata, and save states. The owner requested this policy on 2026-09-29.
No raw cartridge image is present in this checkout. A clone therefore does not
supply the ROM needed to run the emulator.

Commit and push data changes here first, then commit the updated submodule pin
in jus_re. A parent commit alone does not publish submodule content.

## Contents

| Path | Contents |
|---|---|
| `arm9/` | Extracted ARM9/ARM7 code and header metadata |
| `analysis/` | Analysis outputs and binary tables |
| `exported_combat/` | Combat data exports |
| `extracted_chrbin/` | Unpacked character records |
| `ripped_jus_files/` | Bulk asset rip used as source data |
| `extracted/` | Derived assets, including VFX/SFX payloads and rendered previews |
| `sprites/` | Source sheets and generated character split outputs |
| `captures/` | Raw measurements, watch specs, and capture summaries |
| `save_states/` | Gzipped melonDS states and metadata, including the full owner character-mapping source archive |

Read [the savestate index](save_states/INDEX.md) before loading a state.
Read [the sprite guide](sprites/README.md) before refreshing sprite sources.
Research claims and measurement tools belong in jus_re. Use its `GO.md`,
`AGENTS.md`, and `docs/confirmed-facts/` to interpret these files.
A tracked capture preserves evidence; its presence does not establish a PASS.

## arm9/ — the important one for reverse engineering

Regenerate with, from the jus_re checkout:

```bash
python3 scripts/extract_arm9.py /path/to/jus.nds jus_files/arm9
```

Two facts that make this directly usable:

- **The ARM9 binary is uncompressed** and maps 1:1 to RAM at `0x02000000`. So
  `file_offset = runtime_addr - 0x02000000`, with no BLZ decompression step.
- This was verified the strong way, not by inspection: 512 bytes dumped from
  live RAM at `0x02078400` in a running emulator match `arm9.bin` at the
  corresponding offset **byte for byte**.

ARM7 maps to `0x02380000`. `arm9/binaries.json` records the header-derived ROM
offsets, sizes, RAM bases, and entry points.
