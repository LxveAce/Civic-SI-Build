# Intake Manifold Install Guide — Skunk2 Ultra Street + Bored 66mm TB

## Status: Planning — Phase 3

This is the "full bolt-on" finisher. By the time I'm here the car is already tuned on exhaust + headers; the IM + bored TB unlock the top end the RRC manifold was capping. The install itself is intermediate-level wrenching, but there are two catches that will sink a weekend: the **PRB-to-RBC head mismatch** (the Skunk2 Ultra Street is PRB-pattern and my K20Z3 is an RBC head — adapters are mandatory), and the **2-week lead time on the bored throttle body**.

---

## Reality Check

- **DIY time:** 3-5 hours first time, intermediate+ skill level. Not scary like the headers were — no seized studs — but many small lines (vacuum, coolant, fuel, harness) and getting them all back right is what separates a clean install from a 2am vacuum-leak hunt.
- **Coolant drain required:** Partial drain to free TB heater lines and the water-bypass adapter circuit. ~1/2 gallon captured. I'm doing it AFTER the full cooling refresh (09-Cooling-System), so I'm just partially draining fresh Honda Type 2 and putting it back.
- **Throttle body out 1-2 weeks ahead.** Drag Cartel or HeelToe Auto to bore 62mm → 66mm. Ship 2-3 weeks ahead and confirm tracking before I order the manifold.
- **Dyno retune is mandatory.** Tune #2 — "full bolt-on." I do NOT drive WOT on the headers-only calibration. Engine-damage territory.
- **Reliability-first rule:** adapters on the RBC head are non-negotiable. Skipping the water-bypass adapter or the DBW TB adapter is not a shortcut — it's a guarantee of a leak or misalignment.

---

## Prerequisites / Cross-references

### Must Happen Before

