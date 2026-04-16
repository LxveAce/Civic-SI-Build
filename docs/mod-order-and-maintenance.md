# Chronological Mod Order & 170k-Mile Maintenance Plan

## 2009 Honda Civic SI (FG2) — K20Z3, ~170,000 miles, 6MT

This file outlines the recommended order of execution for all planned modifications, which mods can be done standalone vs. together, and the maintenance items critical at 170,000 miles. **Maintenance intervals are based on community experience (8thcivic.com, Reddit r/CivicSi, K-series forums) — NOT Honda manufacturer intervals**, which are widely considered too conservative for a 17-year-old, 170k-mile sport compact.

---

## Phase 0: Critical Maintenance (Do First — Before Any More Mods)

These are reliability items that should be addressed before adding power or stress to the drivetrain. At 170k miles, some of these are overdue.

| # | Item | Why | Community Interval | Est. Cost (DIY) | Est. Cost (Shop) |
|---|------|-----|--------------------|-----------------|-------------------|
| 1 | **Timing chain inspection** | K20Z3 uses a timing chain, not a belt — no replacement interval. BUT: chain stretch is real at 170k. Stretched chain causes retarded cam timing, VTEC engagement issues, and eventually jumps teeth. **Owner already knows this needs checking.** | Inspect at 150k+. Replace if stretch measured or chain noise present. | $20 (inspection) / $300-500 (replacement parts) | $100 (inspection) / $800-1,200 (replacement) |
| 2 | **Valve adjustment** | K20Z3 has solid lifters (no hydraulic lash adjusters). Valves go tight over time — tight valves burn. Community consensus: check every 30k-60k miles on a driven SI. At 170k, if never done or unknown history, this is urgent. | Every 30,000-60,000 miles | $10 (feeler gauges) | $150-250 |
| 3 | **Spark plugs** | NGK ILZKR7B-11S (stock iridium, pre-gapped). Even iridium plugs degrade by 100k. At 170k, if original, they're well past end of life. Misfires, poor fuel economy, lost power. | Every 60,000-80,000 miles (community). Honda says 100k — too long. | $40 (set of 4) | $80-120 |
| 4 | **Coolant flush + thermostat** | OEM Honda Type 2 coolant (blue). At 170k, the coolant has been through thousands of heat cycles. Thermostat can stick partially open (overcooling) or closed (overheating). Replace both proactively. | Coolant every 50,000-60,000 miles. Thermostat at 100k+ or with coolant flush. | $30 coolant + $15 thermostat | $100-150 |
| 5 | **Transmission fluid change** | Honda MTF or Amsoil Synchromesh. 8th gen SI 6MT synchros are sensitive to fluid quality. Notchy 2nd gear is often a fluid issue, not a synchro issue. | Every 30,000-40,000 miles | $25 (3 quarts Honda MTF) | $80-120 |
| 6 | **Brake fluid flush** | DOT 4 (Motul RBF 600 or ATE TYP 200). Brake fluid is hygroscopic — absorbs water, boiling point drops, internal corrosion increases. If never flushed, the fluid is original from 2009. | Every 2 years or 30,000 miles | $15 | $80-100 |
| 7 | **Clutch fluid flush** | Same as brake fluid but separate reservoir on the FG2. Especially important before the CMC/CSC upgrade. | Every 2 years or 30,000 miles | $10 | $50-80 |
| 8 | **Serpentine belt** | Visual inspection — cracking, glazing, squealing. At 170k, likely on the 2nd or 3rd belt. Replace if any signs of wear. | Every 60,000-80,000 miles or at first sign of wear | $25 | $80-120 |
| 9 | **Water pump** | K20Z3 water pump is driven by the timing chain. Inspect during timing chain inspection. Weeping from the weep hole = replace immediately. | Inspect at timing chain service. Replace proactively at 150k+. | $50 (pump) | Included in timing chain labor |
| 10 | **Motor oil + filter** | Honda recommends 0W-20, but community consensus for a 170k-mile K20Z3 that's driven hard: **5W-30 full synthetic** (Mobil 1, Pennzoil Platinum, or Castrol Edge). Thicker oil compensates for worn bearing clearances. | Every 5,000-6,000 miles with synthetic. Honda says 7,500 — too long for an SI driven spiritedly. | $35 | $60-80 |
| 11 | **PCV valve** | 17130-RTA-000 or equivalent. Cheap, easy, often neglected. Failed PCV causes oil consumption, rough idle, and boost leaks if ever turbo'd. | Every 60,000-80,000 miles | $10 | $30-50 |

