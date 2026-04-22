# Pulleys + Harmonic Balancer Install Guide — ATI Super Damper + NST Alt/Idler

## Status: Planning — Phase 4

## Reality Check Before I Start

This job looks simple — swap three pulleys, run a new belt, drive. In reality, the crank bolt is the scariest fastener on this build that isn't an exhaust stud. Factory spec is **131 ft-lb plus a 90-degree yield angle**, and on a 170k-mile engine with original thread-locker the breakaway torque typically lands between **200 and 300 ft-lb**. A 120 ft-lb cordless impact will laugh at this bolt and round the socket before it cracks the bolt.

Budget **3-5 hours, intermediate-level** wrenching. I need either a proper crank pulley holder with a long breaker bar, or a **600+ ft-lb air or high-torque cordless impact**. No heat on this bolt, and no sub-500 ft-lb impacts — both paths end in damaged crank threads or a stretched bolt left behind.

The **yield-bolt sequence is non-negotiable**. The replacement 90017-RWC-A01 is torque-to-yield, single-use. Reusing the old bolt is how dampers walk off the crank nose and destroy engines. I follow the Honda FSM sequence exactly: hand tight → 37 ft-lb → 90 degrees of angle. Done. I do not re-verify with a torque wrench.

The other non-negotiable: **the NST crank pulley from the NST22015K-Purple kit does NOT go on this car.** The ATI Super Damper replaces the crank pulley entirely. I'm using ONLY the NST alternator and idler from that kit — the NST crank piece goes in the spare bin.

---

## Prerequisites / Cross-references

### Must be done first

| Prerequisite | Why |
|--------------|-----|
| Phase 3 full bolt-on tune complete | Pulleys are mechanical only, no retune needed, but a tuned baseline means any post-install shift is attributable to the pulley swap |
| New crank bolt **90017-RWC-A01** in hand | Torque-to-yield, single-use. Do not start if this bolt is not on the bench |
| New crank seal **91214-RZY-A01** in hand | Timing cover is exposed while the damper is off. $15 now prevents a second teardown when the 170k-mile seal starts weeping |
| Engine fully cold | Overnight ideal. I don't want coolant splashing if a hose is bumped |

### Must NOT be done / known conflicts

- **NST crank pulley MUST NOT be installed.** ATI Super Damper replaces it. Installing both deletes damper function or creates mechanical interference. Coordinate with [`21-Purple-Cosmetics/overview.md`](../21-Purple-Cosmetics/overview.md) — the purple NST kit is purchased as a 3-piece, but only alt + idler are installed.
- **Do not reuse the old crank bolt.** Yield bolts are stretched past their elastic limit by design. They cannot provide correct clamp load a second time regardless of how clean they look.

### Opportunistic bundling

If I'm pulling the timing cover for [`05-Timing-Chain-Maintenance/`](../05-Timing-Chain-Maintenance/) or the VTC actuator under [`06-Ignition-Refresh/`](../06-Ignition-Refresh/), this pulley job is already half-done and should be combined. Crank bolt comes out either way — doing it twice wastes yield bolts and labor.

---

## Tools Required

### Critical — do not start without these

| Tool | Purpose |
|------|---------|
| Crank pulley holder tool | Holds crank stationary for breaker-bar method. AutoZone loan-a-tool or Evergreen HCPH1 (~$35) |
| **OR** 600+ ft-lb impact wrench | Alternative to holder + breaker bar. Genuine 600+ ft-lb rated — Milwaukee 2767, Ingersoll Rand 2235. A Harbor Freight "600 ft-lb peak" unit is not the same thing |
| 19mm impact-rated socket | Crank bolt head, 1/2" drive. Chrome sockets shatter under these loads |
| 18"+ breaker bar | 24"+ preferred for the breaker-bar method |
| 150 ft-lb torque wrench, 1/2" drive | Final torque pass at 37 ft-lb |
| Angle gauge | 90-degree rotation after 37 ft-lb. ~$20 at Harbor Freight. You cannot eyeball this |
| Harmonic balancer puller (3-jaw) | If stock damper is seized. AutoZone loan-a-tool. Pulls from hub center, NOT outer inertia ring |
| **ATI install tool** | Threaded rod + thrust bearing washer to draw the damper onto the crank nose. No hammering, ever |
| Serpentine tensioner tool | Lisle 59250 or 3/8" breaker bar in the tensioner's square drive |
| Lisle alternator pulley tool (59300) | Inner hex holds alt shaft, outer socket turns pulley nut |
| Seal driver | Proper seal driver for the 91214-RZY-A01 |

