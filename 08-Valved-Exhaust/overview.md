# Valved Exhaust — DIY QTP Cutout Bypass

## Status: Planned (Not Yet Purchased)

## Concept

Keep the OEM mufflers for quiet daily driving. Add a valve-controlled bypass that dumps exhaust before the mufflers, creating a straight-pipe experience when the valve is open. A solenoid/relay controls the valve, tied to the Hondata FlashPro calibration selection (daily = closed/quiet, sport = open/loud).

**No bolt-on valved exhaust exists for the 8th gen Civic SI.** This is a DIY build using proven universal components.

## Design

### Exhaust Path

```
Cat -> Front Pipe -> [QTP CUTOUT HERE] -> Resonator -> Rear Muffler -> Tailpipe
                          |
                     Dump Pipe (short, angled rearward)
                          |
                     Exit Tip (passenger side rear)
```

- **Valve closed:** 100% of exhaust flows through the stock path (resonator + muffler). Quiet.
- **Valve open:** Exhaust dumps at the cutout point, bypassing all muffling. Loud.
- **Catalytic converter stays in the flow path at all times** (emissions legal)

### Recommended Valve

**QTP QTEC25 — 2.5" Electric Exhaust Cutout ($220)**
- Stainless steel butterfly valve, 12V DC gear motor
- Motor mounts on a bracket away from the hottest pipe area
- Opens/closes in 2-3 seconds
- Proven product, thousands of installs

### Pipe Diameter

Stock FG2 exhaust is 2.36" (60mm). Using **2.5" (63.5mm)** for the cutout and dump pipe — matches common cutout sizes and aftermarket cat-back diameters.

## Control Methods

1. **Phase 1:** Simple DPDT toggle switch on the dash ($5)
2. **Phase 2:** LattePanda Arduino GPIO -> relay -> QTP motor (tied to tune selection)
3. **Manual override toggle retained** for Phase 2 (works even with PC off)

## See Also

- [brainstorm.md](brainstorm.md) — Full research, alternatives considered, valve options, heat/waterproofing
- [purchasing.md](purchasing.md) — Complete parts list
