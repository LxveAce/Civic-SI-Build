# 4-1 Headers with Trumpet/Merge Collector -- Deep Dive Research

## Status: Research Complete

This document covers 4-1 header designs specifically, with emphasis on trumpet/merge collector technology, scavenging benefits, and available options for the K20Z3 / 8th gen Civic SI (FG2).

---

## 1. What Is a Trumpet / Merge Collector?

### Standard (Stamped) Collector

A standard collector is a simple cone or stamped steel funnel where the primary tubes dump into a larger single pipe. The transition is abrupt -- primary tubes are cut at angles and welded into a cone. Exhaust gas from each tube slams into gas from the other tubes, creating turbulence and pressure waves that fight each other. This is cheap to manufacture but aerodynamically crude.

### Merge Collector

A merge collector (also called a "trumpet collector" due to its shape) is a precision-fabricated component where each primary tube is individually tapered and merged into the collector body in a smooth, overlapping transition. The tubes enter the collector at carefully calculated angles (typically 24, 30, or 40 degrees) and their ends are shaped so that gas from each tube feeds into the collector in a spiraling, organized flow pattern rather than crashing head-on.

Key features of a true merge collector:
- **Individual tube tapering:** Each primary tube is individually necked down and shaped at the merge point
- **Controlled entry angle:** Tubes enter at shallow angles (24-40 degrees) rather than the steep angles of stamped collectors
- **Internal spike/cone:** Many merge collectors include a central spike (a pointed cone in the center of the collector) that guides exhaust flow from the individual primaries into a unified stream
- **Reverse cone / venturi:** Some advanced designs include a venturi section (a brief narrowing after the merge point) that accelerates gas velocity using Bernoulli's principle, creating a stronger scavenging pulse

### Megaphone Collector

A megaphone collector is a variant where the collector gradually expands in diameter after the merge point (like a trumpet bell or megaphone). This expansion creates a low-pressure zone that enhances scavenging. When used with a reverse cone (the collector expands and then contracts again), it creates an even stronger scavenging effect by reflecting pressure waves back up the primaries as negative pressure pulses.

### Nozzle Merge Collector (Hytech Proprietary)

Hytech Exhaust has developed what they call the "Nozzle Merge Collector" -- a proprietary design developed using CFD (Computational Fluid Dynamics) simulation. This design claims increased velocity and superior scavenging compared to standard merge collectors. It is available in 2, 3, 4, and 5-into-1 configurations. Specific technical details of the nozzle design are proprietary, but the principle involves optimizing the internal geometry to maximize exhaust gas velocity at the merge point.

---

## 2. How Scavenging Works (Detailed)

### The Scavenging Principle

When an exhaust valve opens, a high-pressure pulse of exhaust gas rushes down the primary tube. This pulse is a pressure wave traveling at the speed of sound in the exhaust gas (~1500-1700 ft/s depending on temperature). Behind the pulse, a low-pressure region forms.

In a well-designed header, the timing works like this:

1. Cylinder #1 fires -- a pressure pulse travels down primary #1
2. The pulse reaches the collector and partially reflects back as a **negative pressure wave** (rarefaction wave)
3. This negative pressure wave arrives back at cylinder #1's exhaust port during the overlap period (when both intake and exhaust valves are slightly open)
4. The negative pressure literally **sucks** remaining exhaust gas out of the cylinder and helps draw fresh intake charge in
5. Meanwhile, cylinder #3 fires (in the 1-3-4-2 firing order), and its pulse helps pull the remaining gas from cylinder #1's primary

### Why 4-1 Scavenging Is Different from 4-2-1

**4-2-1 (Tri-Y) scavenging:**
- Pairs cylinders by firing order: 1&4, 2&3 (360-degree separation)
- Each pair's pulses interact in the secondary merge (2-into-1 section)
- Scavenging effect is strong in the mid-range because the paired pulses create consistent negative pressure waves at moderate RPM
- The double merge (first 4-to-2, then 2-to-1) creates two scavenging opportunities
- This produces a broad, flat torque curve

