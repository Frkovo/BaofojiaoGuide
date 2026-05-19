---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Question Type 1: Spring Experiments

### 如何识别

题目涉及弹簧、弹力、弹性常数、弹簧的尺寸特性。关键词包括 spring, wire, turns $N$, cross-sectional area $A$, extension $x$, spring constant $k$, width $w$, thickness $t$, density $\rho$。

### 标准解题方法

:::note[Spring Experiment 框架]

**IV**: cross-sectional area $A$ / thickness $t$ / width $w$ / angle $\theta$ 等
**DV**: spring constant $k$ / extension $x$ 等
**CV**: number of turns $N$, density $\rho$, thickness $t$, material $E$, applied mass $m$

**测量 $k$**: 用 $F = kx$，挂已知质量 $m$，测 extension $x$，$k = mg/x$
**测量 $A$**: 测直径 $d$ 用 micrometer，$A = \pi d^2/4$ 或 width $\times$ breadth

:::

### 完整原题

#### Example 1 — 9702/s20/qp/51 Q1（15 marks）

> A student investigates springs made of metal wire. The student constructs several springs from wire of thickness $t$. Each spring has a different cross-sectional area $A$. The student investigates how the spring constant $k$ varies with $A$. It is suggested that:
> $$k = \frac{E\rho t^4}{A^{\frac{3}{2}}N}$$
> where $\rho$ is the density of the metal, $N$ is the number of turns of wire on the spring and $E$ is a constant.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: cross-sectional area $A$ is the independent variable and spring constant $k$ is the dependent variable / vary $A$ and measure $k$
- **B1**: keep number of turns $N$ constant

**Methods of data collection:**
- **B1**: diagram: spring fixed at one end, load attached, labelled load
- **B1**: use different springs with different $A$（or use same spring with different $A$）
- **B1**: measure $A$ using micrometer/calipers（$A = \pi d^2/4$）or $A =$ width $\times$ breadth
- **B1**: measure $k$ by adding masses and using $F = kx$, $k = mg/x$
- **B1**: measure $x$ with ruler

**Method of analysis:**
- **B1**: plot a graph of $k$ against $A^{-3/2}$ or $\lg k$ against $\lg A$
- **B1**: relationship valid if a straight line passing through the origin is produced
- **B1**: $E = \frac{\text{gradient} \times N}{\rho \times t^4}$

**Additional detail:**
- **D1**: repeat measurement of $x$ and average
- **D2**: use safety goggles to protect eyes from snapping springs
- **D3**: measure $t$ using micrometer/calipers
- **D4**: measure $N$ by counting along the spring
- **D5**: cushion/sand box in case load falls

</details>

---

#### Example 2 — 9702/w20/qp/51 Q1（15 marks）

> A student investigates how the extension $x$ of a spring depends on the cross-sectional area $A$ of the wire from which it is made. It is suggested that:
> $$x = \frac{mg w^3 N A^n}{E\rho}$$
> where $m$ is the applied mass, $w$ is the width of the spring, $N$ is the number of turns, $\rho$ is the density of the metal and $E$ and $n$ are constants.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $A$ is independent, $x$ is dependent / vary $A$ and measure $x$
- **B1**: keep $m$, $w$, $N$ constant

**Methods of data collection:**
- **B1**: diagram: spring fixed, masses hung, labelled spring and masses
- **B1**: use springs with different $A$（or same spring with changed $A$）
- **B1**: measure $A$ via $A = \pi d^2/4$ using micrometer
- **B1**: measure $x$ using ruler（initial and final length）
- **B1**: measure $m$ using top-pan balance

**Method of analysis:**
- **B1**: plot $\lg x$ against $\lg A$
- **B1**: straight line produced confirms relationship
- **B1**: $n = \text{gradient}$, $E = \frac{mg w^3 N}{10^{\text{y-intercept}} \times \rho}$

**Additional detail:**
- **D1**: repeat and average
- **D2**: safety goggles for snapping springs
- **D3**: measure $w$ using ruler
- **D4**: measure $N$ by counting
- **D5**: use set square to ensure ruler vertical

</details>

---

#### Example 3 — 9702/w21/qp/52 Q1（15 marks）

> A student investigates how the extension $x$ of a spring relates to the angle $\theta$ of a wooden strip. The strip is hinged at one end. A spring is attached to the free end and to a fixed point. It is suggested that:
> $$\frac{WL}{2}\cos\theta = kxd\sin\alpha$$
> where $W$ is the weight of the strip, $L$ is its length, $k$ is the spring constant, $d$ is the distance from hinge to spring attachment, and $\alpha$ is the angle of the spring.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $\theta$ is independent, $x$ is dependent / vary $\theta$ and measure $x$
- **B1**: keep $L$, $d$, $k$ constant

**Methods of data collection:**
- **B1**: diagram: strip hinged at end, spring attached, protractor to measure $\theta$
- **B1**: vary $\theta$ by tilting the strip
- **B1**: measure $\theta$ using protractor
- **B1**: measure $x$ using ruler
- **B1**: measure $d$ and $L$ using ruler, $k$ from separate $F = kx$ experiment

**Method of analysis:**
- **B1**: plot $\cos\theta$ against $1/x$ or $x$ against $1/\cos\theta$
- **B1**: straight line confirms relationship
- **B1**: $W = \frac{2kd\sin\alpha}{\text{gradient} \times L}$

**Additional detail:**
- **D1**: use set square to ensure ruler vertical
- **D2**: clamp stand securely
- **D3**: repeat and average
- **D4**: measure $\alpha$ using protractor
- **D5**: safety: avoid trapping fingers

</details>

---

### 常见陷阱

:::warning[Spring 陷阱]

- 忘记测量 $N$（匝数通常需要在实验中确定）
- 安全措施只说 "wear safety goggles" 而不说明原因
- 忽略 $\rho$ 的测量或认为 $\rho$ 已知
- 画图时没标注 load / masses

:::

---

## Question Type 2: Electrical Circuit Experiments

### 如何识别

题目涉及电路元件、电压、电流、电阻、电容充放电、电感、互感等。关键词包括 resistor, capacitor, inductor, coil, potential divider, ammeter, voltmeter, transformer, mutual induction。

### 标准解题方法

:::note[Electrical Experiment 框架]

**IV**: 某个电路参数（如电阻 $R$、电容 $C$、匝数比 $n$、距离 $d$ 等）
**DV**: 电流 $I$ / 电压 $V$ / 时间常数 $\tau$ / 感应电动势 $\mathcal{E}$ 等
**CV**: 电源电压、温度、导线电阻、频率（如用交流）等

