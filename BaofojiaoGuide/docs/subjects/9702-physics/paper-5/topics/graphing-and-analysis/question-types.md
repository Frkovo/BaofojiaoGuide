---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Question Type 1: Plotting Graphs with Error Bars

### 如何识别

Part (c)(i) of Q2 — "Plot a graph of Y against X. Include error bars for Y." 题目会提供一个数据表，包含物理量的测量值及其不确定度。

### 标准解题方法

:::note[标准解题方法]

1. 选择刻度，使图至少占网格一半（水平和垂直）
2. 刻度只用 1, 2 或 5 对应 2 cm 方格
3. 坐标轴标注物理量（或符号）和单位
4. 用细 `×` 或 `⊙`（直径 &lt; 1 mm）描点，精确到半小格
5. Error bars：对称，中心在数据点，总长度 = $2 \times \Delta Y$
6. 两端画 cap（小横线）

:::

:::info[评分标准（MS 模式）]

- **M1**: All points plotted correctly within half a small square
- **M1**: Error bars plotted correctly in Y-direction, all points, symmetrical

:::

#### Example 1 — Thermistor Resistance against Temperature

> A student investigates how the resistance $R$ of a thermistor varies with temperature $T$. The thermistor is placed in a water bath and its resistance is measured at different temperatures. The student suggests that $R = R_0 e^{kT}$.
>
> | $T / ^{\circ}\text{C}$ | $R / \Omega$ | $\Delta R / \Omega$ |
> |---------|--------------|--------------------|
> | 20.0 | 5200 | $\pm 200$ |
> | 30.0 | 3200 | $\pm 150$ |
> | 40.0 | 2000 | $\pm 100$ |
> | 50.0 | 1300 | $\pm 70$ |
> | 60.0 | 850 | $\pm 50$ |
> | 70.0 | 550 | $\pm 30$ |
>
> The student calculates $\ln R$ and $1/T$.
>
> (c)(i) Plot a graph of $\ln R$ against $1/T$. Include error bars for $\ln R$.

<details>
<summary>MS 展开查看</summary>

**Plotting:**
- **M1**: All 6 points plotted correctly within half a small square
- **M1**: Error bars in Y-direction ($\ln R$) plotted correctly
  - $\Delta(\ln R) = \Delta R / R$: e.g. 200/5200 = 0.0385, etc.
  - Symmetrical, all points, with caps

**Scales:**
- x-axis: $1/T$ from 0.0029 to 0.0034 K$^{-1}$ (sensible range)
- y-axis: $\ln R$ from 6.0 to 8.6

</details>

---

#### Example 2 — Cooling of a Liquid

> A student investigates the cooling of a hot liquid. The liquid is placed in a beaker and allowed to cool. The temperature $\theta$ is measured at different times $t$. It is suggested that $\theta = \theta_0 e^{-kt}$.
>
> | $t / \text{s}$ | $\theta / ^{\circ}\text{C}$ | $\Delta\theta / ^{\circ}\text{C}$ |
> |----|-----------|-------------------|
> | 0 | 80.0 | $\pm 0.5$ |
> | 30 | 67.5 | $\pm 0.5$ |
> | 60 | 57.0 | $\pm 0.5$ |
> | 90 | 48.5 | $\pm 0.5$ |
> | 120 | 41.0 | $\pm 0.5$ |
> | 150 | 35.0 | $\pm 0.5$ |
> | 180 | 30.0 | $\pm 0.5$ |
>
> (c)(i) Plot a graph of $\ln \theta$ against $t$. Include error bars for $\ln \theta$.

<details>
<summary>MS 展开查看</summary>

**Plotting:**
- **M1**: All 7 points plotted correctly to within half a small square
- **M1**: Error bars in Y-direction ($\ln \theta$) plotted
  - $\Delta(\ln \theta) = \Delta\theta / \theta$: 0.5/80.0 = 0.00625, 0.5/67.5 = 0.00741, etc.
  - Caps drawn at both ends of each bar

**Scales:**
- x-axis: $t$ from 0 to 200 s
- y-axis: $\ln \theta$ from 3.4 to 4.4

</details>

---

#### Example 3 — Period of a Simple Pendulum

