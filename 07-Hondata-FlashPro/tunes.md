# Tunes — Live Tracking

> Every calibration I have, with screenshots, parameter extracts, safety assessments, and revision notes. This file is constantly updated as I create new tunes, consult on existing ones, or change parameters after dyno sessions.

**Living document** — entries get added, modified, and revised. History is preserved in git (use `git log docs/reports/tunes.md` or directly browse commits if I ever want to see what changed when).

---

## How Entries Are Structured

Each tune gets its own section with:

1. **Tune header** — name, source (tuner / self-made / community base map), hardware it's calibrated for, date, file path
2. **Safety pre-check** — is it matched to my actual hardware? Is the stock backup saved?
3. **Tab-by-tab capture** — screenshots or text extracts of every tab/table I've reviewed
4. **Parameter table** — key values I care about (WOT AFR, timing peaks, VTEC, VTC, rev limit)
5. **Assessment** — does this tune pass the reliability-first ceilings from [tuning-workflow-and-maps.md](tuning-workflow-and-maps.md)?
6. **Revision log** — what changed and when
7. **Next actions** — what I'd do with this tune before driving on it

---

## Safety Reference (Quick Ceilings)

From [tuning-workflow-and-maps.md](tuning-workflow-and-maps.md) — every tune I log here gets compared to these:

| Parameter | Hard Ceiling | Notes |
|-----------|--------------|-------|
| Knock count at WOT | 0 (always) | Any is too much on 170k motor |
| Pump gas WOT AFR | ≥ 12.0 | Never leaner |
| E85 WOT lambda | ≥ 0.82 | Never leaner |
| Injector duty cycle | ≤ 85% sustained | Headroom is safety |
| Rev limiter | ≤ 8400 RPM (stock internals) | +200 over stock max |
| VTEC engagement | ≥ 4500 RPM | Below this, cam doesn't match airflow |
| ECT sustained | ≤ 210°F under WOT | Above = cooling system issue |

---

## Tune 1 — Factory Flash - Stock Tune

### Header

| Field | Value |
|-------|-------|
| **Filename** | `Factory Flash - Stock Tune.fpcal` |
| **Location** | `C:\Users\extra\OneDrive\Documents\FlashPro Calibrations\Factory Flash - Stock Tune.fpcal` |
| **Source** | Read from ECU (factory OEM calibration) |
| **Hardware calibrated for** | Completely stock 2009 Civic SI (FG2, K20Z3) — ZERO aftermarket |
| **Date saved** | 2026-04-19 20:58:51 |
| **File size** | 22,431 bytes |
| **Flashed to ECU?** | This IS what's on the ECU (never been modified yet) |
| **Purpose** | Factory reset / insurance. If anything goes wrong with a performance tune, I flash this back. |

### Safety pre-check
- ✅ **Matched to hardware** — this IS the hardware state the ECU shipped with
- ✅ **Saved as backup** — that's its entire purpose
- ✅ **Stock ceilings** — Honda's engineers set this. It's the safest possible calibration by definition.

### Parameter extract
*(To be populated if user exports HTML report of stock tune for reference. Optional — this tune should never need changing.)*

### Assessment
**PASS** on all reliability ceilings. This is the ground-truth reference. Any deviation in other tunes that moves AFR leaner than this, timing more advanced than this, or VTEC lower than this should be justified by either (a) hardware that changes the engine's breathing, or (b) a specific dyno-verified finding.

### Revision log
- 2026-04-19: Initial read from ECU. Saved to FlashPro Calibrations folder.

### Next actions
- Do NOT modify
- Do NOT flash experimentally
- If anything feels wrong on any other tune, this is the escape hatch

---

## Tune 2 — performance tune

### Header

| Field | Value |
|-------|-------|
| **Filename** | `performance tune.fpcal` |
| **Location** | `C:\Users\extra\OneDrive\Documents\FlashPro Calibrations\performance tune.fpcal` |
| **Source** | **UNKNOWN — to be clarified with LxveAce** (self-made? community base map? from tuner?) |
| **Hardware calibrated for** | **UNKNOWN — critical to establish before flashing** |
| **Date saved** | 2026-04-18 19:53:05 |
| **File size** | 22,842 bytes (411 bytes larger than stock) |
| **Flashed to ECU?** | UNKNOWN — to confirm with LxveAce |
| **Purpose** | TBD |