**关键仪器**: ammeter（串联）, voltmeter（并联）, switch, power supply, rheostat, stopwatch（for capacitor discharge）

:::

#### Example 1 — 9702/s21/qp/51 Q1（15 marks）

> A student investigates how the current $I$ in a coil varies with the resistance $R$ of the coil. The coil is connected in series with a power supply and an ammeter. It is suggested that:
> $$I = \frac{V}{R + r}$$
> where $V$ is the e.m.f. of the power supply and $r$ is the internal resistance.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $R$ is independent, $I$ is dependent / vary $R$ and measure $I$
- **B1**: keep $V$ constant

**Methods of data collection:**
- **B1**: diagram: power supply, coil, ammeter in series, variable resistor to change $R$
- **B1**: vary $R$ using a variable resistor / substitution box
- **B1**: measure $I$ using ammeter
- **B1**: measure $R$ using ohmmeter / known values from box
- **B1**: measure $V$ using voltmeter across supply

**Method of analysis:**
- **B1**: plot $I$ against $1/R$ or $1/I$ against $R$
- **B1**: straight line confirms relationship
- **B1**: $r = \frac{\text{y-intercept}}{\text{gradient}}$ from $1/I$ against $R$

**Additional detail:**
- **D1**: repeat and average $I$
- **D2**: turn off between readings to avoid heating
- **D3**: use rheostat to vary $R$ smoothly
- **D4**: allow time for coil to cool
- **D5**: check for zero error on ammeter

</details>

---

#### Example 2 — 9702/s22/qp/51 Q1（15 marks）

> A student investigates how the capacitance $C$ of a parallel-plate capacitor varies with the separation $d$ of the plates. It is suggested that:
> $$C = \frac{\varepsilon_0 A}{d}$$
> where $A$ is the area of overlap of the plates and $\varepsilon_0$ is the permittivity of free space.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $d$ is independent, $C$ is dependent / vary $d$ and measure $C$
- **B1**: keep $A$ constant

**Methods of data collection:**
- **B1**: diagram: parallel plates connected to capacitance meter / digital multimeter
- **B1**: vary $d$ using a micrometer screw / spacer
- **B1**: measure $d$ using micrometer / ruler
- **B1**: measure $C$ using capacitance meter
- **B1**: measure $A$ using ruler（length $\times$ width）

**Method of analysis:**
- **B1**: plot $C$ against $1/d$
- **B1**: straight line through origin confirms relationship
- **B1**: $\varepsilon_0 = \frac{\text{gradient}}{A}$

**Additional detail:**
- **D1**: repeat and average $C$ at each $d$
- **D2**: ensure plates are parallel using spacers
- **D3**: discharge capacitor before handling
- **D4**: use large $A$ to get measurable $C$
- **D5**: avoid touching plates to maintain insulation

</details>

---

#### Example 3 — 9702/s23/qp/52 Q1（15 marks）

> A student investigates mutual induction between two coils. Coil $P$ is connected to an a.c. power supply. Coil $S$ is placed near $P$ and connected to a voltmeter. The student investigates how the induced e.m.f. $\mathcal{E}$ in coil $S$ depends on the distance $d$ between the centres of the coils. It is suggested that:
> $$\mathcal{E} = \frac{k}{d^n}$$
> where $k$ and $n$ are constants.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $d$ is independent, $\mathcal{E}$ is dependent / vary $d$ and measure $\mathcal{E}$
- **B1**: keep frequency $f$, number of turns $N_P$, $N_S$ constant

**Methods of data collection:**
- **B1**: diagram: a.c. supply connected to $P$, $S$ connected to voltmeter, labelled coils and distance $d$
- **B1**: vary $d$ by moving coils apart on a bench
- **B1**: measure $d$ using metre ruler
- **B1**: measure $\mathcal{E}$ using a.c. voltmeter / oscilloscope
- **B1**: measure frequency using oscilloscope / frequency meter

**Method of analysis:**
- **B1**: plot $\lg \mathcal{E}$ against $\lg d$
- **B1**: straight line confirms relationship
- **B1**: $n = -\text{gradient}$, $\lg k = \text{y-intercept}$

**Additional detail:**
- **D1**: repeat and average
- **D2**: keep coils aligned along same axis
- **D3**: avoid metal objects near coils
- **D4**: use a.c. supply with stabilised voltage
- **D5**: safety: do not touch exposed wires

</details>

---

### 常见陷阱

:::warning[Electrical 陷阱]

- 混淆串联（ammeter）和并联（voltmeter）接法
- 忘记考虑 internal resistance
- 没有断开电源导致元件发热影响结果
- 电容实验忘记放电安全

:::

---

## Question Type 3: Thermal Experiments

### 如何识别

题目涉及温度变化、加热、冷却、热容、热传导等。关键词包括 temperature, specific heat capacity, cooling, heating, Newton's law of cooling, thermal conductivity, rate of cooling。

### 标准解题方法

:::note[Thermal Experiment 框架]

**IV**: 温度 $T$ / 时间 $t$ / 厚度 $x$ / 表面积 $A$ 等
**DV**: 温度变化率 / 冷却速率 / 热量 $Q$ 等
**CV**: 环境温度、液体体积/质量、容器材料、搅拌方式

**关键仪器**: thermometer / temperature sensor, stopwatch, heater, beaker, heat-proof mat, insulation

:::

#### Example 1 — 9702/s21/qp/52 Q1（15 marks）

> A student investigates the cooling of a hot liquid. The liquid is placed in a beaker and allowed to cool. The temperature $\theta$ of the liquid is measured at different times $t$. It is suggested that:
> $$\theta = \theta_0 e^{-kt}$$
> where $\theta_0$ is the initial temperature and $k$ is a constant.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $t$ is independent, $\theta$ is dependent / vary $t$ and measure $\theta$
- **B1**: keep volume of liquid, room temperature, beaker size constant

**Methods of data collection:**
- **B1**: diagram: beaker with liquid, thermometer, stopwatch, labelled
- **B1**: heat liquid to initial temperature then allow to cool
- **B1**: measure $\theta$ using thermometer / temperature sensor at regular $t$
- **B1**: measure $t$ using stopwatch
- **B1**: measure volume using measuring cylinder

**Method of analysis:**
- **B1**: plot $\ln \theta$ against $t$
- **B1**: straight line confirms relationship
- **B1**: $k = -\text{gradient}$