### Standard tools

Metric sockets 10/12/14/17/19mm, 3/8" and 1/2" ratchets + extensions, metric wrenches, shop light, rags, brake cleaner, floor jack + stands + chocks, drip pan, paint marker.

---

## Parts List

| # | Item | Part Number | Notes |
|---|------|-------------|-------|
| 1 | ATI Super Damper | **ATI 918477** | K-series harmonic damper, SFI 18.1, 6-rib serpentine. ~$352 at Drag Cartel |
| 2 | NST Alternator Pulley | from NST22015K-Purple | Overdrive alt, 6061-T6, purple anodize |
| 3 | NST Idler Pulley | from NST22015K-Purple | Lightweight idler, 6061-T6, purple anodize |
| 4 | NST Crank Pulley (from kit) | **DO NOT INSTALL** | ATI replaces this. Spare bin |
| 5 | Serpentine Belt | Honda OEM or Gates K070663 | Fresh belt every pulley swap |
| 6 | **Crank Bolt (ONE-TIME-USE YIELD)** | **90017-RWC-A01** | NEW, single-use, non-negotiable |
| 7 | Front Crank Seal | **91214-RZY-A01** | Replace while apart, ~$15 |

**Total parts cost:** ~$640-760.

---

## Step-by-Step Procedure

### Phase A: Pre-Install Prep (20-30 min)

1. Engine **fully cold**. Overnight is ideal.
2. Level ground, rear wheels chocked.
3. **Disconnect battery negative.** Alternator pulley comes off; I don't want anything live nearby.
4. Raise passenger side. Jack stands on the pinch weld.
5. Remove passenger front wheel.
6. Remove inner fender liner (plastic pop-clips + 10mm bolts). Exposes the accessory drive from the wheel well.
7. Remove lower engine splash shield if present.
8. **PHOTOGRAPH the serpentine belt routing.** From wheel well and from above, multiple angles. I'll need this at Phase I. Also confirm the routing diagram on the underside of the hood is legible.

### Phase B: Serpentine Belt Removal (10-15 min)

9. Locate the auto-tensioner (spring-loaded pulley).
10. With the tensioner tool or a 3/8" breaker bar in the tensioner's square drive, rotate **clockwise** against spring pressure to slacken the belt.
11. Hold tensioner relaxed, slip the belt off the most accessible pulley (alternator or idler).
12. Slowly release the tensioner. It should spring back firmly. **If the tensioner is weak, bouncy, or doesn't return firmly, replace it now** (Honda 31170-RRB-A02) — I don't want to find this after everything is buttoned up.
13. Work the belt off the remaining pulleys by hand.
14. Inspect the old belt. Glazing, cracks across the ribs, missing chunks, or oil contamination mean something caused it — investigate alignment before installing new pulleys.

### Phase C: Break the Crank Bolt (THE HARD PART) (15-60 min)

This is where most DIY pulley swaps stall. Factory 131 ft-lb + 90-degree yield, heat-cycled 170k miles. Breakaway **200-300 ft-lb** is normal.

**Three options in order of preference:**

15a. **Option 1 — Crank pulley holder + long breaker bar (preferred).**
   - Install the holder onto the stock damper per its instructions.
   - Brace the holder against the subframe or a frame rail — NOT against the oil pan.
   - 19mm impact socket on the bolt, 24"+ breaker bar. Steady constant pressure counter-clockwise. Do not jerk — shock loading breaks things.
   - Bolt breaks with a loud pop. Normal.

15b. **Option 2 — 600+ ft-lb impact wrench.**
   - 19mm impact socket, short bursts. Crank's rotational mass resists the impact; no holder needed with a real impact.
   - If the impact hums 10 seconds with no movement, stop. It isn't rated high enough. Switch to Option 1.

15c. **Option 3 — Starter-bump (NOT RECOMMENDED unless experienced).**
   - Wedge the breaker bar against the subframe, bump the starter briefly to use engine torque to break the bolt.
   - Can work; also can destroy things quickly if the bar slips. I'm not doing this unless Options 1 and 2 are unavailable.