### Safety pre-check
- ❓ **Matched to hardware?** — UNKNOWN. Critical gap. Current car state: Exedy Stage 1 + lightweight flywheel installed, K&N Typhoon intake installed, Acuity short shifter + bushings installed, DWS06 tires. Engine mounts + brakes + FlashPro are bought but not installed. A "performance tune" built for FBO+E85 flashed onto a car that has only an intake is dangerous.
- ✅ **Stock backup exists** — as of 2026-04-19 20:58, yes. Good.
- ❓ **Reliability ceilings** — UNKNOWN without parameter extract

### Parameter extract
*(To be populated — either from HTML export of this .fpcal file, or from screenshots of tabs as user sends them)*

**To capture:**
- Fuel tables (low-cam + high-cam WOT AFR targets)
- Ignition tables (low-cam + high-cam timing at peak cells)
- VTEC engagement RPM
- VTC target map (low-cam + high-cam)
- Rev limiter settings (main + per-gear if set)
- Idle target
- Fan ON/OFF temps
- Launch control status (on/off? RPM target?)
- Flat-foot shift status
- Torque management status
- Analog input configurations (any wideband wired?)
- DTC defeat flags (rear O2? IMRC?)
- Injector characterization data (stock 310cc or upsized?)

### Assessment
**PENDING** — cannot assess until parameters are known.

### Revision log
- 2026-04-18 19:53: Saved (origin and intent unknown)

### Next actions
1. **Confirm where this came from** — self-made? community download? tuner-made?
2. **Confirm if it's been flashed** — if yes, what state is the ECU currently in?
3. **Open in FPM → File → Save As HTML** (or screenshot each tab) — get the actual parameter values
4. **Cross-check** — does it match current hardware? Does it pass safety ceilings?
5. **Do not drive hard on it** until confirmed safe

---

## Template for Future Tunes

When I create, receive, or analyze a new tune, add a section like this:

```
## Tune N — [Name]

### Header
| Field | Value |
|-------|-------|
| Filename | xxx.fpcal |
| Location | [path] |
| Source | [self / community / tuner name + date] |
| Hardware calibrated for | [exact mod list] |
| Date saved | YYYY-MM-DD HH:MM |
| File size | xxx bytes |
| Flashed to ECU? | Yes/No |
| Purpose | [daily / sport / e85 / test / etc] |

### Safety pre-check
- [ ] Matched to current hardware
- [ ] Stock backup verified
- [ ] Reliability ceilings confirmed (knock 0, AFR ≥ 12.0 pump / lambda ≥ 0.82 E85, inj duty ≤ 85%, rev ≤ 8400, VTEC ≥ 4500)

### Parameter extract
[Table-by-table values from HTML export or screenshots]

### Assessment
[PASS / FAIL / PENDING, with reasoning]

### Revision log
- YYYY-MM-DD: [what changed]

### Next actions
[Specific things to do with this tune]
```

---

## Comparison Matrix (As Tunes Accumulate)

Once I have 3+ tunes in here, maintain a side-by-side view:

| Parameter | Stock | Performance Tune | [Future Daily Map] | [Future Sport Map] |
|-----------|-------|------------------|--------------------|--------------------|
| WOT AFR low-cam | ? | ? | TBD | TBD |
| WOT AFR high-cam | ? | ? | TBD | TBD |
| Peak timing high-cam | ? | ? | TBD | TBD |
| VTEC engagement | ? | ? | TBD | TBD |
| Rev limit | ? | ? | TBD | TBD |
| Fan ON temp | ? | ? | TBD | TBD |
| Launch control | off | ? | off | TBD |
| Flex fuel | off | ? | off | TBD |

(Fills in as tunes get analyzed.)

---

## Known Off-the-Shelf & Community Tunes — Reference Library