**Additional detail:**
- **D1**: stir liquid before each reading for uniform temperature
- **D2**: repeat experiment and average
- **D3**: use insulation around beaker
- **D4**: safety: use heat-proof mat and tongs
- **D5**: ensure room temperature is constant

</details>

---

#### Example 2 — 9702/s24/qp/51 Q1（15 marks）

> A student investigates how the rate of cooling of a liquid depends on the surface area $A$ of the liquid exposed to the air. The liquid is heated to a fixed initial temperature and then allowed to cool. It is suggested that:
> $$\frac{\Delta\theta}{\Delta t} = -\frac{hA}{mc}(\theta - \theta_{\text{room}})$$
> where $h$ is a constant, $m$ is the mass of the liquid and $c$ is the specific heat capacity.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $A$ is independent, $\Delta\theta/\Delta t$ is dependent / vary $A$ and measure rate of cooling
- **B1**: keep $m$, initial $\theta$, $\theta_{\text{room}}$ constant

**Methods of data collection:**
- **B1**: diagram: beaker of liquid, thermometer, stopwatch, dimension labelled
- **B1**: vary $A$ by using beakers of different diameters
- **B1**: measure diameter using ruler / vernier calipers
- **B1**: measure $\theta$ using thermometer at regular $t$ intervals
- **B1**: measure $m$ using top-pan balance

**Method of analysis:**
- **B1**: plot $\frac{\Delta\theta}{\Delta t}$ against $A$ or rate against $A$
- **B1**: straight line confirms relationship
- **B1**: $h = \frac{\text{gradient} \times mc}{(\theta - \theta_{\text{room}})}$

**Additional detail:**
- **D1**: repeat and average
- **D2**: use lid with hole for thermometer to reduce evaporation
- **D3**: start timing when temperature reaches set point
- **D4**: use a data logger for continuous recording
- **D5**: safety: use heat-proof mat

</details>

---

### 常见陷阱

:::warning[Thermal 陷阱]

- 忘记搅拌液体导致温度不均匀
- 环境温度变化影响实验结果
- 液体蒸发导致质量变化未被考虑
- 加热时忘记使用隔热措施

:::

---

## Question Type 4: Wave Experiments

### 如何识别

题目涉及波、振动、频率、波长、驻波、声速等。关键词包括 standing wave, stationary wave, frequency, wavelength, sound, vibrating string, air column, resonance, speed of sound。

### 标准解题方法

:::note[Wave Experiment 框架]

**IV**: 频率 $f$ / 长度 $L$ / 张力 $T$ / 线密度 $\mu$ 等
**DV**: 波长 $\lambda$ / 驻波节点数 $n$ / 谐振位置等
**CV**: 温度（影响声速）、线密度、振幅

**关键仪器**: signal generator, loudspeaker / vibrator, metre ruler, microphone / CRO, oscillator

:::

#### Example 1 — 9702/s20/qp/52 Q1（15 marks）

> A student investigates stationary waves on a stretched string. One end of the string is attached to a vibrator connected to a signal generator. The other end passes over a pulley and carries a load of mass $m$. The student investigates how the wavelength $\lambda$ of the stationary wave varies with the tension $T$ in the string. It is suggested that:
> $$\lambda = \frac{1}{f}\sqrt{\frac{T}{\mu}}$$
> where $f$ is the frequency and $\mu$ is the mass per unit length of the string.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $T$ is independent, $\lambda$ is dependent / vary $T$ and measure $\lambda$
- **B1**: keep $f$ and $\mu$ constant

**Methods of data collection:**
- **B1**: diagram: string, vibrator, pulley, masses, signal generator, labelled
- **B1**: vary $T$ by changing mass $m$ on the pulley
- **B1**: measure $T = mg$ using top-pan balance for $m$
- **B1**: measure $\lambda$ using ruler（distance between adjacent nodes $\times 2$）
- **B1**: adjust frequency to get clear standing wave / measure $f$ using signal generator

**Method of analysis:**
- **B1**: plot $\lambda$ against $\sqrt{T}$ or $\lambda^2$ against $T$
- **B1**: straight line through origin confirms relationship
- **B1**: $\mu = \frac{1}{f^2 \times \text{gradient}^2}$ or from $\lambda^2$ graph

**Additional detail:**
- **D1**: repeat measurement of $\lambda$ at different positions
- **D2**: measure $\mu$ by weighing known length of string
- **D3**: ensure string is horizontal between pulley and vibrator
- **D4**: safety: stand clear of breaking string
- **D5**: use marker to identify node positions

</details>

---

#### Example 2 — 9702/w21/qp/51 Q1（15 marks）

> A student investigates the speed of sound in air using a resonance tube. A tuning fork of frequency $f$ is held above the open end of a tube partially filled with water. The length $L$ of the air column is adjusted until resonance is heard. It is suggested that:
> $$f = \frac{v}{4(L + c)}$$
> where $v$ is the speed of sound and $c$ is the end correction.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $L$ is independent, $f$ is dependent / vary $L$ and measure $f$
- **B1**: keep temperature constant（affects $v$）

**Methods of data collection:**
- **B1**: diagram: resonance tube, water reservoir, tuning fork, ruler, labelled
- **B1**: vary $L$ by adjusting water level
- **B1**: measure $L$ using metre ruler
- **B1**: measure $f$ using frequency of tuning fork（known / calibrated）
- **B1**: use set of tuning forks of different frequencies

**Method of analysis:**
- **B1**: plot $1/f$ against $L$ or $L$ against $1/f$
- **B1**: straight line confirms relationship
- **B1**: $v = 4 \times \text{gradient}$, $c = \text{y-intercept} / (-\text{gradient})$

**Additional detail:**
- **D1**: repeat at different $L$ for same $f$
- **D2**: measure temperature using thermometer
- **D3**: strike tuning fork on rubber pad（not hard surface）
- **D4**: hold tuning fork at same height
- **D5**: ensure tube is vertical using set square

</details>

---

#### Example 3 — 9702/s23/qp/51 Q1（15 marks）

> A student investigates how the speed $v$ of a wave on a stretched string depends on the tension $T$. It is suggested that:
> $$v = \sqrt{\frac{T}{\mu}}$$
> where $\mu$ is the mass per unit length. The student measures the frequency $f$ and wavelength $\lambda$ to determine $v$. It is suggested that:
> $$f = \frac{n}{2L}\sqrt{\frac{T}{\mu}}$$
> where $n$ is the number of loops in the standing wave and $L$ is the length of the string.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $T$ is independent, $f$ is dependent / vary $T$ and measure $f$
- **B1**: keep $L$, $\mu$, $n$ constant

