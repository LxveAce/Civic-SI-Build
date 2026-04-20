# Hondata FlashPro Deep Dive Report — 2026-04-19

> Report on the second pass of work on this repo: deep research and documentation buildout for the entire Hondata FlashPro realm. Captures what I asked for, what was produced, the research limitations encountered, and the final state of the `07-Hondata-FlashPro/` folder.

**Date of work:** 2026-04-19
**Starting state:** 33 markdown files, 124-page Build Guide PDF
**Ending state:** 34 markdown files (one of the six new Hondata files was added as part of this — others added to existing folder), 169-page Build Guide PDF

---

## What I Asked For

Two things:

1. Go as in-depth as possible on the Hondata/FlashPro/K20Z3 tuning realm.
2. Look up stuff from all edges of the internet — all the 8th gen forums that exist, everything.

The intent was to build out the `07-Hondata-FlashPro/` folder into a genuine professional-grade reference, not just a basic overview. The user (me) has the original FlashPro (not FlashPro 2) and has never flashed anything yet — novice-to-FlashPro with a 170k-mile K20Z3 that I care about preserving.

---

## What Got Done

### 1. Dispatched Five Parallel Research Agents

Each agent was given a specific focused prompt with WebSearch and WebFetch expected to be available:

| Agent | Topic |
|-------|-------|
| 1 | FlashPro hardware + FlashProManager software deep dive |
| 2 | K20Z3 tuning tables + Hondata community base maps |
| 3 | Flex fuel on 8th gen SI via Hondata — exact wiring + calibration |
| 4 | LattePanda + FlashPro automation — APIs, auto-logging, scripting |
| 5 | 8thcivic forums + tuner directory + dyno reputation |

### 2. Research Limitation Encountered

**Three of the five agents reported that WebSearch and WebFetch were denied by their sandbox permissions.** They correctly refused to fabricate URLs, pin numbers, or forum citations rather than generate unverifiable content — the right call for a build where engineering accuracy matters.

