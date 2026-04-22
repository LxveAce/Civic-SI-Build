# Clutch & Flywheel Install Guide — Exedy Stage 1 (08806) + LW Flywheel (HF02)

## Status: ALREADY INSTALLED — reference doc

I did this job myself at ~170k miles. The original clutch was smoked and I wasn't paying a shop $1,200+ to drop the trans when I had a weekend and a buddy. This doc is my record of what I did and the playbook if I ever go back in there.

**If you are about to do this:** read the "While You're In There" section twice. The single biggest mistake on this job is pulling the trans and not refreshing every wear item while the driveline is open. You do not want to do this job twice.

---

## Reality Check

This is a **transmission-out** job. That's the whole story. The actual clutch-and-flywheel swap is maybe 90 minutes of real wrenching — the other 7+ hours is getting access and reassembling.

**Difficulty for a first-timer:** high. Not because any single step is technical, but because the job is long, parts are heavy and awkward, and there are a dozen small things (dowel pins, pilot bearing, input shaft alignment, bellhousing bolt lengths) that will bite you if you skip them.

**Time budget:**

- **DIY first-timer:** 10-12 hours. Full weekend. Nothing else that day.
- **DIY experienced:** 6-8 hours.
- **Shop labor:** 6-8 billed hours, ~$800-1,200.

**Reliability-first rule for this job:** every accessible seal, bearing, and bushing behind the bellhousing gets refreshed now. Every one I skip is a future trans-drop I'm signing up for. That's the heart of the "while you're in there" philosophy and it applies here harder than anywhere else on the car.

---

## Prerequisites / Cross-References

Dropping the transmission is the single most-enabling disassembly on this car. Several unrelated jobs become effectively free labor the moment the trans is on the floor. **If any of the following are on the to-do list, do them now:**

| Also Do | Why it's free labor now | Cross-ref |
|---------|-------------------------|-----------|
| **Clutch master + slave cylinder + braided line** (Hybrid Racing HYB-CMC-01-20) | CSC is on the bellhousing. Doing it separately later = pulling the trans twice. | [07-Clutch-Hydraulics/](../07-Clutch-Hydraulics/) |
| **Rear main seal** (91214-RDA-A01) | Crank is exposed the moment the flywheel comes off. $20. 170k RMS weeps within a year guaranteed. | — |
| **Pilot bearing** (91006-RWC-003) | Lives in the crank center. Accessible only with flywheel off. ~$15. | — |
| **Throwout bearing** (22810-RWC-003) | Lives on the input shaft. Trans-out only. ~$40. | — |
| **Fresh Honda MTF-3** (08798-9031, 2.2 qt) | Trans is drained for removal anyway. | — |
| **Trans-side shifter cable bushings** (Acuity) | If not already done. | [02-Short-Shifter-and-Bushings/](../02-Short-Shifter-and-Bushings/) |
| **Engine/trans mounts** (Hybrid Racing 70A) | Trans mount has to come out anyway. | [08-Engine-Mounts/](../08-Engine-Mounts/) |

**I did the first five on my install.** Shifter bushings were already done on a previous session. I deferred the 70A mounts and regret it — pulling the trans mount with stock hardware installed is the same effort as pulling it to install the Hybrid Racing piece.

---

## While You're In There — Read This Section Twice

The entire point of this job is to not do this job twice. Trans-out labor is what's expensive. The parts you touch while it's out are cheap.

**Do now, every time, no arguments:**

1. **Clutch hydraulics (CMC + CSC + braided line).** This is the single biggest parallel job. At 170k the stock CMC/CSC is on borrowed time — it's a known 8th gen failure point. The Hybrid Racing HYB-CMC-01-20 is a complete drop-in kit and the CSC lives on the bellhousing. Doing this clutch-and-flywheel install without the hydraulics upgrade is leaving a trans-out job on the calendar for next year. **This doc and [07-Clutch-Hydraulics/](../07-Clutch-Hydraulics/) are meant to be read as a pair. I consider them one single job.**
2. **Rear main seal.** Pop old, press new, done. 15 minutes.
3. **Pilot bearing.** Slide-hammer puller or the grease-packing trick. Pre-lube the new one.
4. **Throwout bearing.** Verify the Exedy 08806 kit ships one; if not, OEM is $40.
5. **Fresh MTF-3.** 2.2 qt Honda MTF-3, no substitutes — aftermarket GL-4 makes the synchros hate you.

**Don't skip. Any of them. Ever.**