**Methods of data collection:**
- **B1**: diagram: string, vibrator, pulley, masses, signal generator, labelled with $L$
- **B1**: vary $T$ by adding masses to the hanger
- **B1**: measure $T = mg$ using balance
- **B1**: measure $f$ from signal generator / stroboscope / CRO
- **B1**: measure $L$ using ruler

**Method of analysis:**
- **B1**: plot $f$ against $\sqrt{T}$
- **B1**: straight line through origin confirms relationship
- **B1**: $\mu = \left(\frac{n}{2L \times \text{gradient}}\right)^2$

**Additional detail:**
- **D1**: repeat and average
- **D2**: measure $\mu$ by weighing a known length of string
- **D3**: ensure pulley is frictionless
- **D4**: adjust frequency to get stable $n$ loops
- **D5**: use marker to identify node positions

</details>

---

### 常见陷阱

:::warning[Wave 陷阱]

- 驻波中 node 和 antinode 混淆
- 忘记 end correction $c$（resonance tube）
- 线密度 $\mu$ 的测量方法不具体
- 频率计/信号发生器的使用没说明

:::

---

## Question Type 5: Damped Oscillations — Copper Sheet in Magnetic Field

### 如何识别

题目涉及金属片在磁场中摆动、振幅衰减、涡流阻尼。关键词包括 damped oscillations, copper sheet, magnetic field, eddy current, amplitude decay, electromagnetic braking。

### 标准解题方法

:::note[Damped Oscillations 框架]

**IV**: 金属片面积 $A$ / 厚度 $z$
**DV**: 5 次摆动后的距离 $s$ / 停止时间 $t$
**CV**: 磁场强度 $B$、初始位移 $s_0$、材料类型

**关键关系**: $s = s_0 e^{-ABKt}$，振幅随面积指数衰减

**测量 $t$**: 用 stopwatch 测量从释放到停止的时间
**测量 $A$**: 用 ruler 测长宽计算面积

:::

#### Example 1 — 9702/w22/qp/51 Q1（15 marks）

> A student investigates the damping of oscillations of a copper sheet placed between the poles of a strong magnet. The sheet is suspended by a thread and set into oscillation. The amplitude of the oscillations decreases due to eddy currents induced in the sheet. It is suggested that the distance $s$ moved by the sheet after 5 complete oscillations is given by:
> $$s = s_0 e^{-ABKt}$$
> where $s_0$ is the initial amplitude, $A$ is the area of the sheet, $B$ is the magnetic flux density, $K$ is a constant and $t$ is the thickness of the sheet.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: cross-sectional area $A$ is the independent variable, distance $s$ after 5 oscillations is the dependent variable / vary $A$ and measure $s$
- **B1**: keep $s_0$, $B$, $t$ constant

**Methods of data collection:**
- **B1**: diagram: copper sheet suspended by thread between magnet poles, ruler beside to measure amplitude
- **B1**: use sheets of different area $A$（vary length/width）
- **B1**: measure $A$ using ruler / vernier calipers（$A = \text{length} \times \text{width}$）
- **B1**: measure $s$ using ruler adjacent to sheet
- **B1**: measure $t$ using micrometer

**Method of analysis:**
- **B1**: plot $\ln s$ against $A$
- **B1**: straight line confirms relationship $s = s_0 e^{-ABKt}$
- **B1**: $K = -\frac{\text{gradient}}{B t}$

**Additional detail:**
- **D1**: repeat and average $s$ at each $A$
- **D2**: ensure same initial displacement $s_0$ using marker / release mechanism
- **D3**: use marker on sheet for consistent reading point
- **D4**: avoid air currents / draughts
- **D5**: safety: cushion in case sheet falls

</details>

---

#### Example 2 — 9702/w22/qp/52 Q1（15 marks）

> A student investigates how the time $t$ taken for a copper sheet to stop oscillating depends on the thickness $z$ of the sheet. The sheet is suspended between the poles of a magnet and set into oscillation. It is suggested that:
> $$t = \frac{K z^q}{A B \rho}$$
> where $A$ is the area of the sheet, $B$ is the magnetic flux density, $\rho$ is the resistivity of copper and $K$ and $q$ are constants.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: thickness $z$ is the independent variable, time $t$ is the dependent variable / vary $z$ and measure $t$
- **B1**: keep $A$, $B$ constant

**Methods of data collection:**
- **B1**: diagram: copper sheet suspended, magnet poles, stopwatch, labelled
- **B1**: use sheets of different thickness $z$（same area $A$）
- **B1**: measure $z$ using micrometer
- **B1**: measure $t$ using stopwatch（from release to rest）
- **B1**: measure $A$ using ruler

**Method of analysis:**
- **B1**: plot $\lg t$ against $\lg z$
- **B1**: straight line confirms relationship
- **B1**: $q = \text{gradient}$, $\lg K = \text{y-intercept} + \lg(A B \rho)$

**Additional detail:**
- **D1**: repeat and average $t$
- **D2**: use same initial amplitude for each trial
- **D3**: ensure magnet poles are aligned
- **D4**: clamp magnet securely
- **D5**: safety: gloves for sharp edges of sheet

</details>

---

### 常见陷阱

:::warning[Damped Oscillations 陷阱]

- 忘记说明如何确保每次初始振幅相同
- 测量 $s$ 时视差问题未处理
- 忽略空气流动对阻尼的影响
- 磁场强度 $B$ 的恒定性未考虑

:::

---

## Question Type 6: Ballistic Pendulum / Projectile Motion

### 如何识别

题目涉及抛射体撞击摆锤、摆动高度与质量关系。关键词包括 ballistic pendulum, projectile, clay block, pendulum, conservation of momentum, height of swing。

### 标准解题方法

:::note[Ballistic Pendulum 框架]

**IV**: 抛射体质量 $Z$
**DV**: 摆锤摆动高度 $h$
**CV**: 摆锤质量 $M$、初速度 $u$、重力加速度 $g$

**关键关系**: $h = \frac{u^2}{2g}\left(\frac{Z}{M+Z}\right)^2$

**测量 $h$**: 用 ruler / protractor 测最大摆动高度
**测量 $Z$**: 用 top-pan balance 称质量

:::

#### Example 1 — 9702/w23/qp/51 Q1（15 marks）

