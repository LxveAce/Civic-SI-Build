# Valved Exhaust — DIY 3" QTP Cutout Bypass

## Status: Planned (Not Yet Purchased)

## Concept

Keep the OEM resonator and muffler for quiet daily driving. Add a valve-controlled bypass that dumps exhaust before the resonator/muffler, creating a straight-pipe experience when the valve is open. A relay controls the valve, tied to the Hondata FlashPro calibration selection (daily = closed/quiet, sport = open/loud).

**No bolt-on valved exhaust exists for the 8th gen Civic SI.** This is a DIY build using proven universal components.

## Design

### Exhaust Path (Updated: 3" Dump with Step-Down)

```
4-1 Header ─► High-Flow Cat ─► 3" Pipe ─┬─► [QTP QTEC30 CUTOUT] ─► 3" Dump Pipe ─► Exit Tip
                                          │
                                          └─► [3" to 2.5" Reducer Cone]
                                                      │
                                              2.5" Pipe ─► Resonator ─► Rear Muffler ─► Stock Tailpipe
```

### How It Works

- **Valve CLOSED (Daily):** Cutout butterfly is shut. 100% of exhaust flows through the reducer cone, down to 2.5", through the resonator and muffler. Quiet, stock-like.
- **Valve OPEN (Sport):** Cutout butterfly opens. Exhaust takes the path of least resistance — dumps out the 3" straight pipe. Bypasses resonator and muffler completely. Very loud.
- **Catalytic converter stays in the flow path at all times** (emissions legal)

### Pipe Diameter Strategy

| Section | Diameter | Reason |
|---------|----------|--------|
| Header collector to cutout | **3"** | Maximum flow for sport mode. Matches 4-1 header collector output. |
| Sport dump pipe (cutout to exit) | **3"** | Full flow, no restriction when valve is open |
| Daily path (cutout to resonator) | **3" → 2.5" reducer** | Steps down to match resonator/muffler inlet size |
| Resonator → muffler → tailpipe | **2.5" / stock** | Retains stock components, no modification needed |

**Why 3" on the dump side:**
- The 4-1 header collector outputs at 2.5-3". Carrying 3" to the dump maximizes flow for the sport path.
- On an NA K20Z3 at 220-240 WHP, 3" won't hurt low-end torque (common myth). Exhaust gas velocity matters less than minimizing restriction at this power level.
- 3" sounds deeper and more refined than 2.5" when the valve is open
- Provides headroom if forced induction is ever added

**Why step down to 2.5" for the muffled path:**
- The stock resonator and muffler inlets are ~2-2.5". You can't feed 3" into them.
- A gradual reducer cone (3" to 2.5", ~6" long) creates a smooth transition with minimal turbulence
- The muffled path doesn't need maximum flow — it's the quiet mode

**Note:** The FG2 SI has ONE resonator (small canister, ~under rear seats) and ONE rear muffler (large canister, under trunk) — NOT two mufflers.

### Recommended Valve

**QTP QTEC30 — 3" Electric Exhaust Cutout (~$240-260)**
- Stainless steel butterfly valve, 12V DC gear motor
- **3" bore** (upgraded from the originally planned 2.5" QTEC25)
- Motor mounts on a bracket away from the hottest pipe area
- Opens/closes in 2-3 seconds
- Proven product, thousands of installs

### QTP Cutout Positioning

Place the cutout **after the high-flow cat, before the resonator**, with at least 14" between the header collector and the cutout (QTP's thermal recommendation for motor protection).

## Control Methods

1. **Phase 1:** Simple DPDT toggle switch on the dash ($5)
2. **Phase 2:** LattePanda Arduino GPIO -> relay -> QTP motor (tied to tune selection)
3. **Manual override toggle retained** for Phase 2 (works even with PC off)

## Updated Parts List

| # | Item | Product | Price |
|---|------|---------|-------|
| 1 | Electric Cutout Valve | QTP QTEC30 (3") | ~$250 |
| 2 | 3" Stainless Pipe | Mandrel-bent sections for dump pipe | ~$40 |
| 3 | 3" to 2.5" Reducer | Stainless reducer cone (~6" long) | ~$20 |
| 4 | 2.5" Adapter Pipe | Connect reducer to stock resonator inlet | ~$15 |
| 5 | 3" Exhaust Tip | Stainless rolled tip for dump exit | ~$30 |
| 6 | Gaskets & Clamps | 3" and 2.5" band clamps, gaskets | ~$25 |
| 7 | Exhaust Hangers | Rubber hangers + brackets | ~$15 |
| 8 | Wiring & Control | Toggle switch, high-temp wire, connectors | ~$50 |
| 9 | Heat Protection | DEI fire sleeve, silicone tape | ~$40 |
| | **Total** | | **~$485** |
| | Muffler shop labor (if not welding) | | $150-250 |

## See Also

- [brainstorm.md](brainstorm.md) — Full research, alternatives considered, valve options, heat/waterproofing
- [purchasing.md](purchasing.md) — Original detailed parts list (to be updated for 3" spec)

---

*Last updated: 2026-04-16*
