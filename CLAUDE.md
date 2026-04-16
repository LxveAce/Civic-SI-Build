# AI Assistant Reference — 2009 Honda Civic SI Build

> This file provides full context for AI assistants (Claude, ChatGPT, Copilot, etc.) helping with this project. If you are an AI reading this, use the information below to understand the car, the owner's goals, what has been done, and what is planned. Always reference this file before making suggestions.

---

## Owner Profile

- Mechanically capable — does own clutch replacements, intake installs, suspension work, etc.
- New to ECU tuning software (Hondata FlashPro) — has not yet used it
- Comfortable with basic electrical work but not a professional electrician
- Prefers practical, well-researched modifications over impulse buys
- Values the ability to switch between daily-driver comfort and sporty driving

---

## Vehicle

| Field | Value |
|-------|-------|
| Year | 2009 |
| Make/Model | Honda Civic SI |
| Body | Coupe |
| Chassis Code | FG2 |
| Generation | 8th Gen (2006-2011) |
| Engine | K20Z3 — 2.0L DOHC i-VTEC |
| Stock Power | 197 HP @ 7800 RPM / 139 lb-ft @ 6200 RPM |
| Compression | 11.0:1 |
| Transmission | 6-speed manual (stock) |
| Color | Blue |
| Mileage | ~170,000 miles |
| Fuel Requirement | Premium 91+ octane |
| ECU | PRB |
| OBD2 Port Location | Under dash, left of steering column |
| Interior Fuse Box | Driver side lower dash, mini blade fuses |
| Stock Exhaust Diameter | 2.36" (60mm) from catalytic converter back |

---

## Current Modification State

### Installed

1. **Clutch:** Exedy OEM Stage 1 (KHC10) — OEM replacement, organic disc
2. **Intake:** K&N Typhoon 69-1014TS — Hot-side mount with partial heat shield, uses stock fresh air duct
3. **Short Shifter:** Acuity Instruments 3-Way Adjustable — Adjustable throw reduction
4. **Shifter Bushings:** Acuity Instruments Shifter Cable Bushings — Transmission-side, replaces soft OEM rubber

### Purchased, Not Yet Installed

5. **Brakes:** Hawk HPS Street/Sport pads (Front: HB361F.622, Rear: HB145F.570) + R1 Concepts WCPN2-59004 Slotted Black Rotors — Full 4-corner upgrade
6. **Strut Bar:** Megan Racing Front Upper Race Spec (Polished) for Civic & SI 06-11 — BLOCKED by clearance issue (not caused by the intake, root cause unknown)
7. **ECU Tune:** Hondata FlashPro (original, not FlashPro 2) — Not yet flashed, paired, or used
8. **Engine Mounts:** Hybrid Racing 70A durometer polyurethane mount kit

### Planned (Not Purchased)

9. **Valved Exhaust:** DIY build using QTP QTEC25 2.5" electric cutout — Inline cutout after cat, before mufflers. Keeps OEM mufflers. Solenoid/relay controlled. Daily (closed/quiet) and Sport (open/straight pipe) modes.
10. **In-Car PC:** LattePanda 3 Delta permanent install with 7" touchscreen — For Hondata FlashPro management, datalogging, gauges, and exhaust valve control
11. **Headers:** Skunk2 Alpha or PLM 4-2-1 (under consideration, not decided)

---

## Build Philosophy & Decision Context

