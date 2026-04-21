# Complete Fuel System + Flex Fuel Build — 2009 Civic SI (FG2 / K20Z3)

**Date:** 2026-04-20
**Theme:** Purple engine bay, Acuity brand consistency, reliability-first
**Power targets:** 220-240 WHP on 93 octane, 230-250 WHP on E85 (NA)
**Centerpiece:** Acuity Instruments K-Series Fuel Rail — Satin Purple (1913-PPL)
**Companion:** [overview.md](overview.md) covers the "is flex fuel on NA worth it" decision and the cost-vs-WHP analysis. This doc is the build spec.

---

## Table of Contents

1. [Acuity Fuel Rail](#1-acuity-fuel-rail) · 2. [Bosch EV14 550cc Injectors](#2-bosch-ev14-550cc-injectors) · 3. [DW300C Fuel Pump](#3-dw300c-fuel-pump) · 4. [Continental Flex Fuel Sensor](#4-continental-flex-fuel-sensor) · 5. [FlashPro Flex Fuel Setup](#5-flashpro-flex-fuel-setup) · 6. [Fuel Pressure Regulator](#6-fuel-pressure-regulator) · 7. [Fuel Lines](#7-fuel-lines) · 8. [AN Fittings & Purple Aesthetic](#8-an-fittings--purple-aesthetic) · 9. [Fuel Filter](#9-fuel-filter) · 10. [Purple Summary](#10-purple-summary) · 11. [Install Procedure](#11-install-procedure) · 12. [E85 Operating Notes](#12-e85-operating-notes) · 13. [Cost + Phased Plan](#13-cost--phased-plan) · 14. [Sources](#14-sources)

---

## 1. Acuity Fuel Rail

### The Purple One Exists from the Factory

I was braced to pay a custom anodizer to strip and re-color a black rail. I don't have to — **Acuity sells the K-series rail in satin purple straight from the factory as PN 1913-PPL**, same price as any other color. This is the visual anchor of the purple engine bay.

### Part Numbers, Colors, Price

| SKU | Finish | Price (MSRP) |
|---|---|---|
| **1913-PPL** | **Satin Purple** | **~$199** |
| 1913-BLK | Satin Black | ~$199 |
| 1913-RED | Satin Red | ~$199 |
| 1913-TEL | Satin Teal | ~$199 |

K Series Parts lists ~$199.86 MSRP with promo pricing occasionally dropping to ~$177. Acuity direct lists $199. Budget $200 + tax/ship. No premium for the purple finish.

### Specifications

- **Material:** CNC-machined 6061-T6 billet aluminum, hard-anodized satin purple, laser-etched logo
- **Bore:** 15mm (0.59") ID — rated "1000+ HP" (wildly over-spec for my 250 WHP NA target, which is fine — oversize bore stabilizes rail pressure under injector duty)
- **Ports:** -8 ORB center-feed (for tucked/center-fed lines), -8 ORB on both ends (for OEM feed or return-style), 1/8" NPT gauge port on top face
- **Injector bores:** 14mm standard — accepts Bosch EV14, ID, DW, Grams, KTuned, etc.
- **Included:** Rail, (2) class 10.9 M8 mounting screws, (1) stainless 1/8" NPT port plug
- **NOT included:** Any AN fittings (sold separately; Acuity offers 6 dedicated fittings for this rail)

### Fitment with Skunk2 Ultra Street IM + K20Z3

The rail itself is universal across the K-series injector pattern, including the Skunk2 Ultra Street (307-05-0600). The **harder compatibility problem is the IM, not the rail**: Skunk2 Ultra Street uses the early PRB/PRC head + TB pattern, so to run it on my RBC-head K20Z3 I need a **water-bypass adapter** (for the RBC coolant ports the PRB manifold doesn't have) and the **Skunk2 DBW TB adapter (PN 309-05-0120)** to mate my DBW (bored-to-66mm) TB to the PRB-pattern manifold flange. Full intake manifold detail lives in [`14-Intake-Manifold/`](../14-Intake-Manifold/). Once those adapters are in place, **the Acuity rail bolts directly to the manifold with no fitment issue** — same injector bore pattern as stock.

### Install Torque Specs

| Fastener | Torque | Notes |
|---|---|---|
| Acuity rail M8 mounting screws | **10 ft-lb (13.6 Nm)** | 6mm Allen. Radium's published K-rail guide specifies the same spec — community reference. |
| Stock-equivalent rail-to-IM bolt spec | 108 in-lb / **9 ft-lb** | FSM spec. Acuity uses the same mounting pattern with aluminum IM threads — be gentle. |
| Injectors into rail | Hand press + verify seating | Lube O-rings with engine oil, press in, push down to bottom, verify upper O-ring still seated. |
| -8 ORB fittings into rail | Hand tight + 1/4 to 1/2 turn past O-ring contact | O-ring seal — never over-torque. |
| 1/8" NPT plug / gauge port | Snug + PTFE tape | Tapered — seals before fully seated. |

### Warranty + Reviews

**1-year defect warranty** from Acuity. Returns accepted within 14 days if unopened. For a billet rail with no moving parts this is more than enough — the rail either leaks/cracks (warranty) or it lasts the life of the car.

Community take: Acuity K-rail is effectively the default K-series "beyond stock" upgrade alongside Radium 20-0230-02 (black only, ~$150-175, larger 0.69" bore but no purple option) and Hybrid Racing's equivalent. Fit/finish is clean, anodize is even, laser etch is a nice touch. Brand consistency with my Acuity shifter + the purple theme seals it.

---

## 2. Bosch EV14 550cc Injectors

### Decision: Bosch EV14 550cc, Not RDX, Not ID1050x

| Option | Flow | Verdict |
|---|---|---|
| **RDX 410cc** (Acura OEM) | 410 cc/min @ 3 bar | Rejected. No published dead-time data, ~6% set-to-set flow variance. Tight E85 headroom at 240 WHP. |
| **Bosch EV14 550cc** (PN 0280158117) | 550 cc/min @ 3 bar | **Chosen.** Bosch OE line, <1% matched, published Hondata dead times, ~$200-280/set, right-sized for NA E85 with margin. |
| **Injector Dynamics ID725** | 725 cc/min @ 3 bar | Runner-up if turbo becomes real. ~$450-500. Overkill for current NA target. |
| **ID1050x** | 1065 cc/min @ 3 bar | Rejected (same call as overview.md): 3.4x oversized, minimum pulse-width issues at idle, ~$550. |

### Bosch EV14 550cc Fitment

- **PN: 0280158117** — 550 cc/min @ 43.5 PSI / 3 bar
- **Body:** 48mm mid-length (standard short K-series top-feed form)
- **O-rings:** 14mm top + 14mm bottom — Viton-family, **fully E85-compatible from the factory**. Included with genuine Bosch injectors (verify with the reseller).
- **Impedance:** 12 ohm (high-impedance, same as stock K20Z3 — plugs into stock injector drivers, no driver box)
- **Max pressure:** 100 PSI (running ~58 PSI, zero concern)
- **Connector:** USCAR/EV6 — **needs Honda OBD2 adapter clips**

### Adapter Clips

Two paths:
1. **One-piece pigtail adapters** (recommended, reversible): $15-25/set of 4. Sources: OBD Innovations, DeatschWerks USCAR-to-Honda, Clean Injection, Injector Nation.
2. **Re-pin the harness**: cleaner, permanent, more labor.

Going with pigtails. Some resellers (Clean Injection, Injector Nation, CP Fuel & Race) bundle the adapters into the injector set price — **check the listing before buying adapters separately**.

### Price per Set of 4

- Bare genuine Bosch 0280158117 (no adapters): **~$200-240** (Polmaxracing, eBay, TRE Performance)
- Flow-matched branded sets with Honda OBD2 adapters included: **~$280-350** (Clean Injection, Injector Nation)
- High Flow Fuel w/ adapter kits: **~$220-280**

**Budget: $280** for a set with adapters bundled.

### Dead Time Data for Hondata

This matters — K-series ECU fueling accuracy at idle/low pulse depends on correct dead-time curves.

- **Bosch published spec:** ~0.538 ms @ 14V / 0.846 ms @ 12V (per Ford Racing / EV14 bench data)
- **Hondata's recommendation:** K-series ECUs want scaled dead times closer to **~1.2 ms @ 14V** as a baseline. Bosch's raw spec is from a different bench methodology and causes +25-30% idle trim drift if plugged in directly.
- **Workflow:** Load a Hondata-community-published EV14 550cc dead-time map at install time, then live-tune on the dyno to fine-tune. Don't trust Bosch's raw sheet numbers.

### O-rings / Seals

Genuine Bosch ships with 14mm top + 14mm bottom Viton-family O-rings installed. Fully E85-compatible. Budget $5-10 for a spare pack for peace of mind. Lube with engine oil at install.

---

## 3. DW300C Fuel Pump

### Part Number + Fitment

- **Kit P/N: DeatschWerks 9-307-1008** — DW300C 340 LPH pump + complete 8th-gen Civic (2006-2011) install kit
- **Direct drop-in for FG2** — no hanger modification. Kit includes pump, in-tank strainer, grommet, hose, clamps, Honda-specific electrical connections.
- **Flow:** 340 LPH @ 40 PSI, ~305 LPH @ 60 PSI (my actual rail pressure)
- **E85-compatible by design:** carbon commutators + fully-encapsulated armature
- **PWM-compatible** — critical because the 8th gen Civic SI pump is PWM-controlled by the ECU, not on/off. A non-PWM-rated pump will have weird current and heat behavior.

### Price

~$186-210 across vendors (DeatschWerks direct ~$189, MAPerformance ~$187-199, K Series Parts / HARDmotion / RallySport Direct in the same range). **Budget: $200 including shipping.**

### Flow Headroom for 250 WHP E85

At 250 WHP peak on E85, estimated peak fuel volume is ~100-120 LPH at WOT. The DW300C delivers ~305 LPH at 60 PSI → **~2.5-3x headroom**. Injector duty stays in 70-80% range with 550cc injectors, comfortably under the 85% reliability ceiling. Reliability-first rule satisfied.

### Alternatives (Rejected)

| Pump | Flow | Why not |
|---|---|---|
| Walbro 450 (F90000267) | 450 LPH | Overkill for NA. Louder. Designed for high-boost. |
| AEM 50-1200 | 340 LPH | Equivalent perf, universal kit — less clean fit on Honda hanger than DW. |
| DW65C / DW200 | 255-265 LPH | Marginal E85 headroom at 240 WHP. DW300C is same price class — buy once. |

### Reviews + Warranty

DW300C on the 8th gen Civic is **well-established**: quiet, PWM-compatible, smooth idle, no pressure instability reported on E85 builds up through mid-300 WHP. **3-year no-fault DeatschWerks warranty.** Tilts reliability-first heavily in its favor.

---

## 4. Continental Flex Fuel Sensor

### Part Number: Continental 13577429

- Formerly Siemens/VDO, now Continental. Aftermarket PN **SE1004S**. ACDelco sells the same part as 13577429.
- This is the **"small" (shorter) GM flex fuel sensor** — the one most K-series kits use. Reports 0-100% ethanol + fuel temp.
- Continental's OE Flex Fuel Sensor catalog also lists the larger 13577394 — different sizes for different GM vehicles. **13577429 is the Honda standard** (smaller, cheaper, plentiful).

### Price

- ACDelco 13577429 on Amazon: **~$75-85**
- GMPartsDirect historical: ~$44-55
- High Flow Fuel kit (sensor + -6AN barbs + stainless bracket): **~$95-105** ← easiest path
- Racetronix / Platinum Racing Products: ~$85-115

**Budget: $95** (sensor-plus-barbs bundle from High Flow Fuel).

### Fittings

- **Sensor ports:** 3/8" SAE EFI quick-connect (male input, female output) — GM standard
- **On Honda (5/16" feed):** Convert 3/8" QC to -6AN via either bundled barb kit ($95 total path) or bare sensor + 2x 3/8" SAE QC-to--6AN adapters (~$115-145 total) from JBtuned, Summit, or Radium

### Mounting

**Inline on high-pressure feed, between fuel filter and rail, post-filter.** Canonical for three reasons: sensor needs flow to read accurately; upstream-of-rail placement minimizes detection lag on fillups; post-filter keeps the sensor clean.

**Physical mount:** Bracket on a spare bolt boss on the firewall or battery tray area. **Constraint:** I'll need to delete the stock EVAP canister to make engine-bay room for filter + sensor + fittings (noted by JBtuned + SiriMoto install guides). EVAP delete requires Hondata to suppress the codes — FlashPro handles cleanly.

### Wiring (3 Wires)

| Wire | Function | Connects to |
|---|---|---|
| 12V switched | Sensor power (ignition-on) | Under-hood switched-12V source or add-a-fuse |
| Ground | Sensor ground | Clean chassis ground near sensor |
| Signal (50-150 Hz PWM) | **Through a converter/gauge module** → 0-5V analog to ECU pin A33 (ECT2) | Innovate MTX-D or similar is the converter |

**Important:** K-series ECU's ECT2 pin reads analog voltage (0-5V), not raw frequency. **Hondata's explicit recommendation:** use a converter module or a flex-fuel gauge with analog output. Do NOT wire the sensor's raw frequency output directly to ECT2.

---

## 5. FlashPro Flex Fuel Setup

### ECU Pin: ECT2 at A33

FlashPro's flex fuel implementation on the 8th gen SI uses the **ECT2 input at ECU pin A33** — the unpopulated secondary coolant-temp sensor pin on the K20Z3, which is a free analog input.

- **Input type:** 0-5V analog, internal 5V pull-up
- **Voltage-to-ethanol mapping:** 0V = 0% ethanol, 5V = 100% ethanol (linear after calibration)
- **Install hook:** Unplug the blue ECT2 connector on the engine (passenger side near lower radiator hose on most K-series) and splice the flex-fuel gauge/converter output there — signal reaches the ECU without running a new wire through the firewall.

### Does FlashPro Read 0-85% Ethanol Linearly? Yes, After 2-Point Calibration

1. **Low-Side Calibration:** Fill tank with E15 or lower (regular pump gas). Run engine, connect FlashPro Live Tuning, confirm flex gauge reads low, adjust **Column 1 of "Ethanol Percentage vs Volts"** table so displayed % matches reality.
2. **High-Side Calibration:** Drain + fill with E65+ (fresh E85). Confirm gauge reads high, adjust **Column 2** of same table.
3. FlashPro linearly interpolates for any intermediate voltage. All blends E0-E85 read correctly once both endpoints are set.

### Flex Fuel Tune Workflow — Pump First, Then E85, Interpolate

Hondata-recommended order:

1. **Tune on pump gas first.** Build the base 93-octane map (or load my existing FlashPro calibration). This is the E0/E10 endpoint.
2. **Tune the ethanol compensation tables** (not separate maps — compensation overlays):
   - **Ethanol Fuel Compensation:** additional fuel % at each ethanol content step. E85 baseline: ~+30-40%.
   - **Ethanol Timing Compensation:** additional timing advance at each ethanol step. E85 on 11.0:1 K20Z3 with good bolt-ons: +3 to +5 deg.
3. **Dyno-verify E85.** Fresh E85 fill, back-to-back pulls with logs, confirm AFR and timing hit targets.
4. **Live interpolation.** Once both endpoints are calibrated, FlashPro blends automatically based on sensor reading. Fill with any ratio — ECU handles it seamlessly.

### Ethanol % Behavior Across the Range

| Ethanol | Timing Δ | Fuel Δ | WOT AFR | Feel |
|---|---|---|---|---|
| **E0-E10** | Baseline | Baseline | 12.5-13.0 (0.88 lambda) | Pump-gas tune, ~220-240 WHP |
| **E30-E40** | +1 to +2° | +10-15% | 12.2-12.5 (0.85) | Modest bump, minimal MPG hit, ~225-240 WHP |
| **E50** | +2 to +3° | +18-22% | 12.0-12.3 (0.82) | Noticeable, moderate MPG hit, ~230-245 WHP |
| **E85 (summer)** | +3 to +5° | +30-40% | 11.5-12.0 (0.80) | Peak, ~230-250 WHP, 25-30% MPG penalty |

### Ethanol Content Gauge In-Car

Because the sensor signal goes through a converter anyway, I get a visible cabin readout. Options:

| Gauge | Price | Notes |
|---|---|---|
| **Innovate MTX-D** | ~$140 | 52mm OLED. Ethanol % + fuel temp. **Also acts as the 0-5V converter for FlashPro.** SiriMoto's default. |
| Innovate ECB-1 | ~$300 | Ethanol + boost + wideband. Boost channel wasted on NA. Useful if turbo later. |
| AEM 30-2201 flex kit | ~$230 | Sensor + gauge + harness bundled |

**Decision: Innovate MTX-D ($140).** Documented SiriMoto path, outputs the voltage FlashPro wants, clean install.

### Acuity Fuel Pressure Gauge — Brand Consistency

Acuity 100 PSI fuel pressure gauge (Marshall Instruments-built, 52mm face), available in **Satin Black** or Polished Stainless — **not currently offered in purple, but dial face is white/black and coordinates with purple AN fittings and the Acuity rail**. ~$100-130. Screws into the 1/8" NPT port on top of the Acuity rail.

Buying one gives me (1) live rail pressure during install leak check, (2) Acuity brand consistency, (3) early warning for pump failure before fuel trims go haywire. **Budget: $115 (Satin Black).**

---

## 6. Fuel Pressure Regulator

### Keep the Stock In-Tank FPR

The 8th gen Civic SI uses a **returnless fuel system** — regulator is integrated into the in-tank pump hanger, not in the engine bay. Base pressure ~50-58 PSI, PWM-modulated by the ECU.

**For 250 WHP NA on E85 with 550cc injectors: stock FPR is adequate.** Every flex-fuel 8th gen Civic SI build in the community at or below this power level confirms. Injector duty stays well under 85% at peak, no pressure droop, no benefit from an external adjustable FPR.

**Decision: Keep stock. No adjustable FPR.**

### When Adjustable FPR Would Make Sense

Turbo/SC with rising-rate fuel pressure needs, 1000cc+ injectors needing lower base pressure for idle quality, alcohol-injection or port+DI hybrid setups, or dyno-chasing the last 3-5 WHP at injector duty ceiling. None apply now. If I go turbo later, I'd convert to return-style with a Radium DMR or FUELAB FPR then.

### Radium FPR Reference (if ever needed)

- **Radium DMR (Direct Mount Regulator):** 20-1623-00 (black) or 20-1623-01 (green), ~$290-340
- **Radium FPR with Bosch OEM top:** 3 bar = 20-0014-00, 4 bar = 20-0014-01, ~$180-240
- **No purple option from Radium.** Custom anodize $50-100 if ever installed to match theme.

### Base Pressure Procedure (If Adjustable FPR Added)

Prime (KOEO x3), read on Acuity gauge, start + warm idle, target **~58 PSI (4 bar) static** — community standard for 550cc EV14 + Hondata dead-time data. Adjust hex screw 1/4 turn = ~3-5 PSI. Lock with lock nut. Verify at idle, 3500 RPM, and WOT; should hold ±2 PSI.

---

## 7. Fuel Lines

### Stock 8th Gen Lines vs. PTFE

Modern Honda fuel lines (post-2006 fluoroelastomer spec) are **generally E85-compatible for moderate-term use** — documented safe by the 8thcivic FAQ and multiple K-series shops. **Long-term sustained straight E85** is where PTFE starts to matter.

### My Plan — Phased

**Phase 1 (initial install):** Keep stock feed line tank-to-engine-bay. Add **one short -6AN PTFE section** from filter → flex sensor → Acuity rail inlet — the area getting fittings work anyway. ~$60-90 parts, zero extra labor, upgrades the hardest-working section.

**Phase 2 (if needed):** If I see stock-line degradation or commit to full-time E85, upgrade full feed line from tank-hardline to rail. $200-350 parts, $150-300 shop labor if I have them build/crimp.

### Options If Upgrading Later

- **Hybrid Racing K-Series Fuel Line Kit:** ~$180-250, PTFE-lined, pre-assembled AN ends
- **Custom -6AN PTFE** (Summit, Fragola, Earl's, Aeroquip components): ~$80-180 for feed only
- **JBtuned 8th Gen Civic SI full fuel system + return kit:** ~$600-900, full replacement + return conversion

### Install Difficulty

Proper PTFE field assembly requires a hose vise + crimping tool. For Phase 1 scope (short rail-feed PTFE section), **pre-made -6AN PTFE hoses from Summit/Russell/Fragola** eliminate the crimping requirement entirely.

---

## 8. AN Fittings & Purple Aesthetic

### Minimum Fittings (Phase 1)

| Location | Fitting | Qty |
|---|---|---|
| Acuity rail inlet (center -8 ORB) | -8 ORB to -6AN male adapter OR -8 ORB to Honda QC | 1 |
| Acuity rail end ports (unused) | -8 ORB plug | 2 |
| Sensor inlet/outlet (3/8" SAE QC) | 3/8" SAE QC to -6AN male | 2 |
| PTFE line ends | -6AN hose-end fittings (straight or 45°) | 2-4 |
| Fuel filter adapter | 5/16" Honda QC to -6AN | 1-2 |

**Total ~8-10 pieces. Budget $140-220 for a complete Phase 1 set.**

### Purple Anodized AN Fittings

- **Fragola Performance Systems** — top pick. US-made (Connecticut), one-piece design, J-gauge threads. Offers purple anodize across standard -6AN hose ends, NPT adapters, bulkheads.
- **Vibrant Performance** — purple PTFE hose ends in the 28xxx series, filterable at Summit Racing. $15-30 per fitting.
- **Russell / Edelbrock** — purple in limited legacy runs, availability thinning.
- **Earl's** — primarily black/blue/red; occasional purple runs.

### Cost Estimate

| Fitting | Qty | Est. (purple anodize) |
|---|---|---|
| -8 ORB to -6AN male | 1-2 | $12-18 ea |
| 3/8" SAE QC to -6AN | 2 | $25-40 ea |
| -8 ORB plugs | 2 | $8-12 ea |
| -6AN straight hose-ends | 2-4 | $15-30 ea |
| -6AN 45°/90° hose-ends | 1-2 | $20-40 ea |
| 5/16" Honda QC to -6AN | 1 | $18-25 ea |

**Realistic total for full purple fitting set: $140-220. Budget: $180.** Black-anodized equivalent saves $40-60. Paying the premium for theme consistency.

---

## 9. Fuel Filter

### OEM In-Tank + Optional Engine-Bay Inline

On the 8th gen Civic SI, the **OEM fuel filter is in-tank, part of the pump hanger** — the DW300C 9-307-1008 kit includes a fresh strainer, so it's replaced automatically at the pump install.

**Additional engine-bay inline filter is recommended for flex fuel:** ethanol can loosen decades-old tank deposits that a single in-tank strainer won't catch, and the Continental sensor downstream benefits from clean fuel.

### Options

- **Aeromotive AN-6 Fuel Filter:** ~$90-140, well-regarded, easy sourcing
- **Radium Engineering Fuel Filter Kit:** ~$80-130, replaceable element, -6AN male ends, 10-40 micron
- **Fuelab Prodigy:** ~$140-200, premium

**Budget: $90** for an Aeromotive or Radium -6AN 10-micron inline filter mounted engine-bay, upstream of the flex sensor.

No separate OEM disposable fuel filter purchase needed — the 8th gen's service filter lives in the tank and ships with the pump kit.

---

## 10. Purple Summary

| Component | Purple Available? | Path |
|---|---|---|
| Acuity fuel rail | **Yes — 1913-PPL factory** | $199 |
| Bosch EV14 injectors | No | Not visible after install |
| DW300C pump | No (in-tank, invisible) | N/A |
| Flex fuel sensor | No (black body) | DIY purple bracket if visible |
| Radium FPR (if ever) | No | Custom anodize $50-100 |
| **AN fittings** | **Yes** — Fragola, Vibrant | $180 for full set |
| PTFE hose | Standard stainless/black braid | Purple braid rare/expensive |
| Fuel pressure gauge | Satin Black or Polished Stainless | $115 |
| Fuel filter | Red/blue/black typical | Not purple |
| Sensor mount bracket | DIY anodize | $25-50 |

**Visible purple in finished engine bay:** Acuity rail (the money shot, sitting on top of the IM) + ~8 purple AN fittings snaking from filter through sensor to rail + DIY bracket if desired. Theme reads clean without paint or re-anodize work.

---

## 11. Install Procedure

Combined injectors + rail + pump + sensor + filter + wiring. **Estimated: 6-10 hours over 1-2 weekends solo, not counting dyno.**

### Safety Pre-Work

Outdoors or well-ventilated garage. Fire extinguisher in arm's reach. Nitrile gloves + safety glasses. No smoking, no grinding, no pilot lights. Fuel at ~58 PSI — respect it.

### Stage 1 — Pressure Relief + Battery Disconnect

1. Cold vehicle (overnight rest). Open fuel filler cap for tank vapor relief.
2. Pull **PGM-FI Main Relay 2** (fuel pump relay) from the **auxiliary under-hood fuse/relay box** (top row center per FSM — verify for my VIN).
3. Start engine, idle until stall (15-60 sec). Crank 2-3 sec after stall to fully bleed rail.
4. Disconnect negative battery terminal (10mm). Tuck cable clear of the post.
5. Reinstall relay (easier for reassembly; pull again if needed during rail work).

### Stage 2 — Remove Stock Rail + Injectors

1. Remove engine/rail cover (4-6x 10mm).
2. Unclip 4 injector connectors.
3. Release Honda QC fitting at stock rail feed — shop rag ready for residual fuel. Use Honda QC release tool if seized, don't pry.
4. Remove 2x M8 rail-to-IM bolts (108 in-lb / 9 ft-lb). Gently work rail off injector tops.
5. Lift rail + 4 injectors up together.
6. Inspect + replace any damaged lower-injector O-rings in manifold bores.

### Stage 3 — Pre-Assemble Acuity Rail + EV14 Injectors

1. On clean bench: Acuity rail, 4x Bosch EV14 550cc, OBD2 pigtail adapters, spare 14mm O-rings.
2. Verify/install upper + lower O-rings. **Lube with fresh engine oil** (no silicone grease — degrades rubber).
3. Hand-press each injector upper into the Acuity rail bore. Check O-ring not rolled/pinched.
4. Connect each injector's USCAR plug to Honda OBD2 pigtail. Verify retention clip engagement.
5. Set pre-assembled rail aside on clean rag.

### Stage 4 — Install Rail Assembly onto IM

1. Lube lower-injector O-rings.
2. Line up 4 injectors with IM bores. Press rail straight down — even pressure both ends, hand pressure only.
3. **Push each injector downward to bottom it; verify upper O-rings still seated in rail.** Re-seat if any backed out.
4. Install 2x M8 mounting screws. **Torque: 108 in-lb (9 ft-lb).**
5. Do not connect fuel feed or injector harness yet — staged for Stage 6.

### Stage 5 — Tank Drop for DW300C (Actually No Tank Drop)

**The 8th gen Civic SI has a rear-seat service panel — no tank drop required.** Saves ~2 hours.

1. Remove rear seat bottom cushion (pull up firmly to release 2 clips, slide rearward out of rear hook).
2. Lift floor carpet, locate fuel pump hanger access cover on passenger side (4-6 Phillips screws or plastic fasteners).
3. Remove cover. Disconnect hanger electrical + fuel line/evap QCs.
4. Remove hanger retaining ring with Honda FSM spanner or large rubber-strap wrench. **Do not use hammer + drift — cracks the tank.**
5. Lift hanger straight up, be careful of the fuel level float arm.
6. On bench: transfer DW300C pump into the hanger per 9-307-1008 kit instructions — old pump out, new DW300C in with supplied grommet/hose/clamps, new in-tank strainer, verify electrical pass-through.
7. Reinstall hanger into tank with fresh O-ring/gasket. **Retaining bolts torque: 39 in-lb** (very gentle, plastic tank threads).
8. Reconnect electrical + fuel/evap lines.
9. Pour ~1 gallon of pump gas if tank is empty (need liquid at the strainer for first prime).
10. Reinstall access cover, carpet, seat cushion.

### Stage 6 — Flex Fuel Sensor + Wiring

1. Choose mount location (inline filter-to-rail, post-filter). Fabricate or buy bracket mounted to firewall/battery-tray bolt boss.
2. **EVAP delete** (if going that route): remove canister + hoses. Ensure Hondata tune suppresses EVAP codes before first start.
3. Route line: stock hardline outlet → inline filter → Continental 13577429 → Acuity rail -8 ORB center-feed.
4. Route -6AN PTFE with slack, no sharp bends. Secure with cushioned P-clamps.
5. Torque AN: tube-nut fittings hand tight + 1/4 turn; -6AN to -8 ORB hand tight + 1/4 to 1/2 turn past O-ring contact; QC-to-AN per vendor (usually 15-25 ft-lb).
6. Wire sensor:
   - 12V switched: tap or add-a-fuse in under-hood box (10A)
   - Ground: clean chassis near sensor
   - Signal: into Innovate MTX-D → gauge's 0-5V output into ECT2 connector at ECU pin A33
7. Verify no wiring chafe near hot exhaust or moving accessories.
8. Pre-key-on visual inspection of every fitting joint.

### Stage 7 — 3-Stage Leak Check

**7A — Cranking only (no start):**
Reconnect battery. Key on/off/on/off/on — pump primes 3 cycles fully. **5-minute visual inspection of every joint.** Beading, wetness, smell. Do NOT start engine until 100% leak-free.

**7B — Idle:**
Start engine (cranking slightly longer than stock — system refilling from empty). Let warm to ~90°C. Re-inspect joints (vibration + thermal expansion reveal leaks not visible at static pressure). Verify Acuity gauge reads ~50-58 PSI warm idle.

**7C — Post-drive:**
20-minute drive cycle, <4000 RPM. Re-inspect on return. Full thermal cycling + real demand variation. Pass = clean. Fail = address before next drive.

### Stage 8 — First Start + Fuel Trims

Live FlashPro monitoring for first 10 min: idle RPM, ECT, STFT, LTFT, rail pressure.

Expected on pump-gas base map: idle ~800 RPM smooth, STFT ±5%, LTFT ±8% first cycle, no CEL. **If trims are +10% sustained:** likely dead-time mismatch or sensor miscalibration. Don't chase the tune — calibrate sensor first.

### Stage 9 — Flex Calibration + Dyno Tune

1. **Calibrate Low Side** with known pump gas (Column 1 of "Ethanol % vs Volts" table).
2. Drive 1-2 tanks pump gas, let pump-gas tune stabilize.
3. **Book dyno session** ($500-650, 3 hr expected). Bring fresh E85 for High-Side calibration.
4. At shop: baseline pump-gas pulls, drain, fill E85, calibrate High Side (Column 2), run compensation tune for fuel + timing, back-to-back dyno validation.
5. Archive `.fpc` file + CSV dyno data for future reference.

---

## 12. E85 Operating Notes

### Fuel System Compatibility — All Green

Every component post-build is E85-safe: polyethylene tank (OEM, E85 OK), DW300C pump (carbon commutators + encapsulated armature), in-tank + inline filters (E85-rated elements), Continental sensor (built for E85), PTFE line section, Acuity rail (6061-T6 aluminum + hard anodize + Viton O-rings), Bosch EV14 injectors (factory E85-compatible Viton seals). **Stock feed hardline is E85-OK medium-term**; replace if degradation appears.

### Cold Start

- >40°F: no issue with proper tune
- 20-40°F: cranking 2-4 sec (vs ~1 sec gasoline), slightly rougher first 30 sec — manageable
- <20°F: straight E85 can fail to start. **Winter-blend E85 (often E55-E65 by law in cold states) helps substantially**. E30-E40 pragmatic in deep winter.
- Tuning mitigation: richer cold-start enrichment + longer cranking priming for high-ethanol end of compensation tables. My tuner dials this.

### Fuel Economy

~25-30% worse MPG on E85 vs pump gas (lower energy density). 26 MPG gasoline → 18-20 MPG E85. E30 ~10-12% worse; E50 ~15-20% worse. E30-E40 is the practical daily sweet spot.

### Tank Water Absorption

E85 is hygroscopic but **tolerates ~4% water by volume** before phase separation — a 13-gallon tank can absorb ~0.5 gal water without phase-separating. In practice a non-issue for a daily driver burning through tanks weekly. For storage >3 months: drain, fill with non-ethanol, or run tank to 1/4 and refill with pump gas. Keep tank full during normal use to minimize condensation air-space. **Burn through, don't store.**

### Pump Octane Variance

ASTM D5798 allows "E85" to range **51-83% actual ethanol**. Winter-blend pumps may sell E51-E70 as "E85." Summer: E70-E83. Midwest (corn belt) hits higher end consistently; coasts/Southeast less consistent. **Sensor handles all of this automatically** — the reason a flash-for-E85 tune without a sensor is dangerous.

### Sensor + Gauge Integration

Innovate MTX-D: ethanol % + fuel temp real-time in cabin. FlashPro datalogger captures same data as "Ethanol Content %" in `.fpdl` logs for post-drive forensics. Both live and forensic — every fill-up documented.

---

## 13. Cost + Phased Plan

### Complete Parts Cost (USD, inc. tax/shipping)

| # | Component | Part | Cost |
|---|---|---|---|
| 1 | Fuel rail | Acuity 1913-PPL Satin Purple | **$219** |
| 2 | Rail fitting (inlet adapter + plug) | -8 ORB to -6AN + 1/8 NPT plug | $20 |
| 3 | Injectors (4) | Bosch EV14 550cc w/ Honda adapters | **$280** |
| 4 | Fuel pump + kit | DW300C 9-307-1008 | **$200** |
| 5 | Flex fuel sensor kit | Continental 13577429 + -6AN barbs | **$95** |
| 6 | Flex fuel gauge/converter | Innovate MTX-D | **$140** |
| 7 | Fuel pressure gauge | Acuity 100 PSI Satin Black | **$115** |
| 8 | PTFE -6AN hose | ~3 ft braided PTFE | $45 |
| 9 | Purple AN fittings | ~8-10 Fragola/Vibrant | **$180** |
| 10 | Sensor QC-to-AN | 3/8" SAE QC to -6AN x2 | $50 |
| 11 | Inline engine-bay filter | Aeromotive -6AN 10-mic | **$90** |
| 12 | Sensor bracket | Custom/aftermarket | $20 |
| 13 | Wiring | Wire, pigtails, fuse tap | $30 |
| 14 | Misc hardware | O-rings, P-clamps, ties | $20 |
| **Parts subtotal** | | | **$1,504** |
| 15 | Sales tax (~8%) | | ~$120 |
| 16 | Flex fuel dyno tune | 3 hr pro session | **$550** |
| **Grand total** | | | **~$2,174** |

### Minimum Viable (skip purple premium, gauge, inline filter)

Skip filter (-$90), fuel pressure gauge (-$115), purple premium on fittings (black instead, -$80). **Minimum: ~$1,890 parts + tune.**

### Phased Purchase Plan

**Phase A — Hardware (~$1,020 parts + ship):** Acuity rail, EV14 injectors + adapters, DW300C, Continental sensor kit, Innovate MTX-D, basic -6AN fittings + short PTFE, engine-bay filter. Complete functional flex-fuel system minus full purple aesthetic + pressure gauge. Bundle-ship from 1-2 retailers. Install in one weekend.

**Phase B — Aesthetic (~$300):** Purple AN fittings to replace the black ones from Phase A. Acuity fuel pressure gauge. Pure visual upgrade, swap fittings during a regular oil change.

**Phase C — Tuning ($550-650):** Book dyno after ~500 miles. Bring fresh E85 for high-side cal. Walk out with dialed flex tune.

**Phase D — Future:** Full PTFE feed line ($200-300) if stock lines degrade. Return-style + adjustable FPR if/when turbo (not soon).

### Dyno Time + Tuning Cost

Base NA tune ~$500 (3 hr). Flex surcharge +$150. Overage ~$150/hr. Deposit ~$150 to book. **Realistic total: $500-650 for complete pump-gas + E85 flex cal.**

---

## 14. Sources

### Part Numbers / Pricing

- [Acuity K-Series Fuel Rail — Satin Purple (1913-PPL)](https://acuityinstruments.com/products/k-series-fuel-rail-in-purple-satin-finish)
- [Acuity K-Series Fuel Rail — Satin Black](https://acuityinstruments.com/products/k-series-fuel-rail-in-black-satin-finish)
- [K Series Parts — Acuity Satin Purple (1913-PPL)](https://www.kseriesparts.com/ACI-1913-PPL.html)
- [Nippon Power — Acuity Purple Fuel Rail](https://nipponpower.com/products/acuity-instruments-k-series-fuel-rail-satin-purple-finish-honda-k20-k24-1913-ppl)
- [Radium K-Series Fuel Rail (20-0230-02)](https://www.radiumauto.com/products/fuel-rail-honda-k-series)
- [Radium K-Rail Install Instructions PDF](https://data.radiumauto.com/PublicDocs/19-0129.PDF)
- [Clean Injection — K20/K24 550cc Bosch Injectors](https://www.cleaninjection.com/product-page/honda-civic-acura-rsx-k20-k24-r18-k20z1-k20z3-k24a4-550cc-bosch-fuel-injectors)
- [Polmax Racing — Bosch EV14 550cc Genuine](https://polmaxracing.com/index.php/product/4-new-genuine-bosch-ev14-52lb-550cc-fuel-injectors-k20-k24-series-engines/)
- [CP Fuel & Race — K20/K24 Bosch EV14 550cc USCAR](https://cpfuelandrace.com/products/honda-k20-k24-4x-550cc-bosch-ev14-fuel-injectors-uscar-connector)
- [High Flow Fuel — Bosch EV14 550cc (0280158117)](https://www.highflowfuel.com/bosch-ev6-ev14-52lb-550cc-fuel-injectors-280158117-choose-qty/)
- [Bosch Motorsport EV14 Data Sheet PDF](https://www.bosch-motorsport.com/content/downloads/Raceparts/Resources/pdf/Data%20Sheet_67797771_Injection_Valve_EV_14.pdf)
- [DeatschWerks DW300C 9-307-1008](https://deatschwerks.com/products/9-307-1008)
- [K Series Parts — DW300C 9-307-1008](https://www.kseriesparts.com/DWS-9-307-1008.html)
- [MAPerformance — DW300C 9-307-1008](https://www.maperformance.com/products/deatschwerks-dw300c-340lph-fuel-pump-w-install-kit-2006-2011-honda-civic-9-307-1008)
- [ACDelco Continental 13577429 on Amazon](https://www.amazon.com/ACDelco-13577429-Original-Equipment-Sensor/dp/B01GQR9C5O)
- [High Flow Fuel — Continental 13577429 w/ AN Barbs](https://www.highflowfuel.com/gm-continental-vdo-flex-fuel-sensor-e85-13577429-an-barbed-fittings-adapter-plug/)
- [Continental OE Flex Fuel Sensors Catalog PDF](https://www.continental-aftermarket.com/media/3213/oe_ffs_conti_2023.pdf)
- [Innovate Motorsports — Ethanol Content Gauges](https://www.innovatemotorsports.com/shop-all/measurement/ethanol-content-e85.html)
- [Innovate MTX-D Gauge](https://www.innovatemotorsports.com/mtx-d-ethanol-content-percentage-fuel-temp-gauge-kit-ethanol-sensor-not-included.html)
- [Acuity 100 PSI FP Gauge — Satin Black](https://acuityinstruments.com/products/acuity-100-psi-fuel-pressure-gauge-in-satin-black-finish)
- [Radium Engineering FPR](https://www.radiumauto.com/products/fuel-pressure-regulator)

### Hondata / Tuning References

- [Hondata ECU Connectors Reference](https://www.hondata.com/help/flashpro/ecu_connectors.htm)
- [Hondata Ethanol Parameters (FlashPro flex fuel tuning)](https://www.hondata.com/help/flashpro/ethanol_tuning.htm)
- [Hondata Forum — Flex Fuel Support](https://www.hondata.com/forum/viewtopic.php?t=21344)
- [Hondata Forum — 550cc EV14 Install Info](https://www.hondata.com/forum/viewtopic.php?t=25170)
- [Hondata Forum — Injector Dead Times (550cc)](https://www.hondata.com/forum/viewtopic.php?t=16773)
- [Hondata Forum — ID Dead Times + Calibration](https://www.hondata.com/forum/viewtopic.php?t=16235)
- [Hondata Forum — E85 Sensor + ECT2 Input](https://www.hondata.com/forum/viewtopic.php?t=24824)

### Install References

- [SiriMoto 8th Gen Civic Si Flex Fuel Kit Install Guide PDF](https://www.sirimoto.com/download/instructions/SiriMoto%20-%20Flex%20Fuel%20Install%20Guide%20-%208th%20Gen%20Civic%20Si.pdf)
- [Hybrid Racing K-Series Fuel Rail Install Guide](https://guides.hybrid-racing.com/Guide/Install+Guide+for+K+Series+Fuel+Rail/66)
- [JBtuned 8th Gen Civic SI Full Fuel System Replacement](https://www.jbtuned.com/products/jbtuned-8th-gen-civic-si-full-fuel-system-replacement-with-return-line-all-fuel-types.html)
- [8thcivic Forum — K20Z3 Torque Specs](https://www.8thcivic.com/threads/all-torque-specs-for-k20z3.242730/)
- [Nthefastlane — K-Series Torque Specs](https://www.nthefastlane.com/k-series-torque-specs)

### Skunk2 Ultra Street + K20Z3 Compatibility

- [Skunk2 Ultra Street Intake Manifold (307-05-0600)](https://skunk2.com/induction/intake-manifolds/ultra-street-intake-manifolds/307-05-0600.html)
- [Hybrid Racing — Skunk2 Ultra Street](https://www.hybrid-racing.com/products/skunk2-k20a2-ultra-street-intake-manifold)
- [TF-Works — Skunk2 PRB-to-RBC TB Adapter](https://www.tf-works.com/skunk2-72mm-prb-flange-to-rbc-pattern-throttle-body-adapter-dbw-to-skunk2-ultra-manifold/)

### E85 Chemistry / Storage

- [PetroClear — Phase Separation in Ethanol Blends](https://petroclear.com/resources/dont-be-phased.php)
- [Ethanol RFA — Water Uptake of Ethanol-Gasoline Blends PDF](https://ethanolrfa.org/file/1793/Water-Update-Weathering-of-Ethanol-Gasoline-Blends-in-Humid-Environments_NREL_2016-09.pdf)
- [NREL Handbook for Handling E85 PDF](https://docs.nrel.gov/docs/fy13osti/57590.pdf)
- [eFlexFuel — Does E85 Go Bad?](https://eflexfuel.com/us/blog/does-e85-go-bad)

### AN Fittings / PTFE

- [Summit Racing — Purple Anodized AN Hose Assemblies](https://www.summitracing.com/search/part-type/an-hose-assemblies/hose-end-fitting-finish/purple-anodized)
- [Fragola Performance Systems](https://fragolaperformancesystems.com/)
- [Vibrant Performance PTFE Hose Ends (Summit Racing)](https://www.summitracing.com/parts/vpe-28006)

### Tuning Pricing

- [XYR Tuned — Hondata FlashPro Service](https://xyrtuned.com/product/flashpro-tuning-service/)

---

## Cross-References

- [`overview.md`](overview.md) — strategic "is flex fuel worth it on NA K20Z3" analysis, cost-vs-WHP breakdown, E85 chemistry background.
- [`../10-Hondata-FlashPro/tuning-workflow-and-maps.md`](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) — Daily/Sport two-map reliability-first tune ceilings this calibration plugs into.
- [`../14-Intake-Manifold/`](../14-Intake-Manifold/) — Skunk2 Ultra Street install, water-bypass adapter, DBW TB adapter spec. Manifold must be finalized before rail install.
- [`../11-Wideband-AFR/`](../11-Wideband-AFR/) — AEM X-Series 30-0300 wideband. Mandatory before flex tune.
- [`../docs/torque-specs.md`](../docs/torque-specs.md) — canonical fastener spec table.
- [`../docs/maintenance-parts-catalog.md`](../docs/maintenance-parts-catalog.md) — add Acuity 1913-PPL, Bosch 0280158117, DW 9-307-1008, Continental 13577429 once finalized.

---

*Last updated: 2026-04-20*
