# HANDOFF — Session Continuation Notes

**Session paused:** 2026-04-20
**Author:** Claude (Opus 4.7) collaborating with LxveAce
**Purpose:** This file is a self-contained brief for the next Claude session picking up this work. Read this first before touching anything.

---

## Who This Is For (Read This First)

You (next-session Claude) are continuing a large multi-part restructure and content-add pass on LxveAce's 2009 Civic SI (FG2 / K20Z3) build repo. The user approved multiple parallel research streams, issued folder-reorg instructions, and approved specific paths on 5 major decisions. All of that work has been committed to git. You are picking up mid-task. Don't re-litigate decisions that are already made — they're documented below.

**Build target:** Full bolt-on NA K20Z3, 220–240 WHP pump / 230–250 WHP E85.
**Rule that overrides everything:** engine longevity before power, always.
**Aesthetic theme:** purple engine bay.
**Owner mileage at start of session:** ~170,000.
**Current state:** front brakes installed 2026-04-20; otherwise mods in the "Installed" section of README are on the car.

---

## What Was Decided In This Session (Do Not Re-Litigate)

User explicitly approved each of these:

1. **Folder sort:** install order (per `docs/mod-order-and-maintenance.md`). Done.
2. **Purple calipers:** **Option A (caliper covers / paint NOW)** + **Option C (defer Wilwood big-brake kit to future phase)**. Rejected Option B (full Wilwood now) because it would throw away the 3-day-old R1 Concepts + Hawk HPS fronts.
3. **Head work:** aftermarket drop-in head (not maintenance refresh). User said "go all out" on head. Recommended + documented path is **4 Piston Pro 156v2 All Motor Package** ($2,740 assembled, RBC-compatible).
4. **Timing chain:** full maintenance now + upgrade options documented (defaulted to OEM maintenance — no billet tensioner needed for 240 WHP street).
5. **Built motor (pistons/rods/bearings/ARP/oil pump):** documented as a **future phase appendix**. Not a current purchase plan.

All four of the above have dedicated folders + overview.md files now.

User also wants, but **has not yet been delivered**:
6. **In-depth step-by-step install/maintenance guide for EVERY mod in the repo.** Partial — `13-Headers/install-guide.md` and `05-Timing-Chain-Maintenance/overview.md` (with phased step-by-step inside) exist. Still to write: dedicated `install-guide.md` for each of the remaining mod folders. See "Remaining Work" below.

---

## Folder Reorganization — What Changed

Every numbered folder was renamed to reflect install order. **Mapping (old → new):**

| Old | New |
|-----|-----|
| 01-Clutch | 03-Clutch-and-Flywheel |
| 02-Cold-Air-Intake | 01-Cold-Air-Intake |
| 03-Short-Shifter-and-Bushings | 02-Short-Shifter-and-Bushings |
| 04-Engine-Mounts | 08-Engine-Mounts |
| 05-Brakes | 04-Brakes |
| 06-Strut-Bar | 18-Strut-Bar |
| 07-Hondata-FlashPro | 10-Hondata-FlashPro |
| 08-Valved-Exhaust | 12-Valved-Exhaust |
| 09-Headers | 13-Headers |
| 10-Intake-Manifold | 14-Intake-Manifold |
| 11-Pulleys-and-Harmonic-Balancer | 15-Pulleys-and-Harmonic-Balancer |
| 12-Flex-Fuel-and-Fuel-System | 19-Flex-Fuel-and-Fuel-System |
| 13-Clutch-Hydraulics | 07-Clutch-Hydraulics |
| 14-Suspension | 17-Suspension |
| 15-Ignition-Refresh | 06-Ignition-Refresh |
| 16-Cooling-System | 09-Cooling-System |
| 17-Wideband-AFR | 11-Wideband-AFR |

**New folders added (4):**
- **05-Timing-Chain-Maintenance** — Phase 0 maintenance before any performance mods
- **16-Cylinder-Head** — aftermarket drop-in head plan (4P Pro 156v2)
- **20-Built-Motor-Bottom-End** — future phase appendix (pistons/rods/bearings/ARP/oil pump)
- **21-Purple-Cosmetics** — aesthetic layer