---

## Tools Required

**Critical:**

- **Flywheel holder tool.** K-Tuned or similar. Improvisable with a ratchet strap + bellhousing bolt but the real tool is $30.
- **Clutch alignment tool** (ships with Exedy 08806).
- **Transmission jack** or floor jack + wide wood cradle + helper.
- **Impact gun** (1/2"). Axle nuts are 181 ft-lb and 170k old.
- **Torque wrenches:** 1/2" (30-250 ft-lb) and 3/8" (10-80 ft-lb), both in-lb for small stuff.
- **14mm, 17mm, 19mm sockets** + wrenches, shallow and deep.
- **32mm axle nut socket.**
- **Pilot bearing puller** (or grease-packing method).
- **4-ton jack stands** on subframe pinch welds. Never under a jack alone.
- **2x new ARP-rated or OEM flywheel bolts** — flywheel bolts are one-time-use per Exedy.

**Also useful:** creeper, headlamp, drip pan, magnetic tray, Loctite 242 (blue), 2+ cans brake cleaner, sharpie.

---

## Parts List

| # | Item | Part Number | Source |
|---|------|-------------|--------|
| 1 | Exedy Stage 1 Organic Clutch Kit (disc + PP + TOB + alignment tool) | **08806** | shop.redline360.com |
| 2 | Exedy Lightweight Chromoly Flywheel | **HF02** | shop.redline360.com |
| 3 | OEM Rear Main Seal | 91214-RDA-A01 | Honda dealer |
| 4 | OEM Pilot Bearing | 91006-RWC-003 | Honda dealer |
| 5 | OEM Throwout Bearing (verify kit) | 22810-RWC-003 | Honda dealer |
| 6 | Honda MTF-3, 2.2 qt | 08798-9031 | Honda dealer |
| 7 | Loctite 242 (blue) | — | AutoZone |

**Paired install:** Hybrid Racing HYB-CMC-01-20 clutch hydraulics kit — see [07-Clutch-Hydraulics/](../07-Clutch-Hydraulics/).

---

## Step-by-Step

### Phase A: Disconnect and Lift (30-45 min)

1. Disconnect battery negative.
2. Loosen front lug nuts while car is on the ground.
3. Raise front, set on 4-ton jack stands on subframe pinch welds. Chock rear.
4. Remove both front wheels.
5. Remove engine bay splash shield.

### Phase B: Axle Removal (30-45 min)

6. Remove 32mm axle nuts, both sides. Impact gun.
7. Remove lower ball joint pinch bolts (these are stretch bolts — replace them).
8. Pop ball joints out of knuckles with pickle fork or separator.
9. Walk axle stubs out of hubs.
10. At the trans, pry axles out of the diff. Fluid drips — drip pan ready. Plug the trans holes with rag or caps.
11. Set axles aside.

### Phase C: Top-Side Disconnects (20 min)

12. Disconnect shifter cables from trans selectors (two cable ends, clips).
13. Disconnect reverse lockout switch, speed sensor, backup light switch, any other harness plugs.
14. Unbolt ground strap from bellhousing.
15. Remove starter: two wires + two mounting bolts.

### Phase D: Support Engine + Drop Trans Mount (15-20 min)

16. Support the engine from above (support bar) or from below (floor jack + wood block under pan). **The engine cannot drop when the trans mount comes out.**
17. Position trans jack under the transmission, snug up.
18. Unbolt trans mount from chassis and from trans bracket. Remove mount.

### Phase E: Unbolt Bellhousing (20-30 min)

19. Remove bellhousing bolts from under the car (6-7 of them, various lengths — **phone picture which length goes in which hole**). Some are buried up top; long extension from below.
20. Unbolt CSC line bracket / clutch fork cover.
21. Leave two bellhousing bolts finger-tight until you've confirmed nothing else is attached.

### Phase F: Lower the Trans (30-45 min)

22. Final walkaround: harness clips, ground straps, anything still bolted. **Anything.**
23. Remove last two bellhousing bolts.
24. Pull trans straight back off the input shaft dowels. **Do not let it hang on the input shaft.** If it won't release, wiggle side-to-side — it's hung on dowel pins, not the input shaft.
25. Lower the jack, walk the trans out from under.
26. Beer checkpoint.

### Phase G: Pressure Plate + Flywheel Off (20 min)

27. Install flywheel holder.
28. Unbolt pressure plate in a star pattern, a little at a time — the diaphragm spring is under tension and uneven loosening warps the cover. 6 bolts.
29. Pull PP off, catch falling disc.
30. **Inspect input shaft splines on the trans.** Sharp edges + light film of grease = good. Rounded or pitted = trans needs a second look before reinstall.
31. Unbolt flywheel. 8 bolts, star pattern, staged. **One-time-use per Exedy.**
32. Lift flywheel off (heavy).

### Phase H: Rear Main Seal + Pilot Bearing (30-45 min)

33. **Rear main seal:** pry old seal out carefully — do not gouge the aluminum housing or crank sealing surface. Plastic trim tool or seal puller.
34. Brake cleaner + lint-free rag.
35. Press new seal (91214-RDA-A01) in square and flush. A large socket matching the seal OD, tapped gently with a dead-blow, does the job.
36. **Pilot bearing:** slide-hammer puller, or pack the cavity behind the bearing with wheel bearing grease, insert a snug wooden dowel, hammer — hydraulic pressure ejects the bearing. Messy but works.
37. Brake cleaner in the bore.
38. Press new bearing in with a socket that contacts the outer race only (never the inner — you'll brinell it). Drive until it bottoms.
39. Dab of fresh high-temp grease on the inner race.

### Phase I: Flywheel Install (20 min)

40. Clean crank flange mating face with brake cleaner. No oil, no fingerprints, no old Loctite crumbs.
41. Place HF02 flywheel on the crank. **Note the dowel pin** — the flywheel only goes on one way. If it doesn't sit flat, the dowel is missed. Do not force.
42. Drop of Loctite 242 on each new flywheel bolt thread. Do not drown.
43. Thread all 8 by hand. Snug in star pattern.
44. Install flywheel holder.
45. Torque in 3 passes, star pattern: 30 ft-lb → 60 ft-lb → **87 ft-lb final** per [docs/torque-specs.md](../docs/torque-specs.md). Verify against Exedy instructions — some kits spec torque-to-yield (angle gauge on final pass).

### Phase J: Disc + Pressure Plate (15 min)

46. Identify which side of the disc faces the flywheel. Stamped marking ("FLYWHEEL SIDE" or similar). **Installing the disc backwards is the classic first-time mistake and means dropping the trans again.** Double-check.
47. Hold the disc against the flywheel, insert the Exedy alignment tool through the disc hub into the pilot bearing — centers the disc.
48. Place pressure plate over disc, aligning dowel pins with flywheel holes.
49. Thread all 6 PP bolts by hand.
50. Torque in 3 passes, star pattern: 8 ft-lb → 14 ft-lb → **19 ft-lb final**. **Do not over-torque** — these are small bolts and over-torquing warps the cover permanently.
51. Pull alignment tool. Disc should wiggle slightly between flywheel and PP.

### Phase K: Throwout Bearing + Fork (10 min)

52. Inspect clutch fork pivot ball — replace if sloppy.
53. Light dab of high-temp grease on pivot ball and TOB fingers. **Light.** Excess grease slings onto the disc and causes chatter forever.
54. Install new TOB on the fork or input shaft collar (kit-dependent — the 08806 ships with a sleeve-style TOB).
55. Clip fork retainer so TOB doesn't walk off during reinstall.

### Phase L: Trans Reinstall (45-60 min — reverse of removal)

56. **If doing the CMC/CSC upgrade, install the new CSC on the bellhousing now** — trivially easier with the trans out. See [07-Clutch-Hydraulics/](../07-Clutch-Hydraulics/).
57. Roll trans under car, raise to mating height.
58. Line up input shaft to disc hub **by eye** — the alignment tool work means the disc is centered, so the input shaft slides home with gentle pressure.
59. **Do not hammer the trans onto the engine.** If it won't mate, the input shaft is misaligned or dowel pins aren't seated — pull back and check.
60. Install all bellhousing bolts finger-tight, then torque to **47 ft-lb** cross-pattern.
61. Reinstall trans mount, torque to spec.
62. Remove engine support.

### Phase M: Reconnect Everything (30-45 min)

63. Reinstall starter (wires + torque).
64. Reconnect all harness plugs.
65. Reconnect shifter cables to trans selectors. Verify each clips in solidly.
66. Reinstall axles, trans-side first (push until circlip clicks into diff — tug to confirm). Reinstall hub-side, new lower ball joint pinch bolts to spec.
67. Torque axle nuts to **181 ft-lb.** Re-torque after 100 miles.
68. Refill trans with 2.2 qt fresh MTF-3. Fill to dripping out of the fill plug.
69. Splash shield back on.
70. Wheels on, lugs **80 ft-lb** star pattern.
71. Lower car.
72. **Bleed clutch hydraulics** — full procedure in [07-Clutch-Hydraulics/](../07-Clutch-Hydraulics/). Do not skip.
73. Reconnect battery.
74. Key on, do NOT start — verify clutch pedal feel. Pump 10-15 times, re-check. Mushy = bleed more.

---

## First Start / First Drive

75. Start car. Idle 2 minutes. Listen at the bellhousing — light TOB whir for the first few hours is normal; grinding or screeching is not.
76. Foot on brake, clutch in, shift through every gear: 1, 2, 3, 4, 5, 6, R. Each should engage cleanly.
77. Clutch out slowly in neutral — pedal returns smoothly.
78. Empty parking lot test drive. Engage at low RPM. **Engagement point mid-pedal, clean progressive bite.**

### First-drive checklist

- [ ] Engagement point mid-pedal, clean bite
- [ ] No chatter on launch
- [ ] No shudder at partial engagement
- [ ] No slip at light throttle in any gear
- [ ] Reverse engages without grinding
- [ ] No fluid dripping from bellhousing
- [ ] No MIL

**Do not WOT for 500 miles.** See bed-in below.

---

## Bed-In Procedure (Per Exedy)

An organic disc needs heat cycles to mate properly to the flywheel and PP surfaces. Skip bed-in and you glaze the disc — it'll slip or chatter forever.

**Exedy's spec for the 08806:**

- **First 500 miles: no WOT, no launches, no aggressive engagements.** Drive it like it's your grandmother's car.
- **Vary load.** Mix stop-and-go with highway. Multiple full heat cycles (warm up, many engagements, cool down) are better than one long highway cruise.
- **No holding the clutch at the engagement point.** Partial engagement burns the disc.
- **No slipping the clutch on hills.** Either fully engaged or handbrake.
- **After 500 miles:** gradually increase load. First short WOT at ~750 miles. Full-send after 1,000 miles.

I logged ~700 miles of mixed commuting before my first proper pull. No slip, no chatter, engagement still crisp. Bed-in worked.

---

## Common Mistakes

1. **Disc backwards.** Disc is asymmetric. Backwards = clutch won't release = drop the trans again. **Check the stamped side marking.**
2. **Missing the flywheel dowel pin.** If the flywheel doesn't sit dead flat, the dowel is missed. Forcing bolts cracks the flywheel or the crank flange.
3. **Forgetting to prime the pilot bearing.** No grease = dry chirp after 50 miles.
4. **Cross-threading flywheel or PP bolts.** Always hand-start every bolt. Ratchet only after all are finger-tight.
5. **Over-torquing the pressure plate.** 19 ft-lb final. Over-torque warps the cover and causes permanent chatter. Calibrated torque wrench, not feel.
6. **Skipping the alignment tool.** Eyeballing disc centering doesn't work — trans won't mate, or it will mate and the clutch won't release.
7. **Dropping the trans onto the input shaft during removal or install.** Bends input shaft, kills pilot bearing. Keep the trans supported at bellhousing height.
8. **Reusing flywheel bolts.** Torque-to-yield = one-time use. Reused can fail catastrophically.
9. **Skipping the bleed before first start.** Air in system = pedal to floor = stuck in gear = dangerous.
10. **Cleaning flywheel face with WD-40 or oil.** Brake cleaner only. Oily film = immediate slip.

---

## See Also / Cross-References

- [overview.md](overview.md) — why I chose the 08806 + HF02 combo, power headroom, daily-driver feel.
- **[../07-Clutch-Hydraulics/](../07-Clutch-Hydraulics/) — do this install at the same time. Single session. The CSC lives on the bellhousing and doing hydraulics separately means pulling the trans twice. Most important cross-reference in this document.**
- [../02-Short-Shifter-and-Bushings/](../02-Short-Shifter-and-Bushings/) — if trans-side bushings aren't already done, do them while the trans is accessible.
- [../08-Engine-Mounts/](../08-Engine-Mounts/) — trans mount comes out anyway; best opportunity for the Hybrid Racing 70A kit.
- [../docs/torque-specs.md](../docs/torque-specs.md) — every torque value used here, FSM-cross-referenced.
- [../CLAUDE.md](../CLAUDE.md) — overall build context.

---

*Last updated: 2026-04-20*
