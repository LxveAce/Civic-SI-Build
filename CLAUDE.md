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

1. **Clutch & Flywheel:** Exedy Stage 1 Organic (08806) + Exedy Lightweight Flywheel (HF02), both from shop.redline360.com — **$960.43** (bundled with strut bar, incl. tax/shipping)
2. **Intake:** K&N Typhoon 69-1014TS — Hot-side mount with partial heat shield, uses stock fresh air duct — **$504.17**
3. **Short Shifter:** Acuity Instruments 3-Way Adjustable — Adjustable throw reduction — **$622.20** (with bushings, incl. tax/shipping)
4. **Shifter Bushings:** Acuity Instruments Shifter Cable Bushings — Transmission-side, replaces soft OEM rubber — (included in #3)
5. **Tires:** Continental ExtremeContact DWS06 Plus 215/45ZR17 91W XL (15572680000) — **$715.00** (purchased 2026-06-16)

### Purchased, Not Yet Installed

6. **Brakes:** Hawk HPS Street/Sport pads (Front: HB361F.622, Rear: HB145F.570) + R1 Concepts WCPN2-59004 Slotted Black Rotors — **$532.14** ($309.69 rotors + $222.45 pads)
7. **Strut Bar:** Megan Racing Front Upper Race Spec (Polished) for Civic & SI 06-11 — BLOCKED by clearance issue (included in #1 bundle)
8. **ECU Tune:** Hondata FlashPro (original, not FlashPro 2) — Not yet flashed, paired, or used — **$859.59**
9. **Engine Mounts:** Hybrid Racing 70A durometer polyurethane mount kit — **$657.15**

**Total spent to date: $4,850.68**

### Planned (Not Purchased)

9. **Valved Exhaust:** DIY build using QTP QTEC30 3" electric cutout — 3" pipe from header to cutout, 3" dump pipe when open, 3"→2.5" reducer for muffled path. Keeps OEM resonator + muffler. Daily (closed/quiet) and Sport (open/straight pipe) modes. ~$485 parts + $150-250 muffler shop labor.
10. **In-Car PC:** LattePanda 3 Delta permanent install with 7" touchscreen — For Hondata FlashPro management, datalogging, gauges, and exhaust valve control
11. **Headers:** Skunk2 Alpha 4-2-1 (412-05-1930, ~$700-800) with stepped primaries (1.625"→1.75") + Berk Technology HFC (~$300-400). Best-performing header available for FG2. 10-18 WHP gain. See 13-Headers/ for full analysis.
12. **Intake Manifold:** Skunk2 Ultra Street (307-05-0600, ~$565-620) + bored stock DBW throttle body (62mm→66mm, ~$150 via Drag Cartel or HeelToe Auto). See 14-Intake-Manifold/.
13. **Pulleys + Harmonic Balancer:** ATI Super Damper (918477, ~$360-380) for proper harmonic damping + NST accessory pulleys for underdrive. See 15-Pulleys-and-Harmonic-Balancer/.
14. **Flex Fuel & Fuel System:** Continental ethanol sensor + Bosch EV14 550cc injectors + Acuity K-Series fuel rail + DeatschWerks DW200 fuel pump. E85 adds 5-15 WHP on NA over pump gas (modest vs turbo). Best value at E30-E40 blend. See 19-Flex-Fuel-and-Fuel-System/.
15. **Clutch Hydraulics:** Hybrid Racing CMC (or RSX Type-S CMC swap) + RSX OEM CSC + stainless braided clutch line + DOT 4 fluid. 170k-mile reliability upgrade — stock CMC/CSC are a known failure point. See 07-Clutch-Hydraulics/.
16. **Suspension:** BC Racing BR coilovers (A-18-BR, ~$1,195) + Skunk2 Pro Series rear camber arms (516-05-0625, ~$333) + Energy Suspension master bushing kit (16.18114G, ~$278) + Hardrace trailing arm bushings (6926, ~$150) + Progress sway bars (front 27mm + rear 24mm adjustable) + K-Tuned roll center adjusters + new tie rods/ball joints + alignment. Complete suspension overhaul targeting daily/sport adjustability. See 17-Suspension/.

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
- **Fuel:** Must run 93 octane (or highest available premium) with pump gas tune. E85 flex fuel planned as final power adder (5-15 WHP on NA — modest vs turbo).
- **Full bolt-on target:** 220-240 WHP on pump gas, 230-250 WHP on E85 (NA E85 gains are modest: 5-15 WHP, not turbo-level)

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

### QTP QTEC30 Exhaust Cutout
- **Size:** 3" (upgraded from originally planned 2.5" QTEC25)
- **Type:** Electric motor-driven butterfly valve
- **Control:** 12V DC gear motor, polarity-dependent direction (forward = open, reverse = close)
- **Draw:** ~5-8A
- **Position:** After catalytic converter, before resonator/muffler (mid-pipe area)
- **Default state:** Use normally-open relay → valve defaults to CLOSED (quiet) when power is off
- **Dump path:** 3" straight pipe to exit tip
- **Muffled path:** 3"→2.5" reducer cone to stock resonator + muffler

---

## File Structure Convention

Every mod folder contains AT LEAST these two files (as of 2026-04-20):
| File | Purpose |
|------|---------|
| `overview.md` | What it is, why chosen, part numbers, current status |
| `install-guide.md` | Step-by-step install / maintenance procedure — tools, torque specs, phased walkthrough, first-start checks, common mistakes, cross-references to related mods and `docs/torque-specs.md` |

Complex mods also contain:
| File | Purpose |
|------|---------|
| `brainstorm.md` | Research, alternatives, pros/cons analysis |
| `purchasing.md` | Complete parts list with part numbers and prices |

The `install-guide.md` set was filled in on 2026-04-20 for all 19 mod folders. The authorial voice across all guides is first-person owner ("I'll...", "honestly..."), reliability-first (engine longevity > power), no emojis, no marketing copy, real part numbers only, heavy cross-referencing between related mods.

---

## Important Warnings

1. **Reliability over power, always.** Owner stated this in caps: engine life comes first. Leave power on the table before you leave a safety margin. Applies to every tune, every part, every decision where there's a trade-off.
2. **Every tune = two maps:** Daily (quiet, conservative) + Sport (aggressive-within-envelope). Never ship a single map.
3. **DO NOT recommend leaning out fuel tables** without dyno verification and wideband AFR monitoring
4. **DO NOT recommend adding ignition timing** beyond base map values without knock monitoring on a dyno
5. **DO NOT suggest a Raspberry Pi** for running Hondata — researched and ruled out
6. **The Megan Racing strut bar is DEFERRED, not blocked.** Don't diagnose clearance now — BC Racing BR coilovers (Phase 5) will change strut-top geometry anyway. Revisit post-coilover install.
7. **The FlashPro has NOT been used yet** — assume first-time setup
8. **Stock calibration must be saved** before any flashing — the factory reset button
9. **Cross-reference interactions between mods** whenever writing a doc. "If you're doing X anyway, Y becomes easier/moot/different."

## Install Guide Pass (2026-04-20)

Every mod folder now has a dedicated `install-guide.md` — 19 new files totaling ~62,000 words. Each guide follows the same template (Reality Check → Prerequisites → Tools Required → Parts List → phased Step-by-Step → First Start → Common Mistakes → See Also). The guides cross-reference each other for bundled-labor opportunities (e.g., 03-Clutch-and-Flywheel + 07-Clutch-Hydraulics + 02-Short-Shifter share a trans-out teardown; 05-Timing-Chain + 06-Ignition-Refresh share VTC actuator labor; 09-Cooling + 13-Headers + 14-IM + 15-Pulleys + 16-Cylinder-Head all bundle during a major Phase 4.5 teardown).

## New Folders and Docs (Added 2026-04-18)

Additions filling gaps the original scope missed:

- **`06-Ignition-Refresh/`** — Plugs + OEM coils + VTC actuator (14310-RBC-003 revised part). Must happen before any dyno tune.
- **`09-Cooling-System/`** — Koyorad aluminum radiator + OEM thermostat/hoses/water pump. Plastic end tank failure insurance + E85 heat headroom.
- **`11-Wideband-AFR/`** — AEM X-Series 30-0300. Required before any tune. Bung welds into Skunk2 Alpha collector during header install.
- **`10-Hondata-FlashPro/tuning-workflow-and-maps.md`** — Daily/Sport map rules, reliability-first ceilings, CSV export workflow for working with Claude on tune analysis.
- **`13-Headers/install-guide.md`** — Full install with stud-prep schedule and shop-vs-DIY decision logic.
- **`docs/torque-specs.md`** — Every fastener I'll touch, OEM spec, cross-referenced.
- **`docs/maintenance-parts-catalog.md`** — Every OE + aftermarket part number in one place.
- **`docs/baseline-logs.md`** — A/B datalog protocol for every mod milestone.

## Key Parts Decision Updates (Post-Research 2026-04-18)

| Item | Previous | Now | Reason |
|------|----------|-----|--------|
| Flex fuel injectors | ID1050x | **Bosch EV14 550cc** | ID1050x is 3.4x oversized for 250 WHP target; hurts idle and cold start |
| Flex fuel pump | Leaning DW200 | **DW300C** | DW200 marginal on E85 headroom; reliability-first rule |
| Strut bar status | "Blocked — diagnose" | "Deferred — wait for coilovers" | Pillow-ball camber plates will change strut-top geometry |
| VTC actuator | Not listed | **OEM 14310-RBC-003 (revised)** | Universal 170k fix for cold-start rattle |
| Radiator | Stock replacement | **Koyorad HH060063 (all-aluminum)** | Plastic end tank failure known issue + E85 heat |

---

*Last updated: 2026-04-20*
