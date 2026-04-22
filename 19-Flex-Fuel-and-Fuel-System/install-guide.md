# Flex Fuel + Fuel System Install Guide — Acuity Rail + EV14 + DW300C + Continental Sensor

## Status: Planning — Phase 6 (final power adder)

Install companion to [`acuity-fuel-rail-and-flex-fuel-build.md`](acuity-fuel-rail-and-flex-fuel-build.md) (parts + wiring deep dive) and [`overview.md`](overview.md) (strategic NA-flex-fuel analysis). Those docs cover WHAT and WHY. This doc is HOW — the procedure for getting it on the car without starting a fire.

---

## Reality Check Before I Start

This is the most electrically and plumbing-intensive job on the build. The wrenching is moderate, but it touches the fuel system at every level: in-tank pump, feed line, inline sensor, rail, injectors, ECU wiring. Any one of those joints leaking is a fire hazard. Any one wired wrong is either no signal or a damaged sensor.

**Time budget, honest:**

- **Day 0 (full Saturday):** Phase A depressurize → Phase B pump → Phase C sensor plumbing → Phase D rail + injectors. ~8-10 hours solo.
- **Day 1:** Phase E wiring → Phase F FlashPro config → Phase G first-start leak checks. ~4-6 hours.
- **Dyno day (scheduled 2-4 weeks out):** Phase H Tune #3. ~3-4 hours at the shop.

**Difficulty: moderate-high.** The difficulty lives in fuel risk, not mechanical steps. Rush the leak check, buy a garage fire. Skimp on an O-ring, buy a leak on the highway two weeks later. Every fitting, every O-ring, every clamp — right the first time.

**Bundle opportunity:** If doing [`14-Intake-Manifold/`](../14-Intake-Manifold/) around the same time, **combine them.** Rail swap while IM is off the bench saves 2-3 hours of teardown and a round of leak-checking.

---

## Safety First — Read This Twice

**58 PSI of atomized E85 off a loose fitting will find an ignition source I didn't know I had.**

1. **No open flames, grinding, pilot lights, or smoking** anywhere in the garage. Water heater pilot is a killer — shut off gas to the garage or work in the driveway.
2. **Fire extinguisher (Class B or ABC) in arm's reach** — at the fender, not in the corner.
3. **Depressurize the fuel system before ANY line disconnect.** Phase A. No skipping steps.
4. **No sparks.** Battery disconnected before touching any fuel-carrying component.
5. **Work outdoors or garage door wide open.** Fuel vapor pools low and travels farther than I'd expect.
6. **Safety glasses + nitrile gloves** (not latex — latex swells with gasoline).
7. **Keep fuel clean.** Every opened fitting is a chance for dirt to enter. Blue shop towels, sealed catch container — not a coffee can.
8. **If I smell fuel at any point after reassembly, STOP.** Don't crank, don't drive. Find it, fix it, retest.

---

## Prerequisites / Cross-References

### Must Be Done FIRST

| Prerequisite | Why | Reference |
|---|---|---|
| **FBO pump gas Tune #2 complete** | The E0 endpoint in the flex tune IS the FBO calibration. No point interpolating off a calibration that doesn't exist. | [`../10-Hondata-FlashPro/tuning-workflow-and-maps.md`](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) |
| **Wideband AFR installed and reading** | Tuner needs it on the dyno; I need it for Phase G logs. | [`../11-Wideband-AFR/`](../11-Wideband-AFR/) |
| **FlashPro analog 2 input type VERIFIED** | **Critical unknown.** Frequency-capable or voltage-only? Decides whether MTX-D is inline or standalone. See Decision Tree below. | [`../10-Hondata-FlashPro/hardware-software-deep-reference.md`](../10-Hondata-FlashPro/hardware-software-deep-reference.md), [`acuity-fuel-rail-and-flex-fuel-build.md`](acuity-fuel-rail-and-flex-fuel-build.md) |
| **Cooling refresh + ignition refresh complete** | E85 tune extracts more power = more heat. Weak coil shows up as E85-load misfire. | [`../09-Cooling-System/`](../09-Cooling-System/), [`../06-Ignition-Refresh/`](../06-Ignition-Refresh/) |
| **Innovate MTX-D converter ON HAND** | Even if analog 2 is frequency-capable, MTX-D is the drop-in fix if Phase F shows no signal. No shipping delay mid-install. | — |
| **Dyno session pre-booked** | Flex tune shops book 2-4 weeks out. Book when I order parts, not after install. | [`../10-Hondata-FlashPro/tuning-workflow-and-maps.md`](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) |

