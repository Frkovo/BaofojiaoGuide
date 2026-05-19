---
title: 题型分析
sidebar_position: 2
---
# 题型分析 — Gravitational Fields

## Question Type 1: 引力场强度计算

### 如何识别
给出天体质量 $M$ 和半径 $R$，求表面或某高度的引力场强度 $g$。

### 标准解题方法
:::note[方法]
1. 确定目标点到中心距离 $r$
2. 用 $g = GM/r^2$
3. 若求百分比变化：计算新旧 $g$ 之比
:::

### 评分标准
:::info[评分要点]
- **C1**: $g = GM/r^2$
- **C1**: 正确代入 $G$, $M$, $r$
- **A1**: 答案含单位
:::

### 完整原题

**Example 1 — 9702_w20_qp_41 (6 marks):**
> An isolated planet may be assumed to be a uniform sphere of radius $3.39 \times 10^6$ m with its mass of $6.42 \times 10^{23}$ kg concentrated at its centre.
> (b) Calculate the gravitational field strength at the surface of the planet.
> (c) Calculate the height above the surface of the planet at which the gravitational field strength is 1.0% less than its value at the surface.

<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $g = GM/R^2$
- **C1**: $= (6.67 \times 10^{-11} \times 6.42 \times 10^{23})/(3.39 \times 10^6)^2$
- **A1**: $g = 3.73$ N kg$^{-1}$
- **C1**: $0.99 \times 3.73 = GM/r^2$
- **C1**: $r = 3.41 \times 10^6$ m
- **A1**: height $= r - R = 2 \times 10^4$ m
</details>

**Example 2 — 9702_w23_qp_41 (4 marks):**
> Fig. 1.2 shows the variation with $x$ of the gravitational field $g$ at point $P$ due to a sphere. The magnitude of the gravitational field at the surface of the sphere is $Y$. Calculate the field at $2R$ from centre.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $g \propto 1/r^2$
- **C1**: field at $2R = Y/4$
- **A1**: $Y/4$
</details>

### 常见陷阱
:::warning[注意]
- $r$ 从**中心**算起，不是表面
- 区分 $G$ 和 $g$
- 百分比减少是 $0.99g$ 不是 $0.01g$
:::

## Question Type 2: 卫星轨道与开普勒第三定律

### 如何识别
给轨道周期/半径求半径/周期，或证明 $T^2 \propto r^3$。

### 标准解题方法
:::note[推导步骤]
1. 引力 = 向心力：$GMm/r^2 = mr\omega^2$
2. $\omega = 2\pi/T$
3. $GM/r^3 = 4\pi^2/T^2$
4. $T^2 = (4\pi^2/GM)r^3$
:::

### 评分标准
:::info[评分]
- **B1**: gravitational force provides centripetal force
- **M1**: 写出方程
- **A1**: 完成推导
:::

### 完整原题

**Example 1 — 9702_s21_qp_41 (6 marks):**
> A satellite of mass 1200 kg is in a circular orbit about the Earth. The period of the orbit is 94 minutes.
> (b) Calculate the radius of the orbit.
> (c) The satellite enters a new orbit with period 150 minutes.
> (i) Show that the radius of the new orbit is $9.4 \times 10^6$ m.
> (ii) State whether the gravitational potential energy increases or decreases.
> (iii) Determine the magnitude of the change in gravitational potential energy.

<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $GMm/r^2 = mr\omega^2$ and $\omega = 2\pi/T$
- **C1**: $6.67 \times 10^{-11} \times 6.0 \times 10^{24} = r^3 \times [2\pi/(94 \times 60)]^2$
- **A1**: $r = 6.9 \times 10^6$ m
- **C1**: $r^3/T^2 = \text{constant}$
- **A1**: $r^3 = (6.9 \times 10^6)^3 \times (150/94)^2$, $r = 9.4 \times 10^6$ m
- **B1**: separation increases, so potential energy increases
- **C1**: $\Delta E_P = GMm(1/r_1 - 1/r_2)$
- **C1**: $= 6.67 \times 10^{-11} \times 6.0 \times 10^{24} \times 1200 \times (1/6.9\times10^6 - 1/9.4\times10^6)$
- **A1**: $= 1.9 \times 10^{10}$ J
</details>

**Example 2 — 9702_w22_qp_41 (7 marks):**
> (a) State the equation for the gravitational force between two point masses.
> (b) Show that $T^2 = kR^3$ for a satellite in circular orbit.
> (c) Calculate the radius of a geostationary orbit (T = 24 h, M = $6.0 \times 10^{24}$ kg).
> (ii) State the other two conditions for a geostationary orbit.

<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **M1**: $F = Gm_1m_2/r^2$
- **A1**: identifies $G$ as gravitational constant
- **B1**: gravitational force provides centripetal force
- **M1**: $mR\omega^2 = GMm/R^2$ and $\omega = 2\pi/T$
- **A1**: completes algebra to $T^2 = (4\pi^2/GM)R^3$
- **C1**: $(24 \times 3600)^2 = (4\pi^2 \times R^3)/(6.67 \times 10^{-11} \times 6.0 \times 10^{24})$
- **A1**: $R = 4.2 \times 10^7$ m
- **B1**: above the Equator
- **B1**: west to east
</details>

### 常见陷阱
:::warning[注意]
- 卫星质量 $m$ 在推导中消去
- 周期必须用秒（s）
- geostationary 要三个条件：24 h、赤道上空、西向东
:::

## Question Type 3: 引力势与引力势能

### 如何识别
求引力势 $\phi$ 或势能 $E_P$，或计算逃逸能量。

### 标准解题方法
:::note[定义题]
Gravitational potential at a point = work done per unit mass in bringing a small test mass from infinity to that point.

$\phi = -GM/r$，越近越负。

引力势能 $E_P = m\phi = -GMm/r$。
:::

### 评分标准
:::info[评分要点]
- **M1**: work done per unit mass
- **A1**: from infinity
- **C1**: $\phi = -GM/r$
- **A1**: 数字正确
:::

### 完整原题

**Example 1 — 9702_s24_qp_41 (5 marks):**
> (a) Define gravitational potential at a point.
> (b) Satellite X of mass M orbits at distance 4R, satellite Y of mass 2M orbits at distance R. Gravitational potential at X is $-\phi$.
> (ii) State the gravitational potential at Y in terms of $\phi$.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **B1**: work done per unit mass
- **B1**: (bringing small test mass) from infinity (to the point)
- **B1**: $\phi \propto 1/r$
- **B1**: at Y, $r = R$, which is 1/4 of distance to X
- **B1**: so potential at Y = $4$ times at X = $-4\phi$
</details>

**Example 2 — 9702_w23_qp_42 (4 marks):**
> Define gravitational potential. Calculate gravitational potential at the surface of the Moon. Mass of Moon = $7.35 \times 10^{22}$ kg, radius = $1.74 \times 10^6$ m.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **B1**: work done per unit mass
- **B1**: from infinity (to the point)
- **C1**: $\phi = -GM/r$
- **A1**: $\phi = -(6.67 \times 10^{-11} \times 7.35 \times 10^{22})/(1.74 \times 10^6)$
- **A1**: $\phi = -2.82 \times 10^6$ J kg$^{-1}$
</details>

### 常见陷阱
:::warning[注意]
- 势能是负的！负号不能丢
- "from infinity" 是定义关键
- 势能变化：$\Delta E_P = E_{P2} - E_{P1}$
- 逃逸时 $\frac12 mv^2 = GMm/r$
:::
