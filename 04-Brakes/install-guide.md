# Brake Install Guide — Hawk HPS + R1 Concepts Slotted + G2 Purple Calipers

**Status:** Fronts installed 2026-04-20. Rears + G2 purple caliper paint PENDING — planned as a combined weekend session so the paint and rear R&R share labor.

---

## Reality Check Before I Start

Brakes are the most-commonly-DIY'd job on any car, and that's exactly why it's easy to get complacent. **This is the mod with the highest safety stake on the whole build.** A caliper bracket bolt that wasn't torqued, or a rushed bed-in that crystallizes the Hawk HPS friction layer, costs me a rotor or an intersection.

**Time budget:**
- Fronts: 2-3 hours DIY for both sides (actual 2026-04-20 session: ~2.5 hours)
- Rears: 2-3 hours DIY for both sides — slightly slower because the rear pistons screw in
- Paint session (on top of rear install): add 1.5-2 hours of active work plus 24-hour air-cure before driving

**Difficulty:** Intermediate. Nothing here is rocket science, but it is unforgiving of skipped steps. No shortcuts. Rushed bed-in = warped rotors + crystallized pad surface = buy the set twice. Reliability-first: I would rather drive home on an unpainted caliper than an untorqued one.

---

## Prerequisites / Cross-References

### Things that need to be done FIRST or AT THE SAME TIME

| Do First / Also Do | Why |
|--------------------|-----|
| **New DOT 4 brake fluid flush** simultaneous with rear install | Fluid is overdue at 170k. Rotating the rear pistons pushes old fluid back up the lines — flushing at the end turns a contamination event into a maintenance win. Shares DOT 4 stock with [`../07-Clutch-Hydraulics/`](../07-Clutch-Hydraulics/). |
| **Torque wrench, calibrated** | Non-negotiable. Caliper bracket bolts are the fastener that turns a weekend mod into a crash. [`../docs/torque-specs.md`](../docs/torque-specs.md) has every value. |
| **Bed-in procedure** after all four corners are done | Non-negotiable. Hawk's bed-in is what makes HPS compound deposit correctly on the R1 rotor. Skip it and I get judder + a hot-spot pattern I can't polish out. |
| **Alignment re-check** after rear install | Any hub play or loose suspension found during rotor R&R means a check is prudent. See [`../17-Suspension/`](../17-Suspension/). |

### What this mod does NOT need

- No tuning impact. Pure mechanical change.
- No electrical. No sensors. No ECU concerns.
- No cross-impact on the rest of the build until the BBK question re-opens at 260+ WHP (see Defer Plan below).

---

## Tools Required