**Two agents produced substantial output from their January 2026 training knowledge with explicit uncertainty markers** (`UNVERIFIED` / `VERIFY` flags on every specific claim they weren't fully confident about):

- Agent 1: FlashPro hardware + software — produced the deepest usable content
- Agent 5: Tuner directory — produced regional shop listings with clear "verify before booking" caveats

The practical implication: the documents I wrote for this deep dive are based on my accumulated K-series/FlashPro training knowledge plus the two agents' output, with every specific claim flagged `[VERIFY]` where I want confirmation before acting. This is honest depth, not fabricated citations.

### 3. New Documentation Written (6 files in `07-Hondata-FlashPro/`)

| File | Purpose | Approx PDF pages |
|------|---------|------------------|
| **`hardware-software-deep-reference.md`** | Full FlashPro hardware inventory (LEDs, buttons, connector, firmware), FlashProManager software architecture, `.fpdl` / `.fpc` file format notes, analog inputs, what's possible vs impossible, ownership housekeeping (re-registration fee, counterfeits) | ~6 |
| **`calibrator-tables-reference.md`** | Every tunable table category — fuel (low-cam, high-cam, flex fuel E85 endpoint), ignition, VTEC, VTC cam phase, idle, rev limits, launch control, torque management, fan tables, sensor settings, DTCs. Safe ranges for my 170k NA K20Z3. | ~5 |
| **`datalog-analysis-guide.md`** | How to read a `.fpdl`/CSV log, analysis order (knock count → fuel trims → WOT AFR → ignition → VTC → injector duty → thermal → electrical → flex fuel), common patterns and what they mean, red-flag quick checklist | ~5 |
| **`advanced-features.md`** | Launch control, flat-foot shifting, per-gear rev limits, torque management disable, shift light/indicator, rev hang reduction, gear detection calibration, speed limiter removal, A/C WOT cut, fan tables, CEL defeat flags. Daily/Sport settings matrix. | ~6 |
| **`troubleshooting-and-faq.md`** | Connection/software issues (FTDI driver gremlins), every common K20Z3 DTC code + what it means + when to fix vs tune out, tuning/datalog issues, hardware issues, calibration issues, emergency protocols, FAQ covering Googled-more-than-once questions | ~5 |
| **`tuner-directory.md`** | Selection criteria (non-negotiable, strongly preferred, red flags), regional shop breakdown (West Coast, Rocky Mountain/Southwest, Midwest, Southeast, Northeast, Remote-only), typical pricing for my three sessions, dyno type expectations, my three-session plan, vetting questions to ask any shop | ~5 |

### 4. Existing Files Updated

- `generate-pdf.py` — added all 6 new files to `FILE_ORDER` in correct sequence (right after the existing FlashPro overview, before the valved exhaust section)
- PDFs regenerated via `python generate-pdf.py`

### 5. Memory Updated

Saved to Claude's persistent project memory for future sessions:

- Specific FlashPro original hardware details (USB Mini-B, 2 analog inputs, no Bluetooth, no CLI, no public API)
- Flex fuel sensor wiring open question (analog 2 direct vs rear O2 signal pin — load-bearing, must be verified before wiring)
- Injector duty ceiling (85% sustained), AFR floors (12.0 pump / lambda 0.82 E85), rev limit cap (+200 RPM on stock internals)
- AI tuning workflow reality: Claude cannot flash ECU directly; works from pasted CSV datalogs, proposes specific table cell edits, user applies in FPM manually

---

## Key Technical Findings Captured in the Docs

### On the Original FlashPro vs FlashPro 2

- Original FlashPro (mine) has everything I need for a K20Z3 build. No features required that only FlashPro 2 provides.
- FlashPro 2 adds Bluetooth (mobile app), more analog inputs, different USB connector. Not worth a $700 upgrade for my use case.
- **Original FlashPro cannot switch calibrations on-unit** — every daily↔sport switch requires a PC flash (~20-45 seconds). This is why the LattePanda build makes sense for me: in-car PC permanently connected = one-tap calibration switching via a Python script.

### On Integration Possibilities (the LattePanda Automation Path)

- **Hondata has no public API or documented CLI.** No SDK, no REST, no IPC.
- `.fpdl` datalog files are proprietary binary. **CSV export from FPM is the only machine-readable path.**
- Automation options, best to worst:
  - **Best:** File-system watching — Python script monitors FPM's datalog folder, triggers something when a new file appears
  - **Workable:** UI automation (pywinauto, AutoHotkey) driving FPM's Export → CSV dialog
  - **Not possible:** Direct `.fpdl` parsing in Python
- **Claude cannot flash the ECU.** Workflow is: drive → export CSV → paste to Claude → Claude proposes specific cell edits → I apply in FPM manually → flash → verify.

### On Flex Fuel Implementation

- The **#1 open technical question** in my build: does the original FlashPro's analog 2 input read the GM flex fuel sensor's frequency output natively, or does wiring need to go to the ECU's rear O2 signal pin instead?
- Both paths are claimed in forum sources; they conflict; neither was verifiable without web access during this session.
- **Action item before flex fuel hardware purchase:** email Hondata support OR confirm with my chosen tuner OR find the current Hondata flex fuel setup KB article.
- Once the wiring path is confirmed, everything else (sensor part number, injector sizing, pump sizing, calibration approach) is well-documented in `12-Flex-Fuel-and-Fuel-System/overview.md` already.

### On Tuner Selection

- **BrenTuning** in Massachusetts is the community default for remote FlashPro tuning. Strong recommendation for Tunes #1 and #2 on my plan. Workflow: email datalogs + car info → receive `.fpc` → flash → log → iterate.
- **Church Automotive Testing** (Wilmington, CA) or **4Piston Racing** (Danville, IN) or **HARDmotion** (Atlanta, GA) are top picks for in-shop work on Tune #3 (flex fuel, worth traveling for eyes-on-the-car).
- Total 3-session tuning budget: $1,300-1,800.
- Separate sessions > combined package — cleaner attribution of gains per hardware change.

### On Safe Tuning Envelopes for My 170k K20Z3

Captured across `calibrator-tables-reference.md` and `tuning-workflow-and-maps.md`:

| Parameter | Safe Ceiling |
|-----------|-------------|
| Knock count at WOT | **0** (zero, always, no exceptions) |
| Pump gas WOT AFR | **≥ 12.0** (never leaner) |
| E85 WOT lambda | **≥ 0.82** (never leaner) |
| Injector duty cycle | **≤ 85% sustained** |
| Fuel pressure at WOT | Within 2 PSI of base spec |
| Rev limiter | **+200 RPM over stock max (8400 total)** |
| VTEC engagement | **≥ 4500 RPM** (never lower) |
| ECT sustained | **≤ 210°F under WOT** |

---

## Uncertainty Flags — What I Still Need to Verify

All documents include `[VERIFY]` markers on specific claims where I want live confirmation. The most important ones:

1. **Flex fuel wiring path on original FlashPro** (analog 2 direct vs rear O2 ECU pin) — load-bearing for Phase 6.
2. **Exact LED behavior on my specific FlashPro unit** (check box quick-start card).
3. **Current Hondata ECU re-registration fee** (last known $200 — verify current at hondata.com/support).
4. **Whether FPM has a documented CLI** for automated CSV export (determines LattePanda auto-export feasibility).
5. **Specific PRB ECU sub-revision idiosyncrasies** (if any — I suspect none but haven't confirmed).
6. **Current shop availability and pricing** for every tuner listed in `tuner-directory.md`.
7. **Exact per-gear rev limit parameter location** in current FPM (menu path).
8. **Whether `.fpc` export produces a diffable text report** in current FPM version.

---

## What I Deliberately Did NOT Do

- Did NOT fabricate citation URLs. The three agents that got blocked on web tools correctly refused to invent sources; I respected that and wrote knowledge-based content with uncertainty flags rather than fake citations.
- Did NOT create a "LattePanda automation Python script" yet. The research question (whether FPM has a CLI or requires UI automation) isn't resolved. Once I confirm that, I'll build the script.
- Did NOT write install guides for every advanced feature. Advanced features should be tuner-configured during dyno sessions, not DIY'd in the garage.

---

## Final Repo State (End of 2026-04-19)

- **Now 36 markdown files** (was 33 at start of this session, +6 new in 07-Hondata-FlashPro/, +2 reports in docs/reports/)
- **`07-Hondata-FlashPro/` now contains 9 markdown files:**
  - `overview.md` (original)
  - `Temporary-Setup/getting-started.md` (original)
  - `Permanent-LattePanda-Install/full-guide.md` (original)
  - `tuning-workflow-and-maps.md` (added 2026-04-18)
  - `hardware-software-deep-reference.md` (added 2026-04-19)
  - `calibrator-tables-reference.md` (added 2026-04-19)
  - `datalog-analysis-guide.md` (added 2026-04-19)
  - `advanced-features.md` (added 2026-04-19)
  - `troubleshooting-and-faq.md` (added 2026-04-19)
  - `tuner-directory.md` (added 2026-04-19)
- **169-page Build Guide PDF** (was 124)
- **10-page Mod Order PDF**
- `generate-pdf.py` updated

---

## Next Steps I Plan to Take

1. **First priority:** verify the flex fuel sensor wiring path (email Hondata support or ask my chosen tuner).
2. **Before first flash:** walk through `Temporary-Setup/getting-started.md` and `hardware-software-deep-reference.md` action-item checklist.
3. **Tune session planning:** pick a tuner from `tuner-directory.md` based on my actual geography (TBD) and book sessions.
4. **Datalog discipline:** every drive once FlashPro is live, following the protocol in `docs/baseline-logs.md`.
5. **Ongoing:** as I verify `[VERIFY]` items, go back and update the docs so the uncertainty flags decrease over time.

---

*Report written: 2026-04-19*