Final list (sorted):
```
01-Cold-Air-Intake       (installed)
02-Short-Shifter-and-Bushings  (installed)
03-Clutch-and-Flywheel   (installed)
04-Brakes                (fronts installed 2026-04-20, rears pending)
05-Timing-Chain-Maintenance  (NEW — Phase 0 maintenance)
06-Ignition-Refresh      (Phase 0.5)
07-Clutch-Hydraulics     (Phase 1A)
08-Engine-Mounts         (Phase 1B)
09-Cooling-System        (Phase 1F)
10-Hondata-FlashPro      (Phase 1E)
11-Wideband-AFR          (Phase 1G — tied to header install)
12-Valved-Exhaust        (Phase 2A)
13-Headers               (Phase 2B)
14-Intake-Manifold       (Phase 3)
15-Pulleys-and-Harmonic-Balancer  (Phase 4)
16-Cylinder-Head         (NEW — Phase 4.5)
17-Suspension            (Phase 5)
18-Strut-Bar             (Phase 5 — deferred with coilovers)
19-Flex-Fuel-and-Fuel-System  (Phase 6)
20-Built-Motor-Bottom-End  (NEW — Future / aspirational)
21-Purple-Cosmetics      (NEW — aesthetic, anytime)
docs/
```

**All cross-references were updated** (22 files) by a one-shot rewrite script (which was deleted after use).

---

## Files Created or Modified This Session

### New overview files (content from research agents integrated)
- `05-Timing-Chain-Maintenance/overview.md` — full parts list, step-by-step, torque specs, cost, symptoms dictionary
- `16-Cylinder-Head/overview.md` — 4P Pro 156v2 All Motor Package plan + hardware + install considerations + tune implications
- `20-Built-Motor-Bottom-End/overview.md` — future-phase reference (Wiseco pistons, BC625+ rods, ACL Race bearings, ARP 208-4701, Honda PRB-A01 oil pump)
- `21-Purple-Cosmetics/overview.md` — Acuity oil cap, K-Tuned dipstick, NST pulleys, Dress Up Bolts, Skunk2 hardware, powder-coat batch list
- `04-Brakes/purple-calipers.md` — G2 purple paint now + Wilwood BBK deferred plan
- `19-Flex-Fuel-and-Fuel-System/acuity-fuel-rail-and-flex-fuel-build.md` — complete flex fuel + Acuity rail 1913-PPL (satin purple) + EV14 550cc + DW300C + Continental sensor + FlashPro wiring + install procedure (authored by research agent directly)

### Modified files
- `09-Cooling-System/overview.md` — corrected thermostat P/N (19301-RAF-004), water pump P/N (19200-RBC-013), added purple cooling section (Samco purple hoses, Radium reservoir, Royal Purple Purple Ice)
- `README.md` — updated path references (older update — still has pre-reorg folder numbering in a few places; NEEDS FINAL PASS to add new folder rows)
- `CLAUDE.md` — path references updated
- `docs/mod-order-and-maintenance.md` — path references updated (**needs additional pass** to add Timing Chain, Cylinder Head, Built Motor, Purple Cosmetics phases explicitly)
- `docs/maintenance-parts-catalog.md` — `12-Flex-Fuel` → `19-Flex-Fuel-and-Fuel-System` reference fixed
- `generate-pdf.py` — FILE_ORDER list rewritten for new folder numbers (**needs additional pass** to add new folder `overview.md` entries)
- All other cross-reference updates across 22 files (Hondata reference docs, install guides, etc.)

### Previously committed from earlier session (2026-04-20)
- `10-Hondata-FlashPro/tune-profiles/performance-tune-1.md` — performance tune #1 profile doc + datalog analysis
- `10-Hondata-FlashPro/tune-profiles/fix-list-2026-04-20.md` — 5 cell-level corrections for the Sport tune
- `10-Hondata-FlashPro/tune-profiles/screenshots/*.png` — 10 annotated FlashPro tab screenshots
- `10-Hondata-FlashPro/tune-profiles/archive/*.fpcal` — archived tune files (performance-tune + stock)
- `10-Hondata-FlashPro/tune-profiles/datalogs/2026-04-20_pull-set-1/*.csv` — 8 datalog CSVs

---

## Research Agent Outputs Summary (All 7 Completed)

All 7 research agents returned in this session. Their findings were integrated into the overview files above. Key conclusions:

1. **Purple cosmetics (Agent 1)** — True purple off-the-shelf options: Acuity 1927-PPL oil cap ($80), K-Tuned DP2-K20-PRP dipstick ($72), Acuity ESCO-T6 1886-T6P shift knob ($92), Dress Up Bolts HON-027-TI kit ($125), Skunk2 649-05-0120-PPL valve cover hardware ($55), NST22015K-Purple alt+idler pulleys (~$180 — **SKIP the crank pulley, it conflicts with ATI Super Damper**). Total tier-1 "full purple" package: ~$966. Custom powder-coat batch for valve cover + strut bar + fluid caps: ~$330–565.