**Critical:**
- 1/2" drive torque wrench, 30-150 ft-lb range (caliper bracket and lugs)
- 3/8" drive torque wrench, 10-40 ft-lb range (slide pins)
- C-clamp OR dedicated caliper piston compression tool (**fronts only — rears need the cube tool, see below**)
- **Rear caliper piston rotation tool** — 4-way cube or dedicated rear caliper windback tool. FG2 rear pistons **screw in, not compress.** Trying to C-clamp them will tear the piston boot.
- 14mm socket (caliper slide pin bolts)
- 17mm socket (front caliper bracket bolts — double-check on my car, some FG2s use 19mm)
- 19mm socket (front caliper bracket bolts on most FG2 SI fronts; 12mm on rear brackets per torque-specs)
- Lug nut socket (21mm for OEM, check aftermarket)
- Breaker bar (18"+) for lugs that have been on a while
- Slide-pin silicone grease (NOT copper anti-seize — silicone is what the rubber boots tolerate)
- Pad abutment / shim grease (Permatex Ceramic Extreme or equivalent)
- Wire brush
- Brake cleaner (2-3 cans — I always underestimate this)
- Jack + 4-ton jack stands (never trust the jack alone)
- Wheel chocks
- Nitrile gloves
- Shop rags

**Useful:**
- Bungee cord or wire to hang the caliper off the strut (never hang a caliper by the flex hose)
- Rubber mallet or dead-blow hammer (for rotors that don't want to come off)
- Sharpie (mark left vs right pads so they go back in the same position if ever removed)
- Penetrating oil for the 7 ft-lb rotor retaining screw (tiny cross-head on the rotor face — strips easily)

**Paint session adds (from [`purple-calipers.md`](purple-calipers.md)):**
- G2 G2165 Purple High Temp Epoxy kit (3.5 oz base + 0.5 oz hardener, one kit does all 4 corners)
- Red Scotchbrite pads
- Painter's tape
- Cardboard scrap (rotor face masking)
- Extra nitrile gloves (G2 hardener is nasty)

---

## Parts List

| # | Item | Part # | Position | Source | Cost |
|---|------|--------|----------|--------|------|
| 1 | R1 Concepts Slotted Black Disc Brake Rotor Set (full set, F+R) | WCPN2-59004 | All 4 | R1 Concepts | $309.69 |
| 2 | Hawk HPS Street/Sport pads, front | HB361F.622 | Front | Hawk distributor | (part of $222.45) |
| 3 | Hawk HPS Street/Sport pads, rear | HB145F.570 | Rear | Hawk distributor | (part of $222.45) |
| 4 | G2 High Temp Epoxy Paint — Purple | G2165 | All 4 calipers | Amazon / G2USA | ~$55-75 |
| 5 | DOT 4 brake fluid (1 qt minimum for flush) | Motul RBF 600 or ATE Type 200 | Reservoir | Any | ~$18-25 |
| 6 | Fresh crush washers (banjo fittings, if disturbed) | OEM | Lines | Dealer | ~$5 |

See [`overview.md`](overview.md) for rotor + pad rationale and [`purple-calipers.md`](purple-calipers.md) for the G2 decision.

---

## Step-by-Step

This install runs in three phases. Phase A is already done and documented below so I have a reference for when I do the rears. Phases B and C happen together.

### Phase A: Front Install (COMPLETED 2026-04-20 — documented for reference)

Done passenger-side then driver-side. Recording here so the rear session has a known-good procedure to mirror.

1. **Park flat, chock opposite wheels** (rears, chocked diagonally).
2. **Loosen front lug nuts 1/2 turn** while wheel is still on the ground.
3. **Jack up front corner, set on jack stand** on the pinch weld. Never trust the jack alone.
4. **Remove wheel.**
5. **Retract the front caliper piston BEFORE touching the bracket.** Loosen the brake fluid reservoir cap. Place an old pad or block of wood between the piston and rotor, compress slowly with the C-clamp. Watch the reservoir rise — wipe any overflow immediately, brake fluid eats paint. (Skipping this step leaves pads jammed against the rotor and the caliper won't come off cleanly.)
6. **Remove the two caliper slide pin bolts** (14mm). Back them out fully.
7. **Slide the caliper body off the bracket.** Hang it on the coil spring with bungee cord or wire. **Never let it dangle from the brake hose** — tears internal reinforcement that fails later at speed.
8. **Remove the old pads from the bracket.** Note orientation (inner vs outer, wear indicator tang direction).
9. **Remove the two caliper bracket bolts** (19mm on the fronts). Breaker bar — torqued to 80 ft-lb for 170k miles.
10. **Remove the bracket.**
11. **Remove the old rotor.** Small cross-head retaining screw on the rotor face — usually seized; penetrant + hand impact driver. If rotor is stuck on the hub (it will be), **tap the rotor hat evenly around the circumference with a dead-blow.** Never strike the rotor face.
12. **Wire-brush the hub face** down to bare metal. Scale here causes rotor runout.
13. **Thin layer of anti-seize on the hub face only.** Not on the rotor face, not anywhere near the pads. Purely prevents future seizing.
14. **Install the new R1 Concepts WCPN2-59004 rotor.** Slots point in direction of wheel rotation at outer edge — R1 ships them marked "left" and "right." Thread the rotor retaining screw back in, torque **7 ft-lb** (anti-seize on threads — it's tiny, do not over-muscle).
15. **Reinstall caliper bracket. Torque 80 ft-lb** per [`../docs/torque-specs.md`](../docs/torque-specs.md).
16. **Install Hawk HPS HB361F.622 pads into the bracket.** Wear indicator tang on inboard pad, facing front of car. Shims come pre-attached — do not peel. Thin coat of pad slide grease on the abutment ears only, NEVER on the friction face.
17. **Slide the caliper body back over the new pads.** Should seat cleanly if piston is fully retracted. If it doesn't, retract more — forcing it bends the slide pins.
18. **Install caliper slide pin bolts** with fresh silicone grease on the pin shafts. **Torque 25 ft-lb.**
19. **Reinstall wheel.** Hand-thread all 5 lugs, lower until wheel bites the ground, torque star pattern to **80 ft-lb.**
20. **Repeat for driver side.**
21. **Pump the brake pedal 10-15 times with engine off** before driving. First presses will be soft as pistons travel out. Do not skip — first press in the driveway otherwise goes floor-to-firewall.
22. **Check brake fluid reservoir**, top up to MAX with DOT 4 if needed.

**Outcome 2026-04-20:** Firm pedal after 12 pumps. No leaks at flex hose or bracket. Low-speed drive confirmed no pull, no grinding. Bed-in deferred until rears are in.

### Phase B: Rear Install (PENDING — planned procedure)

Same basic job as fronts with two critical differences: parking brake integration, and the rear pistons **screw in, they do not compress.** Wrong tool = torn piston boot + destroyed parking brake mechanism.

1. **Parking brake OFF.** Piston can't rotate against e-brake engagement. Car in gear on jack stands.
2. **Chock front wheels.**
3. **Loosen rear lug nuts 1/2 turn** on the ground.
4. **Jack up rear corner, set on jack stand.**
5. **Remove wheel.**
6. **Check e-brake cable tension at the caliper arm.** If tight, loosen the e-brake adjuster at the handle to free slack. Note current adjustment position to restore later.
7. **Disconnect e-brake cable from caliper arm** (small clip retainer).
8. **Remove caliper slide pin bolts** (14mm).
9. **Slide caliper off bracket, hang on wire** — not on the hose, not on the e-brake cable.
10. **Rotate the rear piston INWARD using the cube tool.** The FG2 rear piston has two notches on its face; the parking brake mechanism screws it in/out. Turn clockwise (viewed from piston face) with gentle inward pressure until fully seated. **C-clamping a rear piston destroys the internal screw mechanism — #1 rear-brake mistake.**
11. **Remove old pads.**
12. **Remove rear caliper bracket bolts** (12mm). Breaker bar.
13. **Remove bracket.**
14. **Remove old rotor.** Retaining screw, tap hat evenly if seized.
15. **Wire-brush hub face. Anti-seize on hub face only.**
16. **Install new R1 Concepts rear rotor** (from WCPN2-59004 set). Same directional check. Retaining screw **7 ft-lb**, anti-seize on threads.
17. **Reinstall caliper bracket. Torque 54 ft-lb** per [`../docs/torque-specs.md`](../docs/torque-specs.md).
18. **Install Hawk HPS HB145F.570 rear pads.** Shims pre-attached. Slide grease on abutment ears only.
19. **Slide caliper body over pads — align piston face notches with the raised bumps on the inner pad backing plate.** If they don't line up, nudge piston with cube tool, retry. This keeps pad orientation correct as piston rotates under e-brake use.
20. **Torque slide pin bolts to 25 ft-lb.**
21. **Reconnect e-brake cable to caliper arm** (clip retainer).
22. **Reinstall wheel, torque lugs to 80 ft-lb star pattern.**
23. **Repeat for driver side.**
24. **Re-adjust e-brake** at the handle to restore original tension. Car should hold on moderate incline at 4-5 clicks.
25. **Pump the pedal 10-15 times** to extend rear pistons back out against new pads.
26. **Low-speed road test (5 mph parking lot crawl) BEFORE bedding in.** Apply parking brake — does it hold? Pull firmly — does it grab evenly without pulling? If e-brake doesn't hold, diagnose before higher-speed driving; usually means piston didn't fully seat back out or cable isn't reconnected. Do NOT bed in until e-brake confirms good.

### Phase C: Purple Caliper Paint — G2 G2165 (during rear install)

Fronts aren't painted yet, so this session paints **all four calipers at once.** The rears are already exposed from Phase B. Fronts get pulled a second time — extra labor, but the alternative is mismatched cure or a third paint session.

Procedure integrates G2 instructions from [`purple-calipers.md`](purple-calipers.md). One corner at a time. Car anchored on the other three jack stands.

1. **After Phase B is reassembled and confirmed (through step 26)**, come back and paint.
2. **Per corner: remove wheel, remove caliper fully** (slide pins out, lifted off bracket). **Support on wire.** No weight on the flex hose.
3. **Wire-brush loose rust** on visible caliper faces. Not worrying about what's hidden behind the caliper.
4. **Scuff all paintable surfaces with red Scotchbrite.** Kill the factory gloss so the epoxy has a key to grip.
5. **Brake cleaner — spray, drip, spray again.** Spotless. No oil, no fingerprints, no brake dust. Highest-leverage step for paint durability. Keep cleaner off the pad friction faces.
6. **Mask everything not going purple:**
   - Rotor face (cardboard disc between pad and rotor, or tape the edge)
   - Brake pads and backing plates
   - Brake flex hose
   - Bleeder screw (keep paintable-free for future flushes)
   - Slide pin boots (heat-sensitive rubber — do not paint)
   - Dust shield (optional)
7. **Mix G2 kit per instructions.** Hardener bottle into the paint bottle, cap, shake 2 minutes. Pot life ~2 hours once mixed.
8. **Apply 2-3 thin coats with ~30 minutes flash between coats.** Thin is the word — thick coats run and pool. Thin coats self-level and cure harder.
9. **No drips on rotor surface.** If it happens, wipe immediately with brake cleaner on a rag.
10. **24-hour air cure before driving.** G2 is a two-part epoxy that cross-links at room temp over 24 hours, then finishes curing under brake heat.
11. **During air cure, reinstall caliper** (slide pins torqued 25 ft-lb — paint is on the body, not pin bores, no torque impact). Wheel on with lugs finger-tight so the corner is safe overnight.
12. **Next day: torque lugs to 80 ft-lb** before driving.
13. **Heat-cure happens during bed-in.** Intentional: Hawk bed-in cycles calipers from ambient through ~500°F repeatedly, which is exactly how G2 epoxy finishes its full cross-link. G2165 is rated to 980°F — zero risk of bed-in damaging the paint. Natural cure cycle, which is why I paint the weekend of the install rather than a separate day.

**On doing fronts retroactively later:** considered and rejected. (a) Front pads are already bedded — re-pulling fronts breaks the seated pad-to-rotor transfer, wasteful. (b) Separate paint day = separate full mask-and-prep cycle. (c) Rears would cure before fronts, mismatch visible until fronts caught up. All four together is the right call.

---

## Hawk HPS Bed-In Procedure (from Hawk's published spec)

Do not skip. Do not abbreviate. Rushed bed-in = crystallized pad surface (glazed, loss of bite) + uneven pad deposit on the rotor (braking vibration I can't polish out — buy rotors again).

Find an empty stretch of road where I can do this without stopping completely at either end.

1. **6-10 moderate stops from 40 mph down to 5 mph.** Firm but not panic-brake. Do not come to a full stop — roll through and accelerate back to 40. Heats pads into operating range and deposits an even friction layer without letting the pad sit stationary on a hot rotor (which imprints).
2. **Cool down: drive 5-10 min at steady cruise** with minimal brake use. Airflow sheds the heat.
3. **2-3 harder stops from 60 mph down to 10 mph.** Closer to ABS-threshold firm, but not triggering ABS. Do not fully stop. Roll through, accelerate again.
4. **Drive 10 minutes at cruise to cool fully.** Do NOT park on hot pads — that's exactly how a pad shape gets imprinted into the rotor.
5. **Normal driving from here.** Full performance available after ~200 miles of mixed driving as the transfer layer matures.

**If I feel pulsing or vibration during bed-in: stop, cool completely, resume gently.** First sign of uneven deposit — continuing to hammer makes it worse.

---

## First Drive Checklist

After pump-up pedal test and bed-in, on the first real drive:

- **No pull** to either side under normal braking
- **No pedal fade** over repeated stops — pedal height and firmness consistent
- **No grinding, scraping, or rhythmic ticking** (slotted rotors will make a faint cold hiss — that's normal, not grinding)
- **No burning smell persisting past 10 minutes** (slight smell during bed-in is expected; persistent = something is dragging)
- **Even pad deposit on rotor face when cool** — uniform dark transfer. Blue patches = overheated spot; bare silver rings = uneven deposit, may need to redo bed-in
- **E-brake holds on moderate incline at 4-6 clicks** (rears)

If any fail, diagnose before highway-speed driving.

---

## Common Mistakes (the ones I'm specifically avoiding)

1. **Compressing rear pistons with a C-clamp instead of rotating with the cube tool.** Destroys the parking brake screw mechanism — replacement caliper territory.
2. **Forgetting to retract the piston before removing the bracket.** Old pads stay jammed against the rotor; swinging the caliper off rips the slide pin boots.
3. **Greasing the pad friction face.** Contaminated pads go in the trash. Grease on abutment ears and slide pins only.
4. **Not torquing lugs in star pattern.** Warps the rotor over the next 200 miles as hub face stress settles unevenly. Star pattern, 80 ft-lb final, every time.
5. **Rushing or skipping bed-in.** Glazed pads + uneven deposit = buying the set again in 5,000 miles. 20 minutes is cheap insurance on the whole mod.
6. **Hanging the caliper from the brake hose.** Invisible internal damage surfaces later as a hose failure at speed. Always wire or bungee.
7. **Painting before cleaning properly.** G2 won't bond to factory gloss + brake dust + 170k of road grime. Prep is 70% of a durable paint job.
8. **Torquing lugs with wheel hanging free.** Always bring wheel to the ground (or just barely loaded) so the hub isn't spinning against the wrench.

---

## Defer Plan — Big Brake Kit

Per [`purple-calipers.md`](purple-calipers.md), the Wilwood FNSL 6R front (140-11978) + D154 rear (140-11979-R) BBK is **deferred, not cancelled.** Trigger points to revisit:

- Power crosses ~260 WHP (post-FBO + E85 — see [`../13-Headers/`](../13-Headers/), [`../14-Intake-Manifold/`](../14-Intake-Manifold/), [`../19-Flex-Fuel-and-Fuel-System/`](../19-Flex-Fuel-and-Fuel-System/))
- 40-50k miles from now when Hawk HPS + R1 Concepts wear out
- First track day where HPS shows fade (IR-thermometer the rotor; upgrade pad compound first before BBK)
- Move to 18" wheels

The G2 purple paint is intentionally low-investment (~$95) to minimize sunk cost when the BBK happens. Custom purple anodize on the Wilwoods is the endgame; this is the interim that looks intentional without pre-committing $3,000. Throwaway if BBK lands Year 2-4: ~$380-430. Known number, accepted.

---

## See Also / Cross-References

- [`overview.md`](overview.md) — parts selected, rationale for Hawk HPS + R1 Concepts over OEM refresh
- [`purple-calipers.md`](purple-calipers.md) — full G2 G2165 research, Wilwood BBK deferral plan, MGP cover rejection
- [`../docs/torque-specs.md`](../docs/torque-specs.md) — caliper bracket (F: 80 ft-lb, R: 54 ft-lb), slide pins (25 ft-lb), rotor screw (7 ft-lb), lug nuts (80 ft-lb), all cross-checked against Honda FSM
- [`../07-Clutch-Hydraulics/`](../07-Clutch-Hydraulics/) — DOT 4 flush shares fluid stock with the clutch hydraulic refresh, plan them together
- [`../17-Suspension/`](../17-Suspension/) — alignment re-check after brake work is prudent, and the coilover + camber arm install is the right session to verify hub health at the same time
- [`../21-Purple-Cosmetics/overview.md`](../21-Purple-Cosmetics/overview.md) — the purple calipers are the cornerstone of the overall purple cosmetic theme

---

*Last updated: 2026-04-20*