**4-1 scavenging:**
- All four primaries merge at a single point
- Scavenging depends on the pressure pulses from ALL four cylinders interacting at the collector
- At low RPM, the pulses are too far apart in time to effectively draft each other -- scavenging is weak
- At high RPM (above ~5500-6000 RPM on a K20Z3), the pulses are close enough together that each one drafts the previous, creating a strong and continuous scavenging effect
- The scavenging effect intensifies as RPM climbs, producing a dramatic power surge at the top end
- A merge collector amplifies this effect because the organized flow allows the pulses to interact more efficiently

### Anti-Reversion Technology

Anti-reversion refers to preventing exhaust gas from flowing **backward** up the primary tubes during the overlap period. When the exhaust valve opens and the intake valve is also slightly open, there is a risk that exhaust gas can flow backward into the intake port, contaminating the fresh charge.

**Anti-reversion chambers** (as used by Hytech and others) are small diameter increases in the primary tubes, typically 2-3 inches from the head flange. The chamber is slightly larger in diameter than the rest of the primary (~0.25" larger for ~2" of length). This creates a one-way effect:

- Forward-flowing exhaust gas passes through the chamber with minimal disruption (slight expansion, slight re-acceleration)
- Backward-flowing reversion pulses hit the chamber and are partially reflected forward, reducing the amount of exhaust gas that re-enters the cylinder
- The effect is like a diode for pressure waves -- it attenuates backward flow more than forward flow

This is particularly valuable on engines with aggressive cam profiles that have long overlap durations (like VTEC high-cam operation on the K20Z3).

---

## 3. 4-1 vs 4-2-1 on the K20Z3: Trade-Offs

### Power Characteristics

| RPM Range | 4-2-1 | 4-1 | Difference |
|-----------|-------|-----|------------|
| 2000-3500 (low) | Better torque, smoother | Slightly hollow, less torque | 4-2-1 wins by 5-10 lb-ft |
| 3500-5500 (mid) | Strong, broad powerband | Moderate, building | 4-2-1 wins by 3-8 lb-ft |
| 5500-7000 (VTEC range) | Good, but plateauing | Rapidly increasing, overtakes 4-2-1 | 4-1 catches up, then passes |
| 7000-8400 (top end) | Falls off slightly | Peak power, screaming | 4-1 wins by 5-15 WHP |
| **Peak HP** | ~215-225 WHP (FBO + tune) | ~225-240 WHP (FBO + tune) | 4-1 wins by 10-15 WHP at peak |
| **Peak TQ** | ~155-165 WTQ | ~150-160 WTQ | 4-2-1 wins by 3-8 WTQ |

### Key Insight: VTEC Crossover

The K20Z3's VTEC crossover (when the aggressive high-lift cam profile engages) occurs at approximately 5800 RPM stock, and is typically adjusted to 4500-5500 RPM with Hondata tuning. The 4-1 header really comes alive **above** the VTEC crossover point. Below it, the 4-2-1 is the stronger design.

This means:
- **For daily driving (2000-5000 RPM most of the time):** The 4-2-1 feels noticeably punchier and more responsive
- **For spirited driving / track (5500-8400 RPM):** The 4-1 pulls harder and makes more peak power
- **For drag racing (launch and hold WOT to redline):** The 4-1 wins overall because most of the run is in the high-RPM sweet spot

### Quantified Trade-Off Summary

A 4-1 header on the K20Z3 will typically:
- **Gain** 5-15 WHP at peak (above 7000 RPM) compared to the best 4-2-1
- **Lose** 3-10 WTQ in the 2500-5000 RPM range compared to the best 4-2-1
- **Break even** around 5500-6000 RPM
- Peak power shifts higher in the RPM band (to ~8000-8400 RPM vs 7800-8000 with 4-2-1)

### Who Should Choose 4-1?

The 4-1 is the right choice if:
- You prioritize maximum peak power over daily-driving torque
- You frequently rev above 6000 RPM (spirited driving, canyon carving, track days)
- You want the most aggressive exhaust note possible
- You are willing to accept a slightly lazier feel below 5000 RPM
- You plan to lower the VTEC engagement point via Hondata to bring the power on earlier

