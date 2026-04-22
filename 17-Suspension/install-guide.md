# Suspension Install Guide — BC Racing BR + Bushings + Sway Bars + Alignment

## Status: Planning — Phase 5

This is the biggest, most invasive mechanical job on my entire build. Coilovers at all four corners, polyurethane bushing refresh, front and rear sway bars, roll center correction, tie rods, ball joints, and a mandatory professional alignment at the end. Every wear item I can touch gets touched.

---

## Reality Check

2-3 full day DIY job if I do everything in one session, which is the only sane way to approach it — the car is already apart. Shop labor runs $800-1,500. I'm doing it myself, but I'm not fooling myself on scope.

Time breakdown, realistic:

| Sub-project | DIY time | Notes |
|-------------|----------|-------|
| Front coilover install (both sides) | 4-6 hrs | Straightforward strut swap, but ball joint separation is the wildcard |
| Rear coilover + Skunk2 camber arms | 4-6 hrs | Trunk liner access for top hats adds time |
| Energy Suspension master bushing kit | 6-10 hrs | **Requires hydraulic press for LCA bushings** — shop trip or own tool |
| Hardrace trailing arm bushings | 3-5 hrs | **Requires press.** $150-300 to outsource, often worth it |
| Progress sway bars F+R | 2-3 hrs | Bolt-in, easy win |
| K-Tuned roll center adjusters | 1-2 hrs | Ball joint work |
| Tie rods + ball joints | 2-3 hrs | Ball joint separator/press needed |
| Torque-down + load settle | 1 hr | Critical — see below |
| Alignment (at shop) | 1-2 hrs | **Not DIY, don't try** |

**Realistic total: 20-35 hours across 2-3 full days, PLUS one press-shop trip PLUS one alignment rack appointment.** Two weekends or a long holiday weekend is the right budget.

**Two things I cannot DIY:**

1. Pressing OEM rubber bushings out of steel control arms. Takes 10+ tons and proper fixtures. Either take arms to a machine shop with a 20-ton hydraulic press, or buy pre-bushed complete arms and skip pressing.
2. 4-corner performance alignment. A Hunter HawkEye rack with a trained tech is $150 well spent. Tire wear on a mis-aligned lowered car starts in days.

Book the alignment appointment BEFORE teardown. Find a shop that does performance alignments — not "we align to factory spec" but "we'll hit your target numbers."

---

## Prerequisites / Cross-References

**No tune dependency.** Suspension doesn't touch the ECU. Install any time after Phase 1-4.

| Prereq | Cross-reference | Why |
|--------|-----------------|-----|
| Brake refresh complete | [04-Brakes/](../04-Brakes/) | Wheels are off anyway. Do them first or same session. |
| Alignment shop booked | External — call first | Don't start teardown without a rack reservation. |
| Bushing press plan decided | Shop list or DIY | Either a 20-ton press shop or pre-bushed arms. No improvising with a bottle jack. |
| Dry indoor workspace | My garage | 2-3 days of parts on the floor. |
| Strut bar install stays deferred | [18-Strut-Bar/install-guide.md](../18-Strut-Bar/install-guide.md) | **Do NOT install the Megan bar this session.** Pillow-ball camber plates change strut-top geometry; final fitment is only knowable post-alignment. |

Short version on the strut bar: BC Racing BR camber plates change the strut-top stud pattern and top-deck height. Forcing the Megan bar onto stock-geometry assumptions is how tower welds crack. Coilovers this session; bar install is a separate session after alignment.

---

## Tools Required

### Coilover install

- 1/2" drive torque wrench, 30-250 ft-lb
- 3/8" drive torque wrench, 10-80 ft-lb
- 14mm, 17mm, 19mm, 21mm sockets + matching wrenches
- Breaker bar, 18"+ — for stubborn lower control arm bolts
- Ball joint separator (pickle fork or press-type)
- Tie rod puller
- 4-ton jack stands (4 of them) — car fully elevated with all 4 wheels off
- Floor jack, 2-ton minimum
- Spring compressor — NOT needed; coilovers ship pre-assembled. Explicitly don't buy one.

### Bushing work

- **Hydraulic press (20-ton)** — I don't own one. Shop pressing runs $50-100 per bushing. For LCA and trailing arm bushings, that's the plan.
- Bushing driver set (optional) — sway bar bushings only.

### Sway bar install

- 14mm + 17mm sockets, grease for the poly bushings.

### Alignment

- A drive to the shop. Not DIY.

---

## Parts List

Everything from [overview.md](overview.md), consolidated. Before I start, I verify every box on this list is physically in my garage — no "I'll order that when I get to it" mid-install.