16. **DO NOT heat the crank bolt.** Heat is for exhaust studs. Localized heat on the crank nose risks annealing steel and cooking the crank seal right behind the damper.
17. **DO NOT use a sub-500 ft-lb impact.** Either fails to break the bolt or partially loosens it into an unknown state.
18. Once loose, thread the bolt out by hand. **Throw this bolt away immediately.** No matter how good it looks.

### Phase D: Remove the Stock Damper (10-30 min)

19. With the bolt out, the damper should slide off the crank nose by hand. Wiggle back and forth pulling straight out. Crank has a Woodruff key — do not rotate while pulling.
20. If seized on (likely at 170k), use the 3-jaw puller:
   - Jaws grip the **hub** (inner metal), NOT the outer elastomer ring or inertia weight. Pulling on the outer ring separates the damper.
   - Center bolt pushes against the crank nose. Use a protective cap or soft shim between puller bolt and crank threads — the crank threads must stay perfect for the new bolt.
   - Tighten slowly. Damper pops free with moderate force.
21. Find and remove the **Woodruff key** in the crank keyway. Magnet or needle-nose pliers. Put it in a dedicated container. **Do not lose it.** The new damper needs this key to index. If stuck, tap it out gently — do NOT pry with anything that gouges the keyway.
22. Inspect crank nose for damage, galling, corrosion. Brass brush + brake cleaner. Must be smooth, dry, clean before the new damper goes on.

### Phase E: Replace the Crank Seal (15-20 min)

With the damper off, the timing cover seal is fully accessible. Replace it. The 170k-mile seal is hardened and almost certainly weeping microscopically.

23. Small pick or seal puller to remove the old seal.
24. **Do not gouge the crank nose or the seal bore.** Any scratch is a future leak path. Angle the pick toward the seal, not the crank or the aluminum cover.
25. Clean the seal bore thoroughly with brake cleaner and a lint-free rag.
26. Light film of fresh engine oil on the lip of the new seal.
27. Drive the new seal squarely with a proper seal driver. Seat it **flush with the face of the timing cover** — not recessed, not proud.
28. **No hammer directly on the seal.** Proper driver only. Socket-as-driver works only if it's exactly the seal's OD.

### Phase F: Install the ATI Super Damper (15-20 min)

29. Confirm the Woodruff key is seated flat in the crank keyway, fully engaged.
30. Align the keyway in the ATI hub with the Woodruff key.
31. Slide the damper onto the crank by hand. It binds before fully seating — normal. The crank-nose interference is snug by design.
32. **Use the ATI install tool (threaded rod + bearing washer).**
   - Thread the rod into the crank's center thread.
   - Bearing washer and nut over the rod, against the damper face.
   - Tighten the nut to draw the damper on smoothly and squarely.
   - Seated when it bottoms against the timing cover boss / crank spacer. Hard stop — do not force past.
33. **NEVER HAMMER THE DAMPER.** Hammer blows crack the ATI hub, knock the elastomer out of round, and bend the crank nose. This is how a $350 damper becomes scrap.
34. Remove the install tool. Damper should be flush against the timing cover and rotate freely with the crank.

### Phase G: New Crank Bolt — YIELD TORQUE SEQUENCE (10 min)

**Non-negotiable. Read twice.**

35. Verify I'm using the **NEW 90017-RWC-A01.** Not the old one. The new OEM yield bolt.
36. Inspect threads on the new bolt and in the crank. **Clean and DRY.** No oil, no anti-seize, no thread locker. Factory spec assumes dry friction coefficients. Lubricant dramatically over-clamps and can snap the bolt.
37. Thread by hand until it contacts the damper face.
38. **Pass 1:** Torque to **37 ft-lb** with a calibrated torque wrench.
39. **Pass 2:** Rotate an additional **90 degrees** using the angle gauge. Paint-marker the bolt head at the 0-degree position if it helps me track.
40. **DO NOT re-check with a torque wrench after the angle pass.** The bolt is past its yield point — torque readings are meaningless. It has correct clamp load by design. Touching it with a torque wrench is how DIYers talk themselves into "just a little more" and snap the bolt.
41. Wipe the damper face clean. Crank bolt is done.

### Phase H: Install NST Alt + Idler Pulleys (20-30 min)

