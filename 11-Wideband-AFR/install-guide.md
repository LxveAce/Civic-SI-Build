# Wideband AFR Install Guide — AEM X-Series 30-0300

## Status: Pending — install tied to header install (Phase 2B / 1G)

The bung welding step physically happens DURING my Skunk2 Alpha header install (see [13-Headers/install-guide.md](../13-Headers/install-guide.md) Phase H). The rest of this job — sensor, gauge, wiring, FlashPro config — can be done in the days after the header swap, before I hand the car over for a dyno tune.

---

## Reality Check Before I Start

Mid-complexity install with two skill demands: welding (or hiring it out) and careful low-voltage wiring. The wiring is where most DIY installs fail and then spend a week chasing phantom AFR noise in datalogs.

- **Bung welding:** 30 min at a muffler shop, $20-40 cash. I'm NOT welding stainless exhaust tube myself unless I have a proper MIG/TIG setup with stainless filler. Leaky bung weld = lean-reading sensor = engine damage. Outsource this.
- **Wiring:** 2-3 hrs careful work. Crimp, solder critical joints, heat-shrink, twisted-pair signal, star-ground topology.
- **Total hands-on time:** ~3 hrs if welding is outsourced and header install is already happening.
- **Reliability note:** NEVER tune without a working wideband. Every fuel table decision depends on this sensor. A bad wideband reading is worse than no wideband reading — it produces confidently wrong tuning changes.

---

## Prerequisites / Cross-references

### Must be done FIRST or AT THE SAME TIME

| Requirement | Why |
|-------------|-----|
| Header install in progress (see [13-Headers/install-guide.md](../13-Headers/install-guide.md) Phase H) | The bung welds into the Skunk2 Alpha collector while the exhaust section is off the car. Retrofitting later is a pain. |
| FlashPro paired + first flash complete (see [10-Hondata-FlashPro/overview.md](../10-Hondata-FlashPro/overview.md)) | I need FPM working before I can enable and scale Analog Input 1. |
| FlashPro analog pinout confirmed (see [10-Hondata-FlashPro/hardware-software-deep-reference.md](../10-Hondata-FlashPro/hardware-software-deep-reference.md) Section 2) | Wrong pin = no signal or ECU damage. Verify from Hondata's published diagram before wiring. |

### Must be done BEFORE any dyno tune

| Rule | Why |
|------|-----|
| Wideband MUST be installed, calibrated, and verified before dyno time (see [10-Hondata-FlashPro/tuning-workflow-and-maps.md](../10-Hondata-FlashPro/tuning-workflow-and-maps.md)) | The tuner will not (and should not) touch fuel tables without real AFR data. Showing up to a dyno session without a working wideband wastes the appointment. |
| Commanded vs actual AFR verified in datalog | If the wideband reads 0.5+ AFR off commanded at steady-state cruise on a stock-ish tune, something is wrong (exhaust leak, bung placement, sensor aging) and the tuner needs to know BEFORE pulling on throttle. |

### Shared analog input budget

My FlashPro (original, not FlashPro 2) has **2 analog inputs**. The allocation is locked:

- **Analog Input 1 → Wideband AFR (this mod)**
- **Analog Input 2 → Flex fuel ethanol sensor** (see [19-Flex-Fuel-and-Fuel-System/](../19-Flex-Fuel-and-Fuel-System/))

There is no third input. If I ever want oil pressure or boost logging later, I'm either upgrading to FlashPro 2 or reading those values through a separate datalogger.

---

## Tools Required

**For the bung weld (if DIY — otherwise muffler shop does this):**
- MIG or TIG welder capable of clean stainless welds
- 308L or 316L stainless filler rod/wire
- Step drill or hole saw sized for the 18mm bung
- Grinder with stainless-safe flap disc
- Welding helmet, gloves, leather

**For sensor install:**
- O2 sensor socket (22mm, with wire slot) — already own from header job
- Torque wrench, 30-40 ft-lb range
- Copper anti-seize (NOT aluminum, NOT nickel — copper handles exhaust temps better)