2. **Purple cooling (Agent 2)** — Only path to true purple silicone hoses is **Samco Sport custom color** ($280–340, 4–6 week lead). Radium 20-0270-00 reservoir with custom purple anodize (~$310, call Radium direct at 503-244-0990). Hybrid Racing HYB-TBC-00-10 stainless T-bolt clamps ($45 — no purple T-bolts from reputable brands). Honda Type 2 coolant + Royal Purple Purple Ice 01600 additive. **Do not powder-coat Koyorad core** — reduces cooling efficiency. Updated part numbers: thermostat 19301-RAF-004, water pump 19200-RBC-013.

3. **Acuity fuel rail + flex fuel (Agent 3)** — Acuity **1913-PPL** is factory satin purple, same price as other colors (~$199). Bosch EV14 550cc = **0280158117** (genuine Bosch), Hondata dead time ~1.2 ms. DW300C kit = **9-307-1008**. Continental **13577429** flex sensor — outputs 50-150 Hz, requires Innovate MTX-D converter (~$140) before reaching ECU pin A33. **⚠️ IM compatibility warning:** Skunk2 Ultra Street (307-05-0600) uses PRB/PRC pattern, requires water-bypass adapter + Skunk2 DBW TB adapter 309-05-0120 to run on K20Z3 RBC head. Complete build ~$2,174 parts + tune.

4. **Purple calipers (Agent 4)** — G2 **G2165** purple epoxy is the pick ($55–75, 980°F rating, one kit covers all 4 corners). Foliatec **FT-2179** Deep Violet ($50–80, 572°F) is a solid alt. MGP Caliper Covers don't stock purple; custom PPG match is $400-500 + 12 bizdays. Defer Wilwood BBK: front **140-11978** (FNSL 6R, ~$1,400–1,700, custom purple anodize ~+$250-400, fits stock 17" wheels). Rear **140-11979-R** (~$964). Target trigger: 260+ WHP or track day or 40-50k more miles.

5. **Timing chain maintenance (Agent 5)** — 13.5mm tensioner rod protrusion = go/no-go threshold. Core parts: chain **14401-PNA-004** ($75), tensioner **14510-PRB-A01** ($65), arm **14520-PNA-003** ($45), guide **14530-PNA-003** ($35), crank bolt **90017-RWC-A01** (one-time-use, $15), crank seal **91214-RZY-A01**. Use valve cover kit **12030-PNC-000** (includes plug tube seals). Key torques: valve cover **7.2 ft-lb**, timing cover **8.7 ft-lb**, VTC actuator **83 ft-lb** (no impact wrench), crank pulley **131 → loosen → 37 → +90°**. Require Lisle 37950 cam lock tool ($40). Total DIY parts ~$445 (chain job) / ~$725 with VTC actuator bundled.

6. **K20 drop-in head (Agent 6)** — K20Z3 is **RBC casting**, not PRB — critical confirm-before-buy check. Pick: **4 Piston Pro 156v2 All Motor Package $2,740** (Ferrea valves + Supertech springs + Ti retainers + locks assembled, NEWEN 5-angle valve job, 360 CFM, RBC-compatible). Required adders: Cometic **C4561-030** .030" MLS head gasket ($85), ARP **208-4701** head studs ($200, NOT 208-4303 which is B-series). Skunk2 Tuner Stage 2 cams + Skunk2 Pro adjustable cam gears ~$820. **Mandatory dyno retune after install ($500-800).** Bundle cooling + headers + IM + VTC + wideband during same teardown.

7. **Built motor bottom end (Agent 7)** — For future (not current) phase. Wiseco **K573M86AP** 86mm 11.6:1 ArmorGlide pistons ($760). BC **BC6044** ProH625+ H-beam rods ($934). ACL Race **4B1946H-STD** rod + **5M1959H-STD** main bearings. Honda **15100-PRB-A01** RSX Type S oil pump upgrade ($300). Reuse stock crank (micropolish + balance ~$500). ATI Super Damper **918477** (already owned from Phase 15). Total mid-range DIY ~$4,444–4,944. Turn-key 4P short block ~$4,500–5,500. **Stock block is fine up to 270 WHP NA pump, 400 WHP E85 boost** — don't build yet at current target.

---

## Git State At Time Of Handoff

This handoff file + all work above is being committed in a single commit at session pause time. The user will push to `origin/master` before launching the next session.