> A student investigates the behaviour of a ballistic pendulum. A projectile of mass $Z$ is fired horizontally into a stationary block of clay of mass $M$ suspended as a pendulum. The projectile embeds itself in the clay and the pendulum swings to a maximum height $h$. It is suggested that:
> $$h = \frac{u^2}{2g}\left(\frac{Z}{M+Z}\right)^2$$
> where $u$ is the speed of the projectile and $g$ is the acceleration of free fall.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: mass of projectile $Z$ is the independent variable, height $h$ is the dependent variable / vary $Z$ and measure $h$
- **B1**: keep $M$, $u$ constant

**Methods of data collection:**
- **B1**: diagram: pendulum with clay block, projectile gun, ruler to measure $h$, labelled
- **B1**: use projectiles of different mass $Z$
- **B1**: measure $Z$ using top-pan balance
- **B1**: measure $h$ using ruler / marker on the scale behind pendulum
- **B1**: measure $M$ using top-pan balance

**Method of analysis:**
- **B1**: plot $\sqrt{h}$ against $\frac{Z}{M+Z}$ or $h$ against $\left(\frac{Z}{M+Z}\right)^2$
- **B1**: straight line through origin confirms relationship
- **B1**: $u = \sqrt{2g \times \text{gradient}}$ for $h$ vs $\left(\frac{Z}{M+Z}\right)^2$

**Additional detail:**
- **D1**: repeat and average $h$ for each $Z$
- **D2**: ensure pendulum swings freely without friction
- **D3**: use plumb line to check vertical alignment
- **D4**: use safety screen around apparatus
- **D5**: safety: stand clamped securely, wear goggles

</details>

---

#### Example 2 — 9702/w23/qp/53 Q1（15 marks）

> A student investigates how the angle $\theta$ of swing of a ballistic pendulum depends on the mass $m$ of the projectile. A projectile of mass $m$ is fired into a stationary pendulum of mass $M$. The pendulum swings to a maximum angle $\theta$. It is suggested that:
> $$\cos\theta = 1 - \frac{u^2}{2gL}\left(\frac{m}{M+m}\right)^2$$
> where $L$ is the length of the pendulum and $u$ is the speed of the projectile.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $m$ is independent, $\theta$ is dependent / vary $m$ and measure $\theta$
- **B1**: keep $M$, $L$, $u$ constant

**Methods of data collection:**
- **B1**: diagram: pendulum, protractor to measure $\theta$, projectile launcher, labelled
- **B1**: vary $m$ using projectiles of different masses
- **B1**: measure $m$ using top-pan balance
- **B1**: measure $\theta$ using protractor at maximum swing
- **B1**: measure $L$ using ruler

**Method of analysis:**
- **B1**: plot $\cos\theta$ against $\left(\frac{m}{M+m}\right)^2$ or $\theta$ against $m$
- **B1**: straight line confirms relationship
- **B1**: $u = \sqrt{-2gL \times \text{gradient}}$

**Additional detail:**
- **D1**: repeat and average $\theta$
- **D2**: use marker on the scale to read $\theta$ consistently
- **D3**: ensure projectile is fired horizontally
- **D4**: clamp stand securely
- **D5**: safety: stand behind safety screen

</details>

---

### 常见陷阱

:::warning[Ballistic Pendulum 陷阱]

- 忘记保持 $u$ 恒定（需要相同的发射装置/弹簧压缩量）
- 没说明如何测量 $h$（从起始位置到最高点）
- 空气阻力和摩擦力忽略导致系统误差
- 摆长 $L$ 未测量

:::

---

## Question Type 7: Capillary Rise / Surface Tension

### 如何识别

题目涉及毛细管中液面上升高度与管径关系、表面张力测量。关键词包括 capillary, surface tension, meniscus, tube diameter, rise height, adhesion。

### 标准解题方法

:::note[Capillary Rise 框架]

**IV**: 毛细管直径 $d$
**DV**: 液面上升高度 $h$
**CV**: 液体种类（$\rho$、$\gamma$）、温度

**关键关系**: $h = \frac{4\gamma}{d\rho g}$

**测量 $h$**: 用 travelling microscope 或 ruler 配合 set square 读取弯月面底部
**测量 $d$**: 用 travelling microscope / micrometer

:::

#### Example 1 — 9702/w20/qp/52 Q1（15 marks）

> A student investigates the rise of water in capillary tubes of different diameters. The student places a capillary tube vertically into a container of water and measures the height $h$ to which the water rises above the surface of the water in the container. It is suggested that the height $h$ is related to the diameter $d$ of the tube by:
> $$h = \frac{4\gamma}{d\rho g}$$
> where $\gamma$ is the surface tension of the water, $\rho$ is the density of water and $g$ is the acceleration of free fall.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: diameter $d$ is the independent variable, height $h$ is the dependent variable / vary $d$ and measure $h$
- **B1**: keep temperature, liquid type constant

**Methods of data collection:**
- **B1**: diagram: capillary tube in water container, ruler / travelling microscope beside tube, labelled
- **B1**: use capillary tubes of different internal diameters $d$
- **B1**: measure $d$ using travelling microscope / micrometer
- **B1**: measure $h$ using travelling microscope / ruler with set square
- **B1**: measure temperature using thermometer

**Method of analysis:**
- **B1**: plot $h$ against $1/d$
- **B1**: straight line through origin confirms relationship
- **B1**: $\gamma = \frac{\rho g \times \text{gradient}}{4}$

**Additional detail:**
- **D1**: repeat and average $h$ for each tube
- **D2**: ensure tube is vertical using set square
- **D3**: measure from water surface to bottom of meniscus
- **D4**: clean tubes thoroughly before use
- **D5**: use dye in water to improve visibility

</details>

---

### 常见陷阱

:::warning[Capillary Rise 陷阱]

- 弯月面读数位置不明确（应读底部）
- 忘记清洁毛细管（污染影响表面张力）
- 温度变化导致 $\gamma$ 和 $\rho$ 变化
- 毛细管未完全垂直放置

:::

---

## Question Type 8: LR Circuit / Time Constant

### 如何识别

题目涉及电感线圈、电阻、时间常数、电流上升/衰减。关键词包括 inductor, LR circuit, time constant, current growth, decay, coil, resistance。

### 标准解题方法

:::note[LR Circuit 框架]

**IV**: 电阻 $R$
**DV**: 电流达到最大值的时间 $t$
**CV**: 线圈匝数 $N$、线圈面积 $A$、线圈长度 $L$

**关键关系**: $t = \frac{K N^2 A}{L R}$

**测量 $t$**: stopwatch 测量从闭合开关到电流达到某值的时间
**测量 $R$**: ohmmeter / 从电阻箱读取

