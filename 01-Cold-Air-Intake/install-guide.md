# Cold Air Intake Install Guide — K&N Typhoon 69-1014TS

## Status: ALREADY INSTALLED — this is my reference doc for re-install, reverse-engineering, and future reference if I pull the intake for any reason (base-map flashing, MAF cleaning, sensor swap, shop inspection)

---

## Reality Check

This is the easiest mod on the whole build. The actual wrenching is maybe 45 minutes of real work for someone who's never opened the hood. I'm writing this guide anyway because:

1. I'll probably pull the intake at some point to clean or re-oil the K&N filter, or to swap back to the stock airbox for a dealer visit or emissions concern. Re-install is less obvious the second time around when the novelty's worn off.
2. If I ever re-flash the ECU for a fresh Hondata base map, I want to know exactly what I installed so the tune matches reality.
3. K&N's own instructions are fine but thin. Honda-specific tips (the hidden plenum clip, the MAF sensor orientation, the fresh-air duct trick) come from 8thcivic.com threads, not the kit.

**Difficulty:** Beginner (2/10 on wrenching scale)
**Time Budget:** 45-90 minutes. Budget 90 if it's the first time.
**Shop-worthy?** No. Not even close. Pay a shop $100+ for this and you're paying them to not let you learn your own engine bay. The only fasteners I touch are hose clamps, 10mm bolts, and one sensor plug. If any of those scare me, I shouldn't be building the car at all.

**Reliability-first framing on this mod:** The ONLY thing that can hurt the engine here is (a) over-oiling the K&N filter and contaminating the MAF sensor, or (b) missing a vacuum/PCV hose connection that causes a lean code. Both are preventable with patience. Power gain is 3-8 HP and is the secondary reason I did this — primary was the sound.

---

## Prerequisites and Cross-References

### Things That Must Be Done First

| Do First | Why |
|----------|-----|
| Baseline datalog on stock airbox | Without a before/after, I can't tell if the new intake + tune actually improved anything. See [docs/baseline-logs.md](../docs/baseline-logs.md). |
| Confirm stock MAF sensor is clean and functional | A dirty or drifting MAF on the stock airbox is a pre-existing problem that'll haunt me on the new intake. Spray it with CRC MAF cleaner (NOTHING ELSE) before I swap. |
| Have the Hondata base map (stock + intake) downloaded | I don't need to flash it on install day, but I want it on hand. Car runs on stock calibration after intake — closed-loop O2 correction handles the fueling shift — but it's not optimized until I flash. |

### Things to Do at the Same Time (if the car is already apart)

| Also Do | Why |
|---------|-----|
| Inspect PCV valve and hose | It's right there. 170k miles, cheap to replace (Honda PCV is ~$15). Cracked PCV hose causes lean codes that'll get blamed on the new intake. |
| Inspect and clean the throttle body | Throttle plate is exposed while intake tube is off. Quick wipe with throttle body cleaner + rag. Do NOT spray aggressively — DBW actuator is behind the plate. |
| Inspect the fresh-air duct (behind the driver-side headlight, routes to airbox area) | This is the duct I'll reuse to feed cooler air toward the K&N filter. If it's cracked from 170k miles of heat cycling, I want to know now. |

### Mods That Change or Obsolete This Install Later

- **[14-Intake-Manifold/](../14-Intake-Manifold/)** — When I install the Skunk2 Ultra Street IM with a bored throttle body, the intake tube's throttle-body-side coupling may need a different adapter. K&N's coupler is sized for the stock 62mm TB; bored 66mm TB needs a different reducer or the next size up silicone coupler. Plan ahead: don't discard the K&N packaging.
- **[13-Headers/](../13-Headers/)** — Headers radiate significantly more heat under the hood. Once headers go in, the hot-side placement of this intake becomes a bigger concern. I may add a better heat shield (DEI reflective wrap around the filter) or eventually switch to a true cold-side relocation kit. For now, stock fresh-air duct + partial heat shield is the compromise.
- **[10-Hondata-FlashPro/tuning-workflow-and-maps.md](../10-Hondata-FlashPro/tuning-workflow-and-maps.md)** — This is the one installed mod that affects the ECU tune. Base map flashes after this is on the car and baseline-logged.

---

## Tools Required

**Critical:**
- 10mm socket + short extension, 1/4" drive ratchet (all airbox bolts are 10mm)
- Flathead screwdriver (hose-clamp duty — the K&N kit uses worm-gear clamps, stock airbox uses spring clamps)
- Spring-clamp pliers (for stock MAF-to-airbox spring clamps; a stubborn-grip channel-lock works in a pinch)
- Long-nose pliers (for the PCV and IAT sensor connectors; the clips are tiny)
- Torque wrench, 3/8" drive, 10-80 ft-lb range (only for the intake-to-throttle-body clamp area, honestly — most of this install is hand-tight territory)

