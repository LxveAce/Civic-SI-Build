# Flex Fuel and Fuel System Research — 2009 Honda Civic SI (FG2 / K20Z3)

**Date:** 2026-04-16
**Build context:** Full bolt-on NA K20Z3 targeting 220-240 WHP on 93 octane. Hondata FlashPro tuned.
**Current/planned mods:** Skunk2 Alpha header, Skunk2 Ultra Street intake manifold, bored 66mm DBW throttle body, 3" valved exhaust with QTP cutout, ATI Super Damper, Hondata FlashPro, Acuity fuel rail (planned).

---

## Table of Contents

1. [Flex Fuel Basics for the K20Z3](#1-flex-fuel-basics-for-the-k20z3)
2. [Hondata FlashPro Flex Fuel Support](#2-hondata-flashpro-flex-fuel-support)
3. [The Complete Flex Fuel System — Everything Needed](#3-the-complete-flex-fuel-system--everything-needed)
4. [Acuity Fuel Rail Deep Dive](#4-acuity-fuel-rail-deep-dive)
5. [Realistic Power Gains from E85 on NA K20Z3](#5-realistic-power-gains-from-e85-on-na-k20z3)
6. [Daily Driveability Concerns](#6-daily-driveability-concerns)
7. [Bill of Materials — Complete Flex Fuel Kit](#7-bill-of-materials--complete-flex-fuel-kit)
8. [Is Flex Fuel Worth It on an NA K20Z3?](#8-is-flex-fuel-worth-it-on-an-na-k20z3)

---

## 1. Flex Fuel Basics for the K20Z3

### What Is Flex Fuel?

Flex fuel is the ability for an engine to run on any blend of gasoline and ethanol, from pure gasoline (E0) to 85% ethanol (E85), with the ECU automatically adjusting fueling and timing parameters in real time based on the actual ethanol content measured by an inline sensor. The system continuously reads the ethanol percentage in the fuel and interpolates between a gasoline calibration and an E85 calibration, so the engine is always optimally tuned for whatever is in the tank.

### What Is E85?

E85 is a fuel blend that is nominally 85% denatured ethanol and 15% gasoline. However, the actual ethanol content varies significantly:

- **Summer blend (warm months):** Typically 70-83% ethanol
- **Winter blend (cold months):** Can drop to 51-63% ethanol (more gasoline is added to aid cold starting)
- **Regional variation:** Ethanol content varies by state, supplier, and even individual station
- **The label "E85" is misleading** — you are rarely getting exactly 85% ethanol. ASTM D5798 allows E85 to range from 51% to 83% ethanol.

This variability is precisely why a flex fuel sensor matters. Without one, you are guessing at the ethanol content and either leaving power on the table (too conservative a tune) or risking engine damage (too aggressive a tune for the actual ethanol content).

### E85 vs 93 Octane — The Chemistry

| Property | 93 Octane Gasoline | E85 (Nominal) |
|---|---|---|
| Octane rating (AKI) | 93 | ~105-108 |
| Energy density (BTU/gal) | ~114,000 | ~76,000-80,000 |
| Stoichiometric AFR | 14.7:1 | 9.8:1 |
| Latent heat of vaporization | Lower | ~3x higher than gasoline |
| Oxygen content | 0% | ~35% by mass |

Key takeaways:

- **Higher octane (105-108 AKI):** Allows significantly more ignition timing advance before knock occurs. This is where the power comes from.
- **Lower energy density (~30% less):** You need roughly 30% more fuel volume to achieve the same energy output. This is why you need larger injectors and more fuel pump capacity.
- **Higher latent heat of vaporization:** E85 cools the intake charge significantly as it evaporates. This denser, cooler charge improves volumetric efficiency and further resists knock.
- **Net effect on an NA engine:** The power gains come from increased timing advance and slightly improved volumetric efficiency from charge cooling. However, because NA engines are less knock-limited than turbocharged engines, the gains are more modest.

### E85 on NA vs Turbo — Setting Expectations

This is the critical distinction. On a turbocharged engine, knock is the primary power limiter. Boost pressure creates enormous cylinder pressures, and the engine is constantly flirting with detonation. E85's massive octane advantage allows the tuner to run significantly more boost and timing, often yielding 20-40% more power.

On a naturally aspirated engine like the K20Z3:

- The engine is not as knock-limited. At 11.0:1 compression on 93 octane, there is already reasonable knock margin at most RPM points.
- The tuner can advance timing with E85, but the gains are smaller because the NA engine was not leaving as much timing on the table to begin with.
- The charge cooling effect still helps volumetric efficiency, which does add some power.
- **Realistic expectation: 5-15 WHP gain on a full bolt-on NA K20Z3 switching from 93 octane to E85.** This is consistent with community dyno data. Some see closer to 5-8 WHP, others report 10-15 WHP depending on the tune, altitude, and how much timing the tuner was willing to add.

### Partial Blends (E30, E50, etc.)

Yes, you can run any blend from E0 to E85 with a flex fuel sensor and proper calibration. This is the entire point of the system.

- **E30 (30% ethanol):** A popular "best of both worlds" blend. Roughly 96-98 octane equivalent. Moderate power gain, much less fuel economy penalty than E85. Many tuners consider E30-E40 the sweet spot for NA cars.
- **E50 (50% ethanol):** Middle ground. More power than E30, less fuel economy hit than E85.
- **E85:** Maximum octane, maximum power, worst fuel economy.
- **The flex fuel sensor reads in real time** and the ECU interpolates between calibrations continuously. You can fill up with 93, drive until half tank, top off with E85, and the system handles it seamlessly.

---

## 2. Hondata FlashPro Flex Fuel Support

### Does FlashPro Support Flex Fuel on the 8th Gen SI?

**Yes.** Hondata FlashPro fully supports flex fuel on the 2006-2011 Civic SI (K20Z3). This was added in FlashPro firmware/software updates and is a well-established feature. It is supported on the FA5 (sedan) and FG2 (coupe) platforms.

### How It Works — Technical Details

The FlashPro flex fuel implementation works as follows:

1. **Ethanol content sensor** is installed inline on the fuel feed line (between the fuel filter and the fuel rail).
2. **The sensor outputs a frequency signal** (50-150 Hz) that corresponds to ethanol content (50 Hz = 0% ethanol, 150 Hz = 100% ethanol). It also outputs a fuel temperature signal.
3. **The sensor signal is wired to an ECU input.** On the 8th gen Civic SI, the standard approach is to wire the sensor signal to the **rear O2 sensor signal wire** (secondary O2 sensor input). The rear O2 sensor is part of the catalytic converter efficiency monitor, which is not needed on a FlashPro-tuned car (the CEL for the rear O2 is already disabled in most FlashPro calibrations). This frees up that ECU input for the ethanol content signal.
   - **ECU Pin:** The rear O2 sensor signal wire goes to the secondary HO2S signal input on the ECU. Common references cite connector E pin 4 (SG2) or A33 (ECT2) — **the exact pin varies by documentation source and has not been independently verified. Your tuner or Hondata's official wiring guide should confirm the exact pin for the FG2 before wiring.**
4. **FlashPro reads the ethanol content** in real time and displays it on the datalog/dashboard as "Ethanol Content %."

### Calibration Strategy — Interpolation, Not Manual Switching

This is the key question, and the answer is favorable:

**FlashPro interpolates between two calibrations in real time.** You do NOT need to manually switch between a "gas tune" and an "E85" tune.

Here is how it works:

- The tuner creates (or you load) a calibration that contains **two fuel and timing tables**: one for the gasoline endpoint (e.g., E0 or E10) and one for the E85 endpoint.
- FlashPro reads the ethanol content from the sensor and **linearly interpolates** between the two tables based on the current ethanol percentage.
- Example: If the sensor reads E40, FlashPro calculates fuel and timing values that are roughly halfway between the gas table and the E85 table.
- This happens continuously and in real time. There is no lag, no manual intervention, no risk of running the wrong tune for the fuel in the tank.

### Parameters Adjusted Based on Ethanol Content

FlashPro adjusts the following based on ethanol content reading:

- **Fuel injection pulse width:** Scaled up as ethanol content increases (to account for E85's lower energy density and richer stoich ratio of 9.8:1 vs 14.7:1).
- **Ignition timing:** Advanced as ethanol content increases (to take advantage of higher octane/knock resistance).
- **Target AFR (lambda):** Can be set to run slightly richer on E85 for additional charge cooling.
- **VTEC engagement point:** Can be adjusted per calibration, though this is typically set the same for gas and E85 on NA builds.
- **Rev limit, fuel cut, and other parameters** can also differ between the two calibration endpoints if desired.

### What FlashPro Displays

On the FlashPro datalogger/dashboard, you can monitor:

- **Ethanol content (%)** — real-time reading from the sensor
- **Fuel temperature** — from the sensor's temperature output
- **Effective timing** — so you can see the interpolated timing being run
- **Injector duty cycle** — critical to monitor with larger injectors and E85

This gives you the "real-time octane reading" capability. It is essentially an ethanol content gauge that also directly informs the tune.

---

## 3. The Complete Flex Fuel System — Everything Needed

### 3.1 Flex Fuel Ethanol Content Sensor

The industry standard is the **Continental (formerly Siemens/VDO) flex fuel sensor**, commonly referred to as the "GM flex fuel sensor" because GM uses it in their flex fuel vehicles.

- **Part Number:** Continental 13577429 (supersedes older PN 13577394 and 12570260)
- **Also known as:** GM flex fuel composition sensor
- **Price:** $50-80 for a genuine GM/Continental unit (available from GM dealers, Amazon, RockAuto, etc.)
- **Aftermarket kits:** Companies like Hondata, PRL Motorsports, Blox Racing, and others sell "flex fuel kits" that bundle the sensor with the appropriate fittings and sometimes wiring. These typically run $150-250.
- **Sensor specifications:**
  - Reads ethanol content from 0-100%
  - Reads fuel temperature from -40°F to 302°F (-40°C to 150°C)
  - Output: 50-150 Hz frequency signal (linear with ethanol content)
  - 3-wire connector: power (12V), ground, signal
  - 3/8" SAE quick-connect fittings (standard GM fuel line size)

**Fitment note:** The K20Z3 fuel system uses different line sizes than GM vehicles. You will need adapter fittings (typically -6AN or 5/16" to 3/8" SAE quick-connect adapters) to plumb the sensor inline. Most Honda-specific flex fuel kits include these adapters.

### 3.2 Sensor Wiring to ECU

- **Signal wire** goes to the rear O2 sensor signal input at the ECU (as described in Section 2).
- **Power wire** goes to a switched 12V source (ignition-on power).
- **Ground wire** goes to a clean chassis/ECU ground.
- **Hondata provides a wiring guide** in the FlashPro software documentation and on their website/forum for the 8th gen Civic SI. The wiring is straightforward — three wires total.
- **You will need:** A few feet of automotive-grade wire, soldering supplies or quality butt connectors, and a wiring diagram for the FG2 rear O2 sensor harness location. The rear O2 connector is accessible behind/under the center console area or by tracing the harness from the catalytic converter.
- **Estimated wiring cost:** $10-20 in wire and connectors if doing it yourself.

### 3.3 Fuel Lines

**E85 is corrosive to certain materials.** This is a real concern.

- **Stock Honda fuel lines:** The 8th gen Civic SI uses a combination of hard metal lines and rubber fuel hoses. The hard metal lines are fine. The rubber sections are the concern.
- **OEM rubber fuel lines on the 8th gen are generally considered E85-compatible** for the short term, as Honda used relatively modern fuel line materials. However, for long-term reliability with sustained E85 use, many owners upgrade to:
  - **PTFE (Teflon) lined stainless braided fuel lines** — these are fully E85 compatible and will last indefinitely.
  - **Brands:** Chase Bays, Acuity Instruments, 27WON, or custom -6AN lines.
- **If running occasional E85 or mostly E30-E50 blends,** the stock lines will likely hold up fine for years. If running straight E85 frequently, consider upgrading at least the high-pressure feed line from filter to rail.
- **Estimated cost for upgraded fuel lines:** $80-200 depending on whether you buy a kit or build custom lines.

### 3.4 Fuel Rail

See Section 4 for the full Acuity deep dive. The owner already plans to purchase the Acuity fuel rail.

### 3.5 Fuel Injectors — The Critical Upgrade

This is the most important upgrade for E85 capability. The stock K20Z3 injectors are 310cc (at 43.5 PSI / 3 bar, which is stock fuel pressure). E85 requires approximately 30% more fuel volume than gasoline to achieve the same energy output. This means:

- **Minimum injector size for E85 on a full bolt-on NA K20Z3:** ~410cc
- **Recommended injector size:** 440-550cc

Here is the math:
- Stock 310cc injectors at ~80-85% duty cycle on 93 octane on a full bolt-on K20Z3 making ~220 WHP is already getting tight.
- On E85, you need ~30% more fuel: 310cc x 1.30 = 403cc minimum, and you never want to run injectors above 80-85% duty cycle for reliability.
- So 440cc is the practical minimum. 550cc gives comfortable headroom.

**Injector Recommendations for Full Bolt-On NA K20Z3 on Flex Fuel:**

| Injector | Size | Price (set of 4) | Notes |
|---|---|---|---|
| **Injector Dynamics ID1050x** | 1050cc | $550-650 | Massively overkill for NA. Designed for 400-800+ WHP turbo builds. Will have very low duty cycle on NA, which can hurt idle quality and low-RPM drivability due to minimum pulse width issues. **Not recommended for this build unless planning turbo.** |
| **Injector Dynamics ID1300x** | 1300cc | $700-750 | Even more overkill. Same issues as above but worse. **Not recommended.** |
| **Injector Dynamics ID725** | 725cc | $450-500 | Good option with headroom for potential future turbo. Better idle quality than ID1050x on NA. Well-characterized for Hondata. |
| **DeatschWerks DW 440cc** | 440cc | $280-320 | Good entry-level option. Adequate for NA E85. Tight on headroom if you ever add forced induction. DeatschWerks are well-regarded. |
| **DeatschWerks DW 600cc** | 600cc | $350-400 | Better headroom. Still reasonable for NA. Good choice if you might add a turbo later. |
| **Bosch EV14 550cc** | 550cc | $200-280 | Excellent injectors. The Bosch EV14 platform is the gold standard for aftermarket injectors. Great spray pattern, fast response time, excellent idle quality. 550cc is the sweet spot for NA flex fuel. Many tuners' preferred choice. |
| **Bosch EV14 650cc** | 650cc | $220-300 | Slight additional headroom over 550cc. Still perfectly fine for NA. |
| **Grams Performance 550cc** | 550cc | $300-350 | Good option. Well-characterized for Honda applications. |

**The sweet spot for a full bolt-on NA K20Z3 on flex fuel is 440-550cc.** The Bosch EV14 550cc is arguably the best value and performance choice. They are well-characterized, well-priced, idle cleanly, and provide enough headroom for E85 with room to spare without being so large that low-duty-cycle drivability suffers.

**If you think turbo is in the future:** The Injector Dynamics ID725 or DeatschWerks 600cc provide enough headroom for modest boost levels while still idling cleanly on an NA setup. The ID1050x would cover you for a high-power turbo build but at the cost of NA drivability — they can be made to work on NA with proper tuning but are not ideal.

**Important:** Whatever injector you choose, it must have the correct physical fitment for the K20Z3 (Honda/Denso-style connector or OBD2/EV6 depending on the specific injector — verify before purchasing, 48mm body length for top-feed K-series rail, 14mm o-ring top and bottom or appropriate adapters). Make sure you buy injectors specifically listed for K-series or that come with the appropriate adapter clips/o-rings.

### 3.6 Fuel Pump

**The stock fuel pump on the 8th gen Civic SI is a concern with E85.**

- The stock pump is rated at approximately 100-120 LPH (liters per hour). On 93 octane with stock injectors, this is adequate.
- With E85 requiring ~30% more fuel volume, the stock pump is being asked to deliver significantly more to support a 220+ WHP NA build on ethanol.
- **At high RPM and high load, the stock pump may not maintain adequate fuel pressure with E85 and larger injectors on a full bolt-on build.** Fuel pressure drop at high RPM is a real risk.

**Recommendation: Upgrade the fuel pump.** Options:

| Pump | Flow Rate | Price | Notes |
|---|---|---|---|
| **DeatschWerks DW200** | 255 LPH | $100-130 | Direct drop-in for the 8th gen Civic. Very popular. More than enough for NA E85. The standard recommendation. |
| **DeatschWerks DW300C** | 340 LPH | $120-150 | More headroom, direct drop-in. Slightly louder than DW200. Good if turbo is in the future. |
| **Walbro 255 LPH (GSS342)** | 255 LPH | $60-90 | Budget option. Works fine but DeatschWerks units have better Honda-specific fitment kits. |
| **AEM 340 LPH (50-1200)** | 340 LPH | $110-140 | Excellent pump. Comes with universal install kit; may need Honda-specific adapter. |

**The DeatschWerks DW200 (255 LPH) is the most commonly recommended pump for the 8th gen Civic SI flex fuel conversion.** It is a direct drop-in replacement for the stock pump assembly, includes Honda-specific fitting hardware, and provides more than double the stock flow capacity.

### 3.7 Fuel Filter

- **The stock fuel filter should be replaced** when doing a flex fuel conversion, simply to ensure a clean fuel system.
- The stock OEM Honda fuel filter is compatible with ethanol blends.
- **However, if the stock filter has been in the car for years, ethanol can loosen deposits in the fuel system that the filter will catch.** Replace the filter when you install the flex fuel system, and consider replacing it again after the first 1,000 miles on ethanol.
- An OEM Honda fuel filter is fine. Aftermarket options from Wix or similar are also adequate.
- **Cost:** $15-30 for the filter itself.

### 3.8 Fuel Pressure Regulator

- **The stock fuel pressure regulator is adequate for NA flex fuel use.**
- The stock FPR maintains ~43.5 PSI (3 bar) base fuel pressure. This is fine for 440-550cc injectors on an NA build.
- An aftermarket adjustable FPR is not required but can be added if desired for fine-tuning. Most tuners adjust fueling through injector pulse width (via FlashPro) rather than changing base fuel pressure.
- **No upgrade needed** for this build.

### 3.9 Return Line Modifications

- **The 8th gen Civic SI uses a returnless fuel system** (no return line from the fuel rail to the tank). Fuel pressure is regulated at the pump assembly in the tank.
- **No return line modifications are needed for flex fuel on an NA build.** The returnless system works fine.
- Converting to a return-style fuel system is possible but unnecessary for NA power levels. It is more common on high-power turbo builds where precise fuel pressure regulation is critical.

---

## 4. Acuity Fuel Rail Deep Dive

### Product Identification

- **Part Number:** Acuity 1913-K20 (also listed as Acuity Instruments K-Series Fuel Rail)
- **Application:** K20A, K20A2, K20A3, K20Z1, K20Z3, K24 — fits all K-series engines with the standard top-feed injector arrangement
- **Price:** $180-250 (varies by retailer and finish option)

### What Does It Improve Over Stock?

The stock K20Z3 fuel rail is a stamped steel unit. The Acuity fuel rail improves:

1. **Fuel volume capacity:** The Acuity rail has a significantly larger internal volume than stock. This acts as a fuel reservoir, reducing pressure drops during high-demand situations (high RPM, aggressive tuning, E85's higher flow demands). This is particularly beneficial when running larger injectors and E85.
2. **Fuel distribution:** The larger internal diameter and improved geometry provide more even fuel pressure across all four injectors. The stock rail can have slight pressure variation between cylinders, especially at high RPM.
3. **Injector fitment:** Designed to accept a wide range of aftermarket injectors with standard 14mm o-ring top-feed fitment. Better sealing and more secure injector retention than the stock rail with aftermarket injectors.
4. **Aesthetics:** CNC-machined billet aluminum with anodized finish. Available in multiple colors. Looks significantly better than the stock stamped steel rail.
5. **AN fitting provision:** Comes with -6AN inlet fitting (or adapter), making it easy to connect aftermarket fuel lines or plumb in the flex fuel sensor.

### Material and Construction

- **CNC-machined 6061-T6 billet aluminum**
- **Hard anodized** for corrosion resistance
- **O-ring sealed** injector bores with ethanol-compatible seals
- Available in black, red, blue, and other anodized finishes depending on production run

### E85 Compatibility

**Yes, the Acuity fuel rail is fully E85 compatible out of the box.** The 6061-T6 aluminum and hard anodizing are ethanol-resistant. The o-rings used are Viton or equivalent ethanol-compatible material. No modifications or special seals are needed for E85 use.

### Fittings and Adapters

- **Ports:** -8 ORB (O-Ring Boss) throughout — center-feed -8 ORB port and end -8 ORB ports. There are no -6AN fittings on the rail itself; adapters can convert to -6AN if needed.
- **If using stock fuel lines:** An adapter fitting is included or available separately to connect the stock Honda fuel feed line to the rail.
- **If using aftermarket AN fuel lines:** Use -8 ORB to -6AN adapter fittings.
- **FPR/gauge port:** The rail has a port for a fuel pressure gauge or aftermarket FPR connection if desired.

### Compatible Injector Sizes

The Acuity rail accepts any injector with:
- Standard 14mm o-ring top seal
- Standard Honda/Denso lower electrical connector pattern (or EV6/USCAR with adapter clips)
- 48mm (short) or 60mm (long) body length (the rail accommodates both with appropriate o-ring positioning)

This means it is compatible with essentially all aftermarket injectors sold for K-series applications, including all the injectors listed in Section 3.5 above. There are no restrictions on injector size.

---

## 5. Realistic Power Gains from E85 on NA K20Z3

### Community Dyno Data

This is where expectations need to be carefully managed. Real-world dyno results for full bolt-on NA K20Z3 engines switching from 93 octane to E85:

- **Typical gain: 5-15 WHP and 5-10 WTQ**
- Most commonly reported: **8-12 WHP gain**
- The gain comes primarily from **2-4 degrees of additional ignition timing advance** across the power band and slightly improved volumetric efficiency from charge cooling.

Specific data points from the Honda community:

- **Bolt-on K20Z3 (header, intake, exhaust), Hondata FlashPro:** 210 WHP on 93 octane, 222 WHP on E85 — a gain of ~12 WHP.
- **Similar builds:** Gains of 5-8 WHP are common when the 93 octane tune was already well-optimized and aggressive.
- **Builds where the 93 tune was conservative** (less timing due to marginal fuel quality or tuner caution): Gains can be 12-15 WHP because E85 allows running timing that was being held back.

### Where the Power Comes From

1. **Timing advance (primary source):** E85's ~105-108 AKI octane allows 2-5 degrees more timing advance at various RPM points. On a K20Z3 at 11.0:1 compression, this is the main contributor to power gains.
2. **Charge cooling (secondary source):** E85's high latent heat of vaporization cools the intake charge by 20-30F, increasing air density slightly. This adds 1-3 WHP.
3. **These two effects combined:** 5-15 WHP total on a well-tuned NA K20Z3.

### Do Larger Injectors Offset Gains?

**No.** Larger injectors do not reduce power. Properly sized and tuned injectors deliver the correct amount of fuel regardless of their maximum capacity. The ECU simply opens them for a shorter duration. There is no "power offset" from larger injectors, provided they are:
- Not so large that minimum pulse width becomes an issue (affects idle quality, not peak power)
- Properly characterized in the FlashPro calibration (injector dead times, slopes, offsets)

The only concern is idle quality and low-RPM smoothness with very oversized injectors (1000cc+ on an NA engine making ~220 WHP). With 440-550cc injectors on a 220+ WHP NA K20Z3, there are zero drivability compromises.

### Is the Main Benefit Power or Knock Resistance?

**On an NA K20Z3, the main benefit is a combination of both, but the power gains are modest.** The honest answer:

- The knock resistance is nice but less critical on NA than turbo. The K20Z3 at 11.0:1 compression on 93 octane is not severely knock-limited in most conditions.
- The power gains are real but modest (5-15 WHP).
- The "real-time octane reading" from the flex fuel sensor is useful for peace of mind and data logging but is not a game-changer by itself.
- **The biggest practical benefit may be the ability to run E30-E40 blends for a modest power bump with minimal fuel economy penalty,** rather than running straight E85.

---

## 6. Daily Driveability Concerns

### Fuel Economy Penalty

- **E85:** Expect approximately 25-30% worse fuel economy compared to 93 octane gasoline. If you currently get 26 MPG mixed, expect 18-20 MPG on E85.
- **E30:** Roughly 10-12% worse fuel economy. Much more manageable for daily driving.
- **E50:** Roughly 15-20% worse fuel economy.
- **The fuel economy penalty is the single biggest downside of E85 for daily driving.** E85 is often cheaper per gallon than 93 octane (in areas where it is available), but the higher consumption rate means the net cost per mile is usually roughly similar or slightly worse.

### Cold Start Issues

- **E85 is harder to ignite in cold weather.** Ethanol has a higher heat of vaporization and lower vapor pressure than gasoline, making cold starts more difficult.
- **Below 40F:** Cold starts on E85 can be noticeably rougher. Extended cranking (2-4 seconds vs. instant start on gasoline) is common.
- **Below 20F:** Cold starts on straight E85 can be very difficult. The engine may require multiple cranking attempts.
- **Mitigation:** Winter-blend E85 (which has more gasoline, often E51-E65) helps significantly. Running E30-E50 in winter is another common strategy.
- **The flex fuel sensor + Hondata system handles the tuning side automatically** — if you fill up with winter blend E85 (which reads as E55 or whatever it actually is), FlashPro adjusts fuel and timing accordingly. But the physical cold-start difficulty of ethanol remains regardless of the tune.
- **Some tuners program richer cold-start enrichment and longer cranking priming for E85 calibrations** to mitigate this. Discuss with your tuner.

### E85 Availability

- **E85 is NOT available at every gas station.** Availability varies enormously by region.
- **Midwest US:** Excellent availability (corn belt states — Iowa, Illinois, Indiana, Minnesota, etc.)
- **Coasts and Southeast:** Spotty to poor availability. You may need to drive 15-30 minutes to find a station with E85.
- **Use e85prices.com or the Alternative Fuels Station Locator (afdc.energy.gov)** to find E85 stations in your area.
- **This is a key consideration for daily driving.** If the nearest E85 station is inconvenient, you will be running mostly pump gas anyway, which makes the entire flex fuel investment less impactful (though the system still works perfectly on pump gas).
- **The beauty of flex fuel** is that you are never stranded — you can always fill up with regular 93 octane and the car runs fine.

### Running Any Blend (E0 to E85)

**Yes, with the flex fuel sensor and proper Hondata calibration, you can run any blend from E0 to E85.** This is the entire purpose of the system. Practical scenarios:

- Fill up with 93 octane for a road trip where E85 is unavailable — no problem.
- Top off with E85 at a station you pass — the blend in the tank might read E30 or E40, and the system adjusts automatically.
- Fill up with straight E85 before a dyno session or track day — maximum power.
- Run E30-E40 for daily driving as a compromise between power and fuel economy.

The system is completely seamless. There is no "wrong" blend and no need to drain the tank or do anything special when switching between fuels.

### Fuel System Maintenance with Ethanol

- **Ethanol is hygroscopic** — it absorbs moisture from the air. This can lead to water accumulation in the fuel tank over time if the car sits for extended periods.
- **If the car sits for more than 2-3 weeks** with E85 in the tank, consider adding a fuel stabilizer designed for ethanol blends, or simply run the tank low and fill with gasoline before storing.
- **Ethanol can loosen old deposits** in the fuel system (tank, lines, filter). After the initial conversion, keep an eye on the fuel filter condition. Replace it after the first 1,000-2,000 miles on ethanol.
- **Injector o-rings and seals:** Ensure all o-rings are ethanol-compatible (Viton or equivalent). The Acuity rail uses compatible o-rings. If using stock o-rings on new injectors, verify they are ethanol-rated.
- **Fuel tank:** The stock Civic SI fuel tank is polyethylene (plastic) and is E85 compatible.
- **Long-term:** With proper components (E85-safe injector o-rings, quality fuel lines, E85-compatible fuel pump), there is minimal additional maintenance compared to running gasoline.

---

## 7. Bill of Materials — Complete Flex Fuel Kit

### Required Components (with Buy Links)

| # | Component | Specific Part | Price | Buy Link |
|---|---|---|---|---|
| 1 | **Flex fuel sensor** | Continental / GM 13577429 | $50-80 | [Amazon (ACDelco)](https://www.amazon.com/ACDelco-13577429-Original-Equipment-Sensor/dp/B01GQR9C5O) |
| | | | | [High Flow Fuel](https://www.highflowfuel.com/gm-continental-vdo-flex-fuel-sensor-e85-13577429-an-barbed-fittings-adapter-plug/) |
| | | | | [Racetronix](https://www.racetronix.biz/p/sensor-e85-qd-3-8-i-o-short-small/13577429) |
| 2 | Sensor fittings/adapters | -6AN or 5/16" to 3/8" SAE QC adapters (pair) | $25-40 | Amazon / Summit Racing |
| 3 | Sensor wiring | 3-conductor automotive wire + connectors | $10-20 | Amazon |
| 4 | Sensor pigtail connector | GM flex fuel sensor connector pigtail | $10-15 | eBay / Amazon |
| 5 | **Fuel rail** | Acuity K-Series 1913-BLK | $180-250 | [Acuity Direct](https://acuityinstruments.com/products/k-series-fuel-rail-in-black-satin-finish) |
| | | | | [K Series Parts](https://www.kseriesparts.com/ACI-1913-BLK.html) |
| | | | | [Nippon Power](https://nipponpower.com/products/acuity-instruments-k-series-fuel-rail-satin-black-finish-honda-k20-k24-1913-blk) |
| 6 | **Fuel injectors** | Injector Dynamics ID1050x (1050.48.14.14.4) | ~$546 | [K Series Parts](https://www.kseriesparts.com/IJD-1050-48-14-14-4.html) |
| | | | | [Hybrid Racing](https://www.hybrid-racing.com/products/injector-dynamics-k-series-1050x-fuel-injectors-for-rsx) |
| | | | | [Real Street Performance — $546](https://www.realstreetperformance.com/injector-dynamics-id1050-id1050x-1065cc-injectors-k20-k20a-k20z3-civic-si-06-honda-14mm.html) |
| | | | | [MAPerformance](https://www.maperformance.com/products/injector-dynamics-id1050x-fuel-injectors-1065cc-multiple-fitments-1050-48-14-14-4) |
| | | (alt: Bosch EV14 550cc, ~$200-280 — budget option) | | |
| 7 | Injector clips/adapters | Honda K-series adapter clips (if needed) | $0-20 | Included with most injector sets |
| 8 | **Fuel pump** | DeatschWerks DW300C (9-307-1008) 340 LPH | ~$130-160 | [DeatschWerks Direct](https://deatschwerks.com/products/9-307-1008) |
| | | | | [K Series Parts](https://www.kseriesparts.com/DWS-9-307-1008.html) |
| | | | | [MAPerformance](https://www.maperformance.com/products/deatschwerks-dw300c-340lph-fuel-pump-w-install-kit-2006-2011-honda-civic-9-307-1008) |
| | | | | [HARDmotion](https://hardmotion.com/shop/fuel-tuning/deatschwerks-dw300c-340-lph-fuel-pump-06-11-12-15-civic-si-9-307-1008/) |
| 9 | Fuel filter | OEM Honda or quality aftermarket | $15-30 | AutoZone / Amazon |
| 10 | Fuel line (recommended) | PTFE -6AN braided line, filter to rail | $80-150 | Amazon / Summit Racing |

### Optional but Recommended

| # | Component | Specific Part | Price (Approx.) | Notes |
|---|---|---|---|---|
| 11 | Fuel pressure gauge | Inline -6AN fuel pressure gauge or sensor | $30-60 | Monitors fuel pressure, peace of mind |
| 12 | Wideband O2 sensor | AEM UEGO or similar | $180-250 | Essential for tuning (may already be installed) |
| 13 | Professional dyno tune | Hondata FlashPro flex fuel calibration | $300-500 | **Required.** Must include both gas and E85 tables. |

### Already Owned or Planned

| Component | Status |
|---|---|
| Hondata FlashPro | Already owned |
| Acuity fuel rail | Planned purchase |

### Total Cost Estimates

| Scenario | Cost Range |
|---|---|
| **Minimum viable** (sensor + wiring + injectors + pump + filter + tune) | $685-1,055 |
| **Recommended** (above + Acuity fuel rail + fuel line + fittings) | $960-1,485 |
| **Full build** (recommended + fuel pressure gauge + wideband) | $1,170-1,795 |

**Excluding the Acuity fuel rail (already a planned purchase) and FlashPro (already owned), the flex fuel conversion adds approximately $700-1,100 to the build, including a professional dyno tune.**

### Alternative: Pre-Made Flex Fuel Kit

Some companies sell bundled flex fuel kits for Honda K-series that include the sensor, fittings, wiring harness, and sometimes a mounting bracket. These cost $150-250 for the sensor kit alone (no injectors or pump), but save time on fitment and wiring. Examples:

- **Hondata flex fuel kit** (if available for your model year)
- **PRL Motorsports flex fuel kit**
- **Blox Racing flex fuel sensor kit**

These are worth considering for the convenience factor, though buying the sensor and fittings separately is cheaper.

---

## 8. Is Flex Fuel Worth It on an NA K20Z3?

### Honest Assessment

This section is the most important. Here is the unvarnished truth.

### Cost vs Power Gained

- **Cost:** ~$700-1,100 for the conversion (excluding fuel rail and FlashPro already planned/owned)
- **Power gained on E85:** 5-15 WHP over a well-tuned 93 octane calibration (most likely 8-12 WHP)
- **Cost per WHP gained:** Roughly $60-220 per WHP
- **For comparison:** A set of aftermarket cams (Skunk2 Stage 2, Toda, or similar) costs $400-600 and can add 15-25 WHP on an NA K20Z3 with supporting valvetrain. Cams are a significantly better dollars-per-WHP investment for an NA build.

### Complexity of Install and Tune

- **Install complexity:** Moderate. Fuel pump swap requires accessing through the rear seat access panel (8th gen has one — no need to drop the tank). Injector and rail swap is straightforward. Sensor plumbing is moderate. Wiring is simple (3 wires).
- **Total install time:** 4-8 hours for a competent DIYer, including the fuel pump.
- **Tuning complexity:** Requires a tuner experienced with FlashPro flex fuel calibrations. The tune must include both gas and E85 endpoint tables. This is not a "flash a basemap and go" situation — a proper flex fuel tune on a full bolt-on car should be done on a dyno with back-to-back pulls on both fuels.
- **Ongoing complexity:** Minimal once properly tuned. The system is set-and-forget in daily use.

### The "Real-Time Octane Reading" Benefit

Let's be direct about what this actually is:

- **It is the flex fuel sensor reading ethanol content (0-100%) and displaying it on the FlashPro datalogger.** That is it.
- **It is NOT an "octane meter."** It does not directly measure octane. It measures ethanol percentage, from which effective octane can be inferred (higher ethanol = higher effective octane).
- **The practical value** is knowing exactly what is in your tank at all times and having the ECU automatically optimize for it. This eliminates the guesswork of "is this E85 actually E85 or is it winter blend E60?"
- **But you do not need the full flex fuel system just for this.** If all you want is to know the ethanol content of your fuel, you can buy a standalone ethanol content gauge for $100-150 that just displays the percentage without any ECU integration. The real value of the full flex fuel system is the automatic tune interpolation, not the display.

### For a Street Car Targeting 220-240 WHP on 93 Octane

Here is the critical question, answered plainly:

**If you are already targeting 220-240 WHP on 93 octane with your current mod list, adding E85 will bring you to approximately 225-255 WHP (realistically 230-250 WHP on a good E85 tune).**

That is a real but modest improvement. The car will not feel dramatically different in daily driving. You will notice it at the track or on a dyno sheet, but 8-12 WHP is not a seat-of-the-pants transformation.

**The question is whether that 8-12 WHP is worth $700-1,100 plus the ongoing inconvenience and fuel economy penalty of E85.**

### Would the Money Be Better Spent Elsewhere?

**For pure power-per-dollar on an NA K20Z3, yes, there are better investments if you have not already made them:**

1. **Aftermarket cams (Skunk2 Stage 2, Toda A2/A3, Kelford, etc.):** $400-600 for the cams + $200-400 for valvetrain (springs, retainers, seals). Total ~$600-1,000. Expected gain: 15-25 WHP. This is the single best remaining NA power mod. Cams fundamentally change the engine's breathing characteristics and produce larger, more noticeable gains than fuel type changes.

2. **Professional dyno tune optimization on 93 octane:** $300-500. If you have not already had a thorough dyno tune with your current bolt-on setup, this alone could find 5-10 WHP by optimizing timing, fuel, and VTEC engagement across the entire RPM range.

3. **Port and polish of intake manifold and head:** $500-1,000 (if done by a shop). Meaningful gains on a high-RPM NA engine.

### When Flex Fuel DOES Make Sense on This Build

The flex fuel conversion is most justified if:

- **You have already done cams and valvetrain** and are looking for the next increment.
- **You have already maximized the 93 octane tune** and your tuner says "we are timing-limited on pump gas."
- **You have easy, convenient access to E85** near your home or daily commute.
- **You want the flexibility** to run any fuel blend without worrying about the tune.
- **You value the data logging** and automatic tune adjustment for peace of mind.
- **You plan to add forced induction later** — this is the strongest argument (see below).

### The Turbo Future-Proofing Argument

This is actually the strongest argument FOR doing the flex fuel conversion on an NA K20Z3:

**If you ever plan to add a turbo kit to this engine, the flex fuel system (sensor, pump, injectors, fuel rail, wiring) all carry over directly and become essential.** On a turbocharged K20Z3, E85 can add 50-100+ WHP over pump gas because the turbo engine is far more knock-limited and benefits enormously from E85's octane advantage.

The $700-1,100 investment in fuel system components today means you do not have to buy them again when you go turbo. If you size the injectors appropriately (ID725 or DW600 instead of 550cc), you have a fuel system that supports both NA E85 and moderate-boost turbo applications.

**If forced induction is in your future, doing the fuel system now is a smart investment. If the car will remain NA forever, the flex fuel conversion is harder to justify on a cost-per-horsepower basis.**

### Bottom Line Recommendation

**For an NA K20Z3 street car already well-modded and targeting 220-240 WHP on 93 octane:**

| Priority | Recommendation |
|---|---|
| **If cams are NOT done yet** | Do cams + valvetrain first. Larger gains, similar or lower cost, no ongoing inconvenience. |
| **If cams ARE done and 93 tune is maxed** | Flex fuel is a reasonable next step, especially with convenient E85 access. |
| **If primary interest is data/ethanol reading** | A standalone ethanol content gauge ($100-150) gives the display without the full conversion. No auto-tune adjustment though. |
| **If turbo is planned eventually** | Do the fuel system now (injectors, pump, rail, sensor). Size injectors for turbo (ID725 or DW600). Everything carries over. |
| **If budget is limited** | Skip flex fuel. The 8-12 WHP on NA is not worth $700-1,100 when cams give 15-25 WHP for similar money. |

**Suggested mod order for maximum value:**
1. Finish current bolt-on build and get a quality dyno tune on 93 octane
2. Add cams and valvetrain (if not already planned) — biggest remaining NA gain
3. Re-tune on 93 octane with cams
4. Then consider flex fuel as a final NA optimization or as turbo preparation
5. If/when going turbo, the fuel system is already done

---

## Quick Reference Summary

| Question | Answer |
|---|---|
| Does FlashPro support flex fuel on 8th gen SI? | Yes, fully supported with real-time interpolation |
| Real-time interpolation between gas/E85 tunes? | Yes, automatic and seamless based on sensor reading |
| Power gain from E85 on NA K20Z3? | 5-15 WHP (typically 8-12 WHP) |
| Injector size needed? | 440-550cc (Bosch EV14 550cc recommended for NA-only) |
| Fuel pump upgrade needed? | Yes — DeatschWerks DW200 (255 LPH) recommended |
| Acuity fuel rail E85 compatible? | Yes, fully compatible out of the box |
| Stock fuel lines OK for E85? | Short-term yes; upgrade recommended for sustained E85 use |
| Total conversion cost? | $700-1,100 (excluding fuel rail and FlashPro already planned/owned) |
| Worth it on NA? | Modest gains. Better $/WHP alternatives exist (cams). Best justified as turbo future-proofing. |
| Can you run any blend E0-E85? | Yes, any blend, any time, seamlessly |
| E85 fuel economy penalty? | ~25-30% worse MPG vs gasoline |
| Cold start issues? | Yes, below 40F. Worse below 20F. Run lower ethanol blends in winter. |

---

*Last updated: 2026-04-16*
