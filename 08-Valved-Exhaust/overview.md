# Valved Exhaust — My DIY 3" QTP Cutout Bypass

## Status: Planned (Not Yet Purchased)

## The Idea

I want to keep my OEM resonator and muffler for quiet daily driving, but have a valve-controlled bypass that dumps exhaust before the resonator/muffler — basically a straight-pipe experience at the flip of a switch. A relay controls the valve, tied to my Hondata FlashPro calibration selection (daily = closed/quiet, sport = open/loud).

**No bolt-on valved exhaust exists for the 8th gen Civic SI.** I looked everywhere. This has to be a DIY build using universal components, which honestly is fine — gives me more control over the design.

## My Design

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

**Why I'm going 3" on the dump side:**
- My 4-1 header collector outputs at 2.5-3". Carrying 3" to the dump maximizes flow for the sport path.
- On an NA K20Z3 at 220-240 WHP, 3" won't hurt low-end torque (common myth). Exhaust gas velocity matters less than minimizing restriction at this power level.
- 3" sounds deeper and more refined than 2.5" when the valve is open
- Gives me headroom if I ever go forced induction

**Why I'm stepping down to 2.5" for the muffled path:**
- The stock resonator and muffler inlets are ~2-2.5". You can't feed 3" into them.
- A gradual reducer cone (3" to 2.5", ~6" long) creates a smooth transition with minimal turbulence
- The muffled path doesn't need maximum flow — it's the quiet mode

**Note:** The FG2 SI has ONE resonator (small canister, ~under rear seats) and ONE rear muffler (large canister, under trunk) — NOT two mufflers.

### The Valve I'm Going With

**QTP QTEC30 — 3" Electric Exhaust Cutout (~$240-260)**
- Stainless steel butterfly valve, 12V DC gear motor
- **3" bore** (upgraded from the originally planned 2.5" QTEC25)
- Motor mounts on a bracket away from the hottest pipe area
- Opens/closes in 2-3 seconds
- Proven product, thousands of installs — this is the move

### QTP Cutout Positioning

I'll place the cutout **after the high-flow cat, before the resonator**, with at least 14" between the header collector and the cutout (QTP's thermal recommendation for motor protection).

## Control Methods

1. **Phase 1:** Simple DPDT toggle switch on the dash ($5)
2. **Phase 2:** LattePanda Arduino GPIO -> relay -> QTP motor (tied to tune selection)
3. **Manual override toggle retained** for Phase 2 (works even with PC off)

## Parts List with Buy Links

| # | Item | Product | Price | Link |
|---|------|---------|-------|------|
| 1 | **Electric Cutout Valve** | QTP QTEC30 (3") | ~$217-269 | [Summit Racing — $217](https://www.summitracing.com/parts/qtp-qtec30) |
| | | | | [Amazon](https://www.amazon.com/QTP-QTEC30-Electric-Exhaust-Cutout/dp/B003R2OQUI) |
| | | | | [QTP Direct](https://quicktimeperformance.com/i-30497764-3-00-inch-qtp-electric-exhaust-cutout-valve.html) |
| | | | | [Real Street Performance — $232](https://www.realstreetperformance.com/quick-time-performance-single-3-inch-electric-exhaust-cutout-qtec30.html) |
| 2 | 3" Stainless Pipe | Mandrel-bent sections for dump pipe | ~$40 | Muffler shop / Amazon |
| 3 | 3" to 2.5" Reducer | Stainless reducer cone (~6" long) | ~$20 | Muffler shop / Amazon |
| 4 | 2.5" Adapter Pipe | Connect reducer to stock resonator inlet | ~$15 | Muffler shop |
| 5 | 3" Exhaust Tip | Stainless rolled tip for dump exit | ~$30 | Amazon / Summit Racing |
| 6 | Gaskets & Clamps | 3" and 2.5" band clamps, gaskets | ~$25 | Amazon / Summit Racing |
| 7 | Exhaust Hangers | Rubber hangers + brackets | ~$15 | Amazon / AutoZone |
| 8 | Wiring & Control | Toggle switch, high-temp wire, connectors | ~$50 | Amazon |
| 9 | Heat Protection | DEI fire sleeve, silicone tape | ~$40 | Amazon / Summit Racing |
| | **Total** | | **~$452-504** |
| | Muffler shop labor (if not welding) | | $150-250 |

## See Also

- [brainstorm.md](brainstorm.md) — Full research, alternatives I looked at, valve options, heat/waterproofing
- [purchasing.md](purchasing.md) — Original detailed parts list (to be updated for 3" spec)

---

*Last updated: 2026-04-16*