**For wiring:**
- 18 AWG automotive primary wire (red, black, and one signal color — I'm using green)
- Quality crimp terminals (butt connectors, ring terminals for ground)
- Solder + flux (for critical joints only — crimps for everything else)
- Adhesive-lined heat-shrink tubing, multiple diameters
- Heat gun (NOT a lighter — uneven heat melts the adhesive unevenly)
- Wire strippers
- Multimeter (continuity + DC voltage modes mandatory)
- Add-a-fuse tap, mini blade style (FG2 interior fuse box uses mini blades per CLAUDE.md)
- Zip ties (high-temp rated for anything within 6" of exhaust)

---

## Parts List

From [overview.md](overview.md), with quantities and placement notes:

| # | Item | Part Number | Qty | Notes |
|---|------|-------------|-----|-------|
| 1 | AEM X-Series Wideband UEGO Gauge Kit | AEM 30-0300 | 1 | Includes gauge, Bosch LSU 4.9 sensor, weld bung, bung plug, wiring harness |
| 2 | Extra 18mm O2 bung (backup) | Universal stainless weld-in | 1 | Kit usually ships with one — this is my backup if the first one gets tacked in the wrong spot |
| 3 | A-pillar gauge pod | Autometer 20400 (black, 06-11 Civic) | 1 | Single 2-1/16" gauge |
| 4 | Mounting hardware for pod | Comes with pod | — | |
| 5 | Add-a-fuse tap (mini blade) | Littelfuse FHM200BP or similar | 1 | For ACC(A) fuse #8 7.5A switched 12V |
| 6 | Inline fuse holder + 5A fuse | Generic | 1 | Protects the gauge power wire past the tap |
| 7 | 18 AWG primary wire | 15 ft red, 15 ft black, 15 ft green | — | Signal run needs to be long enough to route properly |
| 8 | Copper anti-seize | Permatex 80078 or similar | 1 tube | Exhaust threads only |
| 9 | Adhesive-lined heat-shrink assortment | Generic | 1 pack | 3/16" through 1/2" diameters |

Kit contents in the AEM 30-0300 box: X-Series 52mm gauge, Bosch LSU 4.9 sensor (pre-calibrated), 18mm weld-in bung + plug, wiring harness with AO1/AO2 outputs, sensor extension harness, mounting bezel.

---

## Step-by-Step

### Phase A: Bung Welding (during header install — see [13-Headers/install-guide.md](../13-Headers/install-guide.md) Phase H)

This happens while the Skunk2 Alpha + Berk HFC assembly is OFF the car during my header session.

1. **Mark the bung location.** On the Berk HFC section, 12-18" downstream of the Skunk2 Alpha collector outlet. The sensor must be:
   - **Post-collector** — merged flow from all primaries, laminar, cylinder-averaged AFR
   - **Post-HFC** — high-flow cat, so sensor sees exhaust hot enough for the LSU 4.9
   - **NOT inside any catalytic converter substrate** — cat chemistry skews O2 readings
   - **In a straight section** — bends cause swirl and noisy readings
2. **Angle the bung UP.** At least 10 degrees above horizontal (ideally 15-45 degrees) so condensate drains AWAY from the sensor tip on cold starts. The LSU 4.9 will crack if water hits it while heated. Top or upper side of the pipe, NEVER bottom.
3. **Drill the hole.** Step drill sized to snug-fit the bung shank. Deburr.
4. **Weld the bung on.** Muffler shop, $20-40, 30 minutes. Hand them the bung, point at the marked spot, tell them "post-cat, angled up, full penetration weld, no leaks."
5. **Install the bung plug.** The AEM kit ships with a threaded plug. **LEAVE THE PLUG IN during initial header heat cycles and the first 50-100 miles of header break-in.** The LSU 4.9 is fragile to thermal shock and curing ceramic/oil fumes on a fresh header fire-up. Plug first, sensor after bed-in.

### Phase B: Sensor Install (after header break-in, before first tune)

6. **Use the NEW LSU 4.9 from the AEM kit.** Do NOT reuse an old narrowband or used wideband. The kit sensor is pre-calibrated to the gauge electronics.
7. **Apply copper anti-seize to the sensor threads — SPARINGLY.** Thin smear on threads only. Do NOT get anti-seize on the sensor element (the slotted tip) — it will contaminate the sensor permanently. Copper only; aluminum anti-seize degrades at exhaust temps.
8. **Hand-thread the sensor into the bung** until snug. If it doesn't start smoothly, back out — cross-threading wrecks the bung.
9. **Torque to 33 ft-lb** with the O2 socket. See [docs/torque-specs.md](../docs/torque-specs.md).
10. **Route the sensor harness** away from hot exhaust. Minimum 2" clearance. Zip-tie to rigid exhaust-adjacent points (subframe, brackets) — NEVER to the exhaust itself or to anything moving independently of the engine.
11. **Route the harness into the engine bay** following the stock O2 harness path to the firewall grommet.

### Phase C: Gauge Mounting

12. **Pick a mount location.** A-pillar pod (Autometer 20400), dash-top, or vent pod. A-pillar is cleanest.
13. **Temporary mount first.** Before committing to drilling or permanent wiring, sit in the driver's seat with the gauge held in the prospective location and verify: readable in under 0.5s glance, does NOT block view of road/gauges/mirrors, cable run to firewall is feasible.
14. **Run wiring through the existing firewall grommet** on the driver's side near the brake booster. Do NOT drill a new hole — new firewall holes invite water and noise.
15. **Install the gauge in the pod** per the pod instructions.

### Phase D: Wiring

Every wire decision on this gauge matters because the 0-5V analog signal going to FlashPro is low-level and susceptible to EMI from the ignition system.

16. **Power — switched 12V.** Tap the ACC(A) fuse #8 (7.5A) in the interior fuse box per CLAUDE.md. Mini blade add-a-fuse: load side keeps the original 7.5A fuse, hot side gets a NEW 5A fuse protecting my circuit. **DO NOT tap constant 12V (BACK UP fuse #20)** — the LSU 4.9 heater pulls ~2A and will drain the battery overnight.
17. **Ground — chassis, not battery.** Clean, paint-free bare metal stud near the gauge mount (FG2 has one behind the driver's dash near the kick panel). Sand paint, star washer, ring terminal. Routing ground to battery negative directly introduces alternator/starter noise.
18. **Signal wire — 0-5V analog output to FlashPro Analog Input 1.** AEM gauge harness "AO1" → FlashPro AI1 signal pin (exact pinout per [10-Hondata-FlashPro/hardware-software-deep-reference.md](../10-Hondata-FlashPro/hardware-software-deep-reference.md) Section 2). Use 18 AWG, keep short, route AWAY from ignition coils, spark plug wires, and alternator harness.
19. **Signal ground — star ground, NOT daisy chain.** This is where most DIY installs fail. The AEM harness has a dedicated analog/signal ground wire separate from chassis ground. Route it back to the SAME reference point as the FlashPro's analog input ground. All analog grounds meet at ONE point. Daisy-chaining introduces ground-loop drift and noise in the datalog.
20. **Shield wire (if present).** If the AEM harness has a foil shield: ground it at the GAUGE END ONLY, leave the FlashPro end floating. Grounding both ends creates a ground loop.
21. **Twisted pair the signal + signal-ground wires.** ~1 turn per inch for the entire run. Cancels inductively-coupled EMI from ignition coils.
22. **All crimps and critical joints get heat-shrink** — adhesive-lined tubing. For the signal wire joints, I'm soldering AND heat-shrinking, not just crimping. A corroded crimp in the signal path introduces resistance that skews voltage.
23. **Fuse the power wire** with an inline 5A fuse after the add-a-fuse tap — belt-and-suspenders.
24. **Multimeter check before powering on:** continuity YES from gauge power to fuse tap load side, gauge ground to chassis stud, signal output to FlashPro AI1. Continuity NO from gauge power to ground (no short) and signal to ground (no short).

### Phase E: FlashPro Configuration

25. **Plug laptop into FlashPro, connect FlashPro to OBD2 port, key to ON (engine off is fine for config).**
26. **Open FlashProManager.** Load my current calibration (or read from ECU first if I haven't — see [10-Hondata-FlashPro/hardware-software-deep-reference.md](../10-Hondata-FlashPro/hardware-software-deep-reference.md) Section 2 for the Read from ECU workflow).
27. **Navigate to Parameters → Analog Inputs → Analog Input 1** (menu path may vary by FPM version).
28. **Enable AI1.** Check the box or flip the toggle.
29. **Set the scale.** The AEM X-Series 30-0300 default gasoline calibration is:
    - **0V = 10.0 AFR**
    - **5V = 20.0 AFR**
    - Linear in between
    - Verify this against the AEM 30-0300 manual — some revisions use a slightly different curve, and I want the FPM setting to EXACTLY match what the gauge is outputting.
30. **Label the input "Wideband AFR"** so it shows up clearly in the datalog column header.
31. **Save the calibration** with a descriptive filename (e.g. `ADDED_WIDEBAND_AI1_20260420.fpc`).
32. **Flash the updated calibration to the ECU.** ~20-45 seconds.
33. **Verify in Parameter Monitor.** Open FPM's live parameter view with the key on (engine can be off — gauge still outputs a voltage). The Analog Input 1 parameter should show a plausible AFR value. With engine off and sensor in free air, it should read near 20.9 (atmospheric oxygen equivalent).

### Phase F: Calibration Verification

34. **Free-air calibration check.** LSU 4.9 ships pre-calibrated but I verify. Remove sensor from bung (plug back in), expose to ambient air 60 sec. Gauge should read ~**20.9 AFR** (atmospheric oxygen). FPM Parameter Monitor AI1 should match. If off by >0.5 AFR, run AEM's free-air calibration per the 30-0300 manual.
35. **Reinstall sensor.** Re-torque 33 ft-lb. Set the bung plug aside — I'll need it if I ever pull the sensor.
36. **Start the engine.** Let idle until sensor heats up (AEM heater countdown, ~30-60 sec).
37. **Verify closed-loop cruise AFR.** Steady-state 2000-3000 RPM, flat road. Gauge tracks ~**14.7 AFR** stoichiometric. Datalog AI1 matches within 0.2 AFR.
38. **Verify WOT AFR.** Brief WOT 3000→redline in 3rd on a safe open road. Gauge drops into **12.0-13.0 AFR** (enrichment). Datalog AI1 matches gauge within 0.2 AFR.
39. **Gauge vs datalog AI1 mismatch** means scaling error in FPM or voltage drop from a bad ground. Chase it before calling wiring done.

### Phase G: Sanity Check Before Tune

Before I hand the car over for a dyno session, I want to see a clean datalog that confirms everything is working.

40. **Record a 10-minute mixed-drive datalog.** Idle, cruise, part-throttle, one or two brief WOT pulls.
41. **Export to CSV** (see [10-Hondata-FlashPro/hardware-software-deep-reference.md](../10-Hondata-FlashPro/hardware-software-deep-reference.md) Section 2).
42. **Compare "Commanded AFR" vs "Analog Input 1 (Wideband AFR)" in the log:**
    - Closed-loop cruise (light throttle, warm): commanded 14.6-14.8, wideband tracks within 0.3 AFR. 100-200ms lag is normal (sensor is downstream of injection).
    - Warmup (cold): commanded richer (13-14), wideband tracks.
    - WOT: commanded drops to low 12s on stock/base tune, wideband follows.
43. **Red flags that mean STOP and DEBUG before tuning:**
    - Wideband leaner than commanded at cruise → exhaust leak upstream, or bad bung location
    - Wideband richer than commanded at cruise → sensor aging/contaminated or free-air cal drifted
    - Noisy/spiky readings (>0.5 AFR swings at cruise) → EMI, bad ground, or non-twisted-pair run
    - Reads pegged at 10.0 or 20.0 → wiring issue or dead sensor

---

## First Drive Checklist

Before I consider this mod "done":

- [ ] Gauge reads sensible AFR at idle (14-15 warm, possibly 12-13 cold)
- [ ] Gauge reads ~14.7 at steady cruise
- [ ] Gauge reads 12-13 at WOT
- [ ] FPM datalog AI1 matches gauge within 0.2 AFR at multiple operating points
- [ ] No EMI noise spikes visible in datalog during ignition events
- [ ] No CELs thrown by the car (the wideband is a passive add — shouldn't trigger any stock sensor DTCs, but I'm confirming)
- [ ] Sensor harness is not rubbing or melting on any exhaust surface
- [ ] Gauge does not obstruct driver sightline
- [ ] Add-a-fuse tap is seated firmly, fuse box cover closes

---

## Common Mistakes

1. **Bung downstream of HFC but upstream of an exhaust leak.** A pinhole leak between header and sensor admits fresh air = false "lean" reading. Tuner adds fuel to compensate; fixing the leak later leaves the engine dangerously rich. Seal every flange and smoke-test before trusting the wideband.
2. **Signal ground tied to battery negative.** Alternator noise on the 0-5V signal. Star-ground to chassis with FlashPro analog ground as the star point.
3. **Running the header during break-in without the bung plug installed.** Bare sensor exposed to curing coating/residual oils shortens sensor life. Plug in for 50-100 miles of heat cycles.
4. **Mounting the gauge in the driver sightline.** Fails the "glance in under 0.5s" test. Temporary mount first, always.
5. **Mounting the bung on the bottom of the pipe.** Condensate pools and cracks sensor ceramic. Top/upper side only, angled up 10+ degrees.
6. **Using aluminum anti-seize.** Breaks down at exhaust temps and can contaminate the sensor. Copper only.
7. **Skipping the free-air check.** 60 seconds of verification before install saves a wasted tuning session.
8. **Twisted-pairing power and ground instead of signal and signal-ground.** Common reversal — the twisted pair protection belongs on the low-voltage signal, not the robust power wire.

---

## Integration with Dyno Session

The tuner will want this gauge INSTALLED, VERIFIED against a datalog, and REPORTING TO FLASHPRO AI1 before the car goes on the dyno. Showing up with a wideband that "I just put in this morning" wastes the first 30 minutes of paid dyno time on my verification work.

When booking the dyno session:
- Confirm the tuner accepts AEM X-Series 30-0300 as the logging wideband (almost all do)
- Confirm they read via FlashPro datalog AI1 (if they insist on their own dyno-room wideband, I still want mine logging so I have the data in my FPM format for later)
- Offer to send a sample datalog ahead of time — demonstrates clean wiring

---

## See Also / Cross-references

- [overview.md](overview.md) — parts list, rationale, buying links
- [../13-Headers/install-guide.md](../13-Headers/install-guide.md) Phase H — the bung welding step happens HERE, during the header install. Single most important cross-reference on this page.
- [../10-Hondata-FlashPro/hardware-software-deep-reference.md](../10-Hondata-FlashPro/hardware-software-deep-reference.md) Section 2 — FlashPro analog input pinout, AI1/AI2 allocation, FPM config workflow
- [../10-Hondata-FlashPro/tuning-workflow-and-maps.md](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) — how the wideband feeds the daily/sport tune workflow, and why no tune happens without it
- [../19-Flex-Fuel-and-Fuel-System/](../19-Flex-Fuel-and-Fuel-System/) — takes Analog Input 2, completing the FlashPro analog budget
- [../docs/torque-specs.md](../docs/torque-specs.md) — 33 ft-lb for the wideband sensor, 25 ft-lb for any exhaust flanges disturbed during install
- [../docs/baseline-logs.md](../docs/baseline-logs.md) — the datalog protocol that depends on this sensor being live

---

*Last updated: 2026-04-20*