### Bundle Opportunity

- **IM install (`14-Intake-Manifold/`) is the ideal pairing** — rail swap trivial with IM off.
- Headers (`13-Headers/`) separate — one session per major airflow change.

---

## Tools Required

**Critical:**

- **Honda fuel line QC release tool set** (5/16" and 3/8" SAE). Prying with a screwdriver wrecks lines and collars.
- **Torque wrench 1/4" drive, 20-200 in-lb** — rail bolts (108 in-lb) and pump hanger (39 in-lb).
- **Torque wrench 3/8" drive, 10-80 ft-lb** — AN fittings up to 30 ft-lb.
- **Line wrenches** (5/8", 11/16") — grip all 6 flats; open-end wrenches round AN hex.
- **Multimeter** — continuity, 12V verification, sensor signal checks.
- **Scope or frequency-capable DMM (optional)** — reading Continental's 50-150 Hz direct. If skipped, MTX-D readout is verification.
- **Sockets 10/12/14mm.**
- **Rear seat removal tools** — Phillips + 10mm for cushion anchors.
- **Fuel pump hanger spanner or rubber-strap wrench** — for the in-tank retaining ring. **Hammer + drift cracks the plastic tank.**
- **Fire extinguisher, sealed fuel catch container (1-2 gal fuel-rated).**
- **Ratcheting wire crimper, heat shrink, heat gun.** No electrical tape on fuel-system wiring.
- **Nitrile gloves, safety glasses, shop rags/blue towels.**

**Also useful:** magnetic parts tray, inspection mirror + headlamp, carb cleaner + small brush, zip ties, cushioned P-clamps.

---

## Parts List

Full BOM with prices in [`acuity-fuel-rail-and-flex-fuel-build.md`](acuity-fuel-rail-and-flex-fuel-build.md) §13. Install-day checklist:

| # | Part | PN | Qty |
|---|------|-----|---|
| 1 | Acuity K-Series Rail, Satin Purple | **1913-PPL** | 1 |
| 2 | Bosch EV14 550cc injector | **0280158117** | 4 |
| 3 | USCAR-to-Honda OBD2 injector adapter pigtails | (per vendor) | 4 |
| 4 | DW300C pump kit | **9-307-1008** | 1 |
| 5 | Continental flex fuel sensor | **13577429** | 1 |
| 6 | Innovate MTX-D frequency-to-voltage gauge/converter | MTX-D | 1 |
| 7 | PTFE -6 AN braided hose | ~3 ft | 1 |
| 8 | -6 AN fittings + adapters (per build doc §8) | — | ~8-10 |
| 9 | Fresh 14mm Viton O-rings (spare) | — | 2× set |
| 10 | Inline engine-bay filter, -6 AN 10-mic | Aeromotive or Radium | 1 |
| 11 | 18 AWG automotive wire (red/black/white) | — | ~15 ft each |
| 12 | 5A add-a-fuse | mini blade | 1 |
| 13 | Heat shrink + crimp terminals + P-clamps | assortment | — |

**Don't skimp on O-rings.** Reusing a stock O-ring on a new EV14 is the #1 cause of post-install leaks. Fresh Viton pack as install-day insurance.

---

## Step-by-Step — Phased Install

### Phase A — Depressurize the Fuel System

**Most-skipped step on the internet. The one that starts fires. Do not skip.** Rail sits at ~50-58 PSI at rest.

A1. Level surface, engine off, cold.
A2. Open fuel filler cap — relieves tank vapor pressure.
A3. Under-hood **auxiliary fuse/relay box** (driver side). Pull **PGM-FI Main Relay 2** (fuel pump relay). Set aside.
A4. Start engine. Runs 15-60 sec on residual rail pressure and stalls.
A5. Crank starter 2-3 more seconds after stall. Bleeds last of pressurized fuel through injectors.
A6. Key fully off, key out.
A7. Disconnect **negative** battery terminal (10mm). Tuck clear of post.
A8. **Confirm depressurized** by loosening the rail feed union slowly over 30 seconds with a shop rag wrapped around the joint. Residual drip is normal. **Spray means I didn't depressurize** — reconnect, repeat A3-A5.
A9. Reinstall the PGM-FI relay once confirmed (pull again in Phase G if needed).