| # | Part | Part Number | Qty | Price | Source |
|---|------|-------------|-----|-------|--------|
| 1 | BC Racing BR coilovers (front + rear set, pillow-ball camber plates included) | A-18-BR | 1 kit | ~$1,195 | K Series Parts / BC Racing direct / Redline360 |
| 2 | Skunk2 Pro Series rear camber arms | 516-05-0625 | 1 pair | ~$333 | Skunk2 direct / K Series Parts / Hybrid Racing |
| 3 | Energy Suspension master bushing kit (black) | 16.18114G | 1 kit | ~$278 | HARDmotion / Amazon |
| 4 | Hardrace rear trailing arm bushings | 6926 | 1 set (both sides) | ~$150 | Hardrace USA |
| 5 | Progress front sway bar (27mm) | 61.1006 | 1 | ~$288 | Progress Technology direct |
| 6 | Progress rear sway bar (24mm, 3-way adjustable, end links included) | 62.1025 | 1 | ~$349 | Progress Technology direct |
| 7 | K-Tuned roll center adjusters (10mm extended ball joints) | KTD-RCA-611 | 1 pair | ~$190 | K Series Parts |
| 8 | Moog outer tie rod end, passenger | ES800373 | 1 | ~$35 | RockAuto / Amazon |
| 9 | Moog outer tie rod end, driver | ES800374 | 1 | ~$35 | RockAuto / Amazon |
| 10 | Moog inner tie rod end | EV800246 | 2 | ~$70 | RockAuto / Amazon |
| 11 | Honda OEM rear shock top mount | 52675-SNA-A03 | 2 | ~$50 | Honda dealer |
| 12 | SPC EZ-Cam front camber bolts | 81260 | 1 pair | ~$30 | HARDmotion / Amazon |
| 13 | Professional 4-corner performance alignment | — | 1 | ~$150 | Local performance shop |

**Consumables:**
- New cotter pins for castle nuts (tie rods, ball joints) — never reuse
- Anti-seize (copper) for strut top nuts, ball joint threads, any fasteners I'll touch again
- Blue Loctite 242 for sway bar bracket bolts, camber arm lock nuts
- Grease for sway bar bushings (most poly bushings ship with a little tube — have extra)
- Fresh DOT 4 brake fluid if I disturb any brake lines beyond routing (I shouldn't, but have it on hand)

---

## Step-by-Step — Split by Sub-Project

Order: front coilovers → rear coilovers + camber arms → bushings (press shop between those two if needed) → sway bars → roll center adjusters → tie rods/ball joints → torque down loaded → drive to alignment.

### Sub-Project A: Front Coilover Install (4-6 hrs)

1. Park on level ground. Loosen front lug nuts 1/2 turn.
2. Jack up front, set on 4-ton jack stands under the frame rails (NOT the LCAs — those are coming off).
3. Pull both front wheels.
4. Start passenger side (more room):
   - **Remove sway bar end link** from strut body. 14mm on the stud flats while cracking the 17mm nut.
   - **Remove ABS sensor cable clip** from strut. Do NOT cut the wire.
   - **Remove brake line bracket** from strut. Do NOT disconnect the hose itself.
   - **Separate tie rod end from knuckle.** Cotter pin out, castle nut backed off until flush with stud top. Tie rod puller to separate.
   - **Separate lower ball joint from knuckle.** Pinch bolt out (40 ft-lb spec but 170k mi seized, breaker bar). **Pinch bolt is a stretch bolt — new one required on reinstall.** Dead-blow the knuckle to separate from the stud.
   - **Support knuckle** with bungee or wire to the strut spring perch so it doesn't rip the brake hose.
5. **Top of strut** — 3 nuts per tower under the hood. Loosen all 3, hold strut from below, remove the last one.
6. Drop the strut assembly out the top of the wheel well. Heavy — two hands.
7. **Prep BC Racing BR front coilover.** Verify BC's pre-set ride height against their spec sheet. Confirm pillow-ball camber plate orientation (front-facing marking on BC plates). Torque top hat assembly per BC's printed sheet — typically 40-50 ft-lb.
8. **Install coilover bottom-up.** Feed up through wheel well. Thread all 3 top nuts hand-tight before torquing any. Torque top nuts to **29 ft-lb** per [docs/torque-specs.md](../docs/torque-specs.md) OR BC's alternate spec if they deviate.
9. **Reconnect bottom** in reverse:
   - Ball joint stud into knuckle. **New pinch bolt, 40 ft-lb**.
   - Tie rod into knuckle, new castle nut, **40 ft-lb**, new cotter pin (turn up to next slot, NEVER back off).
   - Brake line bracket + ABS sensor clip reattached.
   - Sway bar end link — leave loose for now.
10. **CRITICAL: Do NOT torque strut-to-knuckle bolts or any lower suspension pivot bolts yet.** Stay loose until car is loaded. Torquing unloaded = bushing binding = premature wear.
11. Repeat on driver side.

### Sub-Project B: Rear Coilover Install + Skunk2 Pro Series Rear Camber Arms (4-6 hrs)

Rear is easier (no ball joint, no tie rod) but harder in one way — top hats live under the trunk liner.

12. Move jack stands to rear. All 4 wheels off simultaneously — fronts back on jack stands at frame rails, rears on stands at the rear subframe pinch welds.
13. Pull rear wheels.
14. **Access rear strut top hat** — pull trunk liner and trim covering each shock tower (push-in clips + 10mm bolts).
15. One side at a time, shock and camber arm together.
16. **Remove rear shock lower bolt** (40 ft-lb, breaker bar).
17. **Remove rear shock upper nut** from inside the trunk. Shock drops out.
18. **Remove OEM rear upper control arm** — one bolt at inner pickup, one at knuckle.
19. **Install Skunk2 Pro Series 516-05-0625:** Pre-set length to MATCH stock eye-to-eye — alignment shop fine-tunes. Mounting bolts to **47 ft-lb**. Lock nuts on telescoping section: **35 ft-lb** per Skunk2 spec.
20. **Install new OEM rear shock top mount** (Honda 52675-SNA-A03) onto the BC rear coilover. 170k-mile mounts are compressed — no reason to reuse.
21. **Install BC Racing BR rear coilover:** Pre-set height per BC's spec. Feed up into rear tower, upper nut from trunk side, torque to **22 ft-lb** (or BC's spec). Lower mount onto rear control arm — lower bolt stays hand-tight until car is loaded.
22. Repeat other side.

