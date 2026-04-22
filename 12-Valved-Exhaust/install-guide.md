# Valved Exhaust Install Guide — QTP QTEC30 Custom 3" Build

## Status: Planning

Not purchased yet. This guide is the plan I'll work from once parts are in hand and I've booked the muffler shop appointment. I'll update timings and gotchas after the actual install.

---

## Reality Check Before I Start

**Custom build.** No bolt-on valved exhaust exists for the 8th gen Civic SI (2006-2011). I researched everything in [brainstorm.md](brainstorm.md) — Varex, Fi, Armytrix, IPE, Corsa, Borla — nothing fits the FG2. The DIY QTP cutout path isn't a shortcut, it's the only path.

**Time budget:** Muffler shop fab 4-6 hours (drop off morning, pick up end of day) + DIY electrical 3-4 hours at home next day + 30-minute first drive. Budget a full weekend.

**Cost:** ~$485 parts (see [purchasing.md](purchasing.md)) + $150-250 shop labor.

**Why this matters:** This mod unlocks the Daily/Sport duality the entire tuning philosophy is built around (see [10-Hondata-FlashPro/tuning-workflow-and-maps.md](../10-Hondata-FlashPro/tuning-workflow-and-maps.md)). Every tune after this ships as two calibrations. Getting the cutout right is the foundation for Tune #1.

---

## Prerequisites — Do These First

### MUST BE DONE BEFORE HEADERS

**Hard ordering rule.** Install the cutout BEFORE the Skunk2 Alpha header (→ [13-Headers/](../13-Headers/)). The cutout position depends on downstream geometry — if headers go in first, the Skunk2 Alpha + Berk HFC can shift the cat flange enough to put the cutout in the wrong spot. Install on the stock manifold + cat now (stable known geometry); headers tie into the existing cutout flange later. The 13-Headers guide enforces this. Do not reverse.

### FlashPro First Flash Complete

FlashPro paired, community base map loaded, stock cal saved. I need a known-good calibration running before the cutout install so closed-loop O2 can correct the small AFR shift between valve states on a single map until Tune #1. See [10-Hondata-FlashPro/](../10-Hondata-FlashPro/).

### Interior Fuse Box Access

Switch needs a **switched 12V source** so the cutout can't accidentally open with the car sitting in the driveway. Per [CLAUDE.md](../CLAUDE.md): driver-side lower left dash, behind removable panel. Target fuse **#8 ACC(A) — 7.5A** (live in ACC and RUN only). Mini blade add-a-fuse; hot side gets a new 5A fuse for the trigger circuit, load side takes the original 7.5A. The motor does NOT run off this fuse — that's a dedicated 10 AWG run from the battery. ACC(A) only carries the sub-1A relay-coil trigger.

### Other Cross-References

| Prerequisite | Why |
|--------------|-----|
| [10-Hondata-FlashPro/](../10-Hondata-FlashPro/) first flash done | Base map available for leak-check drive |
| [11-Wideband-AFR/](../11-Wideband-AFR/) installed or at least ordered | AFR datalog pre- and post-install confirms nothing got worse |
| [09-Cooling-System/](../09-Cooling-System/) refresh ideally done | Don't stack unknowns on an aging cooling system |
| Stock cat health verified (no P042X codes) | Post-cat bypass assumes a healthy cat stays in the flow path |

### Do NOT Do This Before the Cutout

- **Headers.** Already covered above. Reordering breaks the geometry.
- **Intake manifold or bored TB.** Those are Tune #2 hardware — way downstream of this step.

---

## Parts List

Full details with buy links in [purchasing.md](purchasing.md). Quick summary of what needs to be on the shelf before muffler-shop day:

### Core exhaust hardware (the shop needs these in-hand)