> A student investigates how the period $T$ of a simple pendulum varies with length $L$. A stopwatch is used to measure the time for 10 oscillations. The period $T$ is then calculated. It is suggested that $T = 2\pi \sqrt{L/g}$.
>
> | $L / \text{m}$ | $T / \text{s}$ | $\Delta T / \text{s}$ |
> |-------|----------|-------------------|
> | 0.20 | 0.90 | $\pm 0.02$ |
> | 0.30 | 1.10 | $\pm 0.02$ |
> | 0.40 | 1.27 | $\pm 0.02$ |
> | 0.50 | 1.42 | $\pm 0.02$ |
> | 0.60 | 1.55 | $\pm 0.02$ |
> | 0.70 | 1.68 | $\pm 0.02$ |
> | 0.80 | 1.79 | $\pm 0.02$ |
>
> (c)(i) Plot a graph of $T^2$ against $L$. Include error bars for $T^2$.

<details>
<summary>MS 展开查看</summary>

**Plotting:**
- **M1**: All 7 points ($T^2$ against $L$) plotted correctly within half a small square
- **M1**: Error bars in Y-direction ($T^2$) plotted
  - $\Delta(T^2) = 2T \times \Delta T$: $2 \times 0.90 \times 0.02 = 0.036$, etc.
  - All 7 bars present, symmetrical, with caps

**Scales:**
- x-axis: $L$ from 0.15 to 0.85 m
- y-axis: $T^2$ from 0.6 to 3.4 s$^2$

</details>

---

## Question Type 2: Best Fit and Worst Acceptable Lines

### 如何识别

Part (c)(ii) — "Draw the straight line of best fit and a worst acceptable straight line." 题目要求在已有的图上画两条线。

### 标准解题方法

:::note[标准解题方法]

1. **Best fit**: 用直尺画直线，使数据点大致均匀分布在直线两侧（忽略明显异常值）
2. **WAL**: 过所有 error bars 的最陡（steepest）或最缓（shallowest）直线
3. 两条线有明显区别
4. 用标签或不同线型区分（如 best fit 实线、WAL 虚线）

:::

:::warning[常见陷阱]

- **不要**连接第一个点和最后一个点
- WAL **必须**穿过所有 error bars
- 如果 error bars 只在一个方向，WAL 可以在 error bars 内旋转
- 两条线不能重合

:::

#### Example 1 — Thermistor Graph (continued)

> (c)(ii) On the graph drawn in (c)(i), draw the straight line of best fit and a worst acceptable straight line.

<details>
<summary>MS 展开查看</summary>

**Best fit:**
- **M1**: Straight line drawn with a ruler
- Points roughly equally distributed above and below the line
- The line passes through the general trend of the data

**WAL:**
- **M1**: Steepest possible straight line that passes through all error bars
- The WAL is clearly different from the best fit line
- Both lines are labelled (or distinguishable)

</details>

---

#### Example 2 — Cooling Graph (continued)

> (c)(ii) On the graph of $\ln \theta$ against $t$, draw the straight line of best fit and a worst acceptable straight line.

<details>
<summary>MS 展开查看</summary>

**Best fit:**
- **M1**: Straight line through the general trend
- More points lie above and below in roughly equal numbers

**WAL:**
- **M1**: Shallowest straight line that still passes through all error bars
- Distinct from best fit, labelled clearly

</details>

---

#### Example 3 — Pendulum Graph (continued)

> (c)(ii) On the graph of $T^2$ against $L$, draw the straight line of best fit and a worst acceptable straight line.

<details>
<summary>MS 展开查看</summary>

**Best fit:**
- **M1**: Straight line through all points (theory predicts $T^2 \propto L$, so line should pass near origin)
- Balanced distribution of points

**WAL:**
- **M1**: Steepest OR shallowest line through all error bars
- Must be labelled

</details>

---

## Question Type 3: Gradient Determination

### 如何识别

Part (c)(iii) — "Determine the gradient of the line of best fit. Include the absolute uncertainty." 有时也会要求给出单位。

### 标准解题方法

:::note[标准解题方法]

1. 在 best fit 线上选两个点（**不是**数据点）
2. 两点间隔 &gt; 所画直线长度的一半
3. 在点旁标注坐标 $(x_1, y_1)$ 和 $(x_2, y_2)$
4. $\text{gradient} = \frac{y_2 - y_1}{x_2 - x_1}$
5. 用相同方法计算 WAL 的 gradient
6. $\text{uncertainty} = |\text{gradient}_{\text{best}} - \text{gradient}_{\text{worst}}|$
7. 结果表示为 $\text{gradient} \pm \text{uncertainty}$，带单位

:::

#### Example 1 — Thermistor Gradient

> The best fit line for $\ln R$ against $1/T$ has the equation $\ln R = \ln R_0 + k(1/T)$.
>
> (c)(iii) Determine the gradient of the best fit line and its absolute uncertainty.