:::

#### Example 1 — 9702/s21/qp/51 Q1（15 marks）

> A student investigates how the time $t$ for the current in an LR circuit to reach a maximum value depends on the resistance $R$ in the circuit. The circuit consists of a coil connected in series with a variable resistor, a switch, and a power supply. It is suggested that:
> $$t = \frac{K N^2 A}{L R}$$
> where $N$ is the number of turns on the coil, $A$ is the cross-sectional area of the coil, $L$ is the length of the coil and $K$ is a constant.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: resistance $R$ is the independent variable, time $t$ is the dependent variable / vary $R$ and measure $t$
- **B1**: keep $N$, $A$, $L$ constant

**Methods of data collection:**
- **B1**: diagram: power supply, coil, variable resistor, ammeter, switch in series, stopwatch
- **B1**: vary $R$ using a variable resistor / resistance box
- **B1**: measure $R$ using ohmmeter / read from resistance box
- **B1**: measure $t$ using stopwatch（from switch closing to current reaching maximum）
- **B1**: measure $I$ using ammeter to identify when maximum is reached

**Method of analysis:**
- **B1**: plot $t$ against $1/R$
- **B1**: straight line through origin confirms relationship
- **B1**: $K = \frac{L \times \text{gradient}}{N^2 A}$

**Additional detail:**
- **D1**: repeat and average $t$
- **D2**: switch off between readings to avoid heating
- **D3**: measure $N$ by counting turns
- **D4**: measure $A$ using ruler（$A = \pi d^2/4$）
- **D5**: safety: switch off before changing resistor

</details>

---

#### Example 2 — 9702/s21/qp/53 Q1（15 marks）

> A student investigates the growth of current in an LR circuit. A coil of inductance $L_c$ and resistance $R_c$ is connected in series with a resistor of resistance $R$ and a battery. The student measures the time $T$ taken for the current to reach half its final value. It is suggested that:
> $$T = \frac{L_c \ln 2}{R + R_c}$$
> where $L_c$ is the inductance of the coil.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $R$ is independent, $T$ is dependent / vary $R$ and measure $T$
- **B1**: keep $L_c$, $R_c$ constant

**Methods of data collection:**
- **B1**: diagram: coil, resistor, ammeter, switch, battery in series, stopwatch
- **B1**: vary $R$ using a variable resistor
- **B1**: measure $R$ using ohmmeter
- **B1**: measure $T$ using stopwatch（switch on, stop when $I = I_{\text{max}}/2$）
- **B1**: measure $I_{\text{max}}$ using ammeter

**Method of analysis:**
- **B1**: plot $T$ against $1/(R + R_c)$
- **B1**: straight line through origin confirms relationship
- **B1**: $L_c = \frac{\text{gradient}}{\ln 2}$

**Additional detail:**
- **D1**: repeat and average $T$
- **D2**: allow coil to cool between readings
- **D3**: use a data logger for precise timing
- **D4**: ensure switch makes good contact
- **D5**: safety: disconnect supply when not in use

</details>

---

### 常见陷阱

:::warning[LR Circuit 陷阱]

- 忽略线圈自身电阻 $R_c$
- 电流最大值判断不准确
- 开关接触电阻未考虑
- 线圈发热导致电感变化

:::

---

## Question Type 9: Doppler Effect

### 如何识别

题目涉及运动声源、观察频率变化、多普勒效应。关键词包括 Doppler effect, moving source, observed frequency, speed of source, signal generator。

### 标准解题方法

:::note[Doppler Effect 框架]

**IV**: 声源速度 $v$
**DV**: 观察频率 $f$
**CV**: 声源频率 $f_s$、声速 $k$

**关键关系**: $f = \frac{f_s k}{k - v}$

**测量 $f$**: 用 microphone 连接 data logger / CRO 测量频率
**测量 $v$**: 用 light gates / motion sensor 测声源速度

:::

#### Example 1 — 9702/s24/qp/51 Q1（15 marks）

> A student investigates the Doppler effect using a loudspeaker attached to a moving trolley. The loudspeaker emits a sound of constant frequency $f_s$ from a signal generator. The trolley moves towards a stationary microphone connected to a data logger. It is suggested that the frequency $f$ measured by the microphone is given by:
> $$f = \frac{f_s k}{k - v}$$
> where $k$ is the speed of sound and $v$ is the speed of the trolley.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: speed of trolley $v$ is the independent variable, measured frequency $f$ is the dependent variable / vary $v$ and measure $f$
- **B1**: keep $f_s$, $k$ constant（$k$ depends on temperature）

**Methods of data collection:**
- **B1**: diagram: trolley with loudspeaker, signal generator, microphone, light gates, data logger, labelled
- **B1**: vary $v$ by adjusting the slope / pushing force on trolley
- **B1**: measure $v$ using light gates connected to timer
- **B1**: measure $f$ using microphone connected to data logger / CRO
- **B1**: measure $f_s$ using signal generator reading / CRO

**Method of analysis:**
- **B1**: plot $1/f$ against $1/v$ or $f$ against $1/(k - v)$
- **B1**: straight line confirms relationship
- **B1**: $k = \frac{f_s \times \text{gradient}}{\text{gradient} - 1}$（depending on linearised form）

**Additional detail:**
- **D1**: repeat and average $f$ at each $v$
- **D2**: measure temperature using thermometer to estimate $k$
- **D3**: ensure trolley moves directly towards microphone
- **D4**: use a long run-up for steady speed
- **D5**: safety: ensure trolley path is clear

</details>

---

#### Example 2 — 9702/s24/qp/53 Q1（15 marks）

> A student investigates how the observed wavelength $\lambda$ of sound from a moving source depends on the speed $v$ of the source. The source emits sound of frequency $f_s$ and moves away from a stationary observer. It is suggested that:
> $$\lambda = \frac{k + v}{f_s}$$
> where $k$ is the speed of sound.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $v$ is independent, $\lambda$ is dependent / vary $v$ and measure $\lambda$
- **B1**: keep $f_s$, $k$ constant

**Methods of data collection:**
- **B1**: diagram: moving loudspeaker, stationary microphone, ruler, signal generator, labelled
- **B1**: vary $v$ using trolley at different speeds
- **B1**: measure $v$ using light gates
- **B1**: measure $\lambda$ using microphone and CRO（distance between successive wavefronts）
- **B1**: measure $f_s$ using signal generator

