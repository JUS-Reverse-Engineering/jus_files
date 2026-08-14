# jus_files

Extracted and derived data from the Jump Ultimate Stars cartridge. Consumed as a
submodule by [JUSToolkit](https://github.com/drj613/JUSToolkit).

Raw cartridge images (`*.nds`, `*.sav`) are deliberately **not** tracked — see
`.gitignore`. Everything here is derived from the cart and can be regenerated.

## Contents

| Path | What it is |
|---|---|
| `arm9/` | ARM9/ARM7 code extracted straight from the cart header |
| `analysis/` | Analysis output over the extracted data |
| `exported_combat/` | Combat data exports |
| `extracted_chrbin/` | Unpacked `chr_b.bin` character records |
| `ripped_jus_files/` | Bulk asset rip (treated as read-only) |

## arm9/ — the important one for reverse engineering

Regenerate with, from the JUSToolkit checkout:

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
