# Header Install Guide — Skunk2 Alpha + Berk HFC

## Status: Planning — install deferred until exhaust cutout working and tuned

## Reality Check Before I Start

This is the single scariest job on my entire build. It's not the technical difficulty — the actual swap is intermediate-level wrenching. It's the **170k miles of seized exhaust manifold studs**. If I snap one and can't extract it, I go from "weekend job" to "head off the engine and machine shop visit." I'm doing 3-5 days of prep work specifically to avoid that outcome.

**I'm strongly considering paying a shop the $300-500 for this one.** The ROI on shop labor is: if they snap a stud, THEY own drilling and extracting it. If I snap a stud DIY, I own it. A Honda specialist shop has seen this a thousand times and has the tools.

**Decision point before I start:** I get my final quote from a Honda specialist shop (one that's done Skunk2 Alpha installs on 06-11 SIs). If under $500 and they have good reviews for header work specifically, I hire it out. If not, DIY and I accept the risk.

---

## Prerequisites — Don't Skip

### Cross-references — things that need to be done FIRST or AT THE SAME TIME

| Do First | Why |
|----------|-----|
| [Phase 0 maintenance](../docs/mod-order-and-maintenance.md) complete | Clean engine baseline means if something goes wrong after install, it's header-related not some other lurking issue |
| [Valved exhaust (QTP cutout)](../08-Valved-Exhaust/) installed and working | Cutout position changes based on header/HFC flow; installing headers first locks me into a downstream geometry I may regret |
| [Wideband AFR bung](../17-Wideband-AFR/) welded into header collector | **Do this at the muffler shop DURING the header installation.** Retrofitting a bung into an installed header is a pain. |
| [Cooling system refresh](../16-Cooling-System/) | Headers add heat. I want fresh cooling headroom before this goes in. |
| PB Blaster on manifold studs — 3-5 days ahead | Seized-stud prevention, starting well before install day |

### Do AT THE SAME TIME (car is already apart)

| Also Do | Why |
|---------|-----|
| Replace upstream O2 sensor | New sensor is ~$100 OEM Denso. Old sensor threads will unscrew with the manifold. Anti-seize new threads. |
| Replace cat-to-B-pipe donut gasket | It's going to get disturbed anyway. |
| Apply ceramic coating or thermal wrap to header | Skunk2 Alpha runs HOT in the FG2 bay; protects alternator harness over time (community-reported issue). Jet-Hot or Swain coatings are ~$200-350. DEI titanium wrap is ~$50 as an alternative. |

---

## Timeline

### Day −5 through Day −1: PB Blaster Prep

| Day | Action |
|-----|--------|
| −5 | Apply PB Blaster or Seafoam Deep Creep to all 8 manifold studs from engine-bay side. Let soak overnight. |
| −4 | Start engine, warm to full temp. Shut off. Apply more penetrant while hot (thermal cycling breaks corrosion bonds). Let cool overnight. |
| −3 | Daily cycle: penetrant → heat → penetrant → cool |
| −2 | Same |
| −1 | One more application. Remove heat shield bolts (they seize too) — spray those too. |
| Day 0 | One final spray 30 min before starting. |

**Have extra PB Blaster on hand.** Not expensive, not worth being caught short.

---

## Day 0: Install

### Total Time Budget

- **DIY (first-timer on high-mileage car):** 8-10 hours — plan a full Saturday, nothing else that day
- **DIY (experienced, no seized studs):** 4-6 hours
- **Shop (Honda specialist):** 3-5 hours

### Tools Required

**Critical:**
- Torque wrench (1/2" drive, 30-150 ft-lb range)
- 14mm, 17mm, 19mm sockets + matching wrenches
- **O2 sensor socket** (22mm, with wire slot) — $10 at AutoZone, worth owning
- **Breaker bar** (18"+) — for the manifold-to-head nuts
- Stud extractor set — Irwin Hanson Bolt-Grip set — for if (when) a stud breaks
- **Double-nut setup** (2x M10x1.25 nuts) — standard stud removal technique
- Penetrating oil (PB Blaster + Seafoam Deep Creep, both)
- Jack + 4-ton jack stands — subframe may need to drop
- Mechanic's creeper + a good droplight or headlamp

**Also useful:**
- Inspection mirror + flashlight
- Parts magnet
- Drip pan (coolant may come out if thermostat housing is disturbed)
- Sharpie for marking bolt positions before removal

### Parts List (Everything I Should Have Before Starting)

| # | Item | Source | Status |
|---|------|--------|--------|
| 1 | Skunk2 Alpha header 412-05-1930 | Hybrid Racing / HARDmotion / JHPUSA | — |
| 2 | Berk Technology HFC BT1101-HFC-MET | Berk direct / Ballade Sports | — |
| 3 | **Exhaust manifold gasket, OEM 18115-RRB-A01** | Honda dealer only — aftermarket blows | — |
| 4 | **ARP exhaust manifold stud kit 208-4301** | Summit Racing | — |
| 5 | Copper-plated flange nuts M10x1.25 (8x) | ARP 200-8321 or equivalent | — |
| 6 | Donut gasket, cat-to-B-pipe | O'Reilly, AutoZone | — |
| 7 | Fresh upstream O2 sensor (Denso 234-9049) | RockAuto | — |
| 8 | O2 sensor anti-seize (Permatex, NOT copper) | AutoZone | — |
| 9 | Copper anti-seize (exhaust threads) | AutoZone | — |
| 10 | Skunk2 O2 extender wire | K Series Parts | — |
| 11 | Heat protection for header (wrap OR ceramic coating) | DEI / Jet-Hot | — |

---

## Step-by-Step

### Phase A: Lift and Access (30-45 min)

1. Let engine fully cool (overnight if possible).
2. Disconnect battery (-) terminal. Exhaust work near alternator wiring = bad surprises without disconnection.
3. Lift front of car, set on 4-ton jack stands on subframe pinch welds. NEVER work under a jack alone.
4. Remove driver-side front wheel and wheel well liner for access.
5. Remove engine-bay strut brace (if mine ends up fitting post-coilovers, not relevant until then — see [06-Strut-Bar/](../06-Strut-Bar/)).
6. Remove the heat shield over the stock manifold (4-6 bolts, they're seized, more PB Blaster).

### Phase B: Disconnect Upstream O2 (10 min)

7. Unclip the upstream O2 sensor connector from the harness (up by the ECU side of the bay).
8. Using the O2 socket, break the sensor loose — if it spins, great. If not, more penetrant and come back in an hour.
9. Unscrew fully, set aside. I'll install the NEW O2 in the new header.

### Phase C: Disconnect Cat from Stock Manifold (15-20 min)

10. Under the car, find the 2 spring-loaded bolts connecting stock manifold to the cat inlet flange.
11. Penetrant, then compress and unbolt. The springs go flying if I'm not careful — hold a rag over them.
12. Set the cat hanging on its own brackets/rear bolts (don't disconnect the cat-to-B-pipe flange yet unless needed for clearance).

### Phase D: Remove Stock Manifold — The Scary Part (30-90 min, depending on studs)

13. **Inspect each of the 8 manifold-to-head nuts.** Penetrant one more time. Let sit 10 minutes.
14. Start with the EASIEST-looking nut (typically a middle one, more protected from heat cycling).
15. Work SLOWLY. Back and forth — loosen 1/8 turn, tighten 1/16, loosen 1/4, tighten 1/8. This walks the corrosion out without shearing the stud. PATIENCE.
16. If any nut feels like it's stripping or the stud is turning out with the nut — STOP. Apply more penetrant. Try heating the nut with a small butane torch (careful of nearby plastic/wiring).
17. Repeat for all 8. If a stud breaks: STOP. Move to extraction procedure (below).
18. Once all 8 nuts are off, wiggle manifold free. It may need to be flipped to come out past the cat converter area.

### Phase E: Install New Studs + Prep Head Surface (20-30 min)

19. **If using ARP studs:** remove any remaining stock stud stubs with the double-nut technique. Then install ARP studs per ARP's thread-prep instructions.
20. Scrape old gasket material off the head mating surface. A plastic razor is safer than metal. Do not gouge the aluminum head.
21. Clean surface with brake cleaner + lint-free cloth.
22. Check head mating surface for flatness with a straight edge — if warped, this is a much bigger job. Expected outcome: flat.

### Phase F: Install Skunk2 Alpha (30-45 min)

23. Place new OEM 18115-RRB-A01 gasket over the studs, making sure orientation is correct (the intake/exhaust port shapes are asymmetric).
24. Lift Skunk2 Alpha into position — heavy and awkward. A second pair of hands helps; otherwise, a floor jack with a 2x4 block supports from below.
25. Thread all 8 copper-plated nuts hand-tight first. All 8 before torquing.
26. Torque in 3 passes, star pattern:
   - Pass 1: 10 ft-lb
   - Pass 2: 18 ft-lb
   - Pass 3: **23 ft-lb (final spec)**
27. Install Skunk2 O2 extender wire, then the fresh Denso O2 sensor with anti-seize on threads only (NOT on the sensor element).
28. Torque O2 sensor to 33 ft-lb.

### Phase G: Connect Header to Berk HFC (20-30 min)

29. Slide HFC onto header collector. Verify O-ring/gasket between them is correctly positioned (Berk ships with spec gasket).
30. Install flange bolts. Torque to 25 ft-lb.
31. Connect HFC outlet to existing exhaust (or to [QTP cutout / dump setup](../08-Valved-Exhaust/) if exhaust is already done).
32. Fresh donut gasket at every flange junction. NEW crush washers on any banjo fittings.

### Phase H: Wideband Bung Install (IF doing this during session)

33. While the system is on the car but before sealing up, mark the wideband bung location in the collector (post-HFC is the usual spot — ask tuner's preference).
34. Remove collector-to-HFC section, take to muffler shop for bung welding. 30 minutes at a local shop, $20-40.
35. Reinstall with fresh gasket.

### Phase I: Reassembly (30-45 min)

36. Reinstall heat shield (or install thermal wrap / ceramic coating if planned).
37. Reinstall wheel well liner, wheel.
38. Reconnect battery (-).
39. Torque lug nuts to 80 ft-lb.

---

## First Start + Break-In

40. Key to ON (not start) for 5-10 seconds. Check for fuel or coolant leaks visible in engine bay.
41. Start engine. Let idle 2 minutes. **Walk around car sniffing for exhaust leaks.** A slight smell of burning off coating is NORMAL for 10-20 minutes on a new header.
42. Listen for any ticking / hissing from manifold area = leak = torque down again or re-gasket.
43. Check all flange junctions for leaks again.
44. **First 50 miles: drive gently. NO WOT pulls.** Let everything heat cycle and seat.
45. After 50 miles: re-torque all exhaust bolts/nuts — they'll have relaxed slightly with heat cycles.
46. After 100 miles: one more re-torque pass. Should be stable by then.

---

## Post-Install Tuning (Cross-reference [07-Hondata-FlashPro/tuning-workflow-and-maps.md](../07-Hondata-FlashPro/tuning-workflow-and-maps.md))

**DO NOT WOT the car on the stock calibration or old tune after a header install.** The airflow characteristics have changed significantly; running aggressive timing on stale maps is how engines get hurt.

**Safe procedure:**

1. Drive gently home from install.
2. Flash a conservative base map (community Skunk2 Alpha + intake map, or previous-session calibration with timing pulled 2 deg as safety buffer).
3. Datalog 3 sessions of mixed driving (~1-2 days of commuting). Confirm zero knock, stable AFR, reasonable fuel trims.
4. Book dyno session (Tune #1 — see [tuning-workflow-and-maps.md](../07-Hondata-FlashPro/tuning-workflow-and-maps.md)).
5. Tuner dials in daily + sport maps on dyno with wideband + knock monitoring.

---

## If a Stud Breaks — Recovery Path

### Case 1: Stud snapped flush with the head or above

- **Extractor kit:** Irwin Hanson Bolt-Grip (spiral-flute extractor). Drill slightly, tap the extractor in with a hammer, back out with a wrench. Success rate ~60-70% if corrosion isn't extreme.

### Case 2: Stud snapped BELOW the head surface

- Much harder. Need to drill the remaining stud, extract with easy-out. If easy-out breaks off inside (hardened steel), I'm at the machine shop.
- Machine shop cost: $200-400 to drill and re-tap if clean, $500-1000+ if they have to pull the head.

### Case 3: Threads are damaged in the head

- **Heli-Coil** or **Time-Sert** repair kit. Re-threading the hole with a larger insert. Restores to full strength if done right.
- DIY-able with a careful hand and $60 kit, but professional shop is safer.

**This is the scenario the $300-500 shop quote is insuring against.** If I DIY and hit Case 2 or 3, I'm paying the shop anyway AND I've lost my weekend.

---

## See Also

- [overview.md](overview.md) — the parts I picked and why
- [brainstorm.md](brainstorm.md) — complete research, all header options compared
- [4-1-header-research.md](4-1-header-research.md) — why I didn't go 4-1
- [../08-Valved-Exhaust/](../08-Valved-Exhaust/) — must be installed first
- [../17-Wideband-AFR/](../17-Wideband-AFR/) — bung goes in during this install
- [../16-Cooling-System/](../16-Cooling-System/) — fresh cooling before more heat
- [../07-Hondata-FlashPro/tuning-workflow-and-maps.md](../07-Hondata-FlashPro/tuning-workflow-and-maps.md) — the tune this enables
- [../docs/torque-specs.md](../docs/torque-specs.md) — all torque values used here

---

*Last updated: 2026-04-18*