---

### Phase B — DW300C Pump Install (In-Tank)

**8th gen has a rear-seat service hatch. No tank drop.**

B1. Remove rear seat bottom cushion — pull firmly at front edge (two plastic clips release), slide rearward to unhook back anchor, lift out.
B2. Fold back carpet above the tank.
B3. Locate **fuel pump access panel** on passenger side. 4-6 Phillips or plastic fasteners. Remove.
B4. **Photograph connections.** Phone camera, 4-5 angles. Reassembly reference.
B5. Disconnect pump harness connector (squeeze tab, pull).
B6. Disconnect fuel feed line at hanger QC. Shop rag wrapped. Slide collar forward, pull line straight off.
B7. Disconnect EVAP line if present at hanger.
B8. Unlock **retaining ring** counterclockwise with spanner or rubber-strap wrench. **Never hammer + drift** — cracks the tank collar.
B9. Lift hanger **straight up** — careful of the fuel level float arm (bends easily).
B10. Move to clean bench with small drip pan.
B11. Per DW 9-307-1008 kit instructions: remove stock pump from hanger, install DW300C with supplied grommet/hose/clamps, install new in-tank strainer, reconnect internal harness per kit polarity diagram.
B12. Inspect hanger-to-tank O-ring/gasket. Replace if crusty (available from DW or dealer).
B13. Lower hanger back into tank, mind the keyed orientation and float arm.
B14. Hand-thread retaining ring clockwise, then tighten. **Torque: 39 in-lb** per [`../docs/torque-specs.md`](../docs/torque-specs.md). Plastic threads — gentle.
B15. Reconnect external pump harness, fuel feed QC (tug-test for click engagement), EVAP line.
B16. If tank is near-empty, pour **~1 gallon pump gas** now. Pump strainer needs liquid for first prime.
B17. Reinstall access panel, carpet, seat cushion. **Leave battery disconnected until end of Phase G.**

---

### Phase C — Install Continental 13577429 Flex Sensor (Inline)

C1. **Location: between inline engine-bay filter and Acuity rail inlet.** Post-filter (sensor sees clean fuel), close to rail (minimal fillup lag). Firewall or battery tray bolt bosses.
C2. **If deleting EVAP canister** (planned per build doc §4): remove canister, cap remaining lines per JBtuned reference. Confirm FlashPro tune suppresses EVAP codes before Phase G start. Keeping EVAP = find space elsewhere (tight).
C3. **Mount the sensor bracket** — simple bent-steel angle from ACE ($5) or purchased from JBtuned/SiriMoto. Mount sensor with **fuel flow arrow pointing toward engine**. Sensor body is marked.
C4. **Line routing:** stock hardline → 5/16" Honda QC-to--6 AN → inline filter (flow arrow) → short PTFE -6 AN → sensor (3/8" SAE QC-to--6 AN each side) → short PTFE -6 AN → -8 ORB-to--6 AN adapter → Acuity rail center-feed.
C5. **Cut stock hardline** at filter inlet. Clean square cut, tubing cutter, not a hacksaw.
C6. Pre-assembled PTFE -6 AN hoses from Summit/Russell/Fragola save the hose-vise crimping step. Measure twice.
C7. **AN torque:**
  - -6 AN unions: hand tight + 1/4 turn (O-ring seals at contact, not crush).
  - -8 ORB at rail: hand tight + 1/4 to 1/2 turn past O-ring contact.
  - QC-to-AN adapters: vendor spec, typically 15-25 ft-lb on AN side.
  - **Never over-torque O-ring joints.** Crush damage causes warm-pressurized leaks.
C8. **Secure with cushioned P-clamps.** No chafe points against body, hot exhaust, moving parts. Trace line visually from tank to rail, confirm no hot/vibrating contact.

---

### Phase D — Acuity 1913-PPL Rail + EV14 Injectors

**Much easier with IM off the car.** Bundle with [`../14-Intake-Manifold/`](../14-Intake-Manifold/) install. Steps below assume IM on the car.