Previous commit (from earlier in this session): `577702b` — "Add cell-level fix list with annotated screenshots for Performance Tune 1" — pushed to origin.

---

## Remaining Work (Prioritized)

### P0 — Finish the reorg polish (small cleanup)
1. **Update README.md "Planned — Not Yet Purchased" table** — add rows for new folders: Timing Chain (05), Cylinder Head (16), Built Motor (20), Purple Cosmetics (21). Currently the table shows mods 5–17 but stops short of the new additions.
2. **Update `docs/mod-order-and-maintenance.md`** — add explicit phases for:
   - Timing Chain service in Phase 0 (alongside other maintenance)
   - Cylinder Head swap as Phase 4.5 (between pulleys and suspension)
   - Built Motor as Phase X / appendix
   - Purple Cosmetics as aesthetic layer (anytime)
3. **Update `generate-pdf.py` FILE_ORDER** — add the 4 new overview.md files + the fuel rail build doc:
   ```
   "05-Timing-Chain-Maintenance/overview.md",
   "16-Cylinder-Head/overview.md",
   "20-Built-Motor-Bottom-End/overview.md",
   "21-Purple-Cosmetics/overview.md",
   "04-Brakes/purple-calipers.md",
   "19-Flex-Fuel-and-Fuel-System/acuity-fuel-rail-and-flex-fuel-build.md",
   ```
4. **Regenerate PDFs** by running `python generate-pdf.py` from repo root. Current PDF is stale (pre-new-folder).

### P1 — User's explicit ask: step-by-step install/maintenance file for every mod
User's words: *"make a very in depth step by step installation/maintance/etc. file under each tab for each part of everything in the entire repo."*

**Current state — what already has an install guide:**
- `13-Headers/install-guide.md` (existed before this session)
- `05-Timing-Chain-Maintenance/overview.md` embeds a full step-by-step within the overview (has Phase A through Phase P walkthroughs)
- `19-Flex-Fuel-and-Fuel-System/acuity-fuel-rail-and-flex-fuel-build.md` embeds procedure for fuel system install

**Needed — create `install-guide.md` in each of these mod folders:**
- `01-Cold-Air-Intake/` — K&N Typhoon 69-1014TS install (already installed but doc for reference)
- `02-Short-Shifter-and-Bushings/` — Acuity 3-way + trans-side bushings (already installed, doc for reference)
- `03-Clutch-and-Flywheel/` — Exedy Stage 1 + LW flywheel install (already installed, doc for reference)
- `04-Brakes/install-guide.md` — Hawk HPS + R1 slotted rotors install + bed-in + rear install procedure + G2 purple paint application
- `06-Ignition-Refresh/install-guide.md` — plugs + coils + VTC actuator install
- `07-Clutch-Hydraulics/install-guide.md` — Hybrid Racing HYB-CMC-01-20 + RMS + throwout + pilot bearing
- `08-Engine-Mounts/install-guide.md` — Hybrid Racing 70A install
- `09-Cooling-System/install-guide.md` — Koyorad + thermostat + hoses + water pump + bleed procedure
- `10-Hondata-FlashPro/install-guide.md` — FlashPro registration + first flash procedure
- `11-Wideband-AFR/install-guide.md` — AEM X-Series 30-0300 bung weld + wiring + FlashPro analog input setup
- `12-Valved-Exhaust/install-guide.md` — QTP cutout + dump pipe + reducer fabrication + valve controller wiring
- `14-Intake-Manifold/install-guide.md` — Skunk2 Ultra Street + bored 66mm TB install + water-bypass adapter + DBW TB adapter
- `15-Pulleys-and-Harmonic-Balancer/install-guide.md` — ATI Super Damper + NST alt/idler install
- `16-Cylinder-Head/install-guide.md` — 4P Pro 156v2 head-off in-car procedure + ARP stud torque sequence + break-in
- `17-Suspension/install-guide.md` — BC Racing BR coilover + bushing + sway bar + alignment
- `18-Strut-Bar/install-guide.md` — Megan Racing install (after coilovers)
- `19-Flex-Fuel-and-Fuel-System/install-guide.md` — companion to existing acuity-fuel-rail doc; dedicated install procedure
- `20-Built-Motor-Bottom-End/install-guide.md` — short block assembly procedure (future-phase reference)
- `21-Purple-Cosmetics/install-guide.md` — powder coat batch handoff + swap procedures for caps/dipstick/oil cap