### Sub-Project C: Energy Suspension Master Bushing Kit 16.18114G (6-10 hrs total — or "send to shop for one day")

The 16.18114G kit covers front LCA bushings, sway bar bushings, and front subframe bushings. Each one is a different level of effort.

**Front Lower Control Arm Bushings — PRESS REQUIRED:**

23. Front end already apart from Sub-Project A. Unbolt front LCAs entirely: front pivot bolt (54 ft-lb spec), rear pivot bolt to subframe (76 ft-lb), ball joint already disconnected.
24. Take LCAs to a press shop. $50-100/bushing outsourced, $200-400 both arms complete. **Alternative: pre-bushed complete LCAs** (~$300-500 pair) saves the shop trip.
25. Reinstall LCAs — both pivot bolts hand-tight only. Leave loose until loaded.

**Sway Bar Bushings (front and rear):**

26. Unbolt the 2 D-cup brackets per bar (14mm). Swap old rubber for new Energy Suspension poly D-cups. Grease the inside face.
27. Repeat on rear bar.
28. Torque bracket bolts to **29 ft-lb**, blue Loctite on threads.

**Front Subframe Bushings:**

29. Requires dropping the front subframe. **Skip this session** unless the subframe is already dropped for a header install ([13-Headers/install-guide.md](../13-Headers/install-guide.md)). Not obligated to use every piece of the kit in one sitting.

### Sub-Project D: Hardrace Trailing Arm Bushings 6926 (3-5 hrs or outsource)

The most notorious 8th gen Civic suspension item. OEM rubber hardens and creaks. Hardrace 6926 replaces with hardened rubber — better NVH than poly for a street car.

30. **Press required.** Take trailing arms to a press shop — $150-300 total outsourced, **often worth it.** Or buy pre-bushed complete Hardrace trailing arms and skip pressing.
31. If removing arms myself: unbolt both ends (both **54 ft-lb** spec, breaker bar). Arm comes out.
32. At the press shop: verify orientation (void/directional indicator points fore-aft correctly).
33. Reinstall — both bolts hand-tight only. Leave loose until loaded.

### Sub-Project E: Progress Sway Bars (front 27mm + rear 24mm adjustable) (2-3 hrs)

Done after coilovers and bushings so that the coilovers' end link geometry is known.

**Front (Progress 61.1006, 27mm):**

34. Stock bar is still on at this point. Unbolt and remove.
35. **Use Progress-supplied bushings** — the Energy Suspension D-cups I just installed are sized for the stock bar and won't fit the thicker 27mm Progress bar. Grease liberally.
36. Slide Progress bar into position, bolt up with new bushings.
37. New end links — **do NOT reuse 170k-mile OEM end links** (worn ball joints, clunking).
38. Bracket bolts **29 ft-lb** (blue Loctite), end link nuts **29 ft-lb** but leave snug until loaded.