D1. Remove engine/rail cover (10mm bolts).
D2. Unclip 4 injector connectors. Label 1-2-3-4 front-to-rear (masking tape).
D3. Disconnect stock feed line at rail union if not already off from Phase A. Shop rag.
D4. Remove 2× M8 rail-to-IM bolts (108 in-lb spec). Gently.
D5. Lift stock rail straight up — the 4 injectors come with it (upper O-ring friction).
D6. Set stock assembly aside as parts-shelf spare.
D7. **Inspect IM injector bores.** Clean rag, small brush + carb cleaner if dirty. No wire brush on sealing surfaces.
D8. **Pre-assemble Acuity rail + EV14s on a clean bench:**
  - Verify all 8 injector O-rings present (top + bottom × 4). Genuine Bosch ships with them. Replace any rolled/pinched/discolored.
  - **Lube every O-ring with fresh engine oil.** Thin coat. Not silicone grease, not assembly lube.
  - **Press each EV14 upper into the Acuity rail.** Straight in, no twisting. Firm hand pressure, no hammer. Verify upper O-ring fully seated.
  - Connect USCAR plug to Honda OBD2 pigtail. Clip must click.
D9. Lube lower O-rings just before IM install (no dust pickup).
D10. Line up 4 injectors with IM bores. **Lower rail straight down, even pressure both ends.** If one resists, back off — rolled O-ring.
D11. **Push each injector down to fully seat in IM.** Then **verify each upper O-ring is still in the rail bore** — pressing down sometimes backs an upper out. If so, re-seat.
D12. Install 2× M8 bolts. **Torque: 108 in-lb / 9 ft-lb** (per [`../docs/torque-specs.md`](../docs/torque-specs.md)). Alternate bolts, two passes, 50% then final. Aluminum IM threads — gentle.
D13. Connect Phase C fuel feed line to rail center-feed -8 ORB. Hand tight + 1/4 to 1/2 turn past contact.
D14. **Do NOT connect injector harness yet.** Staged for Phase G leak check.

---

### Phase E — Wiring — Flex Sensor

**Read the Decision Tree below BEFORE wiring the signal line.**

Continental 13577429 has 3 wires:

| Function | Typical Color | Connects To |
|---|---|---|
| Sensor power | **Red** (verify pinout) | Switched 12V |
| Sensor ground | **Black** | Clean chassis ground |
| Frequency signal out | **White or Yellow** | Per Decision Tree below |

**Verify colors against Continental 13577429 pinout** (ships with High Flow Fuel bundle or Hondata KB).

E1. Route 3-wire harness from sensor to 12V tap, ground, and signal destination. 18 AWG automotive wire, ~6" slack at each end.
E2. Cushioned P-clamps every ~12". No chafe against body, hot surfaces, moving linkages.
E3. **Power (switched 12V):** add-a-fuse on an accessory circuit in under-hood box, 5A new leg. Or splice into injector harness 12V — **verify stable during cranking** (some accessory circuits drop during start).
   - **Never a constant-12V circuit** — sensor draw discharges battery during sits.
E4. **Ground:** clean bare-metal chassis point near sensor. Scuff to bare, ring terminal + lock washer + star washer + M6/M8 bolt.
   - **Star topology — no daisy chains.** Flex sensor, MTX-D (if used), and FlashPro analog all go to the same chassis point, not chained. Chained grounds cause voltage drops that shift signal.
E5. **Signal — follow Decision Tree.**

---

### Flex Sensor Frequency vs Voltage Decision Tree — MOST IMPORTANT SECTION

**FlashPro Original's analog 2 input type is the load-bearing unknown for this install.** Two possible answers, two wiring paths. Verify before wiring.

**How to verify:**

1. Hondata KB — search "flex fuel K20Z3 analog input" for my specific FlashPro unit.
2. **Ask my tuner.** They've wired more of these than I ever will.
3. Cross-ref [`../10-Hondata-FlashPro/hardware-software-deep-reference.md`](../10-Hondata-FlashPro/hardware-software-deep-reference.md) (flagged **[VERIFY]** there).
4. Cross-ref [`acuity-fuel-rail-and-flex-fuel-build.md`](acuity-fuel-rail-and-flex-fuel-build.md) §4-§5. Build doc recommends MTX-D path regardless on the conservative assumption analog 2 is voltage-only. That's the safe default.

#### Path 1 — FlashPro Analog 2 Reads Frequency Natively

Simpler wiring if verified:

- Continental signal wire → directly to FlashPro analog 2 (at FlashPro unit or ECU pin A33 / ECT2 depending on unit termination).
- FPM → Parameters → Analog Inputs → Analog 2: **flex fuel frequency preset**, calibrate 50 Hz = 0%, 150 Hz = 100%.
- No MTX-D inline. MTX-D stays as standalone cabin gauge if desired.

#### Path 2 — FlashPro Analog 2 Is Voltage-Only (Default Plan)

**Default. Build doc §4 recommends this. Documented SiriMoto approach.**

- Continental signal wire → **Innovate MTX-D input.**
- MTX-D reads 50-150 Hz, converts to 0-5V analog.
- MTX-D analog output wire → **FlashPro analog 2** (or ECU pin A33 / ECT2).
- MTX-D powered: switched 12V + chassis ground + illumination if desired. Gauge in-cabin for live ethanol % readout.
- FPM → Parameters → Analog Inputs → Analog 2: **ethanol % vs voltage** mapping. Per MTX-D docs, typical **0V = 0% (50 Hz), 5V = 100% (150 Hz)** linear. **Verify against current Innovate MTX-D manual** — scaling has been updated across revisions.

**My default: Path 2.** If tuner verifies Path 1 for my specific FlashPro Original, simplify later. Path 2 is the safe baseline.

E6. Complete signal wiring per chosen Path. **Every splice: proper crimp + heat shrink.** No electrical tape.
E7. **Continuity check with multimeter before battery reconnect:**
  - Power wire to 12V tap: continuous (0 ohms).
  - Ground wire to chassis: continuous.
  - Signal wire to destination: continuous.
  - No shorts to ground on power or signal wires.

---

### Phase F — FlashPro Configuration

F1. Laptop + FlashPro connected, FPM open. Current calibration = my Tune #2 FBO pump (untouched).
F2. FPM → Parameters → **Flex Fuel → Enable**.
F3. Set **sensor input source** per Decision Tree path:
  - Path 1: analog 2, frequency, 50 Hz = 0% / 150 Hz = 100%, linear.
  - Path 2: analog 2, voltage, 0V = 0% / 5V = 100% (or per MTX-D manual), linear.
F4. **Don't touch fuel/timing tables yet.** This flex-ready tune READS the sensor — the tuner calibrates compensation on the dyno.
F5. Save as **`FBO_PUMP_FLEX_READY_20260420.fpc`**. Keep original FBO pump `.fpc` as untouched backup.
F6. Flash to ECU. Normal flash — engine off, battery > 12.5V.
F7. Verify ethanol sensor appears as monitored parameter in Parameter Monitor. May read 0 or noisy until sensor powered and flowing (next phase).

---

### Phase G — First-Start Verification (Before Dyno)

**Three-stage leak check. Each finds leaks the previous doesn't.**

G1. Reconnect battery negative terminal (~96 in-lb / 8 ft-lb).
G2. Reconnect injector harness — all 4 click.

G3. **Stage 1 — KEY ON, PUMP PRIME, NO START:**
  - Key ON (not START), hold 2 sec, pump primes, OFF. Repeat 3 cycles. Builds rail pressure.
  - **5-minute visual inspection every joint:** pump hanger to tank, feed QC, every AN fitting from hardline to filter to sensor to rail, -8 ORB rail inlet, every injector upper + lower seat (watch around injector body), unused rail -8 ORB plugs.
  - **Any beading/wetness/fuel smell = STOP.** Address leak. Re-prime. Re-inspect. **Do not start.**

G4. **Stage 2 — IDLE:**
  - **Only if Stage 1 is clean.** Start. Longer crank than normal is fine (system refilling after Phase A).
  - Idle 5 min, warm to ~90°C. **Re-inspect during warmup** — vibration + thermal expansion reveal leaks static pressure won't.
  - FlashPro datalog. Monitor:
    - **Ethanol reading** (~0% on pump gas). If it stays 0% on a known E85 fill, wiring is wrong (see Common Mistakes).
    - **STFT / LTFT:** ±5% / ±8% first cycle.
    - **Fuel pressure** on Acuity gauge (if installed): 50-58 PSI steady.
    - **No CEL** (EVAP codes suppressed if canister deleted — verify).
    - **No misfires.**