**Useful:**
- CRC MAF Sensor Cleaner (red can, specifically marked for MAF use — **NOT** carb cleaner, **NOT** brake cleaner, **NOT** throttle body cleaner)
- Clean microfiber rag
- Shop light or headlamp
- Zip ties (K&N kit comes with a few; I wanted more for routing the intake temp sensor wire neatly)
- Sharpie — for marking clamp positions and hose orientations before removal
- Phone camera — take "before" photos of every connector, every hose, every clip orientation. This is free insurance and I use it on every install.

---

## Parts List

These are the real part numbers from [overview.md](overview.md). I'm not fabricating anything.

| # | Item | Source | Part Number |
|---|------|--------|-------------|
| 1 | K&N Typhoon Short Ram Intake kit | K&N direct / Summit / Amazon | **69-1014TS** |
| 2 | (Included in kit) K&N high-flow cotton gauze filter | K&N | Included |
| 3 | (Included in kit) Polished aluminum intake tube | K&N | Included |
| 4 | (Included in kit) Silicone couplers + worm-gear clamps | K&N | Included |
| 5 | (Included in kit) Partial heat shield | K&N | Included |
| 6 | (Included in kit) MAF sensor adapter / grommet (if needed) | K&N | Included |

**Total kit cost as purchased:** $504.17 (including tax/shipping — see [overview.md](overview.md)).

**Things I wanted on hand but are NOT in the K&N kit:**
- CRC MAF Sensor Cleaner — ~$8, AutoZone/O'Reilly
- Fresh PCV valve (if the old one looks tired) — Honda OEM, ~$15
- Extra worm-gear clamps (two spare, just in case) — ~$5 total

---

## Step-by-Step

### Phase A: Prep (10-15 min)

1. Park on level ground. Engine stone cold — ideally overnight cool. Hot engine = burned hands on the intake tube and heat shield.
2. Disconnect the battery negative terminal (10mm). Intake swap doesn't strictly require this, but I'm touching the MAF sensor connector and I don't want a momentary short to fault-code the ECU.
3. Pop the hood all the way up, prop with the stock prop rod.
4. Unbox the K&N kit on a clean surface. Inventory every piece against the K&N instruction sheet. Missing a coupler or clamp and finding out mid-install is the worst way to learn that lesson.
5. Pre-install the MAF grommet into the new intake tube if the kit uses one (check K&N instructions — the 69-1014TS uses a specific grommet orientation; the MAF element must face the airflow correctly).

### Phase B: Remove Stock Airbox (15-20 min)

6. Locate the MAF sensor on the stock intake tube, between the airbox and the throttle body. There's a 5-pin electrical connector on top.
7. Unclip the MAF connector (squeeze the tab, pull straight off). Tuck the connector out of the way so it doesn't flop around and catch on something.
8. Locate the IAT (intake air temperature) sensor — on the 8th gen SI, this is integrated into the MAF sensor on most trims, but double-check. If there's a separate connector, unplug it the same way.
9. Loosen the hose clamp at the throttle-body side of the stock intake tube (10mm or flathead, depending on clamp style). Slide the clamp back but don't fully remove — it'll be easier to reuse as reference later.
10. Disconnect the PCV hose from the stock intake tube (squeeze, pull). Honda's PCV hose has a little clip; be gentle or it cracks.
11. Disconnect any other small vacuum lines on the stock tube — typically there's one breather line. Sharpie a mark on each hose and its port so I can verify orientation on reassembly.
12. Remove the three 10mm bolts holding the stock airbox to the inner fender / engine bay mount points.
13. Lift the stock airbox + intake tube assembly up and out. It'll come out as one piece. Watch for the fresh-air intake snorkel — it slots into a duct at the front of the airbox and typically stays behind in the car (which is what I want).
14. Set the stock airbox in a box and label it "STOCK AIRBOX — FG2 SI K20Z3 — 2026-04." I'm keeping this forever. Emissions/dealer/resale/"what if" insurance.

### Phase C: Install K&N Typhoon (20-30 min)