<details>
<summary>MS 展开查看</summary>

**Best fit gradient:**
- **M1**: Two points on best fit line selected: $(0.00294, 8.55)$ and $(0.00330, 6.95)$
- $\text{gradient}_{\text{best}} = \frac{6.95 - 8.55}{0.00330 - 0.00294} = \frac{-1.60}{0.00036} = -4440 \text{ K}$
- Correct substitution and calculation

**WAL gradient:**
- Two points on WAL: $(0.00294, 8.70)$ and $(0.00330, 6.75)$
- $\text{gradient}_{\text{WAL}} = \frac{6.75 - 8.70}{0.00330 - 0.00294} = \frac{-1.95}{0.00036} = -5420 \text{ K}$

**Uncertainty:**
- **M1**: $\Delta m = |{-4440} - ({-5420})| = 980 \text{ K}$
- Final answer: $m = (-4440 \pm 980) \text{ K}$

</details>

---

#### Example 2 — Cooling Gradient

> The best fit line for $\ln \theta$ against $t$ has the equation $\ln \theta = \ln \theta_0 - kt$.
>
> (c)(iii) Determine the gradient of the best fit line and its absolute uncertainty.

<details>
<summary>MS 展开查看</summary>

**Best fit gradient:**
- **M1**: Two points on best fit line: $(0, 4.38)$ and $(180, 3.40)$
- $\text{gradient}_{\text{best}} = \frac{3.40 - 4.38}{180 - 0} = \frac{-0.98}{180} = -0.00544 \text{ s}^{-1}$

**WAL gradient:**
- Two points on WAL: $(0, 4.40)$ and $(180, 3.30)$
- $\text{gradient}_{\text{WAL}} = \frac{3.30 - 4.40}{180 - 0} = -0.00611 \text{ s}^{-1}$

**Uncertainty:**
- **M1**: $\Delta m = |-0.00544 - (-0.00611)| = 0.00067 \text{ s}^{-1}$
- Final answer: $m = (-0.00544 \pm 0.00067) \text{ s}^{-1}$

</details>

---

#### Example 3 — Pendulum Gradient

> The graph of $T^2$ against $L$ is expected to be linear with $T^2 = (4\pi^2/g)L$.
>
> (c)(iii) Determine the gradient of the best fit line and its absolute uncertainty. Hence determine a value for $g$.

<details>
<summary>MS 展开查看</summary>

**Best fit gradient:**
- **M1**: Two points on best fit line: $(0.20, 0.81)$ and $(0.80, 3.22)$
- $\text{gradient}_{\text{best}} = \frac{3.22 - 0.81}{0.80 - 0.20} = \frac{2.41}{0.60} = 4.02 \text{ s}^2\text{m}^{-1}$

**WAL gradient:**
- Two points on WAL: $(0.20, 0.78)$ and $(0.80, 3.32)$
- $\text{gradient}_{\text{WAL}} = \frac{3.32 - 0.78}{0.80 - 0.20} = \frac{2.54}{0.60} = 4.23 \text{ s}^2\text{m}^{-1}$

**Uncertainty:**
- **M1**: $\Delta m = |4.02 - 4.23| = 0.21 \text{ s}^2\text{m}^{-1}$
- Final answer: $m = (4.02 \pm 0.21) \text{ s}^2\text{m}^{-1}$

**Determining $g$:**
- $g = 4\pi^2 / \text{gradient} = 4\pi^2 / 4.02 = 9.82 \text{ m s}^{-2}$
- Uncertainty: $\Delta g = g \times (\Delta m / m) = 9.82 \times (0.21 / 4.02) = 0.51 \text{ m s}^{-2}$
- $g = (9.82 \pm 0.51) \text{ m s}^{-2}$

</details>

---

## Question Type 4: y-intercept Determination

### 如何识别

Part (c)(iv) — "Determine the y-intercept." 有时会要求不确定性。注意**不能**直接从 y 轴读取。

### 标准解题方法

:::note[标准解题方法]

1. 使用 $y = mx + c$
2. 代入 best fit 线上一个点 $(x, y)$ 和 gradient $m$
3. $c = y - mx$
4. 用 WAL 重复计算得到 $c_{\text{worst}}$
5. $\text{uncertainty} = |c_{\text{best}} - c_{\text{worst}}|$
6. **不能**直接从图坐标轴读值（false origin 时无效）

:::

:::info[评分标准（MS 模式）]

- **M1**: Correct y-intercept calculated using $c = y - mx$
- **M1** (if required): Correct uncertainty in y-intercept