G5. **Stage 3 — SHORT DRIVE:**
  - **Only if Stage 2 is clean.** 20-minute drive, RPM < 4000, no WOT, mixed city/light highway.
  - Return: re-inspect every joint a third time. Thermal + demand reveals slow leaks.
  - Post-drive log review: fuel trims within ±10%, no knock counts, ethanol reading stable and sensible.

G6. **Optional but highly recommended sensor verification:**
  - Drain tank low or burn it down on a drive.
  - Fill a deliberate E30 blend: 30% E85 + 70% pump gas by pump-gallon math.
  - Drive 5-10 miles to mix and feed sensor.
  - FPM ethanol reading climbs from ~0-10% baseline toward ~30%.
  - **No change = sensor dead, wired wrong, or MTX-D not converting.** Diagnose before Phase H.
  - **Change but wrong magnitude** = 2-point calibration endpoints need adjustment (build doc §5).

G7. **No WOT on this flex-ready tune.** Compensation tables aren't loaded yet; the ECU uses the E0 fuel/timing map regardless of ethanol reading. Fine for cruise, lean under WOT if E85 in tank. Stay out of WOT until Phase H complete.

---

### Phase H — Book Dyno Session (Tune #3)

**Most complex tune on the build. Budget $400-600, 3-4 hours.** See [`../10-Hondata-FlashPro/tuning-workflow-and-maps.md`](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) for session planning.

H1. **Bring:**
  - Laptop + FPM, FlashPro + USB cable.
  - `.fpc` files: STOCK backup, Tune #2 FBO pump, FBO_PUMP_FLEX_READY.
  - Phase G datalogs (tuner sees the sensor is reading).
  - **Fresh E85** — 5-gallon jerrycan, verified station. Tank near-empty arriving.

H2. **Pre-session tuner verifies:** wideband idle reading sensible, ethanol sensor tracking real fuel, fuel pressure 58 PSI under load, no pending CELs.

H3. **Session flow (tuner-led):**
  - Baseline pump-gas pulls — confirm E0 endpoint = Tune #2 output.
  - Drain tank, fill fresh E85 from jerrycan. Drive/cycle 5-10 miles to flush old fuel and let sensor catch up (reading climbs to 70-83% — true E85 varies per ASTM D5798).
  - **Calibrate high-side** (E85 endpoint) of ethanol % vs voltage using live flex gauge reading.
  - **Build Ethanol Fuel Compensation** (~+30-40% at E85) and **Ethanol Timing Compensation** (+3 to +5 deg at E85).
  - **Floors (reliability ceilings from tuning-workflow-and-maps):**
    - E85 WOT lambda floor: **0.82 — never leaner.**
    - Pump gas WOT AFR floor: **12.0 — never leaner.**
    - Zero knock counts at WOT, both endpoints.
    - Injector duty < 85% at peak, both endpoints.
    - Fuel pressure ±2 PSI at peak WOT.

H4. **Dual-map × E0/E85 = 4 operating corners tuned:**
  - Daily + E0 — primary daily calibration.
  - Daily + E85 — same conservative character, E85-compensated.
  - Sport + E0 — aggressive-within-envelope on pump gas.
  - Sport + E85 — max power corner, ~230-250 WHP target.
  - (FlashPro Original switches via laptop flash. Daily/Sport = two `.fpc` files, each with E0/E85 endpoints. LattePanda install later makes switching a one-tap operation.)

H5. **Archive all calibrations** — laptop + cloud. Filename convention:
  - `FLEX_DAILY_E0E85_20260520.fpc`
  - `FLEX_SPORT_E0E85_20260520.fpc`
  - Dyno sheets + CSV logs filed alongside.

---

## Post-Install Break-In

- **First 200 miles: pump gas only.** Mixed driving, no WOT. Fuel trims stabilize, thermal cycles reveal slow leaks.
- **Then ethanol gradually:** E30 → E50 → E85. Each fill, drive 5 miles to mix. Confirm FPM reading tracks.
- **Expect ~25-30% fuel economy drop on E85** — normal, lower energy density. >30% drop = something wrong (leak, wrong dead times, miscalibrated sensor).
- **Re-check every AN fitting at 100 mi and 500 mi.** Thermal-cycle seep is the #1 post-install failure.
- **Oil change at 500 mi** — catches any fuel dilution from enrichment early.

---

## First Drive Checklist