15. Verify the throttle body is clean. If it's gunky (170k miles, probably is), wipe the throttle plate perimeter gently with a rag lightly dampened with throttle body cleaner. DO NOT push the plate open with force — DBW actuator is sensitive.
16. Install the K&N rubber coupler onto the throttle body inlet. Slide it on fully until it seats against the throttle body flange. Install a worm-gear clamp on the throttle-body side but leave it loose for now.
17. Install the second coupler clamp on the intake-tube side of the coupler — also loose for now.
18. **Install the MAF sensor into the new K&N tube** in the correct orientation. K&N's instructions show an airflow arrow on the sensor — it MUST point toward the throttle body, not toward the filter. This is the single most common mistake on a Honda intake swap and it throws an immediate CEL plus wildly wrong fueling. Check, double-check, take a photo before I tighten.
19. Torque the MAF sensor mounting screws to hand-tight + a gentle snug. These are plastic-into-plastic threads on the K&N tube and over-torque strips them. 25 in-lb range — just firm.
20. Thread the new K&N intake tube into the coupler at the throttle body. Wiggle until fully seated.
21. Position the heat shield against the inner fender per K&N's diagram. It bolts to two of the same mount points the stock airbox used. Thread the bolts but do NOT torque yet — the shield position needs to clear the filter with a small gap (5-10mm) so vibration doesn't rub through the filter cage over time.
22. Install the K&N filter onto the filter-side end of the intake tube. Slide fully on. Install the worm-gear clamp, tighten snug (not crushing — I'm compressing rubber against aluminum, over-tight just bulges the rubber).
23. Verify the filter clears the heat shield, the inner fender, and any nearby hoses/wires by at least ~10mm. Reposition the shield if needed, then torque the shield bolts to snug (~9 ft-lb — these are into captive nuts in the chassis, not load-bearing).
24. Route the **stock fresh-air duct** from behind the driver-side headlight to point toward the filter area. The duct terminates in an open end — I'm not connecting it to anything, just aiming it at the filter so cooler outside air gets fed into the filter's vicinity. This is what makes the Typhoon a "short ram with fresh-air assist" instead of a pure engine-bay snorkel.
25. Reconnect the PCV hose to the K&N tube's PCV port. Double-check orientation against my sharpie mark from step 11.
26. Reconnect any secondary vacuum/breather lines to their respective ports. Every one of them, no exceptions. A missed line = lean code, rough idle, and me cursing at the dash.
27. Reconnect the MAF sensor electrical connector. It should click positively into place. Tug it lightly to verify latch.
28. Tighten both coupler worm-gear clamps at the throttle body. Snug but not crushing. The rubber should look evenly compressed, not ballooned out the sides.

### Phase D: Reassemble and Sanity Check (10-15 min)

29. Walk around the engine bay and visually confirm: no loose hoses, no dangling connectors, no tools left behind, no rags forgotten. Twice.
30. Reconnect the battery negative terminal. 10mm, snug but not bottomed out into the post.
31. Close the hood, but don't latch it fully yet — I'll want it back up for the first-start inspection.

---

## First Start and Verification

32. Key to ON (NOT START) for 5-10 seconds. Listen for the fuel pump priming. No warning lights beyond the normal bulb check? Good. If I get a CEL immediately, it's the MAF connector not seated, the MAF oriented backward, or a vacuum line I missed.
33. Start the engine. Idle should settle within 5-10 seconds to around 800-900 RPM. A slight 30-second elevated idle (~1100 RPM) is normal for the cold-start strategy.
34. Pop the hood back up while the car idles. Listen carefully near the throttle body coupler and the MAF area. A hissing / whistling sound = vacuum leak. A thin puff of white "smoke" near the filter on first start = normal factory-oil burnoff from the filter. Goes away within a minute.
35. Feel around every hose junction — no sucking air, no warm exhaust smell (shouldn't be any near the intake, but confirms nothing's obviously cross-connected wrong).
36. Let the engine come to full operating temperature (~190°F). Watch the IAT reading if I have an OBD-II reader plugged in — it should climb from ambient to somewhere around 20-30°F above ambient at idle. If it's pegging at 150°F+ at idle with a cold engine, the sensor is in a weird spot or reading wrong. (Normal: IAT will climb significantly once I shut the engine off and heat soaks; this is the hot-side placement penalty.)
37. Short drive around the block, 10-15 minutes of mixed driving. No WOT yet. Listen for the new intake note — distinctly different from stock, a deeper growl above 4500 RPM, borderline glorious above 6000.
38. Return home, pop the hood, re-check every clamp. Vibration may have loosened one. Snug as needed.
39. **After 50 miles:** re-torque / re-snug the throttle-body couplers. Rubber settles.
40. **After 100 miles:** final re-check. Should be stable from here on.

---

## Post-Install Notes

### MAF Recalibration and Fuel Trims

- **The car runs on the stock calibration after this swap.** The ECU uses the MAF signal in closed-loop operation, so it corrects fueling across most of the operating range. Expect **long-term fuel trims (LTFT)** to shift by 3-7% in the first 50-100 miles as the ECU re-learns. This is normal. If LTFT goes above +10% or below -10%, there's a real leak or a MAF issue to diagnose.
- **Short-term fuel trims (STFT)** will look bouncy for the first drive or two. They'll settle.
- **I will flash a Hondata base map ("stock + intake" community map for 8th gen SI) once I have FlashPro set up.** This is NOT urgent — the car runs fine on stock calibration — but it's the first tune I'll do. See [10-Hondata-FlashPro/tuning-workflow-and-maps.md](../10-Hondata-FlashPro/tuning-workflow-and-maps.md).
- **Do NOT clear fuel trim adaptation (disconnect battery + throttle relearn)** unless I'm specifically told to by a tune workflow. Let the ECU adapt naturally.

### Heat Soak Behavior to Expect

- **IAT will climb significantly at idle / in traffic / after shutdown.** This is the hot-side placement penalty — the K&N Typhoon's filter is in the engine bay, not behind the bumper. On a hot summer day in traffic, IAT can hit 140-160°F. The ECU pulls timing as IAT rises, so peak power suffers in heat-soak conditions. This is the tradeoff I accepted for the sound, the simpler install, and the lower cost vs. a true cold-side relocation.
- **Moving cruise recovers fast.** At highway speed, fresh air flowing past the filter drops IAT to 20-30°F above ambient within a couple minutes.
- **I'll monitor IAT via Hondata datalogs** once FlashPro is set up. If hot-day IAT is genuinely hurting performance, I'll revisit (DEI heat wrap around the filter, a proper cold-side relocation kit, or eventually a different intake design).

### K&N Filter Oil Maintenance

- **DO NOT clean and re-oil the K&N filter until at least 50,000 miles** unless it's visibly caked. The factory oil is correct from the box. Early cleaning is how people over-oil and contaminate their MAF.
- **When it IS time to clean:** use K&N's Recharger kit (cleaner + oil). Follow K&N's instructions exactly — spray oil application, not squirt. Light coat. Let it wick in for 20-30 minutes before reinstalling. Over-oiled filter + spinning engine = oil mist on the MAF element = drifting MAF readings = fueling weirdness.
- **Warning signs of MAF contamination:** hesitation off idle, LTFT drifting consistently negative (car thinks it's getting more air than it is), stumble on transition from closed to open throttle. Cure: pull MAF, spray CRC MAF cleaner (red can, MAF-specific), let dry fully, reinstall. Do not wipe the MAF element with anything. Do not use any other cleaner.

---

## Common Mistakes

1. **MAF oriented backward.** Airflow arrow must point toward the throttle body. Immediate CEL and wildly wrong fueling if reversed. Check twice.
2. **Over-oiling the K&N filter at first service.** Factory oil is correct. First cleaning should not be for 50k+ miles and should be K&N's light spray application only.
3. **Missing a vacuum/PCV line on reassembly.** Sharpie every hose before removal. A forgotten breather line causes a lean code and rough idle, and I'll spend an hour chasing it.
4. **Over-torquing the MAF sensor screws into the plastic K&N tube.** Strips the threads. Hand-snug only.
5. **Crushing the silicone couplers with over-tight worm-gear clamps.** Rubber should look evenly compressed, not ballooned. Snug, not crushing.
6. **Skipping the fresh-air duct.** The stock fresh-air duct routes from the front of the car to the airbox area. It's easy to leave it dangling after removing the airbox. Aim it at the K&N filter — this is half the reason the Typhoon works as well as it does despite hot-side placement.
7. **Flashing an aggressive intake tune on day one.** Even the community "stock + intake" base map should go on after a few days of baseline driving and datalogging. Reliability first.
8. **Assuming the stock MAF is fine.** At 170k miles, the stock MAF might be drifting. A quick CRC MAF spray on the stock sensor before it goes into the new tube is cheap insurance.
9. **Forgetting to reconnect the battery before trying to start.** Did this once. Felt stupid. It happens.

---

## See Also

- [overview.md](overview.md) — parts, part numbers, why I picked the Typhoon despite the hot-side placement
- [../docs/torque-specs.md](../docs/torque-specs.md) — general fastener specs (no intake-specific torques are critical, but referenced for anything adjacent like throttle body bolts at 17 ft-lb)
- [../docs/baseline-logs.md](../docs/baseline-logs.md) — the A/B datalog protocol I'm using to confirm this intake actually did what K&N says
- [../10-Hondata-FlashPro/tuning-workflow-and-maps.md](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) — the base map that makes this intake actually worth the gains
- [../13-Headers/install-guide.md](../13-Headers/install-guide.md) — future header install will significantly increase bay temps; may force a heat-management revisit on this intake
- [../14-Intake-Manifold/](../14-Intake-Manifold/) — future IM swap with bored TB may require a different K&N coupler
- [../06-Ignition-Refresh/](../06-Ignition-Refresh/) — fresh plugs and coils must happen before any tune, including the post-intake base map

---

*Last updated: 2026-04-20*
