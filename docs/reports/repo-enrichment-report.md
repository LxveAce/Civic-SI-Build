# Repo Enrichment Report — 2026-04-18

> Report on the first pass of work on this repo: cloning, reading everything, researching gaps, adding missing content, and reconciling inconsistencies. Written so I (or anyone else reading this later) can understand what changed and why.

**Date of work:** 2026-04-18
**Starting state:** 26 markdown files, 2 PDFs, 1 Python generator, 1 .gitignore
**Ending state (same session):** 33 markdown files, 2 PDFs regenerated (124 + 10 pages)

---

## What I Asked For

Two things:

1. Clone the entire GitHub repo to my desktop in a folder matching the repo name, include and update PDFs as needed, read every file.
2. Do independent research across the build and let me know if there's a better plan, method, or parts, given my goals, tasks, and finances. Fill in all the missing parts that someone would normally get. Write everything as if I wrote it so I can re-upload and edit.

Target: a comprehensive, first-person, self-consistent build log ready for re-push.

---

## What Got Done

### 1. Cloned the Repo

- Location: `C:\Users\extra\OneDrive\Desktop\Civic-SI-Build\`
- Full git history preserved
- 26 markdown files, 2 PDFs, `generate-pdf.py`, `.gitignore`, `README.md`, `CLAUDE.md`
- Confirmed `generate-pdf.py` builds the two PDFs from the markdown via `fpdf2` — meaning any content change needs the PDFs regenerated to stay in sync.

### 2. Read Every File

All 26 original markdown files read end-to-end. Key conventions noted:

- Each mod gets its own folder: `overview.md` / `brainstorm.md` / `purchasing.md` / `install-guide.md` (any subset).
- First-person voice throughout ("I", "my", "I'm going with", "I'll admit").
- Honest trade-off discussions with "Why I ruled X out" sections.
- Actual-paid prices (tax, shipping, insurance all included).
- Cross-references and links between related mods.

### 3. Dispatched Three Parallel Research Agents

- **Parts alternatives + pricing audit.** Came back identifying gaps (exhaust manifold gasket, header studs, flex fuel plumbing adapters, front camber bolts, Motive bleeder, correct oil filter P/N, valve cover gasket, etc.) and flagged injector/pump inconsistencies (ID1050x is oversized, DW200 is marginal for E85).
- **Missing mod categories audit.** Identified entire categories I hadn't documented: ignition refresh, cooling system, wideband AFR gauge, LSD (optional), LED headlights (QoL), tools/consumables.
- **Reliability + maintenance gaps for a 170k K20Z3.** Flagged the big one: **VTC actuator 14310-RBC-003 (revised part)** — the universal cold-start rattle fix. Also rear main seal during clutch job, radiator plastic end tank, alternator wear, valve cover gasket, fuel filter before first E85 tank.

### 4. New Mod Folders Added (3)

| Folder | Why |
|--------|-----|
| **`15-Ignition-Refresh/`** | Plugs + OEM Honda coils (30520-RWC-A01) + **VTC actuator 14310-RBC-003 (revised)**. Must happen before any dyno tune. Critical for a 170k-mile K20Z3. |
| **`16-Cooling-System/`** | Koyorad HH060063 aluminum radiator + OEM thermostat/hoses/water pump. Plastic end tank failure insurance + E85 heat headroom. Must precede headers + E85 tune. |
| **`17-Wideband-AFR/`** | AEM X-Series 30-0300 wideband UEGO. Required before any dyno tune. Bung welds into Skunk2 Alpha collector during header install. |

### 5. New `docs/` Reference Files (3)

| File | Purpose |
|------|---------|
| **`docs/torque-specs.md`** | K20Z3/FG2 torque reference for every fastener I'll touch. No more late-night forum hunts. |
| **`docs/maintenance-parts-catalog.md`** | OE + aftermarket part numbers in one place, organized by system (engine, cooling, fuel, drivetrain, suspension, exhaust). |
| **`docs/baseline-logs.md`** | A/B datalog protocol: standard log set I run before and after every mod milestone so I can see what actually moved the needle. |

### 6. New Tuning Doc — The Reliability-First Rule Captured

**`07-Hondata-FlashPro/tuning-workflow-and-maps.md`** — Daily/Sport map definitions, reliability-first ceilings (knock count 0, pump gas WOT AFR ≥ 12.0, E85 lambda ≥ 0.82, rev limiter +200 max, injector duty ≤ 85% sustained), per-mod tune-required matrix, CSV export workflow for working with Claude on tune analysis.

This doc captured the rule I stated explicitly during the session: engine life and reliability come before power, every time.

### 7. New Install Guide

**`09-Headers/install-guide.md`** — Full Skunk2 Alpha + Berk HFC procedure with the 3-5 day PB Blaster schedule, DIY-vs-shop decision logic, stud recovery paths for broken studs. Picked headers specifically because it's the scariest job on the build (seized studs at 170k).

### 8. Significant Edits to Existing Files

| File | Change |
|------|--------|
| `README.md` | Added new folders to tables, added reliability-first callout, added "Build Principles" section, fixed flex fuel part inconsistency (DW300C + EV14 550cc, not DW200 + ID1050x) |
| `CLAUDE.md` | Updated AI warnings, added reliability-first rule, added "New Folders and Docs" section, added "Key Parts Decision Updates" table showing what I changed and why |
| `06-Strut-Bar/overview.md` | Rewrote from "blocked — diagnose" to "deferred until coilovers." BC Racing BR pillow-ball camber plates change strut-top geometry, so any diagnosis now is wasted effort. Clean example of cross-mod reasoning. |
| `12-Flex-Fuel-and-Fuel-System/overview.md` | Reconciled the BOM inconsistency: **Bosch EV14 550cc** (not ID1050x, which is 3.4× oversized and hurts idle) and **DW300C** (not DW200, too marginal on E85 headroom). Added decision blocks with reasoning. |
| `13-Clutch-Hydraulics/overview.md` | Added "same-session free labor" items: rear main seal (91214-RDA-A01), throwout bearing, pilot bearing, MTF refresh. Added Motive power bleeder and clutch pedal bushing. |
| `docs/mod-order-and-maintenance.md` | Added Phase 0.5 (ignition refresh) and extended Phase 1 with cooling system + wideband AFR + updated strut bar status to deferred. Added VTC actuator + valve cover gasket + oil filter housing gasket to Phase 0 maintenance table. |
| `generate-pdf.py` | Updated FILE_ORDER to include all new files in correct sequence. |

### 9. PDFs Regenerated

- **`2009-Civic-SI-Build-Guide.pdf`** — 124 pages (was ~75). Contains every mod doc in reading order.
- **`2009-Civic-SI-Mod-Order.pdf`** — 10 pages. Focused view on the build order + maintenance plan.

Both generated via `python generate-pdf.py` — the pipeline I'll keep using every time markdown content changes.

---

## Key Parts Decision Changes Made

Cross-referenced original content against research findings, made the following specific changes where the existing doc had an inconsistency or could be tightened:

| Item | Previous | Now | Reason |
|------|----------|-----|--------|
| Flex fuel injectors | ID1050x (listed in BOM) | **Bosch EV14 550cc** | ID1050x is 3.4× what's needed for 250 WHP target; hurts idle and cold start drivability |
| Flex fuel pump | Wavered between DW200 and DW300C | **DW300C (340 LPH)** | DW200 marginal on E85 headroom; reliability-first rule says headroom wins |
| Strut bar status | "Blocked — need to diagnose" | **"Deferred — don't diagnose until coilovers"** | BC Racing BR camber plates change the strut-top geometry; any diagnosis now is wasted effort |
| VTC actuator | Not listed | **OEM 14310-RBC-003 (revised)** | Universal 170k K20Z3 fix for cold-start rattle. Must precede tuning. |
| Radiator | Stock OEM replacement if anything | **Koyorad HH060063 (all-aluminum)** | Known plastic-end-tank failure at 170k + E85 heat headroom |

---

## What I Deliberately Did NOT Do

To avoid diluting repo quality with filler content:

- Did NOT create `purchasing.md` and `brainstorm.md` files for every single mod. Most overview files already contain that content; duplication is churn.
- Did NOT create install guides for every mod. Only wrote the scariest one (headers). Others have enough info in the overview files.
- Did NOT add a Tools/Consumables mod folder. Could be valuable later, not urgent now.
- Did NOT add LSD or LED lighting as separate mod folders. These are legitimate QoL items but not aligned with the current build scope.
- Did NOT add aero, seat, or harness folders. Build is daily-driven with sport-mode duality, not a track car.

---

## Memory Saved Across Sessions

Saved to Claude's persistent memory so future sessions carry context:

- **User profile (LxveAce):** mechanically capable DIYer, plans to shop out scariest jobs (headers, suspension bushings), comfortable with mid-complexity work.
- **Project constraints:** 170k K20Z3, FBO targeting 220-240 WHP pump / 230-250 WHP E85, daily-drivable with sport-mode toggle.
- **Invariants:** Never lean WOT fuel without dyno + wideband, never advance timing without knock monitoring, never recommend Raspberry Pi for FlashProManager, reliability > power always.
- **Reference:** Repo lives at `C:\Users\extra\OneDrive\Desktop\Civic-SI-Build\` and mirrors to `github.com/LxveAce/Civic-SI-Build`.

---

## Final Repo State (End of 2026-04-18)

- **33 markdown files** (was 26)
- **3 new mod folders** (15, 16, 17)
- **3 new docs files** (torque-specs, maintenance-parts-catalog, baseline-logs)
- **2 new `07-Hondata-FlashPro/` files** (tuning-workflow-and-maps, plus the headers install guide I put into `09-Headers/`)
- **124-page Build Guide PDF** (was ~75 pages)
- **10-page Mod Order PDF**
- README + CLAUDE updated to reflect everything
- Ready for git push

---

## Loose Ends I Flagged for Later

- Verify current prices on parts I called out (agents couldn't hit live vendor APIs — this was noted explicitly in research).
- Baseline datalog from current state (stock tune + K&N intake) when FlashPro gets its first flash.
- Revisit strut bar fitment once coilovers are installed.
- Confirm Bosch EV14 550cc exact P/N and whether USCAR-to-Honda clip adapters ship with the injectors or need to be sourced separately.

---

*Report written: 2026-04-18*
*Report file added to repo: 2026-04-19*
