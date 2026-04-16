# Chronological Mod Order & 170k-Mile Maintenance Plan

## 2009 Honda Civic SI (FG2) — K20Z3, ~170,000 miles, 6MT

This is my game plan — the order I'm tackling every mod and the maintenance I need to knock out first. **Maintenance intervals here are based on community experience (8thcivic.com, Reddit r/CivicSi, K-series forums) — NOT Honda's factory intervals**, which are way too conservative for a 17-year-old, 170k-mile sport compact that's actually been driven.

---

## Phase 0: Critical Maintenance (Do First — Before Any More Mods)

I need to handle these before adding any more power or stress to the drivetrain. At 170k miles, some of these are honestly overdue.

| # | Item | Why | Community Interval | Est. Cost (DIY) | Est. Cost (Shop) |
|---|------|-----|--------------------|-----------------|-------------------|
| 1 | **Timing chain inspection** | K20Z3 uses a timing chain, not a belt — no replacement interval. BUT chain stretch is real at 170k. A stretched chain causes retarded cam timing, VTEC engagement issues, and eventually jumps teeth. **I already know this needs checking.** | Inspect at 150k+. Replace if stretch measured or chain noise present. | $20 (inspection) / $300-500 (replacement parts) | $100 (inspection) / $800-1,200 (replacement) |
| 2 | **Valve adjustment** | K20Z3 has solid lifters (no hydraulic lash adjusters). Valves go tight over time — tight valves burn. Community consensus: check every 30k-60k on a driven SI. At 170k, if never done or unknown history, this is urgent. | Every 30,000-60,000 miles | $10 (feeler gauges) | $150-250 |
| 3 | **Spark plugs** | NGK ILZKR7B-11S (stock iridium, pre-gapped). Even iridium plugs degrade by 100k. At 170k, if they're original, they're well past done. Misfires, poor fuel economy, lost power. | Every 60,000-80,000 miles (community). Honda says 100k — too long. | $40 (set of 4) | $80-120 |
| 4 | **Coolant flush + thermostat** | OEM Honda Type 2 coolant (blue). At 170k, the coolant has been through thousands of heat cycles. Thermostat can stick partially open (overcooling) or closed (overheating). I'm replacing both proactively. | Coolant every 50,000-60,000 miles. Thermostat at 100k+ or with coolant flush. | $30 coolant + $15 thermostat | $100-150 |
| 5 | **Transmission fluid change** | Honda MTF or Amsoil Synchromesh. The 8th gen SI 6MT synchros are sensitive to fluid quality. Notchy 2nd gear is often a fluid issue, not a synchro issue. | Every 30,000-40,000 miles | $25 (3 quarts Honda MTF) | $80-120 |
| 6 | **Brake fluid flush** | DOT 4 (Motul RBF 600 or ATE TYP 200). Brake fluid is hygroscopic — absorbs water, boiling point drops, internal corrosion increases. If never flushed, the fluid is original from 2009. | Every 2 years or 30,000 miles | $15 | $80-100 |
| 7 | **Clutch fluid flush** | Same as brake fluid but separate reservoir on the FG2. Especially important before the CMC/CSC upgrade. | Every 2 years or 30,000 miles | $10 | $50-80 |
| 8 | **Serpentine belt** | Visual inspection — cracking, glazing, squealing. At 170k, I'm likely on the 2nd or 3rd belt. Replace if there are any signs of wear. | Every 60,000-80,000 miles or at first sign of wear | $25 | $80-120 |
| 9 | **Water pump** | K20Z3 water pump is driven by the timing chain. I'll inspect it during the timing chain inspection. Weeping from the weep hole = replace immediately. | Inspect at timing chain service. Replace proactively at 150k+. | $50 (pump) | Included in timing chain labor |
| 10 | **Motor oil + filter** | Honda recommends 0W-20, but community consensus for a 170k-mile K20Z3 that's driven hard: **5W-30 full synthetic** (Mobil 1, Pennzoil Platinum, or Castrol Edge). Thicker oil compensates for worn bearing clearances. | Every 5,000-6,000 miles with synthetic. Honda says 7,500 — too long for an SI driven spiritedly. | $35 | $60-80 |
| 11 | **PCV valve** | 17130-RTA-000 or equivalent. Cheap, easy, often neglected. A failed PCV causes oil consumption, rough idle, and boost leaks if ever turbo'd. | Every 60,000-80,000 miles | $10 | $30-50 |

### Timing Chain Deep Dive

The K20Z3 timing chain is rated for the life of the engine, but "life of the engine" assumes Honda's idea of a normal lifecycle (~200k miles of grandma driving). On a 170k-mile SI that's been driven like an SI:

- **How to check:** I can measure cam timing with the Hondata FlashPro. Retarded cam timing (more than 2-3 degrees off spec) indicates chain stretch. A mechanic can also check with a dial indicator on the tensioner.
- **Chain noise:** A rattling or slapping noise at cold start (first 5-10 seconds) that goes away once oil pressure builds is the classic symptom of a stretched chain with a maxed-out tensioner.
- **If the chain is fine:** No action needed. I'll recheck at 200k.
- **If the chain is stretched:** Replace chain, tensioner, guides, and VTC actuator as a set. Do NOT replace just the chain. Budget $300-500 in parts, $600-900 in labor (or 8-12 hours DIY).

---

## Phase 1: Immediate Installs (Already Purchased or Priority Purchase, No Dependencies)

These mods are already bought (or need to be bought first) and have no dependencies. Install order within this phase doesn't really matter — they're all standalone.

| Order | Mod | Time (DIY) | Standalone? | Notes |
|-------|-----|-----------|-------------|-------|
| 1A | **Clutch hydraulics (CMC/CSC)** | 3-5 hrs | Yes | **Not yet purchased — priority buy.** I need to do this before anything else. 170k miles = ticking time bomb. Improves pedal feel immediately. |
| 1B | **Engine mounts (Hybrid Racing 70A)** | 3-4 hrs | Yes | Reduces wheel hop, improves shift feel. NVH increase is noticeable but livable. |
| 1C | **Brakes (Hawk HPS + R1 Concepts rotors)** | 2-3 hrs | Yes | Full 4-corner upgrade. I need to bed the pads properly (follow Hawk's bedding procedure). Want this done before I have more power to stop. |
| 1D | **Strut bar (Megan Racing)** | 30 min | **Blocked** | Clearance issue needs diagnosis first. May need spacers or modification. |
| 1E | **Hondata FlashPro — first flash** | 1-2 hrs | Yes | Register unit, flash base map, verify no CELs. I'm not tuning yet — just getting it online. This enables datalogging for all future work. |

**My planned order within Phase 1:** 1A → 1C → 1B → 1E → 1D (if unblocked)

- CMC/CSC first because it's a reliability risk at this mileage
- Brakes second because more power needs more stopping
- Engine mounts third because they don't affect reliability
- FlashPro fourth to start datalogging before adding power mods
- Strut bar last (blocked anyway)

---

## Phase 2: Exhaust System (Must Be Done Together)

The valved exhaust and headers are interrelated. My plan is to install the exhaust cutout first, tune it, then add headers and retune.

| Order | Mod | Time (DIY) | Standalone? | Notes |
|-------|-----|-----------|-------------|-------|
| 2A | **Valved exhaust (QTP QTEC30 cutout)** | 4-6 hrs (shop recommended for welding) | Semi-standalone | Install cutout + dump pipe + reducer. Get both tunes working (valve open/closed). I can do this without headers using the stock manifold. |
| 2B | **Headers (Skunk2 Alpha + Berk HFC)** | 6-10 hrs DIY / 3-5 hrs shop | **Must be done with 2A complete** | PB Blaster the manifold studs 3-5 days before. I'll probably have a shop do this ($300-500 labor) — seized stud risk at 170k is real. |
| 2C | **Hondata retune (dyno)** | 2-3 hrs on dyno | **Must be done after 2A+2B** | Tune both calibrations (daily quiet + sport loud) with headers installed. Verify AFR in both valve positions. Budget $300-500 for dyno tune. |

**Important:** Do NOT install headers without planning the exhaust cutout first. Headers change the entire exhaust flow, and the cutout position needs to account for header length + HFC placement. I'm installing the cutout first (2A), validating it works, then adding headers (2B) and retuning everything (2C).

**Stud prep is critical:** I'm starting PB Blaster on the exhaust manifold studs at least 3-5 days before the header install. Heat cycle the car + spray daily. At 170k miles, those studs WILL be seized. I'll have new M10x1.25 stainless studs and copper-plated flange nuts ready.

---

## Phase 3: Intake System (Must Be Done Together, After Exhaust)

The intake manifold and throttle body work together and need a retune after install.

| Order | Mod | Time (DIY) | Standalone? | Notes |
|-------|-----|-----------|-------------|-------|
| 3A | **Intake manifold (Skunk2 Ultra Street)** | 3-5 hrs | **Paired with 3B** | I could technically install this alone, but doing it with the TB at the same time saves a retune. |
| 3B | **Bored throttle body (stock DBW → 66mm)** | N/A (send out for boring) | **Paired with 3A** | I'll send the stock TB to Drag Cartel or HeelToe Auto for boring to 66mm. Lead time: 1-2 weeks. I need to order this BEFORE buying the manifold so both arrive together. |
| 3C | **Hondata retune (dyno)** | 2-3 hrs on dyno | **Must be done after 3A+3B** | Retune for the new manifold + TB. This is the "full bolt-on" tune. Budget $300-500. |

**Why after exhaust:** The intake manifold tune depends on exhaust flow. If I tune the manifold first and then change headers, I'd need to retune again — wasted dyno time and money. Headers → intake manifold → single comprehensive tune is more efficient.

**Note:** My K&N Typhoon cold air intake (already installed) stays in the system. The flow path becomes: K&N filter → intake pipe → bored TB → Skunk2 Ultra Street manifold → K20Z3.

---

## Phase 4: Rotating Assembly (Standalone, After Full Bolt-On Tune)

| Order | Mod | Time (DIY) | Standalone? | Notes |
|-------|-----|-----------|-------------|-------|
| 4A | **Pulleys + Harmonic Balancer (ATI Super Damper + NST kit)** | 3-5 hrs | Yes | Standalone install. Requires crank bolt removal (impact gun needed, 250+ ft-lbs). Doesn't require a retune — it's a mechanical change, not an airflow change. |

**Why after the tune:** The pulley system doesn't affect tuning, but it does affect accessory drive belt routing. I'm installing it after the full bolt-on tune so I'm not juggling multiple changes at once. The ATI Super Damper is especially important at 170k miles — the stock damper's elastomer is likely degraded by now.

---

## Phase 5: Flex Fuel System (Final Power Adder)

| Order | Mod | Time (DIY) | Standalone? | Notes |
|-------|-----|-----------|-------------|-------|
| 5A | **Fuel pump (DeatschWerks DW300C)** | 1-2 hrs | Can be done early (standalone) | Drop-in replacement. I can install this anytime, even before injectors — the stock ECU handles it fine. |
| 5B | **Fuel rail + injectors (Acuity + ID1050x)** | 2-3 hrs | **Paired with 5C** | Install rail, injectors, and ethanol sensor at the same time. |
| 5C | **Ethanol content sensor + fuel lines** | 1-2 hrs | **Paired with 5B** | Inline sensor before fuel rail. -6 AN PTFE braided lines. |
| 5D | **Hondata flex fuel tune (dyno)** | 3-4 hrs on dyno | **Must be done after 5A+5B+5C** | Flex fuel calibration: gasoline map + E85 map with real-time interpolation. This is the most complex tune in the build. Budget $400-600. |

**Why last:** E85 is the biggest power adder (5-15 WHP) but also the most complex. I want the full bolt-on tune dialed in on pump gas first, THEN add flex fuel as the final layer. That way the tuner has a known-good base to build the flex fuel calibration on top of.

**Clutch warning:** Full bolt-on + E85 targets 230-250 WHP / 165-180 lb-ft. My Exedy 08806 Stage 1 is rated to ~280-300 WHP / ~200-210 lb-ft. I'm within the margin, but I'll be monitoring for clutch slip under hard acceleration in 3rd-6th gear after the E85 tune.

---

## Phase 6: In-Car PC (Quality of Life — Anytime After FlashPro)

| Order | Mod | Time (DIY) | Standalone? | Notes |
|-------|-----|-----------|-------------|-------|
| 6A | **LattePanda 3 Delta permanent install** | 6-10 hrs (spread over a weekend) | Yes | Can be done anytime after the FlashPro is registered and working. The PC replaces my laptop for Hondata management and adds exhaust valve control via Arduino GPIO. |

**Note:** The LattePanda is a quality-of-life upgrade, not a performance mod. It doesn't need to happen in any specific order relative to power mods. That said, having it installed before the flex fuel tune would make the dyno session easier — permanent Hondata connection, real-time monitoring, no laptop balancing act.

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

PHASE 5 — SUSPENSION (can be done anytime, no tune dependency)
  ├── 5A: BC Racing BR coilovers + rear camber arms
  ├── 5B: Full bushing refresh (Energy Suspension + Hardrace)
  ├── 5C: Sway bars (Progress front + rear) + end links
  ├── 5D: Ball joints + tie rod ends + roll center adjusters
  └── 5E: Professional 4-corner performance alignment  ← MANDATORY

PHASE 6 — FLEX FUEL
  ├── 6A: Fuel pump (DeatschWerks DW300C)            ← Can be done earlier
  ├── 6B: Fuel rail + injectors (Acuity + ID1050x)
  ├── 6C: Ethanol sensor + fuel lines
  └── 6D: Dyno tune #3 (flex fuel calibration)       ← Most complex tune

PHASE 7 — IN-CAR PC (anytime after FlashPro)
  └── 7A: LattePanda 3 Delta permanent install
```

---

## Dyno Tune Summary

I'll need **3 dyno sessions** total (or 2 if I combine exhaust + intake in one session — but that's risky because troubleshooting gets harder if something doesn't tune well):

| Session | After Installing | What's Tuned | Est. Cost |
|---------|-----------------|-------------|-----------|
| Tune #1 | Exhaust (cutout + headers + HFC) | Both calibrations (daily quiet + sport loud), AFR, timing with headers | $300-500 |
| Tune #2 | Intake manifold + bored TB | Full bolt-on pump gas tune — the main event | $300-500 |
| Tune #3 | Flex fuel system (injectors + ethanol sensor) | Flex fuel calibration (gas + E85 maps, real-time interpolation) | $400-600 |
| **Total tuning budget** | | | **$1,000-1,600** |

**Tip:** I need to find a tuner experienced with K-series Hondata BEFORE starting Phase 2. The Skunk2 Alpha + Ultra Street combo is the most common full bolt-on setup — any good K-series tuner will have extensive experience with it. I'm going to book the dyno session before ordering parts so I'm not sitting around with untuned mods on the car.

---

## Money Already Spent (Actual Costs — incl. tax, shipping, insurance)

| Item | Actual Paid |
|------|------------|
| Exedy Stage 1 clutch + flywheel + Megan Racing strut bar (bundle) | $960.43 |
| K&N Typhoon 69-1014TS intake | $504.17 |
| Acuity short shifter + cable bushings | $622.20 |
| Hybrid Racing 70A engine mounts | $657.15 |
| R1 Concepts slotted rotors (WCPN2-59004) | $309.69 |
| Hawk HPS brake pads (front + rear) | $222.45 |
| Hondata FlashPro | $859.59 |
| Continental ExtremeContact DWS06 Plus 215/45ZR17 91W XL (15572680000) — purchased 2026-06-16 | $715.00 |
| **Total Spent to Date** | **$4,850.68** |

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

### Modifications (Remaining — Not Yet Purchased)
| Phase | Mod | Est. Parts Cost |
|-------|-----|----------------|
| 1A | Clutch hydraulics | ~$326 (Hybrid Racing kit + Motul RBF 600) |
| 2A | Valved exhaust | ~$485 + $150-250 labor |
| 2B | Headers + HFC | ~$1,000-1,200 + $300-500 labor |
| 2C | Dyno tune #1 | $300-500 |
| 3A+3B | Intake manifold + bored TB | ~$725 |
| 3C | Dyno tune #2 | $300-500 |
| 4A | ATI Super Damper + NST pulleys | ~$640-760 |
| 5A | Coilovers (BC Racing BR) | ~$1,195 |
| 5B | Bushing kit + trailing arm bushings | ~$428 |
| 5C | Sway bars (Progress front + rear) | ~$637 |
| 5D | Ball joints + tie rods + roll center adj | ~$390 |
| 5E | Performance alignment | ~$150 |
| 5 | Rear camber arms (Skunk2) + camber bolts | ~$363 |
| 6A-6C | Flex fuel system | ~$1,075 |
| 6D | Dyno tune #3 | $400-600 |
| 7A | LattePanda PC | ~$400-500 |
| **Remaining Mods Total** | | **~$8,864-11,160** |

### Grand Total Summary
| Category | Amount |
|----------|--------|
| **Already Spent** | **$4,850.68** |
| Maintenance (Phase 0, remaining) | $235-715 |
| Modifications (remaining) | $8,864-11,160 |
| **Remaining to Spend** | **~$9,099-11,875** |
| **Full Build Total (spent + remaining)** | **~$13,950-16,726** |

That assumes I'm doing DIY labor for most installs except headers (shop recommended), exhaust welding (muffler shop), and possibly suspension bushing pressing. Paying a shop for everything would add $2,500-5,000 in labor.

---

## Mods That CANNOT Be Done Standalone

These have hard dependencies — I should never install them without completing the prerequisites:

| Mod | Requires First | Why |
|-----|---------------|-----|
| Headers (2B) | Valved exhaust cutout working (2A) | Cutout position depends on header/HFC length. Install order matters. |
| Hondata tune #1 (2C) | Exhaust complete (2A+2B) | Tune must account for header + cutout flow characteristics |
| Intake manifold (3A) | Full exhaust installed + tuned (Phase 2) | Changing intake after exhaust tune wastes a dyno session |
| Bored TB (3B) | Install with manifold (3A) | Single retune for both saves money |
| Hondata tune #2 (3C) | Manifold + TB installed (3A+3B) | Full bolt-on pump gas tune |
| Flex fuel tune (6D) | All fuel system components (6A+6B+6C) + full bolt-on tune (3C) | Flex fuel calibration is layered on top of the full bolt-on tune |

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
| Suspension (coilovers + bushings + sway bars) | No tune dependency. Can be done anytime. Do all at once — car is already apart. |
| LattePanda PC | Only needs FlashPro registered first. |

---

*Last updated: 2026-04-16*