| # | Part | Spec |
|---|------|------|
| 1 | **QTP QTEC30** — 3" electric cutout valve | Stainless butterfly, 12V DC gear motor, ~5-8A draw, polarity-dependent direction |
| 2 | 3" stainless mandrel-bent straight, ~12" | Dump pipe main section |
| 3 | 3" stainless mandrel 45-degree bend | Dump pipe exit angle toward rocker panel |
| 4 | 3" → 2.5" stainless reducer cone, ~6" long | Smooth transition into muffled path |
| 5 | 2.5" adapter pipe | Connects reducer cone to stock resonator inlet |
| 6 | 3" stainless rolled exhaust tip | Vibrant or Magnaflow universal, rolled for water runoff |
| 7 | 3" and 2.5" exhaust gaskets (3 total) | Standard graphite-faced |
| 8 | 3" and 2.5" band clamps (4) | For any non-welded joints the shop chooses |
| 9 | Rubber exhaust hangers + mount brackets (2) | For the dump pipe and the new reducer-cone section |

### Electrical (DIY side, I handle these at home)

| # | Part | Spec |
|---|------|------|
| 10 | **Normally-open 12V automotive relay, 30A-rated** | Bosch-style 5-pin or equivalent. Critical: NO, not NC — details in Phase D. |
| 11 | 30A in-line fuse holder + 15A fuse | On the power feed from battery to relay |
| 12 | **10 AWG silicone-insulated wire** | Power + ground runs to relay. ~10 ft total. |
| 13 | 14 AWG silicone-insulated wire, 20 ft | Motor leads to cutout + trigger wire through firewall |
| 14 | SPST illuminated rocker switch | Dash or center console mount. 12V-lit so I can see state from the driver's seat. |
| 15 | DEI fire sleeve, 3 ft | Any wire passing within 12" of exhaust |
| 16 | Deutsch DT 2-pin connector sets (2) | Weatherproof disconnect near cutout motor |
| 17 | Dielectric grease | On all underbody connections |
| 18 | 3/8" split wire loom, 10 ft | Routing protection along frame rail |
| 19 | Crimp terminals, assorted ring + spade | For relay + battery terminals |
| 20 | Heat-shrink tubing assortment | Over every crimp, no electrical tape under the car |
| 21 | Fuse tap for ACC(A) mini blade | Interior fuse box connection for trigger |
| 22 | Zip ties + wiring clips | Proper routing, no dangling wire |

**Why 10 AWG on the power run, not 14:** The QTEC30 pulls 5-8A peak while actuating against exhaust pressure. With ~8 ft round-trip wire length and 15A fuse protection, 10 AWG keeps voltage drop under 2% under load. 14 AWG works on paper but sags with heat and cycling. Undersized wire is non-negotiable failure territory.

---

## Tools Required

### At the muffler shop (they have these)