### Timing Chain Deep Dive

The K20Z3 timing chain is rated for the life of the engine, but "life of the engine" assumes Honda's idea of a normal lifecycle (~200k miles of grandma driving). On a 170k-mile SI that's been driven like an SI:

- **How to check:** Measure cam timing with the Hondata FlashPro. Retarded cam timing (more than 2-3 degrees off spec) indicates chain stretch. A mechanic can also check with a dial indicator on the tensioner.
- **Chain noise:** A rattling or slapping noise at cold start (first 5-10 seconds) that goes away once oil pressure builds is the classic symptom of a stretched chain with a maxed-out tensioner.
- **If the chain is fine:** No action needed. Recheck at 200k.
- **If the chain is stretched:** Replace chain, tensioner, guides, and VTC actuator as a set. Do NOT replace just the chain. Budget $300-500 in parts, $600-900 in labor (or 8-12 hours DIY).

---

## Phase 1: Immediate Installs (Already Purchased, No Dependencies)

These mods are already purchased and sitting on the shelf. Install order within this phase doesn't matter — they're all standalone.

| Order | Mod | Time (DIY) | Standalone? | Notes |
|-------|-----|-----------|-------------|-------|
| 1A | **Clutch hydraulics (CMC/CSC)** | 3-5 hrs | Yes | Do this before anything else. 170k miles = ticking time bomb. Improves pedal feel immediately. |
| 1B | **Engine mounts (Hybrid Racing 70A)** | 3-4 hrs | Yes | Reduces wheel hop, improves shift feel. NVH increase is noticeable but livable. |
| 1C | **Brakes (Hawk HPS + R1 Concepts rotors)** | 2-3 hrs | Yes | Full 4-corner upgrade. Bed the pads properly (follow Hawk's bedding procedure). Do this before you have more power to stop. |
| 1D | **Strut bar (Megan Racing)** | 30 min | **Blocked** | Clearance issue needs diagnosis first. May need spacers or modification. |
| 1E | **Hondata FlashPro — first flash** | 1-2 hrs | Yes | Register unit, flash base map, verify no CELs. Don't tune yet — just get it online. This enables datalogging for all future work. |

**Recommended order within Phase 1:** 1A → 1C → 1B → 1E → 1D (if unblocked)

- CMC/CSC first because it's a reliability risk
- Brakes second because more power needs more stopping
- Engine mounts third because they don't affect reliability
- FlashPro fourth to start datalogging before adding power mods
- Strut bar last (blocked anyway)

---

## Phase 2: Exhaust System (Must Be Done Together)

The valved exhaust and headers are interrelated. The recommended approach is to install the exhaust cutout first, tune it, then add headers and retune.

| Order | Mod | Time (DIY) | Standalone? | Notes |
|-------|-----|-----------|-------------|-------|
| 2A | **Valved exhaust (QTP QTEC30 cutout)** | 4-6 hrs (shop recommended for welding) | Semi-standalone | Install cutout + dump pipe + reducer. Get both tunes working (valve open/closed). Can be done without headers using the stock manifold. |
| 2B | **Headers (Skunk2 Alpha + Berk HFC)** | 6-10 hrs DIY / 3-5 hrs shop | **Must be done with 2A complete** | PB Blaster manifold studs 3-5 days before. Professional install recommended ($300-500 labor) due to seized stud risk at 170k. |
| 2C | **Hondata retune (dyno)** | 2-3 hrs on dyno | **Must be done after 2A+2B** | Tune both calibrations (daily quiet + sport loud) with headers installed. Verify AFR in both valve positions. Budget $300-500 for dyno tune. |

**Important:** Do NOT install headers without planning the exhaust cutout. Headers change the entire exhaust flow, and the cutout position needs to account for header length + HFC placement. Install the cutout first (2A), validate it works, then add headers (2B) and retune everything (2C).

**Stud prep is critical:** Start PB Blaster on the exhaust manifold studs at least 3-5 days before the header install. Heat cycle the car + spray daily. At 170k miles, these studs WILL be seized. Have new M10x1.25 stainless studs and copper-plated flange nuts ready.

---

## Phase 3: Intake System (Must Be Done Together, After Exhaust)

The intake manifold and throttle body work together and require a retune after install.

| Order | Mod | Time (DIY) | Standalone? | Notes |
|-------|-----|-----------|-------------|-------|
| 3A | **Intake manifold (Skunk2 Ultra Street)** | 3-5 hrs | **Paired with 3B** | Can technically be installed alone, but doing it with the TB at the same time saves a retune. |
| 3B | **Bored throttle body (stock DBW → 66mm)** | N/A (send out for boring) | **Paired with 3A** | Send the stock TB to Drag Cartel or HeelToe Auto for boring to 66mm. Lead time: 1-2 weeks. Order this BEFORE buying the manifold so both arrive together. |
| 3C | **Hondata retune (dyno)** | 2-3 hrs on dyno | **Must be done after 3A+3B** | Retune for the new manifold + TB. This is the "full bolt-on" tune. Budget $300-500. |

**Why after exhaust:** The intake manifold tune depends on exhaust flow. If you tune the manifold first and then change headers, you need to retune again (wasted dyno time and money). Headers → intake manifold → single comprehensive tune is more efficient.

**Note:** The K&N Typhoon cold air intake (already installed) remains in the system. The flow path is: K&N filter → intake pipe → bored TB → Skunk2 Ultra Street manifold → K20Z3.

---

## Phase 4: Rotating Assembly (Standalone, After Full Bolt-On Tune)

| Order | Mod | Time (DIY) | Standalone? | Notes |
|-------|-----|-----------|-------------|-------|
| 4A | **Pulleys + Harmonic Balancer (ATI Super Damper + NST kit)** | 3-5 hrs | Yes | Standalone install. Requires crank bolt removal (impact gun needed, 250+ ft-lbs). Does NOT require a retune — it's a mechanical change, not an airflow change. |

**Why after the tune:** The pulley system doesn't affect tuning, but it does affect accessory drive belt routing. Install it after the full bolt-on tune so you're not juggling multiple changes at once. The ATI Super Damper is especially important at 170k miles — the stock damper's elastomer is likely degraded.

---

## Phase 5: Flex Fuel System (Final Power Adder)

| Order | Mod | Time (DIY) | Standalone? | Notes |
|-------|-----|-----------|-------------|-------|
| 5A | **Fuel pump (DeatschWerks DW300C)** | 1-2 hrs | Can be done early (standalone) | Drop-in replacement. Can be installed anytime, even before injectors — the stock ECU handles it fine. |
| 5B | **Fuel rail + injectors (Acuity + ID1050x)** | 2-3 hrs | **Paired with 5C** | Install rail, injectors, and ethanol sensor at the same time. |
| 5C | **Ethanol content sensor + fuel lines** | 1-2 hrs | **Paired with 5B** | Inline sensor before fuel rail. -6 AN PTFE braided lines. |
| 5D | **Hondata flex fuel tune (dyno)** | 3-4 hrs on dyno | **Must be done after 5A+5B+5C** | Flex fuel calibration: gasoline map + E85 map with real-time interpolation. This is the most complex tune in the build. Budget $400-600. |

**Why last:** E85 is the biggest power adder (5-15 WHP) but also the most complex. You want the full bolt-on tune dialed in on pump gas first, THEN add flex fuel as the final layer. This way the tuner has a known-good base to build the flex fuel calibration on top of.

**Clutch warning:** Full bolt-on + E85 targets 230-250 WHP / 165-180 lb-ft. The Exedy 08806 Stage 1 is rated to ~280-300 WHP / ~200-210 lb-ft. You are within the margin. Monitor for clutch slip under hard acceleration in 3rd-6th gear after the E85 tune.

---

## Phase 6: In-Car PC (Quality of Life — Anytime After FlashPro)

| Order | Mod | Time (DIY) | Standalone? | Notes |
|-------|-----|-----------|-------------|-------|
| 6A | **LattePanda 3 Delta permanent install** | 6-10 hrs (spread over a weekend) | Yes | Can be done anytime after the FlashPro is registered and working. The PC replaces the laptop for Hondata management and adds exhaust valve control via Arduino GPIO. |

**Note:** The LattePanda is a quality-of-life upgrade, not a performance mod. It doesn't need to be done in any specific order relative to power mods. However, having it installed before the flex fuel tune makes the dyno session easier (permanent Hondata connection, real-time monitoring).

---

## Master Timeline (Recommended Execution Order)

```
PHASE 0 — MAINTENANCE (do immediately, before any mods)
  ├── Timing chain inspection
  ├── Valve adjustment  
  ├── Spark plugs (NGK ILZKR7B-11S)
  ├── Coolant flush + thermostat
  ├── Transmission fluid (Honda MTF)
  ├── Brake fluid flush (DOT 4)
  ├── Clutch fluid flush (DOT 4)
  ├── Serpentine belt (inspect/replace)
  ├── PCV valve
  ├── Water pump (inspect with timing chain)

PHASE 1 — ALREADY PURCHASED (install in order)
  ├── 1A: Clutch hydraulics (CMC/CSC upgrade)
  ├── 1B: Brakes (Hawk HPS + R1 Concepts)
  ├── 1C: Engine mounts (Hybrid Racing 70A)
  ├── 1D: Hondata FlashPro (first flash + base map)
  └── 1E: Strut bar (if clearance resolved)

PHASE 2 — EXHAUST SYSTEM
  ├── 2A: Valved exhaust (QTP QTEC30 + 3" dump)
  ├── 2B: Headers (Skunk2 Alpha + Berk HFC)        ← PB Blaster studs 3-5 days before!
  └── 2C: Dyno tune #1 (both calibrations)

PHASE 3 — INTAKE SYSTEM
  ├── 3A: Intake manifold (Skunk2 Ultra Street)
  ├── 3B: Bored throttle body (stock DBW → 66mm)    ← Send out 1-2 weeks before
  └── 3C: Dyno tune #2 (full bolt-on tune)

PHASE 4 — ROTATING ASSEMBLY
  └── 4A: ATI Super Damper + NST pulleys             ← No retune needed

PHASE 5 — FLEX FUEL
  ├── 5A: Fuel pump (DeatschWerks DW300C)            ← Can be done earlier
  ├── 5B: Fuel rail + injectors (Acuity + ID1050x)
  ├── 5C: Ethanol sensor + fuel lines
  └── 5D: Dyno tune #3 (flex fuel calibration)       ← Most complex tune

PHASE 6 — IN-CAR PC (anytime after FlashPro)
  └── 6A: LattePanda 3 Delta permanent install
```

---

## Dyno Tune Summary

You will need **3 dyno sessions** total (or 2 if you combine exhaust + intake in one session — but this is risky because it makes troubleshooting harder if something doesn't tune well):

| Session | After Installing | What's Tuned | Est. Cost |
|---------|-----------------|-------------|-----------|
| Tune #1 | Exhaust (cutout + headers + HFC) | Both calibrations (daily quiet + sport loud), AFR, timing with headers | $300-500 |
| Tune #2 | Intake manifold + bored TB | Full bolt-on pump gas tune — the main event | $300-500 |
| Tune #3 | Flex fuel system (injectors + ethanol sensor) | Flex fuel calibration (gas + E85 maps, real-time interpolation) | $400-600 |
| **Total tuning budget** | | | **$1,000-1,600** |

**Tip:** Find a tuner experienced with K-series Hondata BEFORE starting Phase 2. The Skunk2 Alpha + Ultra Street combo is the most common full bolt-on setup — any good K-series tuner will have extensive experience with it. Book the dyno session before ordering the parts so you're not waiting weeks with untuned mods on the car.

---

## Budget Summary (All Remaining Mods + Maintenance)

### Maintenance (Phase 0)
| Item | Cost (Parts) |
|------|-------------|
| Timing chain inspection/replacement | $20-500 |
| Valve adjustment | $10 DIY |
| Spark plugs | $40 |
| Coolant + thermostat | $45 |
| Transmission fluid | $25 |
| Brake + clutch fluid | $25 |
| Serpentine belt | $25 |
| PCV valve | $10 |
| Oil change | $35 |
| **Phase 0 Total (parts)** | **$235-715** |

### Modifications (Phases 1-6)
| Phase | Mod | Parts Cost |
|-------|-----|-----------|
| 1A | Clutch hydraulics | $200-500 |
| 1B | Brakes | Already purchased |
| 1C | Engine mounts | Already purchased |
| 1D | FlashPro | Already purchased |
| 1E | Strut bar | Already purchased |
| 2A | Valved exhaust | ~$485 + $150-250 labor |
| 2B | Headers + HFC | ~$1,000-1,200 + $300-500 labor |
| 2C | Dyno tune #1 | $300-500 |
| 3A+3B | Intake manifold + bored TB | ~$725 |
| 3C | Dyno tune #2 | $300-500 |
| 4A | ATI Super Damper + NST pulleys | ~$500-600 |
| 5A-5C | Flex fuel system | ~$1,075 |
| 5D | Dyno tune #3 | $400-600 |
| 6A | LattePanda PC | ~$400-500 |
| **Phases 1-6 Total** | | **~$5,835-7,560** |

### Grand Total (Everything Remaining)
| Category | Cost Range |
|----------|-----------|
| Maintenance (Phase 0) | $235-715 |
| Modifications (Phases 1-6) | $5,835-7,560 |
| **Grand Total** | **~$6,070-8,275** |

This assumes DIY labor for most installs except headers (shop recommended) and exhaust welding (muffler shop). Professional installation for everything would add $1,500-3,000 in labor.

---

## Mods That CANNOT Be Done Standalone

These mods have hard dependencies and should never be installed without completing their prerequisites:

| Mod | Requires First | Why |
|-----|---------------|-----|
| Headers (2B) | Valved exhaust cutout working (2A) | Cutout position depends on header/HFC length. Install order matters. |
| Hondata tune #1 (2C) | Exhaust complete (2A+2B) | Tune must account for header + cutout flow characteristics |
| Intake manifold (3A) | Full exhaust installed + tuned (Phase 2) | Changing intake after exhaust tune wastes a dyno session |
| Bored TB (3B) | Install with manifold (3A) | Single retune for both saves money |
| Hondata tune #2 (3C) | Manifold + TB installed (3A+3B) | Full bolt-on pump gas tune |
| Flex fuel tune (5D) | All fuel system components (5A+5B+5C) + full bolt-on tune (3C) | Flex fuel calibration is layered on top of the full bolt-on tune |

## Mods That CAN Be Done Standalone (Any Order)

| Mod | Notes |
|-----|-------|
| Clutch hydraulics (CMC/CSC) | No dependencies. Do early. |
| Engine mounts (Hybrid Racing 70A) | No dependencies. |
| Brakes (Hawk HPS + R1 Concepts) | No dependencies. |
| Strut bar (Megan Racing) | No dependencies (once clearance resolved). |
| FlashPro first flash | No dependencies (just needs a laptop). |
| ATI Super Damper + pulleys | No dependencies. No retune needed. |
| Fuel pump (DW300C) | Can be done anytime — stock ECU handles it fine. |
| LattePanda PC | Only needs FlashPro registered first. |

---

*Last updated: 2026-04-16*