| Do First | Why |
|----------|-----|
| [`13-Headers/install-guide.md`](../13-Headers/install-guide.md) complete AND [Tune #1](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) logged | Phase 2 baseline. Changing too many variables between tunes breaks the A/B. |
| [`09-Cooling-System/install-guide.md`](../09-Cooling-System/install-guide.md) complete | Fresh coolant, bled. I'm partially draining a freshly-serviced system, not fighting failing hoses. |
| [`11-Wideband-AFR/`](../11-Wideband-AFR/) AEM X-Series logging | Mandatory before Tune #2. |
| TB shipped + bored + **returned before install weekend** | 1-2 week lead. No install scheduled until tracking shows TB back. |
| **Skunk2 water-bypass adapter in parts bin** | CRITICAL — PRB manifold's coolant ports don't line up with RBC head. Without this, the IM does not seal. |
| **Skunk2 DBW TB adapter 309-05-0120 in parts bin** | CRITICAL — my bored DBW TB is RBC pattern; Skunk2's TB flange is PRB. Without this, the TB flange misaligns. |
| Fresh OEM IM gasket | No reusing 170k-mile gasket. ~$12. |
| FlashPro ready for Tune #2 | Tune #1 `.fpc` archived, conservative base map loaded in case dyno gets delayed. |

### Can Happen At The Same Time

| Also Do | Why |
|---------|-----|
| Fuel rail + injector swap (if bundling [19-Flex-Fuel](../19-Flex-Fuel-and-Fuel-System/acuity-fuel-rail-and-flex-fuel-build.md)) | Rail is off, injectors are out — shared labor hours. Skip this window and I redo the same disassembly later. |
| Fresh PCV valve | Plastic, cheap, 170k old, easy with IM off |
| Clean throttle body internals | Carbon sludge behind the blade — brake cleaner + rag |
| Fresh MAP sensor O-ring | $3, only accessible with IM removed |

---

## Tools Required

**Critical:**
- 10mm, 12mm, 14mm sockets on 3/8" ratchet
- Long extensions (3", 6", wobble) — IM bolts sit deep
- Torque wrench, 3/8" drive, 10-80 ft-lb range
- Torque wrench, 1/4" drive, 20-200 in-lb range (rail, TB, PCV)
- Coolant drain pan, clean, labeled
- Hose clamp pliers
- **Fuel line quick-disconnect tool** (Lisle 39400 5/16" QC, ~$8)
- Vacuum line labels (masking tape + Sharpie) — and phone photos of every joint
- Brake cleaner — large can, for head mating surface
- Plastic razor — NEVER metal on aluminum head
- Fire extinguisher in arm's reach (fuel rail work)
- Headlamp + inspection mirror

**Nice to have:**
- Parts organizer tray — 20+ fasteners come off
- Nitrile gloves
- Intake port covers (blue tape) — keep debris out of open runners

---

## Parts List

| # | Item | Part Number | Notes |
|---|------|-------------|-------|
| 1 | Skunk2 Ultra Street Intake Manifold (black) | **307-05-0600** | ~$565-620; TF-Works, Hybrid Racing, JHPUSA |
| 2 | **Skunk2 water-bypass adapter** (PRB→RBC coolant) | Skunk2 direct / Hybrid Racing | **MANDATORY** |
| 3 | **Skunk2 DBW TB adapter 309-05-0120** | TF-Works, Hybrid Racing | **MANDATORY** |
| 4 | Bored K20Z3 DBW throttle body (62→**66mm**) | Drag Cartel or HeelToe Auto | ~$150, 1-2 wk lead |
| 5 | OEM Honda IM gasket | 17105-RBC-004 | Fresh, ~$12 |
| 6 | Adapter gaskets | Ship with Skunk2 adapters | In kit |
| 7 | Honda Type 2 coolant top-off | OL999-9011 | ~1/2 gallon |
| 8 | **(If bundling)** Acuity 1913-PPL + Bosch EV14 550cc (0280158117) + OBD2 pigtails | See [19-Flex-Fuel](../19-Flex-Fuel-and-Fuel-System/acuity-fuel-rail-and-flex-fuel-build.md) | Optional |

**Part number discipline:** 307-05-0600 is the black Ultra Street **Street** (long-runner). 307-05-8000 is the Ultra **Race** — DIFFERENT manifold, wrong for street. **309-05-0120** is the DBW adapter specifically — there's a cable-throttle variant too, wrong part.

---

## Step-by-Step

### Phase A: Send TB Out (2 weeks ahead)

Do this BEFORE ordering the manifold. If the bore takes 3 weeks instead of 1, I want to know before Saturday's locked.

1. Cold engine. Battery (-) off.
2. Loosen K&N intake tube clamp at TB, pull tube back.
3. Unplug DBW harness connector from TB.
4. Disconnect the 2 small coolant lines on TB heater ports. Small pan ready — ~100ml coolant drips. Plug hose ends with a golf tee to stop siphoning.
5. Remove 4 bolts securing TB to stock IM (10mm). Lift TB off.
6. Bag TB-to-IM gasket, bolts, brackets. Reinstall intake tube loosely on the stock IM so nothing falls in.
7. **Box carefully** — DBW internals are the expensive part. Ship to Drag Cartel (dragcartel.com) or HeelToe (heeltoeauto.com) with: "Bore to 66mm, retain DBW, K20Z3 stock body, return ASAP."
8. Car is undriveable during this window. Park it. Commute differently.
9. **Do NOT proceed until bored TB is back, test-fit, bore measured with calipers.**

### Phase B: Install-Day Prep

10. Cold engine, overnight. Spill mats down — Honda Type 2 stains concrete.
11. Battery (-) off.
12. **Partial coolant drain.** Open rad cap slowly. Open radiator petcock until ~1/2 gallon is in the pan — drops level below IM coolant ports. Close petcock. Save the drained coolant in a sealed container; it's fresh from 09-Cooling-System and goes back in.
13. Remove engine cover (4x 10mm caps + bolts).
14. Loosen K&N intake tube at TB, slide off. Cap both ends with a plastic bag + rubber band.
15. **Take photos.** Phone on macro: overhead of the whole manifold, sides of every vacuum line, MAP, IACV, coolant lines, fuel rail, injector harness, PCV. I will thank myself at reassembly.

### Phase C: Disconnect Stock IM

16. **Fuel pressure relief.** Pull PGM-FI Main Relay 2 (fuel pump relay) from under-hood aux box. Start, idle until stall (15-60 sec). Crank 2-3 sec after stall to bleed rail.
17. Reinstall relay.
18. **Fuel rail disconnect.** Rag wrapped around the Honda QC at the rail feed. Lisle 5/16" QC tool — slide over line, press until retainer releases, gently pull line off. Residual fuel drips. Do NOT pry with a screwdriver.
19. Cap the fuel line end with a clean rubber cap. Route clear.
20. Unclip 4 injector harness connectors.
21. **Label every vacuum line** with masking tape + Sharpie before disconnecting: brake booster, PCV, EVAP purge, MAP. Photo first, then label, then disconnect. Don't yank plastic nipples on a 170k IM.
22. MAP sensor: unplug, remove 1-2 screws, set aside. Reuses with Skunk2.
23. IACV: unplug, set aside. Ultra Street has an IACV provision for street idle quality.
24. **Coolant lines off the IM.** Stock IM circulates coolant through its bypass + TB heater path. Loosen hose clamps with the pliers, work each hose off. Cap each hose with a golf tee.
25. If NOT bundling 19-Flex-Fuel: remove 2x M8 fuel rail bolts (108 in-lb / 9 ft-lb), lift rail with injectors seated, set aside on a clean rag under another rag. No dirt into injector bores.
26. If bundling with 19-Flex-Fuel: leave stock rail in place, bench-swap in Phase H.
27. **IM bolts — REVERSE torque sequence.** Starting from outer bolts working inward (opposite of install order), break each bolt 1/4 turn. Then loosen fully. Outer-to-inner prevents warping the flange or the head surface.
28. Lift stock IM straight off. It's heavier than it looks.
29. **Immediately cover open runners** with blue painter's tape or rag stuffed in each port. Nothing falls in — not a bolt, not a washer.

### Phase D: Head Prep

30. Old gasket material: **plastic razor only**, no metal. K20Z3 head is aluminum — gouges become leak paths forever.
31. Brake cleaner + lint-free cloth. Let flash off.
32. Straight edge check on the mating surface. Expected: flat. Warped = head-off job, above my scope.
33. Keep runner ports covered until the new IM is seconds from going on.

### Phase E: Install Adapters (CRITICAL)

**This is the step that matters most. The Ultra Street is a PRB-pattern manifold — it was designed for the K20A2/K20A3 head (02-06 RSX, EP3 SI), not the RBC head on my 06-11 K20Z3. The two heads differ in coolant port geometry and TB bolt pattern. These adapters are mandatory and sold separately.**

34. **Water-bypass adapter first.** Unbox the Skunk2 water-bypass adapter: plate, gasket (or O-rings), hardware.
35. Dry-fit to the RBC head coolant port. Confirm orientation — adapter re-routes the RBC coolant circuit to an external bypass line since the PRB manifold has no matching internal coolant passage.
36. Supplied gasket between adapter and head. No RTV unless Skunk2's instructions specify — default dry.
37. Hand-thread all adapter bolts, torque to **Skunk2's published spec** (typically 8-10 ft-lb — verify on the sheet).
38. Route the bypass hose per Skunk2's diagram. Usually loops to thermostat housing or block bypass port. Fresh hose clamps.
39. **DBW TB adapter 309-05-0120.** Mounts between the Ultra Street's PRB TB flange and my bored DBW TB's RBC bolt pattern. Dry-fit to the Ultra Street TB flange with supplied gasket.
40. 4 supplied bolts hand-tight, then torque per Skunk2 spec (~15-17 ft-lb). Verify on the sheet.
41. The bored TB mounts to this adapter's outer face in Phase G. The adapter is installed on the IM at this stage for easier access.

### Phase F: Install Skunk2 Ultra Street IM

42. **Fresh OEM IM gasket** (17105-RBC-004) over the head studs/bolt holes. Orientation matters — runner shapes are asymmetric. Sit flush all the way around.
43. **Remove runner-port covers** from Phase C — last thing before IM goes on. Zero debris in head runners.
44. Lift Skunk2 Ultra Street into position. With both adapters already mounted, it's bulky but manageable single-handed.
45. Hand-thread ALL IM bolts before tightening any. If one doesn't start by hand, back out and check for cross-threading — don't muscle it.
46. **3-pass star-pattern torque, center-outward:**
    - Pass 1: 6 ft-lb (seating)
    - Pass 2: 10 ft-lb
    - Pass 3: **12-16 ft-lb final** (Skunk2 aftermarket IM spec; OEM stock is 17 ft-lb but Ultra Street's aluminum flange doesn't need that and over-torque cracks mounting ears). **Honor Skunk2's sheet over mine if they differ.**
47. Reconnect coolant lines per photos/labels. NEW Hybrid Racing T-bolt clamps or fresh spring clamps — no reusing stretched 170k clamps.
48. Reconnect vacuum lines per labels. PCV, brake booster, EVAP, MAP nipple, emissions. **Every line accounted for — an unplugged port is a guaranteed lean-miss idle nightmare.**
49. MAP sensor with fresh O-ring, hand tight + ~7 ft-lb. Harness connected.
50. IACV on Ultra Street's provision. Harness connected.

### Phase G: Install Bored 66mm TB

51. Unwrap the returned bored TB. Visual: smooth bore, no burrs, DBW blade operates freely.
52. Fresh TB-to-adapter gasket (supplied with 309-05-0120).
53. Bolt TB to the outer face of the adapter. 4 bolts hand-tight, then torque **8-10 ft-lb** (Skunk2 adapter flange spec).
54. Reconnect TB heater coolant lines. Fresh clamps.
55. DBW harness connector — retention tab clicks.
56. K&N intake tube back onto TB inlet. Clamp snug + 1/4 turn, no cranking.

### Phase H: Install Fuel Rail + Injectors

**Path 1 — Staying stock (IM swap only):**

57a. Fresh lower-injector O-rings on each of 4 stock injectors. Lube with engine oil (no silicone grease).
58a. Fresh upper O-rings if any look pinched.
59a. Line up 4 injectors with Ultra Street bores. Press rail straight down, even pressure. Verify each injector bottoms and no O-ring rolled.
60a. 2x M8 rail bolts. **Torque 108 in-lb / 9 ft-lb** (crushing aluminum, gentle).
61a. Honda QC back onto rail feed until retainer clicks. Tug-test — cannot pull by hand.
62a. Reconnect 4 injector harness connectors.

**Path 2 — Bundling with [19-Flex-Fuel](../19-Flex-Fuel-and-Fuel-System/acuity-fuel-rail-and-flex-fuel-build.md) (swap to Acuity 1913-PPL + EV14 550cc + OBD2 pigtails):**

57b. Follow Stage 3 (Pre-Assemble Acuity Rail + EV14) and Stage 4 (Install Rail onto IM) in the flex-fuel guide.
58b. Torque Acuity rail M8 screws to **10 ft-lb** (Acuity spec).
59b. Full pump/sensor/gauge hardware only if same session — otherwise stock Honda QC connection to the Acuity rail inlet, save pump/sensor for later.

### Phase I: Refill + Bleed Cooling

60. Walk the bay: every hose connected, every clamp torqued, every vacuum line seated, no tools left on the engine.
61. Close open coolant drains.
62. Pour the saved coolant from Phase B back into the radiator. Top off with fresh Honda Type 2 to MAX COLD at the neck.
63. **Full bleed procedure — follow [`09-Cooling-System/install-guide.md`](../09-Cooling-System/install-guide.md) Phase G.** Lisle funnel on rad neck, open bleed screw on upper hose junction, heater FULL HOT, idle + 2000 RPM cycles, watch funnel until bubbles stop and upper hose is fully hot. #1 DIY-caused K20 failure — don't short it.
64. Top off reservoir to MAX COLD.

### Phase J: First Start + Tune #2 Prep

65. Battery (-) reconnected, terminal torqued.
66. **Fuel prime.** Key ON/OFF/ON/OFF/ON — listen for the pump to prime 2-3 sec each cycle. No start yet.
67. **5-minute leak inspection.** Flashlight walk. Every fuel fitting dry? Every vacuum line seated? No coolant wet? Smell: no fuel, no coolant. Any leak = address now.
68. Start. Cranking ~2-3 sec longer than normal (fuel rail refilling, IACV learning). First idle may be rougher — larger plenum, unlearned trims. Normal.
69. Idle 5 min minimum. Watch:
    - Temp gauge reaching normal in ~5 min
    - No CEL
    - No vacuum hiss
    - No fuel or coolant smell
    - Heater blows HOT (heater loop bled)
70. Shut off. Cool 15 min. Recheck coolant at rad neck and reservoir. Top off.
71. **Short partial-throttle drive ONLY.** Around the block, <3500 RPM, no aggressive throttle, no VTEC. 5-10 minutes. Not a shakedown — a "does it run" drive.
72. **Datalog baseline.** FlashPro connected, record `.fpdl` of idle + partial-throttle. STFT, LTFT, MAP, IAT, knock counts, ECT. This is the pre-Tune #2 baseline for my tuner.
73. **Book dyno for Tune #2.** Full bolt-on calibration: Ultra Street + 66mm TB + headers + exhaust + intake. Expect **~10-20 WHP pickup** from IM + TB alone on top of headers-tuned baseline (target 220-240 WHP on pump gas). Bring baseline datalog + archived Tune #1 `.fpc`.
74. **DO NOT WOT until Tune #2 is dialed in.** Gentle partial-throttle only between install and dyno. No freeway pulls, no VTEC. Treat it like break-in.

---

## Post-Install Tuning

**Tune #2 — "Full Bolt-On"** replaces Tune #1 (headers-only) as my baseline. See [`10-Hondata-FlashPro/tuning-workflow-and-maps.md`](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) for the Daily + Sport two-map protocol.

- **Fuel tables:** Full recal across 4000-8500 RPM. Larger plenum shifts MAP at low RPM (tip-in enrichment) and runs lean at top without more pulse. Tuner dials.
- **Ignition timing:** +1 to +2° over Tune #1 at peak torque RPM, knock-monitored on dyno.
- **VTEC:** Advance to ~5200-5400 RPM. Ultra Street's powerband wants VTEC earlier.
- **Idle target:** 750 → ~800 RPM. Larger plenum idles rougher; the bump smooths without hurting driveability.
- **Tip-in enrichment:** Richer transient to prevent lean stumble on throttle open (larger plenum = more air to fill before MAP responds).
- **Expected:** +10-20 WHP over Tune #1. Peak shifts from ~6800-7200 to ~7400-7800 RPM. Low-end torque softens slightly below 4000 — expected and acceptable.
- **Ceiling:** Still 220-240 WHP on 93 octane with margins. No chasing the dyno top number. Reliability over power, always.

**Expected from IM + TB alone (over headers-tuned):** +10-20 WHP. Combined total-from-stock with Phase 2: ~40-60 WHP at the wheels.

---

## First Drive Checklist

- No vacuum hiss at idle (stethoscope)
- Idle stable 750-800 RPM, no hunting
- No misfires at idle or low RPM
- No coolant or fuel leaks (visual + smell)
- No CEL
- Temp normal in ~5 min, stays there
- Heater HOT at full hot knob
- STFT within ±5%, LTFT within ±8%
- No knock counts at partial throttle
- Clean throttle response, no tip-in stumble
- **WOT only after Tune #2 is flashed and logged**

---

## Common Mistakes (Don't)

1. **Skipping the water-bypass adapter.** PRB manifold has no coolant circuit matching the RBC head. Bare mount = IM won't seal OR coolant circuit is broken (no heater, overheat risk). Mandatory, not optional.
2. **Skipping the DBW TB adapter 309-05-0120.** Bored K20Z3 DBW TB is RBC pattern; Ultra Street TB flange is PRB. Without adapter, TB flange misaligns and won't seal. Vacuum leak + un-tuneable idle on day one.
3. **Reusing the stock IM gasket.** 170k miles + 1 removal cycle = torn. $12 for fresh OEM. No excuses.
4. **Unlabeled vacuum lines.** "I'll remember" is how a clean install turns into a 3-hour vacuum-leak chase. Label every line, photo every joint.
5. **Over-torquing IM bolts.** Ultra Street is cast aluminum but bolt bosses aren't infinite. Past 16 ft-lb risks cracking a mounting ear. Honor Skunk2's spec.
6. **WOT before Tune #2.** Aggressive throttle on Tune #1 with a different IM is how engines get hurt. Larger plenum + bigger TB = different MAP behavior = old tune is wrong at WOT. Partial throttle only until retune.
7. **Prying the stock fuel QC instead of using the Lisle tool.** Prying cracks the plastic retainer — new fuel line is a dealer $40 part.
8. **No key-cycle fuel prime before first start.** Cold-crank with empty rail = stressed starter + lean first seconds. Three ON/OFF cycles, THEN crank.
9. **Leaving IACV unplugged.** Fighting idle at every cold start. It's a 30-second connection.
10. **Skipping the coolant bleed.** Same K20 head-warping trap 09-Cooling-System warns about. Follow Phase G of that guide fully.

---

## Skunk2 Ultra Street vs RBC Compatibility

The Skunk2 Ultra Street 307-05-0600 was designed for the **PRB casting family** — K20A2/K20A3 on 02-06 RSX Type-S and EP3 Civic SI. My 2009 Civic SI K20Z3 uses the **RBC head casting** (same family as all 06-11 FA5/FG2 SI).

The two casting families differ in two ways that block a direct Ultra Street install on an RBC head:

1. **Coolant port geometry.** The PRB manifold includes an internal coolant passage that mates to PRB head coolant ports. The RBC head has coolant ports in different locations. Bolting the Ultra Street directly leaves the RBC head's coolant ports open to atmosphere (leak) AND provides no path for the bypass circuit (TB heater + head bypass flow). The **Skunk2 water-bypass adapter** caps the RBC head coolant ports at the IM mating surface and routes an external bypass hose around the Ultra Street.

2. **Throttle body bolt pattern.** The PRB TB flange on the Ultra Street uses the 02-06 RSX pattern. My K20Z3 DBW TB (bored to 66mm but same bolt pattern as stock) uses the RBC/06-11 SI pattern. These do not interchange. The **Skunk2 DBW TB adapter 309-05-0120** bolts to the Ultra Street's PRB TB flange on one side and accepts the RBC DBW pattern on the other.

Both adapters sold separately by Skunk2, both mandatory for an RBC-head install, both frequently missing from first-time buyers' orders because the main listing doesn't always flag the RBC requirement. TF-Works and Hybrid Racing have them in stock — buy with the manifold in one order.

(Cross-reference: this is also called out in [`19-Flex-Fuel-and-Fuel-System/acuity-fuel-rail-and-flex-fuel-build.md`](../19-Flex-Fuel-and-Fuel-System/acuity-fuel-rail-and-flex-fuel-build.md) §1 — the Acuity rail bolts directly to the Ultra Street, but only once these adapters are in place.)

---

## See Also

- [`overview.md`](overview.md) — parts decision rationale, Ultra Street vs Pro vs Ultra Race comparison, DBW decision (source of truth)
- [`../19-Flex-Fuel-and-Fuel-System/acuity-fuel-rail-and-flex-fuel-build.md`](../19-Flex-Fuel-and-Fuel-System/acuity-fuel-rail-and-flex-fuel-build.md) — bundle window for Acuity 1913-PPL + Bosch EV14 550cc during this install; IM-compatibility warnings also there
- [`../10-Hondata-FlashPro/tuning-workflow-and-maps.md`](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) — Tune #2 full bolt-on Daily + Sport protocol
- [`../13-Headers/install-guide.md`](../13-Headers/install-guide.md) — Phase 2 prerequisite; Tune #1 must exist before this install
- [`../09-Cooling-System/install-guide.md`](../09-Cooling-System/install-guide.md) — Phase G bleed procedure
- [`../docs/torque-specs.md`](../docs/torque-specs.md) — IM 17 ft-lb OEM / 12-16 ft-lb Skunk2, TB 17 ft-lb OEM / 8-10 ft-lb adapter, fuel rail 9 ft-lb

---

*Last updated: 2026-04-20*