**Method of analysis:**
- **B1**: plot $\lambda$ against $v$
- **B1**: straight line confirms relationship
- **B1**: gradient $= 1/f_s$, y-intercept $= k/f_s$ → find $k$

**Additional detail:**
- **D1**: repeat and average $\lambda$
- **D2**: use data logger for accurate frequency measurement
- **D3**: minimise background noise
- **D4**: ensure microphone is aligned with source path
- **D5**: safety: secure all cables to avoid tripping

</details>

---

### 常见陷阱

:::warning[Doppler Effect 陷阱]

- 声速 $k$ 受温度影响但未测量温度
- 声源是否做匀速运动未确认
- microphone 和 data logger 的采样率不足
- 公式中 $v$ 的符号（接近/远离）混淆

:::

---

## Question Type 10: Resistivity / Wheatstone Bridge

### 如何识别

题目涉及电阻率、金属丝电阻与尺寸关系、Wheatstone 桥电路。关键词包括 resistivity, Wheatstone bridge, wire diameter, length, resistance ratio。

### 标准解题方法

:::note[Resistivity / Wheatstone Bridge 框架]

**IV**: 金属丝长度 $L$ / 直径 $d$
**DV**: 电阻比 $Z/R$（从 bridge 平衡获得）
**CV**: 材料电阻率 $\rho$、温度

**关键关系**: $\frac{Z}{R} = \frac{4\rho L}{\pi Y d^2}$

**测量 $d$**: 用 micrometer 在不同位置测量取平均
**测量 $L$**: 用 ruler

:::

#### Example 1 — 9702/w22/qp/51 Q1（15 marks）

> A student uses a Wheatstone bridge to determine how the ratio $Z/R$ of resistances depends on the length $L$ of a metal wire of diameter $d$. The wire forms part of one arm of the bridge. It is suggested that:
> $$\frac{Z}{R} = \frac{4\rho L}{\pi Y d^2}$$
> where $\rho$ is the resistivity of the metal and $Y$ is a constant.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: length $L$ is the independent variable, ratio $Z/R$ is the dependent variable / vary $L$ and measure $Z/R$
- **B1**: keep $d$, $\rho$, temperature constant

**Methods of data collection:**
- **B1**: diagram: Wheatstone bridge circuit with wire of length $L$, galvanometer, labelled
- **B1**: vary $L$ by using wires of different lengths
- **B1**: measure $L$ using ruler
- **B1**: measure $Z/R$ from balance point on bridge / known resistor values
- **B1**: measure $d$ using micrometer（at several points, average）

**Method of analysis:**
- **B1**: plot $Z/R$ against $L$
- **B1**: straight line through origin confirms relationship
- **B1**: $\rho = \frac{\pi Y d^2 \times \text{gradient}}{4}$

**Additional detail:**
- **D1**: repeat balance measurement and average
- **D2**: avoid heating by switching off between readings
- **D3**: clean wire ends for good electrical contact
- **D4**: use short pulses of current to minimise heating
- **D5**: safety: disconnect power when adjusting circuit

</details>

---

#### Example 2 — 9702/w22/qp/53 Q1（15 marks）

> A student investigates how the resistance $X$ of a metal wire varies with its diameter $d$. The wire is connected in one arm of a Wheatstone bridge. It is suggested that:
> $$X = \frac{4\rho L}{\pi d^2}$$
> where $L$ is the length of the wire and $\rho$ is the resistivity of the metal.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: $d$ is independent, $X$ is dependent / vary $d$ and measure $X$
- **B1**: keep $L$, $\rho$, temperature constant

**Methods of data collection:**
- **B1**: diagram: Wheatstone bridge circuit, wire under test, labelled
- **B1**: vary $d$ by using wires of different diameters
- **B1**: measure $d$ using micrometer
- **B1**: measure $X$ using Wheatstone bridge balance / ohmmeter
- **B1**: measure $L$ using ruler

**Method of analysis:**
- **B1**: plot $X$ against $1/d^2$ or $\lg X$ against $\lg d$
- **B1**: straight line through origin（or straight line for log-log）confirms relationship
- **B1**: $\rho = \frac{\pi \times \text{gradient}}{4L}$ from $X$ vs $1/d^2$

**Additional detail:**
- **D1**: repeat and average $X$
- **D2**: measure $d$ at several points along wire
- **D3**: stretch wire to remove kinks before measuring
- **D4**: use a constant current to prevent heating
- **D5**: safety: avoid touching bare wires

</details>

---

### 常见陷阱

:::warning[Resistivity / Wheatstone Bridge 陷阱]

- 直径 $d$ 只测一端不取平均
- 忘记温度对电阻率的影响
- 接触电阻未消除
- 桥路平衡判断不准确（galvanometer 灵敏度）

:::

---

## Question Type 11: Stellar Physics (lg-lg Plots)

### 如何识别

题目涉及恒星物理数据、光度与质量关系、对数坐标图。关键词包括 luminosity, mass, star, stellar, lg-lg plot, data analysis, published data。

### 标准解题方法

:::note[Stellar Physics 框架]

**IV**: 恒星质量 $M$
**DV**: 恒星光度 $L$
**CV**: 数据来源可靠性

**关键关系**: $L = S Z M^n$，线性化为 $\lg L = \lg(SZ) + n \lg M$

**注意**: 此题型通常为 Q2（数据分析），但可作为 Q1（实验规划）出现，需要学生从文献/数据库获取数据

**数据处理**: 用 $\lg L$ 对 $\lg M$ 作图求 $n$ 和常数

:::

#### Example 1 — 9702/s22/qp/51 Q1（15 marks）

> A student investigates the relationship between the luminosity $L$ of a main sequence star and its mass $M$. The student uses published data from a star catalogue. It is suggested that:
> $$L = S Z M^n$$
> where $S$ and $Z$ are known constants for the star and $n$ is a constant to be determined.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: mass $M$ is the independent variable, luminosity $L$ is the dependent variable
- **B1**: use stars of the same type（main sequence）to keep composition constant

**Methods of data collection:**
- **B1**: obtain data from published star catalogue / database
- **B1**: select stars with known mass $M$ and luminosity $L$
- **B1**: record $M$ in solar masses $M_\odot$ and $L$ in solar luminosities $L_\odot$
- **B1**: use a wide range of $M$ values for reliable graph
- **B1**: ensure data is from reliable sources

**Method of analysis:**
- **B1**: plot $\lg L$ against $\lg M$
- **B1**: straight line confirms relationship
- **B1**: $n = \text{gradient}$, $\lg(SZ) = \text{y-intercept}$