The 4-1 is NOT ideal if:
- You primarily drive in traffic at 2000-4000 RPM and want maximum responsiveness there
- You want the broadest possible powerband
- You never rev past 6500 RPM

---

## 4. Available 4-1 Headers for the K20Z3 / 8th Gen Civic SI

### CRITICAL NOTE: Direct-Fit 4-1 Options Are Extremely Limited

Unlike the 4-2-1 market (which has 8+ options from PLM, Skunk2, K-Tuned, 1320, Invidia, etc.), the 4-1 header market for the 8th gen Civic SI chassis is very limited. Most 4-1 headers in the K-series world are designed for **K-swap applications** (older Civics, Integras) and do NOT bolt into the FG2/FA5 chassis without modification.

### Option 1: Hytech Exhaust -- THE Gold Standard

| Spec | Detail |
|------|--------|
| **Manufacturer** | Hytech Exhaust (separate company from Bisimoto, though sometimes confused) |
| **Design** | Available in both 4-2-1 Tri-Y and 4-1 merge collector configurations |
| **Primary Pairing** | 1,3 and 2,4 configuration |
| **Primary Tube Diameter** | 1.75" (44.5mm) |
| **Primary Length** | Cylinders 1&4: 30", Cylinders 2&3: 30.5" |
| **Anti-Reversion** | Yes -- chambered primaries with anti-reversion bulges near the head flange |
| **Collector Type** | Nozzle Merge Collector (CFD-designed, proprietary) |
| **Collector Outlet** | 2.5" |
| **Material** | Stainless steel, TIG-welded |
| **Included** | Header + high-flow catalytic converter + twin-loop acoustic muffler system |
| **Price** | $1,300 (header + cat + exhaust system, historically) |
| **Power Guarantee** | 20 WHP + 22 lb-ft TQ with Hondata FlashPro tune (money-back guarantee) |
| **With Good Intake** | 230+ WHP claimed |
| **Availability** | Custom made to order. Contact "John" at Hytech. Lead time historically 3-4 weeks. |
| **Current Status (2026)** | UNCERTAIN. Hytech's web presence has been minimal since ~2014-2015. Forum activity from Hytech representatives dropped off. It is unclear if they are still actively manufacturing headers for the 8th gen SI platform. Potential buyers should attempt contact before planning a build around this header. |

**What Makes It Special:**

1. **Nozzle Merge Collector:** Hytech's proprietary CFD-designed collector is not a simple cone or even a standard merge collector. It uses computational fluid dynamics to optimize internal geometry for maximum velocity and scavenging. This is the core technology that separates Hytech from other headers.

2. **Anti-Reversion Chambers:** The small bulbous chambers in the primaries near the head flange are tuned to catch backward-traveling pressure waves during valve overlap. This prevents exhaust gas contamination of the fresh charge, widening the powerband.

3. **Complete System:** Unlike most headers that ship as a bare manifold, Hytech historically included a high-flow catalytic converter and a twin-loop acoustic muffler. This means you get a complete exhaust solution.

4. **Collector Design Precision:** The collector is designed with such minimal internal volume that Hytech advises against placing an O2 sensor in the collector itself (it would disrupt flow).

5. **Power Guarantee:** The 20 WHP / 22 TQ guarantee with Hondata tune is aggressive and reflects genuine confidence in the product.

**Concerns:**
- **Availability is the biggest issue.** As of 2026, it is unclear whether Hytech is still manufacturing these headers. Their web presence essentially vanished around 2014-2015. Multiple forum users from 2014 onward reported difficulty contacting them.
- **Price is 2-3x competitors.** At $1,300 for the complete system, it is significantly more expensive than a PLM V2 + Cat ($575) or even Skunk2 Alpha + Berk HFC ($920).
- **The $1,300 price includes the complete exhaust system** (header + cat + muffler), which is actually reasonable if you need all three components. But if you are keeping stock mufflers (as this build plans to), you are paying for a muffler system you will not use.

### Option 2: PLM K-Swap 4-1 Megaphone Header