**Rear (Progress 62.1025, 24mm, 3-way adjustable):**

39. Same procedure — stock bar out, Progress 24mm in with its supplied bushings.
40. **End link attachment:** Progress 62.1025 has 3 holes per end (soft/medium/stiff). **Start MIDDLE.** Adjust stiffer after shakedown if understeery, softer if snappy. Stiffer rear = more oversteer.
41. End links supplied in the 62.1025 kit — use them. **29 ft-lb**, leave loose until loaded.

### Sub-Project F: K-Tuned Roll Center Adjusters (1-2 hrs)

42. KTD-RCA-611 is a 10mm extended lower ball joint. Replaces stock ball joint with a taller one, moving the stud up 10mm. On a lowered car this restores the LBJ angle toward OEM and moves the roll center back up off the ground — fixes the handling penalty lowering otherwise introduces.
43. LCAs are off the car for bushing press work. NOW is the time to swap ball joints — same press shop handles both jobs in one visit.
44. Old ball joint pressed out, new K-Tuned pressed in. Use supplied retaining hardware (c-clip or threaded collar per K-Tuned spec).
45. **Install on the CORRECT SIDE.** Side-specific due to taper direction. Verify K-Tuned markings before pressing.
46. Reinstall LCA with new ball joint. Knuckle connects to the new extended stud. **New pinch bolt, 40 ft-lb.**

### Sub-Project G: Tie Rods + Ball Joints (2-3 hrs)

Overlaps with Sub-Projects A and F but conceptually its own job.

47. **Ball joints** — already handled in Sub-Project F (K-Tuned RCA replaces ball joint AND corrects roll center).
48. **Outer tie rod ends (Moog ES800373 passenger, ES800374 driver):**
   - Before removing old outers, **count the threads** or measure length from jam nut to end. Gives a ballpark alignment starting point so the car drives to the rack without tramlining.
   - Loosen jam nut, thread off old, thread on new Moog to the SAME length.
   - Outer into knuckle, new castle nut to **40 ft-lb**, new cotter pin.