:::

#### Example 1 — Thermistor y-intercept

> The graph of $\ln R$ against $1/T$ should give a straight line with equation $\ln R = \ln R_0 + k(1/T)$.
>
> (c)(iv) Determine the y-intercept of the best fit line and its absolute uncertainty.

<details>
<summary>MS 展开查看</summary>

**Best fit y-intercept:**
- **M1**: Using $c = y - mx$
- Point on best fit: $(0.00310, 7.72)$, gradient $m = -4440 \text{ K}$
- $c = 7.72 - (-4440 \times 0.00310) = 7.72 - (-13.76) = 21.48$
- y-intercept $= 21.5$ (3 SF)

**WAL y-intercept:**
- Point on WAL: $(0.00310, 7.72)$, gradient $m = -5420 \text{ K}$
- $c_{\text{WAL}} = 7.72 - (-5420 \times 0.00310) = 7.72 - (-16.80) = 24.52$

**Uncertainty:**
- **M1**: $\Delta c = |21.48 - 24.52| = 3.04$
- Final answer: $c = 21.5 \pm 3.0$

**Physical meaning:**
- $\ln R_0 = 21.5$, therefore $R_0 = e^{21.5} = 2.18 \times 10^9 \ \Omega$

</details>

---

#### Example 2 — Cooling y-intercept

> The graph of $\ln \theta$ against $t$ should give a straight line with equation $\ln \theta = \ln \theta_0 - kt$.
>
> (c)(iv) Determine the y-intercept of the best fit line and its absolute uncertainty. State the value of $\theta_0$.

<details>
<summary>MS 展开查看</summary>

**Best fit y-intercept:**
- **M1**: Using $c = y - mx$
- Point on best fit: $(90, 3.88)$, gradient $m = -0.00544 \text{ s}^{-1}$
- $c = 3.88 - (-0.00544 \times 90) = 3.88 - (-0.490) = 4.37$
- y-intercept $= 4.37$

**WAL y-intercept:**
- Point on WAL: $(90, 3.88)$, gradient $m = -0.00611 \text{ s}^{-1}$
- $c_{\text{WAL}} = 3.88 - (-0.00611 \times 90) = 3.88 - (-0.550) = 4.43$

**Uncertainty:**
- **M1**: $\Delta c = |4.37 - 4.43| = 0.06$
- Final answer: $c = 4.37 \pm 0.06$

**Physical meaning:**
- $\ln \theta_0 = 4.37$, therefore $\theta_0 = e^{4.37} = 79.0 \ ^{\circ}\text{C}$
- This matches the measured initial temperature $80.0 \pm 0.5 \ ^{\circ}\text{C}$

</details>

---

#### Example 3 — Pendulum y-intercept

> The graph of $T^2$ against $L$ should give a straight line with equation $T^2 = (4\pi^2/g)L + c$.
>
> (c)(iv) Determine the y-intercept of the best fit line. Comment on whether your result is consistent with the theoretical prediction.

<details>
<summary>MS 展开查看</summary>

**Best fit y-intercept:**
- **M1**: Using $c = y - mx$
- Point on best fit: $(0.50, 2.02)$, gradient $m = 4.02 \text{ s}^2\text{m}^{-1}$
- $c = 2.02 - (4.02 \times 0.50) = 2.02 - 2.01 = 0.01 \text{ s}^2$

**WAL y-intercept:**
- Point on WAL: $(0.50, 2.02)$, gradient $m = 4.23 \text{ s}^2\text{m}^{-1}$
- $c_{\text{WAL}} = 2.02 - (4.23 \times 0.50) = 2.02 - 2.115 = -0.095 \text{ s}^2$

**Uncertainty:**
- $\Delta c = |0.01 - (-0.095)| = 0.105 \text{ s}^2$

**Comment:**
- The theoretical prediction is $c = 0$ (line through origin)
- The experimental value $c = 0.01 \pm 0.11 \text{ s}^2$ includes zero within uncertainty
- Therefore the result is consistent with the theoretical prediction

</details>

---

## 题型对比总结

| 题型 | 对应 Q2 Part | 核心技能 | 分值 |
|------|-------------|---------|------|
| Plotting with error bars | (c)(i) | 选刻度、描点、画 error bars | 2 |
| Best fit + WAL | (c)(ii) | 画两条线，区分标记 | 2 |
| Gradient determination | (c)(iii) | 计算 gradient + 不确定度 | 2 |
| y-intercept determination | (c)(iv) | 代入公式计算 | 1–2 |