**Additional detail:**
- **D1**: include error bars on graph if uncertainty given
- **D2**: use at least 6 data points
- **D3**: check for outliers in published data
- **D4**: state assumptions（stars are main sequence）
- **D5**: reference data sources in report

</details>

---

#### Example 2 — 9702/s22/qp/52 Q1（15 marks）

> A student investigates how the temperature $T$ of a star relates to its colour index $C$. The student collects data from an astronomical database. It is suggested that:
> $$T = \frac{a}{C + b}$$
> where $a$ and $b$ are constants.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: colour index $C$ is the independent variable, temperature $T$ is the dependent variable
- **B1**: select stars of similar spectral type to minimise variation

**Methods of data collection:**
- **B1**: obtain data from astronomical database / star catalogue
- **B1**: record $T$ and $C$ for a range of stars
- **B1**: ensure data covers a wide range of $C$
- **B1**: use data processed by standard methods

**Method of analysis:**
- **B1**: plot $1/T$ against $C$
- **B1**: straight line confirms relationship
- **B1**: $a = 1/\text{gradient}$, $b = \text{y-intercept} / \text{gradient}$

**Additional detail:**
- **D1**: consider uncertainties in published data
- **D2**: use data from multiple sources for verification
- **D3**: check that temperature scale is consistent
- **D4**: note any selection bias in data
- **D5**: calibrate using known standard stars

</details>

---

### 常见陷阱

:::warning[Stellar Physics 陷阱]

- 混淆 $\lg$ 和 $\ln$
- 数据的 uncertainty 未考虑
- 选择的恒星不是同一类型
- 对数图的坐标轴标签不完整

:::

---

## Question Type 12: Gas Laws (pV vs T / V vs θ)

### 如何识别

题目涉及理想气体、压强-体积-温度关系、恒温/恒压实验。关键词包括 gas law, Boyle's law, Charles' law, pressure, volume, temperature, gas syringe, water bath。

### 标准解题方法

:::note[Gas Laws 框架]

**IV**: 温度 $\theta$
**DV**: $pV$ 乘积 / $V$ 体积
**CV**: 气体质量 $n$（物质的量）、体积（如定容）

**关键关系**: $pV = Y k (\theta + Z)$

**测量 $p$**: 用 pressure gauge / manometer
**测量 $V$**: 用 gas syringe / ruler（测柱体长度）
**控制 $\theta$**: 用 water bath + thermometer

:::

#### Example 1 — 9702/s23/qp/52 Q1（15 marks）

> A student investigates how the product $pV$ of pressure and volume of a fixed mass of gas varies with temperature $\theta$. The gas is contained in a syringe placed in a water bath. The temperature is changed by heating or cooling the water. It is suggested that:
> $$pV = Y k (\theta + Z)$$
> where $Y$, $k$ and $Z$ are constants.

<details>
<summary>MS 展开查看</summary>

**Defining the problem:**
- **B1**: temperature $\theta$ is the independent variable, $pV$ product is the dependent variable / vary $\theta$ and measure $p$ and $V$
- **B1**: keep mass of gas constant（sealed system）

**Methods of data collection:**
- **B1**: diagram: gas syringe in water bath, thermometer, pressure gauge, labelled
- **B1**: vary $\theta$ by using water at different temperatures
- **B1**: measure $\theta$ using thermometer / temperature sensor
- **B1**: measure $p$ using pressure gauge connected to syringe
- **B1**: measure $V$ using scale on syringe / ruler

**Method of analysis:**
- **B1**: plot $pV$ against $\theta$
- **B1**: straight line confirms relationship
- **B1**: $Z = -\text{intercept}/\text{gradient}$, $Yk = \text{gradient}$

**Additional detail:**
- **D1**: repeat and average $p$ and $V$ at each $\theta$
- **D2**: stir water bath for even temperature
- **D3**: allow time for gas to reach thermal equilibrium
- **D4**: clamp syringe securely
- **D5**: safety: use heat-proof gloves for hot water

</details>

---

### 常见陷阱

:::warning[Gas Laws 陷阱]

- 忘记气体必须达到热平衡就读数
- 水浴温度不均匀
- 气体泄漏导致质量变化
- 压强单位与体积单位不匹配导致计算错误

:::

---

## 题型对比总结（完整版）

| 题型 | 常见 IV | 常见 DV | 典型 CV | 分析图 |
|------|---------|---------|---------|--------|
| Spring | $A$, $t$, $w$, $\theta$ | $k$, $x$ | $N$, $\rho$, $m$ | $\lg k$ vs $\lg A$ / $k$ vs $A^{-3/2}$ |
| Electrical | $R$, $d$, $n$ | $I$, $V$, $C$, $\mathcal{E}$ | $V$, $f$, $A$ | $C$ vs $1/d$ / $\lg \mathcal{E}$ vs $\lg d$ |
| Thermal | $t$, $A$ | $\theta$, rate | volume, $\theta_{\text{room}}$ | $\ln \theta$ vs $t$ / rate vs $A$ |
| Wave | $T$, $L$, $f$ | $\lambda$, $f$, $v$ | $\mu$, temperature | $\lambda$ vs $\sqrt{T}$ / $1/f$ vs $L$ |
| Damped Oscillations | $A$, $z$ | $s$, $t$ | $B$, $s_0$, material | $\ln s$ vs $A$ / $\lg t$ vs $\lg z$ |
| Ballistic Pendulum | $Z$, $m$ | $h$, $\theta$ | $M$, $u$, $L$ | $\sqrt{h}$ vs $Z/(M+Z)$ / $\cos\theta$ vs $(m/(M+m))^2$ |
| Capillary Rise | $d$ | $h$ | liquid, temperature | $h$ vs $1/d$ |
| LR Circuit | $R$ | $t$, $T$ | $N$, $A$, $L$ | $t$ vs $1/R$ / $T$ vs $1/(R+R_c)$ |
| Doppler Effect | $v$ | $f$, $\lambda$ | $f_s$, $k$ | $1/f$ vs $1/v$ / $\lambda$ vs $v$ |
| Resistivity / Bridge | $L$, $d$ | $Z/R$, $X$ | $\rho$, temperature | $Z/R$ vs $L$ / $X$ vs $1/d^2$ |
| Stellar Physics | $M$, $C$ | $L$, $T$ | star type | $\lg L$ vs $\lg M$ / $1/T$ vs $C$ |
| Gas Laws | $\theta$ | $pV$, $V$ | $n$, mass of gas | $pV$ vs $\theta$ |