49. **Inner tie rod ends (Moog EV800246 x2):** Only replace if play detected. Requires an inner tie rod tool (big crow's-foot on 1/2" drive). Torque per Moog's spec (40-55 ft-lb).

### Sub-Project H: Torque Down + Load Car (1 hr)

This step makes or breaks suspension lifespan. Bushings must be torqued at their NEUTRAL (loaded) position. Torquing on jack stands twists the bushing at its installed angle; every compression cycle after that adds twist load. Bushings wear out in months instead of years.

50. Audit every fastener:
   - Fully torqued (doesn't pivot through travel): strut tops, sway bar brackets, camber arms, RCA pinch bolt, tie rod castle nuts.
   - Hand-tight / snug (pivots with suspension): all LCA pivots, trailing arm pivots, sway bar end links.
51. Lower car to ground. All 4 wheels down.
52. **Roll back and forth ~10 feet** to settle suspension into static loaded position. Bushings rotate to neutral.
53. NOW torque the hand-tight fasteners:
   - LCA front pivot: **54 ft-lb**
   - LCA rear pivot (to subframe): **76 ft-lb**
   - Trailing arm bolts (both ends): **54 ft-lb**
   - Rear lower shock bolt: **40 ft-lb**
   - Sway bar end link nuts: **29 ft-lb** front AND rear
54. Double-check strut top nuts — **29 ft-lb** front, **22 ft-lb** rear.

### Sub-Project I: Mandatory Alignment

55. Drive gently to the alignment shop. Car may pull, track off-center, feel crooked — normal with fresh suspension. Baby it.
56. Request a **4-corner performance alignment** with specs matched to my driving style:

| Parameter | Daily setup | Sport setup |
|-----------|-------------|-------------|
| Front camber | -1.0 deg | -2.0 deg |
| Rear camber | -1.5 deg | -2.0 deg |
| Front toe | slight toe-in (+0.05) | 0 (zero toe) |
| Rear toe | slight toe-in (+0.05) | 0 (zero toe) |
| Front caster | max available | max available |

57. Ask the tech for the **printed alignment sheet** with before/after numbers. Keep with build records as baseline.
58. Pay the ~$150. Even enthusiasts don't DIY a 4-corner performance alignment.

---

## Ride Height Setup (pre-alignment)

Verify ride height is sane and even corner-to-corner before driving to the shop.

59. After torque-down and roll-settle, measure fender-to-hub-center at all 4 corners:
   - Front: 25.5-27" (daily-usable drop, not slammed)
   - Rear: 26-27.5" (~0.5" higher than front — prevents rake-forward look)
60. If one corner is off by more than 0.5", adjust that corner's BC lower perch with the supplied spanner wrenches. One full turn ~ 3mm height change.
61. **Adjust all four corners together** to avoid cross-loading the chassis.
62. Document final heights. Reference for future alignment checks, sag detection, and the strut bar clearance check in [18-Strut-Bar/install-guide.md](../18-Strut-Bar/install-guide.md).

---

## First Drive Checklist

After alignment, short easy drive before highway. Listening for:

- **No clunks** over bumps — unseated bushing or loose fastener
- **No rubbing** at full steering lock — parking lot, lock-to-lock, listen for tire-to-liner contact
- **Steering centered** — wheel straight when driving straight
- **Ride firmer but not harsh** — BC middle damping should be noticeably stiffer, not painful
- **No alignment pull** — car tracks straight hands-off briefly on empty road
- **Brake pedal feel unchanged**
- **Sway bar function** — parking lot circles should show obviously reduced body roll

If any fails, stop and diagnose. Don't highway-drive a suspension that isn't behaving right.

---

## Post-Install Settling

Poly and rubber bushings settle in over the first 100-500 miles. Spring perches seat slightly.

- **100 miles:** re-check torque on all lower fasteners (LCA pivots, trailing arms, end links, brackets).
- **500 miles:** re-measure ride height. If any corner settled >0.25", adjust perches. If pulling or uneven tire wear appears, **go back for re-alignment** — most shops offer a free 30-day recheck.
- **1000 miles:** stable.

---

## Common Mistakes

- **Torquing bushings unloaded = bushings bind = short life.** The single most important rule. LCA pivot bolt torqued on jack stands = bushing twisted every compression cycle, tears internally within a year. **Always torque loaded, after rolling to settle.**
- **Reusing 170k-mile sway bar end links.** Worn ball joints = clicking from day one. New sway bar deserves new end links.
- **Skipping alignment.** Lowered car with wrong rear camber eats the inner shoulder off a rear tire in 2 weeks. No exceptions.
- **Skunk2 camber arm pre-set wrong.** Set length wildly off stock and the shop can't get spec. Match stock eye-to-eye, let the tech fine-tune.
- **K-Tuned RCA on wrong side.** Side-specific due to taper direction. Verify markings before pressing.
- **Subframe bushings attempted without dropping the subframe.** Not accessible otherwise. Skip or combine with a header session.
- **Pillow-ball camber plate without strut bar clearance check** — forcing the Megan bar on afterward cracks tower welds. See [18-Strut-Bar/install-guide.md](../18-Strut-Bar/install-guide.md).
- **Wrong-diameter sway bar bushings.** Energy Suspension D-cups are sized for the stock bar; Progress 27mm needs Progress-supplied bushings. Wrong diameter = rattling bar.

---

## Strut Bar Decision

The Megan Racing Race Spec bar (MR-SB-HC06FU-1P) is in the box on the shelf. **NOT going on during this session.** See [18-Strut-Bar/install-guide.md](../18-Strut-Bar/install-guide.md) for full reasoning. Summary:

- BC Racing BR pillow-ball camber plates replace the stock upper strut mount entirely — top-deck height and stud pattern may differ from stock
- Bar fitment is only knowable after coilovers are installed AND alignment is done (final camber moves the pillow-ball plate slightly)
- Attempt fitment only after this session is closed out — separate install day
- Accept that the bar may not fit with the BR plates; be prepared to shop alternatives (Cusco Type OS Ti, Ultra Racing URTW2-003, or custom)

No measuring or pre-fitting the strut bar during this suspension session.

---

## See Also

- [overview.md](overview.md) — parts research, rationale, budget tier breakdown
- [18-Strut-Bar/install-guide.md](../18-Strut-Bar/install-guide.md) — **strut bar install happens AFTER alignment, with post-coilover clearance check first**
- [04-Brakes/](../04-Brakes/) — brake refresh happens at the same time, wheels are off anyway
- [13-Headers/install-guide.md](../13-Headers/install-guide.md) — if headers are being installed in the same window, the subframe drop there opens access for the Energy Suspension front subframe bushings
- [docs/torque-specs.md](../docs/torque-specs.md) — every torque value referenced here, OEM-spec, cross-checked

---

*Last updated: 2026-04-20*