| Spec | Detail |
|------|--------|
| **Manufacturer** | Private Label Mfg (PLM) / Power Driven |
| **Part Number** | PLM Power Driven K Swap 4-1 Megaphone Header |
| **Design** | 4-1 with megaphone merge collector + reverse cone |
| **Collector Outlet** | 2.5" with V-Band flange |
| **Material** | 304 stainless steel, TIG-welded |
| **Flanges** | CNC machined, 0.38" thick |
| **Tubing** | 18 gauge stainless |
| **Construction** | Two-piece slip-fit design |
| **Price** | ~$400-500 (header only, check current PLM pricing) |
| **Availability** | In stock, ships same/next day from PLM |

**CRITICAL FITMENT WARNING:** This header is designed for **K-Swap applications** (EG, EK, DC2 chassis). It does NOT directly fit the 8th gen Civic SI (FG2/FA5). The FG2 has a different subframe, steering rack position, and firewall geometry than K-swap cars. Installing this header in an FG2 would require custom fabrication of the primary tubes to clear FG2-specific obstacles. This is essentially a custom header build using PLM's merge collector as the starting point.

PLM also sells the **4-1 Megaphone Merge Collector separately** (without primaries) for ~$150-200, which could be used as a collector component for a fully custom 4-1 header build.

### Option 3: PLM K-Swap 4-1 Merge Collector (Collector Only)

| Spec | Detail |
|------|--------|
| **Part Number** | PLM Power Driven K Swap Header 4-1 Merge Collector |
| **Design** | 4-into-1 merge collector with reverse cone |
| **Outlet** | 2.5" V-Band |
| **Use Case** | Convert an existing 4-2-1 header to 4-1, or use as part of a custom 4-1 build |
| **Price** | ~$150-200 |
| **Availability** | In stock from PLM |

**Note:** This is just the collector portion. You would need custom primary tubes fabricated by a professional exhaust shop to create a complete 4-1 header for the FG2 chassis.

### Option 4: Full Custom 4-1 Header

A professional exhaust fabricator can build a custom 4-1 header specifically for the FG2 chassis. This involves:
- Custom-bent stainless primary tubes sized and routed for the FG2 engine bay
- A quality merge collector (PLM, Burns Stainless, or MagnaFlow)
- Professional TIG welding
- Dyno tuning to verify the design

| Spec | Detail |
|------|--------|
| **Cost** | $800-2,000+ depending on fabricator and materials |
| **Lead Time** | 2-6 weeks depending on shop |
| **Primary Tube Options** | 1.625", 1.75", or 1.875" (1.75" is optimal for K20Z3 power levels) |
| **Collector Options** | Burns Stainless merge collectors ($100-200), PLM megaphone ($150-200), or MagnaFlow merge ($50-100) |
| **Advantages** | Can be tuned perfectly for the K20Z3, optimized routing for FG2 chassis, choice of collector type |
| **Disadvantages** | Expensive, time-consuming, quality depends entirely on the fabricator |

### Option 5: Toda Racing

**Toda Racing does NOT make a 4-1 header for the K20Z3.** They make a 4-2-1 equal-length header for the K20A (DC5/EP3 and FD2/CL7 applications). Their FD2 header may have similar fitment to the FG2, but it is a 4-2-1 design, not 4-1. It is also extremely expensive (~$800-1,200) and designed for JDM applications.

### Option 6: DC Sports

DC Sports has discontinued their K20Z3 header and is no longer a viable option. They only made a 4-2-1 design anyway.

---

## 5. Comparison Table -- 4-1 Options Only

| Option | Design | Collector Type | Fits FG2 Direct? | Price | Peak HP Gain | Availability |
|--------|--------|---------------|-------------------|-------|-------------|-------------|
| **Hytech** | 4-1 (or 4-2-1) | Nozzle Merge (CFD) | YES | $1,300 (complete system) | 20+ WHP guaranteed | UNCERTAIN -- may be defunct |
| **PLM 4-1 Megaphone** | 4-1 | Megaphone + Reverse Cone | NO (K-swap only) | ~$400-500 | 15-20 WHP est. | In stock |
| **PLM Collector Only** | Collector only | Merge + Reverse Cone | N/A (needs custom primaries) | ~$150-200 | N/A | In stock |
| **Full Custom** | 4-1 | Builder's choice | YES (built to fit) | $800-2,000+ | 15-25 WHP (design-dependent) | 2-6 week lead |

