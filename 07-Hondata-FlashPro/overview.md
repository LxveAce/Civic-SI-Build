# Hondata FlashPro — ECU Tuning

## Status: Purchased, Not Yet Used

## Part Information

| Field | Value |
|-------|-------|
| Part | Hondata FlashPro |
| Type | Original FlashPro (NOT FlashPro 2 — no Bluetooth) |
| Software | FlashProManager (Windows only, x86) |
| Connection | USB Mini-B to OBD2 (built-in OBD2 connector) |
| Pairing | Locks to one ECU at a time |
| Calibration Files | .fpc format |
| Datalog Files | .fpdl format |

## What It Does

The Hondata FlashPro reflashes the stock Honda ECU, enabling:
- Custom fuel maps, ignition timing, VTEC engagement point
- Rev limiter and speed limiter adjustment
- Launch control, flat-foot shifting
- Real-time datalogging (AFR, knock, temps, fuel trims, etc.)
- Real-time gauge display via FlashProManager
- Multiple calibration storage and switching

## Setup Plans

### Phase 1: Temporary Laptop Setup
- Use any Windows laptop + the FlashPro
- Flash a community base map for "stock + intake" on the 8th gen SI
- Learn the software, datalog, monitor AFR and knock
- Add a 7" external screen for live gauges while driving
- See: [Temporary-Setup/](Temporary-Setup/)

### Phase 2: Permanent In-Car PC
- LattePanda 3 Delta mini PC permanently installed in the car
- 7" touchscreen on dash (same screen from Phase 1)
- Mausberry Circuits car power supply for clean power and auto-shutdown
- Wired to FG2 fuse box (constant 12V + ignition-switched 12V)
- Arduino GPIO controls exhaust valve relay (future)
- See: [Permanent-LattePanda-Install/](Permanent-LattePanda-Install/)

### Phase 3: Dual Calibrations
- **Daily tune:** Conservative, valve closed, quiet
- **Sport tune:** Aggressive, valve open, loud
- One-tap switching via touchscreen app (Python/tkinter script)

## Tuning Notes

- The K&N Typhoon 69-1014TS is the only mod that affects the tune currently
- Start with Hondata community base map — conservative and safe
- Do NOT add ignition timing or lean out fuel tables without a dyno tune
- A professional dyno tune ($300-500) is recommended once headers + exhaust are installed
- Always run 93 octane with any performance calibration
- Always save the stock calibration as a backup before any changes
