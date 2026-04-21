# Timing Chain Maintenance — K20Z3 Preventive Service

## Status: Planned — Phase 0 Maintenance (do before any performance mods)

## The Decision Rule

Honda does not specify a mileage interval for the K20Z3 timing chain. The factory service manual defines one objective measurement: **tensioner rod protrusion length**.

| Rod extension | Action |
|---------------|--------|
| ≥ 13.5 mm | **Chain is stretched — replace chain + guides + tensioner.** |
| 10–13 mm | On the edge. At 170k miles, reliability-first says replace the whole set now while in there. |
| < 10 mm | Chain is healthy. Replace the tensioner only ($75) as insurance, reuse chain and guides. |

My plan: pull the cover (because I'm doing the VTC actuator anyway as Phase 6 Ignition Refresh). Measure. Decide on the spot.

## Why It Makes Sense Now

The VTC actuator (Phase 6 Ignition Refresh) lives behind the timing chain cover. Every labor hour spent accessing the VTC is the same labor hour to inspect the chain. Marginal parts cost for the full chain service while the cover is already off: **~$200 in chain + guides + tensioner**. Marginal labor: under an hour. It would be a mistake not to bundle these.

## No Symptoms — But Going In Anyway

Cold start clean. No rattle. No retard DTCs. No misfires. That's a good sign, not a guarantee. Stretched chains usually announce themselves with cold rattle before catastrophic failure, and the 13.5 mm tensioner measurement catches the rest. At 170k with **plans for a tune**, a drop-in head eventually, and E85 on the horizon, I need a known-clean mechanical baseline. Hidden chain stretch would skew every cam timing measurement during dyno tuning.

---

## Parts List

### Core Timing Parts (OEM Honda — do not cheap out here)

| Part | OEM P/N | Qty | Est. Price | Notes |
|------|---------|-----|-----------|-------|
| Timing chain (cam) | **14401-PNA-004** | 1 | $55–75 | IWIS-made for Honda, 86 links, with 3 colored alignment links |
| Cam chain auto-tensioner | **14510-PRB-A01** | 1 | $55–65 | The "13.5 mm rod" part. Always new with a new chain. |
| Cam chain tensioner arm (pivoting guide) | **14520-PNA-003** | 1 | $35–45 | Plastic wears |
| Cam chain guide (fixed) | **14530-PNA-003** | 1 | $25–35 | Plastic wears |
| Oil pump chain | 13441-PNA-004 | 1 | $30–40 | Lives behind the cam chain — easy replace while in there |
| Oil pump chain tensioner | 13450-RAA-A02 | 1 | $25–35 | Cheap insurance |
| Oil pump chain guide | 13460-PNC-004 | 1 | $25–35 | Plastic wears |
| VTC actuator (REVISED updated part) | **14310-RBC-003** | 1 | $250–300 | **Covered under Phase 6 Ignition Refresh budget, not double-counted here** |
| Crank pulley bolt (torque-to-yield, ONE-TIME-USE) | **90017-RWC-A01** | 1 | $10–15 | **Do not reuse the old one.** |
| Front crank main seal | **91214-RZY-A01** | 1 | $15–20 | Press into cover before installing cover |

### Gaskets & Seals (all new, every time)

| Part | P/N | Price | Notes |
|------|-----|-------|-------|
| Valve cover gasket kit (incl. plug tube seals + grommets) | **12030-PNC-000** | $25–40 | Always the KIT, not bare gasket alone |
| Water pump gasket (if pulling WP at same job) | 19222-PNA-003 | $8–10 | If bundling with cooling system job |
| Oil pan gasket (only if dropping pan — optional) | 11251-RAA-A02 | $15 | Skip if you don't drop the pan |

### Consumables

| Item | P/N | Use |
|------|-----|-----|
| Hondabond HT (high-temp RTV) | **08718-0004** | Timing cover sealing corners |
| Moly 60 assembly grease | 08798-9010 | VTC actuator vanes, cam nose, crank nose |
| Engine oil (4.4 qt 5W-30 full synthetic) | — | Fresh on first start |
| Oil filter | 15400-PLM-A02 | Always new |
| Coolant | Honda Type 2 OL999-9011 | Top off if WP is swapped |
| Dielectric grease | — | Coil boots on reinstall |

### Optional Upgrades — My Verdict

| Upgrade | Verdict |
|---------|---------|
| BillETomic / Blackworks / K-Tuned billet tensioners | **Skip.** Designed for race/boost. On a 240 WHP street build, OEM 14510-PRB-A01 is correct. Billet can *over*-tension and accelerate guide wear. |
| TODA Heavy Duty tensioner | Skip. Race-tier only. |
| Adjustable cam gears | Skip unless dyno-tuning serious big cams later. VTC actuator already varies intake cam 50°. |
| IWIS aftermarket chain vs OEM Honda | Same chain. IWIS is Honda's OEM supplier. Buy OEM packaging. |
| Aftermarket "performance" guides | Skip. Stock guides are fine. |

---

## Tools Required

### Specialty Tools

| Tool | Purpose | Cost |
|------|---------|------|
| **Honda K-series cam alignment tool (Lisle 37950)** | Locks both cams at TDC. **NON-NEGOTIABLE** — without it the cams spring-rotate under valve pressure and hit valves. | Lisle 37950 ~$35–45 |
| Crank pulley holder tool | Holds crank for bolt breakaway. Impact wrench is alternative. | AutoZone loan-a-tool or Evergreen HCPH1 ~$35 |
| Large breaker bar (24"+) | Crank bolt is 181 ft-lb factory and can be 300+ after 170k heat cycles | Own |
| **3/8" torque wrench, in-lb range (0–250 in-lb)** | Valve cover + timing cover bolts are 87 in-lb and 106 in-lb. Big torque wrench can't measure this low accurately. | Harbor Freight Icon or similar ~$60–120 |
| Torque angle gauge | Crank bolt is 37 ft-lb + 90° angle | ~$15–25 |
| Magnetic pickup / flexible grabber | Dropped bolts WILL happen | HF ~$10 |
| Paint marker (white/silver) | Backup chain-to-gear marks | Any |

### Standard Tools (should already have)

- Metric sockets 10/12/14/17/19mm (shallow + deep)
- 1/4", 3/8", 1/2" ratchets + extensions + swivel joint
- Metric combination wrenches, especially 10/12/14/17mm
- Allen/hex bits (some M6 hex-head cover bolts)
- **Plastic or brass gasket scraper (NOT steel)** — steel gouges aluminum = permanent leak
- Shop light, rags, brake cleaner
- Engine oil drain pan
- Floor jack + stands + chocks
- Small block of wood (support engine via oil pan)
- Zip ties (hold chain against cam gear during swap)

---

## Step-by-Step Procedure

See [`install-guide.md`](install-guide.md) for the full walkthrough. Summary:

**Phase A — Prep** (30–45 min): level ground, battery negative off, 4-24 hr cooldown, remove K&N intake, engine cover, drain coolant (if WP swap), remove alternator + A/C compressor + PS pump bracket.

**Phase B — Support engine + remove passenger mount** (20 min): floor jack + wood block under oil pan, take up weight, remove upper passenger mount + engine bracket.

**Phase C — Valve cover off** (30 min): unplug coils, unbolt cover in spiral-outward pattern, inspect cams.

**Phase D — Set TDC cyl 1** (15 min): rotate crank clockwise via 19mm on crank bolt, align pulley mark to pointer, verify both cam gear triangle marks point up parallel to head surface, mark chain-to-gear with paint marker.

**Phase E — Crank pulley off** (20–40 min): impact or breaker bar, remove bolt (discard — one-time-use), slide pulley off.

**Phase F — Timing chain cover off** (45–60 min): 13 bolts of varying lengths — document positions, remove 3 oil-pan-face bolts from below, score Hondabond, tap off, clean both mating surfaces spotless.

**Phase G — MEASURE TENSIONER ROD** (10 min, the go/no-go decision).

**Phase H — Remove tensioner, guides, chain** (30 min): **INSTALL CAM LOCK TOOL FIRST** (Lisle 37950). Compress tensioner rod with retainer pin, unbolt tensioner, remove arm + fixed guide, slip chain off cam gears, slide off crank gear.

**Phase I — VTC actuator swap** (30 min): hold intake cam with wrench, loosen actuator bolt, slide old off, apply Moly 60, install 14310-RBC-003, torque to **83 ft-lb**. No impact wrench.

**Phase J — Install new chain** (30–60 min): route on crank gear first (single colored link to crank mark), route up to cams (two colored links align to cam gear marks — 9 links apart), install fixed guide, install chain arm, install tensioner (pin still in), PULL PIN last, hand-rotate crank 2 full turns, verify cam marks return to TDC.

**Phase K — Oil pump chain** (20 min, since you're there): same conceptual procedure, behind the cam chain.

**Phase L — Reassemble timing cover** (45–60 min): press new crank seal into cover, clean mating surfaces to bare aluminum, apply Hondabond HT 2–3mm bead + extra at corners, install cover within 5 min (skin-over time), torque bolts crisscross from center outward to **8.7 ft-lb**.

**Phase M — Reinstall crank pulley with NEW bolt** (15 min): Moly 60 on crank nose, install damper, NEW 90017-RWC-A01 bolt, torque sequence: **131 ft-lb → loosen fully → 37 ft-lb → +90° angle**.

**Phase N — Valve cover, engine mount, accessories** (45 min): new 12030-PNC-000 gasket kit, Hondabond HT dabs at cam cap corners (4 locations), valve cover torque **7.2 ft-lb** in spiral-out-from-center pattern. **DO NOT OVER-TORQUE** — strips aluminum head.

**Phase O — First start** (30 min): fuel pump prime 3x, start within 3 sec expected, idle 3–5 min watching for leaks/CEL/rattle, short drive 5–10 min low-RPM only.

**Phase P — 100-mile re-torque** (10 min): re-torque valve cover to **7.2 ft-lb**. Visual-check timing cover for weeps. Scan OBD2 pending codes.

---

## Torque Specs

| Fastener | Torque | Notes |
|----------|--------|-------|
| Valve cover bolts | **7.2 ft-lb (9.8 N·m / 87 in-lb)** | Spiral outward from center. Re-torque at 100 mi. |
| Timing chain cover bolts (M6) | **8.7 ft-lb (12 N·m)** | All positions. Hondabond HT is primary seal. |
| Cam chain tensioner bolts | 8.7 ft-lb (12 N·m) | Pin still in until bolted down |
| Cam chain guides (fixed + arm pivot) | 8.7 ft-lb (12 N·m) | |
| Oil pump chain guide/tensioner bolts | 8.7 ft-lb (12 N·m) | |
| **VTC actuator center bolt** | **83 ft-lb (113 N·m)** | Hold cam with wrench. **No impact.** Dry. |
| Exhaust cam sprocket bolt (if touched) | 51 ft-lb (69 N·m) | |
| Cam pulse plate bolts (if touched) | 29 ft-lb (39 N·m) | |
| **Crank pulley bolt (NEW 90017-RWC-A01)** | **131 → loosen fully → 37 ft-lb → +90°** | Torque-to-yield. One-time-use. |
| Passenger engine mount bracket to cover | ~33 ft-lb (44 N·m) | Confirm against kit |
| Passenger engine mount main bolts | ~47 ft-lb (64 N·m) | Hybrid Racing 70A — confirm kit docs |
| Alternator mounting bolts | 33 ft-lb (45 N·m) | |
| A/C compressor mounting bolts | 17 ft-lb (23 N·m) | If touched |
| Oil drain plug | 29 ft-lb (39 N·m) | |

Cross-reference [`docs/torque-specs.md`](../docs/torque-specs.md) for build-wide reference.

---

## Common Mistakes

| Mistake | Consequence | Prevention |
|---------|-------------|------------|
| Rotating crank with chain off and no cam tool | Valve-to-piston or valve-to-valve contact, bent valves | Install Lisle 37950 BEFORE removing chain. Never rotate without it. |
| Chain installed off by one tooth | Low power, DTCs, possible valve damage over time | Verify cam marks align with each other AND crank TDC after 2 full crank rotations |
| Reused crank pulley bolt | Stretches past yield, loosens, eats crank gear, catastrophic | Buy 90017-RWC-A01 new with the kit |
| Reused valve cover gasket | Oil weep day one | Always new. Kit is $25. |
| Skipped spark plug tube seals | Oil pools in plug wells, shorts coils | Kit 12030-PNC-000 includes them |
| Old Hondabond / mating surface not cleaned | Persistent oil leak | Plastic scraper + brake cleaner until bare aluminum |
| Too much Hondabond | Squeezes internal, clogs oil galleries | 2–3 mm bead, not a finger's width |
| Too little Hondabond at corners | Leak at pan/cover/head junctions | Extra dab (4–5 mm) at gasket-meets-gasket junctions |
| VTC actuator installed with impact wrench | Internal damage, phantom VTC DTCs later | Hand wrench only. Torque to 83 ft-lb dry. |
| Moly 60 skipped on cam nose / VTC vanes | Dry start first fire, accelerated wear | Light coat. K20 standard. |
| Valve cover over-torqued | Stripped M6 head threads | **7.2 ft-lb.** Use proper in-lb torque wrench. |
| Skipped 100-mile re-torque | Valve cover weeps within a month | Calendar reminder. 10 minutes. |
| Tensioner pin pulled too early | Chain into wrong position, cover won't seat | Pin stays in until ALL guides + tensioner installed, chain routed, everything bolted. |

---

## Cost Estimate

### DIY Parts
| Category | Cost |
|----------|------|
| Chain set (chain + tensioner + arm + fixed guide) | ~$170 |
| Oil pump chain set | ~$95 |
| VTC actuator | $280 *(budgeted under Phase 6 Ignition Refresh)* |
| Crank bolt + crank seal | ~$30 |
| Gaskets + Hondabond + Moly 60 + misc | ~$75 |
| Oil + filter + coolant | ~$75 |
| **Parts only (chain job)** | **~$445** |
| **Parts w/ VTC actuator included** | **~$725** |

### Specialty Tool Spend (one-time)
- Lisle 37950 cam lock: $40
- In-lb torque wrench (if not owned): $60–120
- Angle gauge: $20
- Crank pulley holder (if not impact): $35
- **Tools subtotal:** ~$155–215

### Shop Labor (for comparison)
- Independent shop: 6–8 hours × $90–130/hr = $540–1,040
- Honda dealer: 6–8 hours × $150–200/hr = $900–1,600
- **Shop total (parts + labor): $1,200–2,000**

### DIY Grand Total
- Parts only: $445 (chain) / $725 (+ VTC actuator bundled)
- With tools: $600–940 first time
- **Time:** 1.5 full weekend days for first-timer, 6–8 hours for experienced

---

## Symptoms Dictionary (If Something Goes Wrong After Install)

| Symptom | Probable cause | Fix |
|---------|----------------|-----|
| Rattle at first start, disappears after 2–3 sec | Tensioner taking up slack on cold oil — normal for a new chain | Monitor. If it persists past a week, pull cover and re-check. |
| Persistent rattle, warm engine | Tensioner retainer pin never pulled, OR chain one tooth off | Pull cover. Fix alignment. |
| **P0341** (cam position sensor A circuit) / **P0344** | Cam timing off by one tooth, OR cam sensor connector not fully seated | Re-verify cam timing. Check sensor connectors. |
| **P0011 / P0014** (VTC phase error) | VTC actuator installed at wrong orientation, OR old -002 actuator installed by mistake | Pull cover, verify -003 actuator, verify orientation matches factory marks |
| Rough idle, no DTCs | Valve cover gasket leaking onto coils (plug tube seals) | Re-torque valve cover. If leak persists, re-do plug tube seals. |
| Rough idle + P03xx misfire | One tooth off on timing | Pull cover, recheck |
| Oil weeping from timing cover seam | Hondabond gap or too little at corner | Clean thoroughly, re-seal |
| Oil weeping from valve cover seam | Gasket pinched or under-torqued | Re-torque to 7.2 ft-lb. If persists, replace gasket again. |
| Oil in spark plug wells | Plug tube seals not seated / not installed | Pull valve cover, re-seat or replace seals |
| No crank / no start | Cam and crank out of time by more than one tooth — ECU refuses to fire | Pull cover, verify timing. Do NOT crank repeatedly — risk of valve contact. |
| Start + immediate loud clatter | Chain jumped, valve contact happening | Shut off immediately. Pull cover. Leakdown test may be needed. |
| Coolant in oil (milky dipstick) | If WP was touched, gasket failure | Pull WP, replace gasket. Drain + refill oil. |

---

## Cross-References

- [`06-Ignition-Refresh/overview.md`](../06-Ignition-Refresh/overview.md) — VTC actuator install (14310-RBC-003) bundles here. Free labor.
- [`09-Cooling-System/overview.md`](../09-Cooling-System/overview.md) — Water pump (19200-RBC-013) bundles here if coolant is drained.
- [`15-Pulleys-and-Harmonic-Balancer/overview.md`](../15-Pulleys-and-Harmonic-Balancer/overview.md) — ATI Super Damper install uses same crank-bolt yield cycle. Bundle if possible.
- [`08-Engine-Mounts/overview.md`](../08-Engine-Mounts/overview.md) — Hybrid Racing 70A passenger mount is removed for access. Install while in there if not already in.
- [`10-Hondata-FlashPro/overview.md`](../10-Hondata-FlashPro/overview.md) — First FlashPro flash only after chain + VTC actuator is done.
- [`docs/torque-specs.md`](../docs/torque-specs.md) — build-wide torque reference.

---

## Reference Resources

- [K-POWERED — K-Series Timing Chain Inspection & Replacement](https://kpowered.net/k-series-timing-chain-inspection-replacement/) — Best overview with 13.5mm rod measurement photos
- [8thCivic — DIY Timing Chain Removal](https://www.8thcivic.com/threads/diy-timing-chain-removal.354154/) — FG2-specific thread with 3-bolt oil-pan-flange gotcha
- [8thCivic — K20Z3 Teardown](https://www.8thcivic.com/threads/k20z3-teardown.256224/) — full teardown photos
- [How to Replace K20 Timing Chain YouTube](https://www.youtube.com/watch?v=W6ez2KneQHg)
- [How To Set Cam Timing Honda K20/K24](https://www.youtube.com/watch?v=jKoxm01BX0M) — watch 3x before starting
- [8thCivic — All Torque Specs Thread](https://www.8thcivic.com/threads/all-encompassing-torque-specs-thread.221874/)
- [K20a.org — How long do timing chains last](https://www.k20a.org/threads/how-long-do-timing-chains-last.46115/) — 13.5mm rule community discussion
- [K20a.org — Crank pulley bolt torque](https://www.k20a.org/threads/crankshaft-pulley-bolt-torque-spec.226743/) — yield torque procedure
- [K Series Parts — Camshaft Install Guide](https://www.kseriesparts.com/gp/SSIICSRI.html)

---

*Last updated: 2026-04-20*