---

## 6. Interaction with the Rest of the Exhaust

### Collector-to-Pipe Transition

A 4-1 header with a 2.5" collector outlet flows directly into 2.5" piping. This is a clean, restriction-free transition. The 4-1 merge collector (especially with a megaphone/reverse cone) actually creates a stronger scavenging pulse than a 4-2-1 collector, which means the pipe after the collector benefits slightly more from maintaining velocity.

### Optimal Pipe Diameter After a 4-1 Collector

For a K20Z3 making 225-240 WHP (4-1 header + FBO + tune):

| Pipe Section | Recommended Diameter | Reasoning |
|-------------|---------------------|-----------|
| Collector outlet to high-flow cat | 2.5" | Matches collector, no adapter needed |
| High-flow cat through cutout | 2.5" | Matches QTP QTEC25 cutout size |
| Cutout to reconnection point | 2.5" | Consistent flow diameter |
| Reconnection to stock muffler | 2.5" to stock adapter | Reduces to mate with stock muffler inlet |

### Is 3" Too Large for an NA K20Z3?

**The short answer: 2.5" is optimal. 3" is borderline and not recommended for most of the exhaust run.**

Detailed analysis:

- **At the collector:** A 4-1 collector with a 2.5" outlet is standard and correct. Going to a 3" collector would reduce gas velocity and hurt scavenging on an NA K20Z3.
- **From collector to cutout:** 2.5" maintains proper exhaust gas velocity (200-250 fps target). 3" would drop velocity below optimal at anything under ~7000 RPM.
- **From cutout dump pipe (open position):** When the cutout is open and dumping to atmosphere, a short 3" dump pipe would not hurt performance because the exhaust is exiting to open air with no velocity concerns. However, the benefit over 2.5" dump is negligible.
- **Community consensus:** Dyno testing on K20 engines shows 3" providing gains of ~7 WHP over 2.5" with no bottom-end losses on one test, but this was on a K-swap with higher power output. For a stock-internals K20Z3 at 225-240 WHP, 2.5" is the sweet spot. 3" is viable but offers diminishing returns.

**Recommendation for this build:**
- 2.5" from header collector through the entire system to the stock muffler
- If you specifically want 3" for the dump section only (from cutout to atmosphere when open), that is fine but unnecessary -- 2.5" dump will flow more than enough for an NA K20Z3
- Do NOT run 3" for the closed-path section (cutout to resonator to muffler). This would reduce gas velocity in daily driving and make the car feel lazier below 5000 RPM.

### Can a 4-1 Header Be Paired with the Stock Catalytic Converter?

**No, not directly.** All aftermarket K20Z3 headers (both 4-1 and 4-2-1) eliminate the stock catalytic converter mounting point. The stock cat bolts to the stock manifold via a specific flange -- aftermarket headers replace the manifold and that flange connection.

You need either:
- A high-flow catalytic converter that bolts to the header's collector outlet (2.5" flange)
- A test pipe (catless, off-road only)
- If using Hytech: their system includes a high-flow cat

The PLM 200-cell HFC (included with the PLM V2 4-2-1 header combo) or the Berk Technology HFC are both viable cat solutions for any aftermarket header with a 2.5" collector.

---

## 7. Sound Character: 4-1 vs 4-2-1 on the K20Z3

### 4-2-1 Sound (for Reference)

- **Idle:** Deeper, slight rumble, "angry Honda" character
- **Cruising (2000-3500 RPM):** Muted, civilized with stock mufflers
- **Acceleration (3500-6000 RPM):** Full-bodied growl, building rasp, classic Honda sound
- **High RPM (6000-8400 RPM):** Raspy, metallic scream, strong induction noise mixes in
- **Overall:** Balanced, aggressive but not extreme

