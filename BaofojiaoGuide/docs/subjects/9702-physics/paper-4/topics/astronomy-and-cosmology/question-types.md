---
title: Question Types
sidebar_position: 2
---

# Question Types — Astronomy and Cosmology

## Question Type 1: Luminosity and radiant flux intensity

### 如何识别
题目给出恒星 luminosity $L$ 和距离 $d$，要求计算 radiant flux intensity $F$，或反推距离。

### 标准解题方法
:::note[标准解题方法]
1. $F = L / (4\pi d^2)$
2. $F$ 单位：W m$^{-2}$
3. $L$ 单位：W（或 solar luminosity $L_{\odot}$）
4. 已知 $F$ 和 $d$ 可求 $L$，已知 $F$ 和 $L$ 可求 $d$
:::

### 评分标准
:::info[评分标准（MS 模式）]
- **B1**: 定义 luminosity
- **C1**: 代入 $F = L / (4\pi d^2)$
- **A1**: 数值 + 单位
:::

### 完整原题

**Example 1 — 9702/w22/qp/41 Q9 (8 marks):**
> (a) State what is meant by the luminosity of a star. (b) A star is at distance $8.14 \times 10^{16}\text{ m}$ from Earth and has luminosity $9.86 \times 10^{27}\text{ W}$, surface temperature 9830 K. (i) Calculate the radiant flux intensity observed from Earth. (ii) Determine the radius of the star. (c) Explain how surface temperature of a distant star may be determined from its wavelength spectrum.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a) total power of radiation emitted (by the star)
- **C1**: (b)(i) $F = L / (4\pi d^2) = 9.86 \times 10^{27} / [4\pi \times (8.14 \times 10^{16})^2]$
- **A1**: $F = 1.18 \times 10^{-7}\text{ W m}^{-2}$
- **C1**: (b)(ii) $L = 4\pi\sigma r^2 T^4$
- **A1**: $r = 1.22 \times 10^9\text{ m}$
- **B1**: (c) wavelength of peak intensity determined from spectrum
- **B1**: Wien's displacement law used ($\lambda_{\max} \propto 1/T$)
- **B1**: compare with known temperature object / calibration
</details>

**Example 2 — 9702/s23/qp/41 Q10(b) (2 marks):**
> A star of luminosity $3.8 \times 10^{31}\text{ W}$ is at a distance of $1.8 \times 10^{24}\text{ m}$ from Earth. Calculate the radiant flux intensity at Earth.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **C1**: $F = L / (4\pi d^2) = (3.8 \times 10^{31}) / [4\pi \times (1.8 \times 10^{24})^2]$
- **A1**: $F = 9.3 \times 10^{-19}\text{ W m}^{-2}$
</details>

**Example 3 — 9702/s24/qp/41 Q10 (8 marks):**
> (a)(i) State what is meant by luminosity of a star. (ii) Explain how a standard candle in a distant galaxy can be used to determine distance. (b) The Sun has mean distance from Earth $1.50 \times 10^{11}\text{ m}$ and radiant flux intensity $1.36 \times 10^3\text{ W m}^{-2}$. (i) Calculate luminosity of the Sun. (ii) The Sun's surface temperature is 5780 K. Calculate its radius.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a)(i) total power of radiation emitted (by star)
- **B1**: (a)(ii) standard candle has known luminosity, measure $F$, use $d^2 = L / (4\pi F)$
- **C1**: (b)(i) $L_{\odot} = F \times 4\pi d^2 = 1.36 \times 10^3 \times 4\pi \times (1.50 \times 10^{11})^2$
- **A1**: $L_{\odot} = 3.85 \times 10^{26}\text{ W}$
- **C1**: (b)(ii) $L = 4\pi\sigma r^2 T^4$, rearrange for $r$
- **A1**: $r = 6.96 \times 10^8\text{ m}$
</details>

---

## Question Type 2: Stellar radius using Wien and Stefan-Boltzmann

### 如何识别
题目给出恒星温度（或 $\lambda_{\max}$）和 luminosity（或 flux），要求估计恒星半径。

### 标准解题方法
:::note[标准解题方法]
1. **Wien's law**: $\lambda_{\max} T = \text{constant} = 2.9 \times 10^{-3}\text{ m K}$，求 $T$
2. **Stefan-Boltzmann law**: $L = 4\pi\sigma r^2 T^4$
3. 整理得 $r = \sqrt{L / (4\pi\sigma T^4)}$
4. 注意 $L$ 有时需通过 $F = L / (4\pi d^2)$ 先求出
:::

### 评分标准
:::info[评分标准（MS 模式）]
- **C1**: 代入 Stefan-Boltzmann 公式
- **C1**: 正确代入数值
- **A1**: 半径数值 + 单位
:::

### 完整原题

**Example 1 — 9702/w22/qp/41 Q9(b)(ii) (2 marks):**
> Star has luminosity $9.86 \times 10^{27}\text{ W}$, surface temperature 9830 K. Determine its radius.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **C1**: $L = 4\pi\sigma r^2 T^4$, $9.86 \times 10^{27} = 4\pi \times 5.67 \times 10^{-8} \times r^2 \times (9830)^4$
- **A1**: $r = 1.22 \times 10^9\text{ m}$
</details>