These aren't on my FlashPro yet — they're tunes I've researched that could be starting points. Full writeup + compatibility analysis is in [fpm-master-reference.md Section 18](fpm-master-reference.md#18-community-tune-landscape-from-web-research-2026-04-19).

### Ranked by fit for my current build

| # | Tune source | Cost | Hardware target | Reliability flag | Fit for me? |
|---|-------------|------|-----------------|-----------------|-------------|
| 1 | **FPM built-in: "Stock + K&N intake" AFM** | Free | K&N / equiv CAI + stock everything else | Hondata-shipped = conservative safe | **✅ YES — first flash starting point** |
| 2 | **BrenTuning remote (custom)** | $300-450 | Tell them my hardware | Custom to mine = safe if I communicate reliability-first | **✅ YES — Tune #1 and #2 sessions** |
| 3 | **Church / 4Piston / HARDmotion in-shop** | $500-800 | Custom to mine | Live dyno verification | **✅ YES — Tune #3 (flex fuel)** |
| 4 | **8thcivic community base map (Skunk2 + CAI + exhaust)** | Free | Matches Phase 2 state | Conservative ignition (community-reported low values) | **🟡 MAYBE — fallback if remote tuner unavailable** |
| 5 | HARDmotion FBO Max Tune | $199-290 | 3-3.5" intake (MAP-based, NO AFM) + race header + 2.5-3" exhaust + optional bored TB | — | **❌ NO — MAP-based, my K&N keeps AFM** |
| 6 | zoshmfg 8th Gen Si FBO tune | $80 | Hybrid Racing CAI + Skunk2 Alpha + Skunk2 exhaust | **⚠️ 13.4-13.7 WOT AFR per review = lean, violates 12.50 ceiling** | **❌ NO — unsafe per my reliability rule** |

### Community consensus parameter targets for NA K20Z3 FBO

From web research (k20a.org, 8thcivic.com, Hondata forum):

| Parameter | Safe value | Notes |
|-----------|------------|-------|
| WOT AFR (pump 93) | **12.0-12.5** (lambda 0.82-0.85) | Hondata hard ceiling 12.50. My reliability rule 12.0-12.2. |
| WOT ignition peak | **24-26°** | 28° gains 2 HP but "not worth the risk" per dyno reports |
| VTEC engagement (stock) | **5400-5700** | Hondata floor 2500, ceiling 6500 |
| VTEC engagement (FBO) | **4800-5200** | Community commonly lands 4475-5100 |
| Rev limit | **8200-8400 max** | My hard ceiling at 170k stock internals |

### Expected dyno numbers (Dynojet, honest shop)

| Hardware state | WHP | WTQ |
|----------------|-----|-----|
| Stock | 170-175 | ~135 |
| Stock + K&N | 178-188 | ~140 |
| + header + HFC + base tune | 200-210 | ~150 |
| Full bolt-on + pro tune (Tune #2) | **220-235** | **155-165** |
| FBO + E85 (Tune #3) | 230-245 | 165-175 |

**Reality check on stock baseline:** web research says stock K20Z3 is 170-175 WHP on honest Dynojet, not the 185 I had in earlier docs. Some dynos read optimistic. My actual baseline pulls will show the real answer.

---

## Workflow Reminders

**When LxveAce sends screenshots of a tune's tabs:**
1. Identify which tune (by filename) is being shown
2. Find or create that tune's section
3. For each screenshot: transcribe the parameter values into the parameter extract table
4. Check each value against the safety ceilings
5. Update the assessment
6. Log what was learned in the revision log
7. Suggest concrete next actions

**When LxveAce creates a new tune:**
1. Create a new section with the template above
2. Ask for the hardware state + flash status + source immediately
3. Don't assess safety until hardware match is confirmed

**When LxveAce modifies an existing tune after dyno:**
1. Add a revision log entry dated to the change
2. Update the parameter extract with the new values
3. Re-assess against ceilings (any ceilings broken? tightened?)
4. Compare to the prior version — what changed, what didn't

---

*Last updated: 2026-04-19*
*Maintained by: LxveAce + Claude, continuously*