### 4-1 Sound

- **Idle:** More hollow, slightly louder, less refined
- **Cruising (2000-3500 RPM):** Can have a slight drone/resonance due to uneven pulse spacing at low RPM
- **Acceleration (3500-6000 RPM):** Building intensity, more of a "wail" than a "growl"
- **High RPM (6000-8400 RPM):** THIS is where the 4-1 shines sonically. A high-pitched, continuous screaming wail that is distinctly different from 4-2-1. More "exotic car" than "tuned Honda." The merge collector creates a unified, continuous exhaust note rather than individual pulse raspiness.
- **Overall:** More of a crescendo effect -- quiet-ish at low RPM, absolute screamer at high RPM. The transition from low to high RPM is more dramatic.

### With Stock Mufflers Retained (Valve Closed)

| Characteristic | 4-2-1 | 4-1 |
|---------------|-------|-----|
| Idle volume increase | +2-3 dB | +3-5 dB |
| Cruise drone | Minimal | Slightly more noticeable |
| WOT volume | Moderate increase | Moderate-loud increase |
| Character | Throaty, refined | Hollow, more raw |

### With QTP Cutout Open

| Characteristic | 4-2-1 | 4-1 |
|---------------|-------|-----|
| Volume | 95-105 dB at WOT | 100-110 dB at WOT |
| Character | Classic Honda rasp/scream | High-pitched continuous wail |
| "Cool factor" | Very aggressive | Exotic/race car territory |
| Drone at cruise | Bad (don't cruise with cutout open) | Worse (definitely don't cruise open) |

---

## 8. Recommendation for This Build

### The Reality Check

The owner wants a 4-1 header with a trumpet/merge collector for the 8th gen Civic SI. Here is the honest assessment:

**The direct-fit 4-1 market for the FG2 is essentially one option: Hytech.** And Hytech's current availability is uncertain. Every other 4-1 header on the market is designed for K-swap applications in older chassis and does not bolt into the FG2.

### Recommended Paths (In Order of Preference)

**Path 1: Attempt to Contact Hytech**
- Try to reach Hytech and confirm they are still manufacturing the SI header
- If available: order the 4-1 configuration with nozzle merge collector
- Budget: ~$1,300 for complete system (header + cat + muffler)
- Note: You would not use their muffler system since you are keeping stock mufflers + QTP cutout. Ask if they sell the header + cat only without the muffler, which should reduce cost.

**Path 2: Custom 4-1 Build**
- Find a reputable local exhaust fabrication shop experienced with Honda K-series builds
- Purchase a PLM 4-1 Megaphone Merge Collector (~$150-200) as the collector component
- Have the shop fabricate custom 1.75" primaries routed for the FG2 engine bay
- Include anti-reversion chambers if the fabricator is experienced enough
- Add a high-flow cat after the collector
- Budget: $800-1,500 for fabrication + $150-200 for collector + $200-350 for HFC = $1,150-2,050 total
- This route gives you a true 4-1 with a quality merge collector, custom-fitted to your specific car

**Path 3: PLM V2 4-2-1 (Fallback)**
- If the 4-1 route proves impractical or too expensive, the PLM V2 4-2-1 + 200-cell HFC at $575 remains an excellent choice
- You sacrifice 5-15 peak WHP compared to a quality 4-1 but gain a broader torque curve and significantly easier installation
- This is the pragmatic choice

### Bottom Line

A true 4-1 header with a merge collector on the K20Z3 is a **premium, enthusiast-grade modification** that will cost 2-4x more than a 4-2-1 and provide marginal gains in daily driving scenarios. The gains are concentrated above 6000 RPM. If the owner frequently drives in that range and values the sound character of a 4-1, it is worth pursuing. If the car is primarily a daily driver with occasional spirited driving, the 4-2-1 is the smarter investment.

---

*Research compiled: 2026-04-16*
*Sources: 8thcivic.com, k20a.org, Private Label Mfg, Burns Stainless, Hytech Exhaust forum posts, Honda-Tech, NASA Speed News, MotoIQ, OnAllCylinders, SPD Exhaust*