**Example 2 — 9702/s23/qp/42 Q9(c) (2 marks):**
> A star has radius $2.3 \times 10^9\text{ m}$ and luminosity $1.4 \times 10^{28}\text{ W}$. Calculate its surface temperature.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **C1**: $L = 4\pi\sigma r^2 T^4$, so $T^4 = L / (4\pi\sigma r^2)$
- **A1**: $T = 5800\text{ K}$ (approximately)
</details>

---

## Question Type 3: Redshift and Hubble's law

### 如何识别
题目给出星系光谱线的实验室波长和观测波长，要求计算 redshift、recession speed、Hubble constant。

### 标准解题方法
:::note[标准解题方法]
1. Redshift: $\Delta\lambda = \lambda_{\text{obs}} - \lambda_{\text{emit}}$（观测值增大）
2. $\Delta\lambda / \lambda \approx v / c$，求 $v$
3. $v \approx H_0 d$，求 $H_0$ 或 $d$
4. 注意：红移表明星系远离我们，宇宙在膨胀
:::

### 评分标准
:::info[评分标准（MS 模式）]
- **B1**: redshift 定义
- **C1**: $\Delta\lambda / \lambda = v / c$
- **C1**: $v = H_0 d$
- **A1**: $H_0$ 数值 + 单位（s$^{-1}$）
:::

### 完整原题

**Example 1 — 9702/s23/qp/41 Q10 (9 marks):**
> (a) State Hubble's law. (b) Star luminosity $3.8 \times 10^{31}\text{ W}$, distance $1.8 \times 10^{24}\text{ m}$, calculate radiant flux. (c) Spectral line known wavelength 486 nm, observed 492 nm. (i) Explain why observed wavelength differs. (ii) Determine Hubble constant $H_0$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: (a) speed is (directly) proportional to distance
- **A1**: $v = H_0 d$, where $v$ is speed of recession, $d$ is distance
- **C1**: (c)(i) galaxy is moving away (from Earth)
- **B1**: wavelength increased by Doppler effect / redshift
- **C1**: (c)(ii) $\Delta\lambda / \lambda = v / c$, $v = (492 - 486) \times 3.00 \times 10^8 / 486 = 3.7 \times 10^6\text{ m s}^{-1}$
- **C1**: $H_0 = v / d = 3.7 \times 10^6 / 1.8 \times 10^{24}$
- **A1**: $H_0 = 2.1 \times 10^{-18}\text{ s}^{-1}$
</details>

**Example 2 — 9702/w24/qp/41 Q10 (9 marks):**
> (a) State what is meant by redshift and explain how it leads to the idea that the Universe is expanding. (b) A spectral line of known wavelength 658 nm from a galaxy is measured as 726 nm. (i) Calculate the distance to the galaxy using $F = L / (4\pi d^2)$. (ii) Calculate the recessional speed of the galaxy. (c)(i) Sketch a graph of recessional speed against distance for galaxies. (ii) Identify the quantity given by the gradient of this graph.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a) redshift is increase in observed wavelength / decrease in observed frequency (caused by Doppler effect)
- **B1**: radiation from distant galaxies is observed to be redshifted
- **B1**: redshift provides evidence that galaxies are moving apart
- **B1**: galaxies moving apart means Universe must be expanding
- **C1**: (b)(ii) $\Delta\lambda / \lambda = v / c$, $(726 - 658) / 658 = v / (3.00 \times 10^8)$
- **A1**: $v = 3.1 \times 10^7\text{ m s}^{-1}$
- **B1**: (c)(i) straight line with positive gradient through origin
- **B1**: (c)(ii) Hubble constant
</details>

**Example 3 — 9702/s22/qp/42 Q9 (7 marks):**
> (a)(i) State Hubble's law. (b) Explain how Hubble's law and the idea of the expanding Universe lead to the Big Bang theory.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a)(i) $v = H_0 d$, speed of recession proportional to distance
- **B1**: (b) Universe has been expanding from a single point
- **B1**: extrapolating backwards, all matter was at a single point
- **B1**: this point is the Big Bang
- **B1**: age of Universe $\approx 1 / H_0$
</details>

---

## Question Type 4: Standard candles

### 如何识别
题目出现 "standard candle"、"known luminosity"、"distance determination"。

### 标准解题方法
:::note[标准解题方法]
1. Standard candle: 已知 luminosity 的天体
2. 测量 radiant flux $F$
3. 使用 $F = L / (4\pi d^2)$ 计算 $d$
4. 用于确定星系距离
:::

### 完整原题

**Example 1 — 9702/s24/qp/41 Q10(a)(ii) (2 marks):**
> Explain how a standard candle in a distant galaxy can be used to determine the distance to the galaxy.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: standard candle has known luminosity
- **B1**: measure radiant flux intensity $F$, then $d^2 = L / (4\pi F)$
</details>