- **Daily/Sport duality:** The owner wants to switch between quiet daily driving and loud sporty driving. This drives the valved exhaust design and the two-tune Hondata setup.
- **OEM mufflers retained:** The valved exhaust bypasses the mufflers when open but keeps them in the flow path when closed. This is a deliberate choice for maximum quiet in daily mode.
- **No aftermarket valved exhaust exists** for the 8th gen Civic SI. The DIY QTP cutout approach is the only viable path.
- **LattePanda over Raspberry Pi:** Hondata FlashProManager is Windows-only x86. A Pi cannot run it reliably (ARM + Wine + USB serial passthrough = unreliable and dangerous for ECU flashing). The LattePanda runs native Windows x86 with direct 12V input and onboard Arduino GPIO for exhaust valve control.
- **Temporary laptop setup first:** The owner plans to use a laptop + 7" external screen to learn FlashPro before building the permanent LattePanda install. The screen is a shared purchase (used for both setups).
- **Headers are last:** Install order is: exhaust cutout → tune → headers → retune. Headers change exhaust flow significantly and require retuning both calibrations.

---

## Tuning Context

- **Only the intake affects the tune** at this point. All other mods are mechanical.
- **Base map approach:** Start with a Hondata community base map for "stock + intake" on the 8th gen SI. Conservative and safe for daily driving.
- **Two calibrations planned:**
  - **Daily:** Valve closed, conservative timing, smooth idle, good economy
  - **Sport:** Valve open, slightly richer WOT AFR (~11.8:1), more aggressive timing (1-2 deg), lower VTEC engagement (~4500-5000 RPM), optional launch control
- **A single tune works for both valve positions** on the NA K20Z3 (closed-loop O2 corrects the small AFR shift from backpressure changes). Two tunes optimize each mode but aren't strictly necessary.
- **Fuel:** Must run 93 octane (or highest available premium) with any performance tune.

---

## Key Technical Details for AI Reference

### FG2 Interior Fuse Box (for LattePanda Install)
- **Location:** Driver side, lower left dash, behind removable panel
- **Fuse type:** Mini blade
- **Constant 12V source:** Fuse #20 "BACK UP" (7.5A) — always hot, powers clock/radio memory/ECU keep-alive
- **Ignition-switched source:** Fuse #8 "ACC(A)" (7.5A) — live in ACC and RUN key positions
- **Add-a-fuse taps:** Mini blade style. Hot side gets the new 5A fuse, load side gets the original fuse.

### FlashPro Details
- **Type:** Original FlashPro (NOT FlashPro 2 — no Bluetooth)
- **Connection:** USB Mini-B to OBD2 (unit has built-in OBD2 connector)
- **Software:** FlashProManager (Windows only, x86)
- **Calibration files:** .fpc format
- **Datalog files:** .fpdl format
- **ECU pairing:** FlashPro locks to one ECU at a time

### QTP QTEC25 Exhaust Cutout
- **Size:** 2.5"
- **Type:** Electric motor-driven butterfly valve
- **Control:** 12V DC gear motor, polarity-dependent direction (forward = open, reverse = close)
- **Draw:** ~5-8A
- **Position:** After catalytic converter, before resonator/muffler (mid-pipe area)
- **Default state:** Use normally-open relay → valve defaults to CLOSED (quiet) when power is off

---

## File Structure Convention

Each mod folder may contain:
| File | Purpose |
|------|---------|
| `overview.md` | What it is, why chosen, part numbers, current status |
| `brainstorm.md` | Research, alternatives, pros/cons analysis |
| `purchasing.md` | Complete parts list with part numbers and prices |
| `install-guide.md` | Step-by-step installation instructions |

Not every mod needs every file. Simple bolt-ons (clutch, bushings) may only have an overview. Complex projects (LattePanda install, valved exhaust) have all four.

---

## Important Warnings

1. **DO NOT recommend leaning out fuel tables** without dyno verification and wideband AFR monitoring
2. **DO NOT recommend adding ignition timing** beyond base map values without knock monitoring on a dyno
3. **DO NOT suggest a Raspberry Pi** for running Hondata — it has been researched and ruled out (see above)
4. **The Megan Racing strut bar clearance issue** is unresolved — root cause is unknown, it is NOT the intake interfering
5. **The FlashPro has NOT been used yet** — any instructions should assume first-time setup
6. **Stock calibration must be saved** before any flashing — this is the factory reset backup

---

*Last updated: 2026-04-16*