- [ ] **No fuel leaks** at any joint (visual + no cabin/bay fuel smell).
- [ ] **Ethanol reading sensible** for current fuel.
- [ ] **Fuel pressure 58 PSI stable** at idle (Acuity gauge if installed).
- [ ] **Injector duty reasonable at cruise** (10-20% at 60 mph typical).
- [ ] **No misfires, no pending CELs, no knock counts.**
- [ ] **Smooth idle** — rough = dead times probably off.
- [ ] **Smooth cold start** — if rough, tuner dials in richer cold enrichment on follow-up.

---

## Fueling Protocol

The flex fuel system handles any blend, but don't dump E85 at random:

- **Blend at the pump over multiple fills.** First switch from pump gas to E85: do E50 (half E85 over half pump gas remainder) before straight E85. Not for the car's sake — for my confidence watching sensor track.
- **Sensor updates within 2-5 miles** of mixed driving after a fresh fill. If it doesn't move after 10 miles, something's wrong.
- **ASTM D5798 allows "E85" to range 51-83% actual.** Sensor handles this automatically. Never assume the pump matches the label.
- **Note consistent stations.** Predictable E-content = predictable power.
- **Don't let E85 sit >3 months.** Hygroscopic. Burn through tanks or drain to empty and fill pump gas for storage.

---

## Common Mistakes

- **Reusing stock injector O-rings on new EV14s.** Looks fine dry, leaks hot and pressurized. Fresh Viton, every time.
- **Installing the flex sensor backwards** (flow arrow toward tank). Sensor may read but lag is much worse; some Continentals won't measure correctly against flow. Check the arrow.
- **Wrong sensor wiring pinout** — ground not grounded, power on constant-12V, signal grounded instead of routed to analog input. Result: reads 0% or intermittent. Multimeter-verify BEFORE first start.
- **Skipping MTX-D when FlashPro Original analog 2 is voltage-only.** Frequency signal into voltage input = no reading, possible input damage. Default Path 2 unless verified otherwise.
- **WOT on E85 before Tune #3.** Flex-ready tune reads the sensor but has no compensation loaded. Running E85 WOT on pump-gas calibration is 30% lean — lean knock, hot plugs, bad day. No WOT until post-dyno.
- **Depressurizing the wrong sequence** (battery disconnect before pulling the pump relay and stalling). System stays pressurized; first line disconnect sprays fuel. Phase A in order.
- **Over-torquing AN fittings.** O-rings seal at contact, not crush. Past contact + 1/4 turn damages the O-ring. Warm pressurized leak appears later.
- **Chained grounds.** Sensor ground → MTX-D ground → analog ground in a daisy chain causes voltage-drop-induced signal drift. Star topology always.
- **Filling tank before first prime.** Dry strainer can burn the pump on first prime. One gallon of pump gas before key-on (Phase B16).
- **Teflon tape on AN fittings.** AN seals on flare or O-ring, not threads. Tape shreds into the fuel system.

---

## See Also / Cross-References

- [`overview.md`](overview.md) — strategic "is flex fuel worth it on NA" analysis, realistic WHP gains, cost-vs-value.
- [`acuity-fuel-rail-and-flex-fuel-build.md`](acuity-fuel-rail-and-flex-fuel-build.md) — **detailed parts + wiring reference.** Source of truth for part numbers, pricing, wiring detail, aesthetics. This install-guide is the procedural companion.
- [`../14-Intake-Manifold/`](../14-Intake-Manifold/) — bundle fuel rail swap with IM off the car.
- [`../10-Hondata-FlashPro/tuning-workflow-and-maps.md`](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) — three-tune plan; this is Tune #3. Daily/Sport rules, reliability-first AFR ceilings.
- [`../10-Hondata-FlashPro/hardware-software-deep-reference.md`](../10-Hondata-FlashPro/hardware-software-deep-reference.md) — FlashPro Original analog 2 input type verification (the load-bearing unknown).
- [`../11-Wideband-AFR/`](../11-Wideband-AFR/) — AEM X-Series required before any dyno tune.
- [`../docs/torque-specs.md`](../docs/torque-specs.md) — canonical specs: rail bolts 108 in-lb, pump hanger 39 in-lb, O2 sensor 33 ft-lb, banjo bolts 25 ft-lb.

---

*Last updated: 2026-04-20*