**Scope estimate:** 18 new install guides × ~1,500–2,500 words each = roughly 30,000–45,000 words of writing. This is the biggest remaining chunk. Each guide should follow a common template: Tools Required → Torque Specs Table → Step-by-Step (Prep, Install, Reassembly, First-Start) → Common Mistakes → Cross-References.

### P2 — Nice-to-have polish
- Update `docs/torque-specs.md` with ARP 208-4701 torque sequence, cam cap torque, timing chain torques, VTC actuator torque, crank pulley yield procedure
- Update `docs/maintenance-parts-catalog.md` with new OEM part numbers (14401-PNA-004, 14510-PRB-A01, 12030-PNC-000, 91214-RZY-A01, 19200-RBC-013, 19301-RAF-004)
- Add purple cosmetics costs to master budget in README

---

## Known Gotchas For Next Session

1. **ATI Super Damper conflicts with NST crank pulley.** The NST22015K-Purple kit includes a crank pulley, but the build plan uses ATI Super Damper as the crank pulley. Contact NST direct to order only the alt + idler pulleys; drop the crank piece. Documented in `21-Purple-Cosmetics/overview.md` and `09-Cooling-System/overview.md`.

2. **Skunk2 Ultra Street IM is PRB-pattern, not native to RBC (K20Z3) head.** Install requires water-bypass adapter + Skunk2 DBW TB adapter (PN 309-05-0120). Documented in `19-Flex-Fuel-and-Fuel-System/acuity-fuel-rail-and-flex-fuel-build.md` and needs to be added prominently to `14-Intake-Manifold/overview.md` if not already there.

3. **K20Z3 head is RBC casting.** 4Piston Pro 156v2 bare head is PRB-base; only the "All Motor Package" (assembled) is RBC-compatible per 4P's fitment list. Email Luke@team4piston.com to confirm before ordering.

4. **ARP 208-4303 is the WRONG part number for K20.** That's the B-series GSR kit. Correct K20 head stud kit is **ARP 208-4701**. Do not propagate 208-4303 anywhere.

5. **Honda thermostat 19301-RNA-305 is the R18 (non-Si Civic) part.** Correct for K20Z3 is **19301-RAF-004**. The old overview had this wrong; fixed.

6. **Honda water pump 19200-RAA-A01 is a different family.** Correct for K20Z3 Civic Si is **19200-RBC-013**. Fixed.

7. **Koyorad SK-C13 radiator cap fits Koyorad necks only, NOT OEM Honda radiator.** Keep a Mishimoto MMRC-13-SM in the parts bin for any emergency OEM-rad run.

8. **Don't powder-coat the Koyorad radiator core** — powder coat on fins reduces cooling efficiency. End-tank-only powder is OK (~$75–125).

9. **Engine Ice coolant (purple) is NOT chemistry-compatible with Honda Type 2.** Don't mix them. If going purple cosmetic, use Royal Purple Purple Ice additive + Honda Type 2 base.

10. **Git identity is not set at system level** on this machine. Use per-command `-c user.name="LxveAce" -c user.email="extrafadexd@gmail.com"` when committing. Do NOT modify global git config without user asking.

---

## How To Resume In The Next Session

When the user launches a fresh Claude session pointed at this repo:

1. **Read this HANDOFF.md first.** Everything is here.
2. **Check git status** to see the commit this work was in. Check the latest commit message for context.
3. **Ask the user to confirm priorities** — do they want you to start with P0 (reorg polish), P1 (write 18 install guides), or both? The install-guide write-up is the biggest remaining chunk; scope it carefully.
4. **Don't re-run the research.** The 7 agent outputs are already integrated into the overview files. Trust the research.
5. **Don't re-litigate the 5 decisions** — the user has explicitly approved them.
6. **Continue working in the same authorial voice** — first-person, reliability-first framing, terse tables for parts, real part numbers only (never fabricate).

---

## Authorial Conventions (Carry Forward)

- Voice: first-person owner ("I'm going with..."). Matches `09-Headers/overview.md`, `19-Flex-Fuel-and-Fuel-System/overview.md`, etc.
- Every doc references reliability-first rule at decision points.
- Every doc cross-references related mod folders in a dedicated Cross-References section.
- Every part number is verified via research or explicitly flagged as "confirm before ordering."
- Never emoji unless user asks.
- Never write marketing copy. Every recommendation includes a tradeoff.
- Cost tables: actual prices where known (tax+ship included), ranges where uncertain.
- Sources section at the bottom of each doc, linking to vendor pages + forum threads where findings were cross-checked.

---

*Last updated: 2026-04-20. This file may be deleted by the next session once its work is consumed and confirmed.*