- TIG or MIG welder with stainless capability
- 3" and 2.5" pipe notcher / bead roller
- Pipe bender (3" mandrel)
- Pressure tester with smoke or soap solution
- Lift + fabrication table

### At home (DIY electrical)

- Multimeter (continuity + 12V DC)
- Crimper — ratcheting, for insulated terminals
- Heat gun (for shrink tubing)
- Wire strippers 10-22 AWG
- 10mm + 12mm sockets (for battery terminal, relay bracket)
- Drill + step bit (for switch mounting hole in dash blank — NO firewall drilling, see below)
- Deutsch DT connector crimper (proper tool, not generic crimps)
- Torque wrench, 10-40 ft-lb range (for band clamps + battery terminal)
- Fuse tap install tool (usually comes with the add-a-fuse kit)
- Trim removal tools (for dash panel + under-dash access)
- Inspection mirror + headlamp (underbody wire routing)
- Zip-tie tensioner

**Do not substitute.** Deutsch connectors crimped with generic terminals fail open at the worst time. A proper DT crimper is $40 and owns the job for life.

---

## Muffler Shop Planning

The shop does the welding I can't. I'm still the engineer — showing up with a drawing, the parts, and a written spec sheet.

### Finding the right shop

Looking for: stainless welding capability (mild-steel weld on stainless = galvanic corrosion in 2 years), custom fab reputation (track/show build photos, not just "swap on a Magnaflow"), willingness to work off my drawing (any "let us do it our way" pushback = wrong shop), and pressure testing included.

### Design brief I bring to the shop

One page, printed:

1. **Final layout drawing** — header → cat → 3" pipe → cutout → Y-branch → dump pipe + reducer to stock path. Same diagram from [overview.md](overview.md).
2. **Cutout position** — after the high-flow cat, before the resonator, **minimum 14" from header collector flange to cutout body** (QTP thermal spec to protect the motor).
3. **Dump pipe** — 3" straight, 45-degree bend exiting forward of the rear axle, rolled tip. **Not toward any tire.**
4. **Reducer cone** — 3"→2.5", ~6" long, smooth transition into OEM resonator inlet.
5. **Hangers** — add 2 rubber hangers: cutout body + dump pipe near exit.
6. **Ground clearance** — dump exit no lower than the lowest stock exhaust point (measured at resonator).
7. **Wideband bung — NOT YET.** Goes in the Skunk2 Alpha collector during header install ([13-Headers/](../13-Headers/)). Premature bung = wrong location.

### Quote + agreements

- $150-250 expected. Under $100 = they missed something, walk. Over $350 = second quote.
- Confirmed design in writing, same-day turnaround if possible, 30-day weld warranty, pressure test included, electrical is mine (they do not wire the motor).

---

## Step-by-Step

### Phase A: Pre-Install Planning (at home, day before shop)

1. **Measure the stock mid-pipe** from cat-back flange to resonator inlet. Record length, bend clock positions. Photograph from 4 angles — reference for the shop.
2. **Plan cutout orientation.** QTEC30 motor mounts **up and slightly outboard** — not dangling where debris can hit it, not facing the hottest pipe. Sketch it on the design brief.
3. **Plan the wire routing.** Battery → relay (engine bay) → through existing driver-side firewall grommet (NO new hole) → along center tunnel under carpet → switch. Separate path: relay → frame-rail grommet or subframe → cutout motor connector.
4. **Pre-make the motor harness at the bench.** Deutsch DT terminated, fire sleeve already applied. Install day becomes plug-and-route, not underbody crimping.
5. **Fuse tap check.** Confirm ACC(A) = fuse #8. Pull and meter: key OFF = dead, key ACC = hot. If the chart doesn't match, stop and verify.

### Phase B: Remove Stock Mid-Pipe (morning of shop day)

6. Let the car sit overnight — cold exhaust bolts back out, hot ones shear.
7. Lift front onto 4-ton jack stands on subframe pinch welds. Never work under a jack alone.
8. **Disconnect battery (-) terminal.**
9. Penetrant on cat-to-B-pipe and resonator flange bolts. Let sit 15 minutes.
10. **Cat-to-B-pipe flange:** 2 spring-loaded bolts, 25 ft-lb per [docs/torque-specs.md](../docs/torque-specs.md). Compress springs and unbolt — rag over the springs so they don't launch.
11. **Resonator flange** at the rear — confirm with the shop whether they want the full section including the resonator or just the mid-pipe.
12. Support on the hangers, slide back to clear the cat flange, remove.
13. Inspect flange faces for pitting. Order fresh donut gaskets if bad.
14. Hand mid-pipe + parts kit + design brief to the shop. Do not hover.

### Phase C: Muffler Shop Fabrication (shop work, 4-6 hours)

Documented so I know what to verify at pickup.

15. Cut a 3" stainless section from the cat flange to calculated cutout position. Minimum 14" cat-to-cutout for heat isolation.
16. Fabricate Y-junction (or tee) downstream of the cutout — one leg is the 3" dump pipe, the other is the reducer cone feeding the OEM path. Geometry: path of least resistance with valve open = dump pipe.
17. QTEC30 welded inline, motor oriented up-and-outboard per brief. V-band clamps at flanges recommended (serviceability — I can pull the cutout later without cutting pipe).
18. Dump pipe: 3" straight + 45-degree bend + rolled tip. Exit clears rocker panel, points down-and-rearward, away from tires.
19. Reducer cone 3"→2.5" welded to the muffled side, feeding stock resonator inlet with a fresh 2.5" gasket.
20. Two new rubber hangers: cutout body + dump pipe near exit.
21. **Pressure test.** Cap cat flange, pressurize, soap all welds. Bubbles = re-weld before it goes on the car.
22. Reinstall. Cat-to-B-pipe spring bolts **16 ft-lb**, resonator/muffler flange bolts **25 ft-lb**, cutout flange bolts **25 ft-lb**. Fresh donut gaskets.
23. **Pickup inspection** — flashlight under the car. Cutout motor up/outboard. Minimum 3" ground clearance at dump exit. No weld splatter on wires/lines/tank. All hangers engaged. V-bands torqued. Motor pigtail protected and reachable.
24. **Drive home sounds stock.** Valve is unpowered — and because I'm using a normally-open relay wiring, no power = valve stays CLOSED. Exact fail-safe behavior I want.

### Phase D: Electrical Wiring — The Fail-Safe Is Everything (3-4 hours, garage)

**The single rule in this phase:**

> **Relay must be NORMALLY-OPEN (NO). Default state — power off, switch off — must be VALVE CLOSED.**

If it's wired NC, any failure (blown fuse, dead battery, chafed wire, dead switch) opens the valve. Loud exhaust at 2 AM because of a corroded crimp is not a failure mode I'm accepting. Fail-safe direction is QUIET. With NO wiring driving the motor OPEN when energized, loss of power = valve returns to closed. The QTEC30's gear motor is non-back-drivable, so the wiring also gives a CLOSE-direction pulse at switch-off — but default with no power is still closed.

#### D1. Battery + main power run

25. Battery already disconnected (step 8).
26. **Mount the relay** on a metal bracket within ~12" of the battery. Dry, shielded from spray, not above the exhaust manifold side.
27. **10 AWG from battery (+) through a 15A in-line fuse within 6" of the battery terminal** to relay common. Ring terminal, crimped + heat-shrunk. Torque battery nut.
28. **10 AWG ground from relay ground pin** to a scraped-paint chassis point with star washer. Not a painted bolt, not a body seam.
29. Route power + ground along factory wire channels. Zip-tie every 6-8". Clear of exhaust and moving suspension.

#### D2. Motor leads — POLARITY MATTERS

30. QTEC30 motor is polarity-dependent. **Bench-test off the car** with a 12V source. Note which lead is positive when the valve OPENS. Label both leads.
31. Route 14 AWG motor leads (fire sleeve within 12" of exhaust) from relay output, through frame-rail grommet, along subframe, to the motor pigtail.
32. **Deutsch DT 2-pin connector** at the motor, dielectric grease in the cavity. Positive lead goes to the motor terminal that drives OPEN.
33. Wrap motor housing with self-fusing silicone tape for a secondary water barrier.

#### D3. Firewall pass-through — NO DRILLING

34. **Use the existing driver-side firewall grommet** where the OEM harness enters. Lift the lip, push an awl through, feed the single 14 AWG trigger wire (signal only — power stays in the engine bay), reseal with silicone.
35. **Drilling a new firewall hole is forbidden.** Any unsealed penetration starts rust. The factory grommet has capacity for one thin signal wire.

#### D4. Switch trigger circuit

36. Route trigger wire along the driver-side center tunnel under the carpet to the switch.
37. Switch gets switched 12V from the **ACC(A) add-a-fuse tap** (fuse #8 — 7.5A original stays in the load side; 5A new fuse on the tap side for the trigger circuit).
38. Switch output → relay coil (+) via the 14 AWG trigger wire through the firewall. Coil (-) to chassis ground.
39. Switch ON = coil energized = relay throws = motor drives OPEN.
40. Switch OFF or key removed = coil dead = motor drive disconnected = valve returns to / stays CLOSED.

#### D5. Protect every connection

41. Heat-shrink on every crimp, no exceptions.
42. Dielectric grease on every underbody connection.
43. Fire sleeve on every wire within 12" of exhaust.
44. Split loom on every other wire for debris protection.
45. Zip-tie every 6-8".

### Phase E: Switch Mounting

46. **Location:** center console blank panel or unused dash switch cutout (the FG2 has a blank switch panel near the steering column on some trims).
47. Drill with a step bit sized exactly for the SPST rocker body. Deburr.
48. **Weatherproof 12V rocker, illuminated.** LED pin wired so it lights only when the switch is ON — dashboard confirmation of commanded valve state.
49. **Label it.** Label-maker, "EXHAUST SPORT" or "VALVE OPEN." Legible. If someone else ever drives the car, they should know what that switch does.

### Phase F: Initial Test (key ON, engine OFF)

50. Reconnect battery, torque terminal to spec.
51. Key to ACC, switch OFF. Nothing should click. LED dark. Valve silently closed.
52. Switch ON. Relay clicks within 50ms. Motor runs 2-3 seconds then stops at the QTEC30 internal limit. LED lights.
53. Switch OFF. Relay clicks off. Motor runs briefly closing. LED dark.
54. **Key-OFF fail-safe check.** Leave switch in ON, cycle key OFF. ACC(A) feed drops, relay drops, valve closes. If valve stays open with the key pulled, the fail-safe is wired wrong — stop and fix before driving.
55. **Visual valve confirmation.** Someone flips the switch while I watch under the car with a flashlight. Open = butterfly parallel to flow (dump pipe open). Closed = perpendicular (dump sealed, all flow to OEM path).

### Phase G: First Drive Test

56. Base calibration already flashed and confirmed.
57. Switch OFF, start engine. Idle sounds stock (OEM resonator + muffler fully in the path). AFR idle 14.5-14.7 closed-loop. **Walk around listening for leaks** — especially new cutout flanges, reducer cone welds, cat-to-B-pipe joint. Ticking or hissing = leak.
58. Drive gently — parking lot, then side street, switch still OFF. No drone, no new resonance, no cabin smell.
59. At 25 mph on a quiet street, switch ON. Valve opens, note transforms immediately to deep straight-piped 3". Quick 2nd-gear WOT blip, 5-7 seconds, not extreme. AFR at WOT ~12.0-12.5 on base cal, maybe 0.2-0.3 leaner than closed-valve WOT from reduced backpressure — closed-loop trims handle it on a single map.
60. Switch OFF at speed. Valve closes in 2-3 seconds, note returns to stock-quiet.
61. Home, cool down, lift, flashlight underneath. Soot around the cutout = leak (small amount normal, shouldn't grow). Hangers seated. Wire routing still off exhaust.
62. **AFR datalog for both valve states** on FlashPro. Save. Baseline for Tune #1.

---

## Tuning Integration

**Single base map handles both valve positions via closed-loop O2 correction.** Closed = more backpressure = slightly richer baseline; open = less backpressure = 0.2-0.5 leaner at WOT. Closed-loop trims compensate at part-throttle; at WOT, open-loop fueling is identical in both states, so the small AFR delta is acceptable on a single map for the first few weeks. No dyno just for the cutout.

**Dual-map tuning comes at Tune #1** (see [10-Hondata-FlashPro/tuning-workflow-and-maps.md](../10-Hondata-FlashPro/tuning-workflow-and-maps.md)), after both the cutout AND the headers + Berk HFC are installed (the header AFR shift is much bigger than the cutout shift, and I'm not paying for dyno time twice). Tune #1 outputs two calibrations:

- **Daily:** valve closed, conservative timing, AFR 12.0-12.2, stock VTEC, stock rev limit.
- **Sport:** valve open, max-safe timing (0 knock verified + wideband confirmed), AFR 11.8-12.0, VTEC lowered to 4800-5200, rev limit +100-200.

Neither ships without hitting every reliability ceiling in the tuning workflow doc. "Reliability over power, always" applies to Sport too — it's "stop leaving free power on the table," not "remove safety margins."

---

## First Drive Checklist

- [ ] Engine starts normally, no new codes
- [ ] Closed mode: idle sounds stock, no resonance, no cabin exhaust smell
- [ ] Open mode: dramatic 3" straight-piped note, no weird rattle or drone
- [ ] Switch transitions smoothly in 2-3 seconds, both directions
- [ ] Key OFF with switch ON → valve physically closes (fail-safe verified)
- [ ] Switch LED tracks state correctly (lit = open, dark = closed)
- [ ] No exhaust leaks at any new flange or weld (soapy-water test the flanges)
- [ ] AFR datalog captured for closed state (quiet commute, 20 min)
- [ ] AFR datalog captured for open state (spirited back-road drive, 20 min)
- [ ] Daily driving comfort acceptable (closed mode = can have a phone call at 70 mph)
- [ ] Sport driving satisfaction (open mode = grinning at every throttle stab)
- [ ] No new check engine codes after 100 miles of mixed driving

---

## Common Mistakes to Avoid

| Mistake | Consequence | My safeguard |
|---------|-------------|--------------|
| Normally-closed (NC) relay instead of NO | Valve fails OPEN when power drops. Wakes the neighborhood when battery dies overnight. | **Specifying NO relay in the parts list, verifying coil state with a multimeter before wiring.** |
| Swapped motor polarity | Switch says OPEN, valve drives CLOSED (and hits its stop, burning out the motor). | **Bench-test motor direction before install. Label leads. Verify visually in Phase F.** |
| Undersized power wire (14 AWG on the main run) | Voltage drop under load, motor stalls partway open, gear motor burns out at 60% travel. | **10 AWG minimum, non-negotiable.** |
| Drilling a new firewall hole | Rust ingress within 2 years. Insurance-annoyance. Pride hit. | **Use OEM grommet. One signal wire fits.** |
| Cutout mounted too low | First speed bump tears the dump pipe off. | **Ground clearance spec in design brief. Shop measures before final weld.** |
| Skipping the shop pressure test | Invisible weld leak detected 500 miles later when the cat code trips. | **Refuse pickup until pressure test completed in front of me.** |
| Dump exit pointed at the rear tire | Blows debris + hot gas into tire sidewall. Tire damage + ugly soot. | **45-degree bend points forward-and-down, outside of tire arc.** |
| Not saving AFR datalogs from both valve states | First dyno session starts blind — tuner has to re-characterize what I already lived through. | **Two 20-min drives, save both logs, bring them to Tune #1.** |
| Running wire along exhaust without fire sleeve | Insulation melts in a season. Short-to-ground. Blown fuse minimum, fire maximum. | **DEI fire sleeve on anything within 12" of exhaust. Period.** |
| Butt splices under the car | Corrode open in one winter. Switch stops working. | **Deutsch DT connectors at every underbody disconnect. Heat-shrink over every crimp.** |

---

## Future Integration: LattePanda + Arduino

Phase 2 replaces the dashboard toggle with software-driven control via the LattePanda 3 Delta + Arduino co-processor:

- **Tune-linked valve state.** FlashProManager on the LattePanda reports the active cal name; a small Python script reads it and commands Arduino GPIO (Daily = LOW/closed, Sport = HIGH/open).
- **Arduino GPIO drives the same relay coil I'm using now.** Phase 1 wiring doesn't change — I'm just replacing the manual switch as the trigger source with an Arduino pin through an optoisolator.
- **Manual override retained.** Physical rocker is wired in PARALLEL with the Arduino output, not in series. LattePanda off, crashed, booting — the switch still works. Non-negotiable: I will not make a physical feature depend on a computer booting.
- **Still NO relay, still fail-safe quiet.** LattePanda dies + switch OFF = valve closed. Either source commands open = valve opens (harmless redundancy). Both closed = closed.

Phase 2 belongs to 20-Permanent-LattePanda-Install. Phase 1 ships fully functional on the manual switch alone.

---

## See Also

- [overview.md](overview.md) — Parts rationale, pipe diameter strategy, design decisions
- [brainstorm.md](brainstorm.md) — Research, alternatives I ruled out, heat/wiring considerations
- [purchasing.md](purchasing.md) — Full parts list with vendor links and prices
- [../13-Headers/install-guide.md](../13-Headers/install-guide.md) — **Install this AFTER the cutout. The install order is enforced.**
- [../10-Hondata-FlashPro/tuning-workflow-and-maps.md](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) — The dual-map framework this unlocks + reliability ceilings that bound Sport-map tuning
- [../11-Wideband-AFR/](../11-Wideband-AFR/) — AFR logging setup. Needed for AFR delta characterization between valve states.
- [../docs/torque-specs.md](../docs/torque-specs.md) — All exhaust flange and battery terminal torque values
- [../CLAUDE.md](../CLAUDE.md) — Owner/vehicle reference + fuse box map (ACC(A) fuse #8)

---

*Last updated: 2026-04-20*