42. **Alternator pulley.** Lisle 59300 tool — inner hex holds alt shaft, outer socket turns pulley nut.
   - Remove stock nut. Slide stock pulley off.
   - Slide NST overdrive alt pulley on.
   - Torque nut per NST: typically **65-80 ft-lb**. Blue (242) thread locker on threads.
43. **Idler pulley.** Remove stock idler bolt (14mm or 17mm center). Slide stock idler off. Install NST idler. Torque center bolt per NST: typically **30-40 ft-lb**. Blue thread locker.
44. **DO NOT INSTALL THE NST CRANK PULLEY.** ATI is on the crank. The NST crank piece goes in the spare bin. If I hit a brain-fart and installed it — remove it now.
45. Rotate both new pulleys by hand. Spin freely, no binding, no lateral play, no bearing noise.

### Phase I: Serpentine Belt Install (15 min)

46. Reference the routing photo from Phase A.
47. Start by wrapping the new belt around the crank (ATI) pulley — secure starting point at the bottom.
48. Route up through the accessory pulleys per the routing diagram (typically crank → A/C → idler → power steering → water pump → alternator → tensioner, but confirm against hood sticker).
49. Last pulley is typically the tensioner or the alternator. Rotate tensioner to slack, slip the belt over the final pulley, slowly release.
50. **Verify:** belt centered on every pulley, no twists, ribs engaged with the grooves on ribbed pulleys, flat back on smooth idlers.
51. Rotate the crank by hand (19mm, gentle clockwise) two full revolutions. Belt tracks centered through full rotation — no rubbing, no slapping.

### Phase J: First Start + Verification (15-20 min)

52. Reconnect battery negative.
53. Reinstall fender liner and splash shield (finger tight for now).
54. **Key ON, do not start, for 5 seconds.** Listen for abnormal electrical sounds. Dash lights come up normally.
55. **Start the engine.** Fires within 2 seconds as usual. If not, kill it and check the alternator connection — that's the only electrical thing I touched.
56. **Idle 30 seconds.** Listen for:
   - Belt squeal (misalignment, contamination, undertension)
   - Chirp (worn tensioner or bad bearing)
   - Grind (bad pulley bearing)
   - Knock or rattle from the damper area (damper unseated or bolt under-torqued — shut off immediately)
57. Dash charging voltage indicator normal. If battery light comes on, the NST alternator pulley install is suspect.
58. **Rev briefly to 2,000-3,000 RPM** a couple times. Watch belt from the wheel well. Stays centered on every pulley.
59. Shut down. 5 minutes to settle.
60. **Visual re-inspection:** everything tight, no oil at the new crank seal, no belt walk, damper still seated, no tools left in the engine bay.
61. **Short shakedown: 5 miles at low-to-moderate RPM.** Home, re-inspect — belt still tracking, tensioner in normal position.
62. Reinstall wheel, torque lug nuts to **80 ft-lb**, star pattern.

---

## Post-Install Break-In

| Interval | Action |
|----------|--------|
| First 100 miles | Drive gently. Avoid sustained WOT. Let the new belt bed in |
| 100-mile inspection | Visual: belt tracking, tensioner position, damper seating, no oil at seal or bolt |
| 500-mile inspection | One more visual. Should be clean |

**No retune required.** Mechanical-only mod. Slight underdrive from NST alt + idler and smaller ATI diameter won't measurably shift AFR or timing. I should still **datalog a baseline after install** per [`docs/baseline-logs.md`](../docs/baseline-logs.md) as a record of the as-installed state.

---

## First Drive Checklist

- [ ] No belt squeal, chirp, or grind at idle or under load
- [ ] No damper noise (thump, knock, rattle) at any RPM
- [ ] Alternator charging — dash or OBD2 reads 13.8-14.4V at idle with accessories on
- [ ] A/C functions normally
- [ ] Power steering functions normally
- [ ] Water pump circulating (heater hot after 5 min)
- [ ] No oil leaks at crank seal, timing cover, or damper face
- [ ] Belt centered on every pulley through a short drive
- [ ] No new OBD2 codes after shakedown

---

## Common Mistakes (Do Not Do These)

| Mistake | Consequence | Prevention |
|---------|-------------|------------|
| **Reusing the yield crank bolt** | Bolt loosens in service → damper walks off crank → destroyed engine. Documented repeatedly on 8thcivic and k20a.org | Buy 90017-RWC-A01 new. Trash the old one immediately |
| **Installing the NST crank pulley despite having the ATI** | Mechanical interference or deleted damper function on a 170k crank | NST crank goes in the spare bin. Only alt + idler from the kit |
| **Hammering the ATI damper onto the crank** | Cracked hub, broken elastomer bond, bent crank nose | ATI install tool (threaded rod + bearing washer) only |
| **Skipping the angle torque (doing just 37 ft-lb)** | Under-clamped bolt → walks loose in service | Full sequence: 37 ft-lb then 90-degree rotation with angle gauge |
| **Oil or anti-seize on the crank bolt threads** | Over-clamp at the same indicated torque → snapped bolt or damaged crank threads | Clean dry threads per FSM |
| **Damaging the crank seal during removal** | New seal leaks from day one | Pick away from the crank nose, never pry against it |
| **Skipping the crank seal replacement** | Weeps within 1-2k miles, second teardown to fix | Replace every time the damper is off. $15 |
| **Using a 300 ft-lb cordless impact on the crank bolt** | Impact hums, bolt doesn't move, socket rounds the head | 600+ ft-lb rated only, or holder + 24" breaker bar |
| **Heating the crank bolt** | Annealed crank steel, cooked crank seal | Never. This is not an exhaust stud |
| **Losing the Woodruff key** | Damper spins on crank nose under load = catastrophic | Dedicated container the moment it comes out |

---

## Why ATI Over Aluminum Underdrive Crank Pulleys

A lot of K-series builders run solid billet aluminum crank pulleys — Buddy Club P1, NST's own crank piece, Unorthodox Racing. Cheaper, lighter, marginally more underdrive effect. **They also delete the harmonic damper entirely.**

Harmonic dampers aren't decorative. The K20Z3 crankshaft has natural torsional frequencies hit within the operating range, and the stock damper's elastomer ring (or the ATI's) absorbs those vibrations before they destroy main bearings and stretch timing chains. At **170k miles on my crank**, with headers, aggressive timing, and higher sustained RPM planned, deleting damper function to save a few dollars and maybe gain a whp is exactly the trade-off my reliability rule forbids.

No one has published a confirmed "billet pulley killed my K20" case. The failure mode is slow and silent: accumulated bearing wear over 20-50k miles, chain stretch, eventual rod knock. By the time damage is visible, the cause is unattributable. The ATI is the insurance policy.

---

## Why NST Purple Alt + Idler (It's an Aesthetic Call)

Realistic power gain from underdriving the alternator and idler is **under 2 WHP**, and on NST's overdrive alt it may be net-zero or slightly negative at higher RPM. Weight reduction on the rotating assembly is real but tiny.

**I'm buying these for the purple anodize, full stop.** They fill the alt + idler slots of my [`21-Purple-Cosmetics/`](../21-Purple-Cosmetics/) theme — reputable brand, correct fitment, CNC 6061-T6. The "underdrive power gain" is a rounding error; the cosmetic payoff is the real reason. I own that honestly.

The one genuine functional benefit of the NST alt is that it **overdrives** the alternator rather than underdriving it — matters because my planned LattePanda in-car PC draws 15-30W continuously, and I want the alternator spinning faster than stock at idle, not slower.

---

## See Also / Cross-references

- [`overview.md`](overview.md) — parts selection rationale, ATI vs Fluidampr, NST vs Buddy Club
- [`../21-Purple-Cosmetics/overview.md`](../21-Purple-Cosmetics/overview.md) — NST22015K-Purple kit notes, crank-pulley conflict
- [`../05-Timing-Chain-Maintenance/overview.md`](../05-Timing-Chain-Maintenance/overview.md) — same yield-bolt procedure; bundle if chain is getting done
- [`../06-Ignition-Refresh/overview.md`](../06-Ignition-Refresh/overview.md) — VTC actuator shares the crank-bolt teardown; bundle opportunistically
- [`../10-Hondata-FlashPro/tuning-workflow-and-maps.md`](../10-Hondata-FlashPro/tuning-workflow-and-maps.md) — no retune required, but log a post-install baseline
- [`../docs/torque-specs.md`](../docs/torque-specs.md) — build-wide torque reference including crank-bolt yield sequence

---

*Last updated: 2026-04-20*
