---
title: Electric Fields — 题型分析
sidebar_position: 2
---

# Electric Fields — 题型分析

## Question Type 1: Definitions (Electric Field / Potential)

### 如何识别

题目包含 "Define electric field strength" 或 "Define electric potential at a point"。

### 标准解题方法

:::note[解题要点]

- **Electric field strength**: force per unit positive charge
- **Electric potential**: work done per unit positive charge in bringing a small test charge from infinity to the point
:::

### 评分标准

:::info[评分模式]

- **B1/B1**: 每题 2 分，包含两个关键要素
- 电场强度：force / per unit charge / positive charge
- 电势：work done / per unit charge / from infinity
:::

### 完整原题

**Example 1 — 9702/41/O/N/20 Q5(a) (2 marks):**

> Define electric potential at a point.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: work done per unit charge
- **A1**: (work done on charge) moving positive charge from infinity
</details>

**Example 2 — 9702/41/M/J/23 Q1(a)(ii) (1 mark):**

> Define electric field.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: force per unit positive charge
</details>

### 常见陷阱

:::warning[常见陷阱]

- 电场强度定义必须提到 "**positive** charge"
- 电势必须提到 "from infinity"（参考点在无穷远）
- 不要只说 "work done per unit charge"——必须说明是 "from infinity"
:::

---

## Question Type 2: Coulomb's Law Calculations

### 如何识别

题目给出两个点电荷的电量和距离，求电场力。

### 标准解题方法

:::note[解题步骤]

1. 写 Coulomb's law: $F = \frac{Q_1 Q_2}{4\pi \epsilon_0 r^2}$
2. 代入数值（注意 $r$ 是距离，单位 m）
3. 计算 $F$
4. 方向判断：同号相斥，异号相吸
:::

### 评分标准

:::info[评分模式]

- **C1**: 写出 $F = Q_1 Q_2 / (4\pi \epsilon_0 r^2)$
- **C1**: 正确代入（包括 $\frac{1}{4\pi \epsilon_0} = 8.99 \times 10^9$）
- **A1**: 正确答案（含单位）
:::

### 完整原题

**Example 1 — 9702/41/O/N/20 Q5(b)(i) (3 marks):**

> Two point charges A (+2.0 × 10$^{-9}$ C) and B are separated by 12.0 cm. Point P lies on the line joining them. The variation of electric potential V with distance x from charge A is shown in Fig. 5.2. Use Fig. 5.2 to determine the charge of B.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **C1**: $\frac{2.0 \times 10^{-9}}{4\pi \epsilon_0 (4.0 \times 10^{-2})} + \frac{Q}{4\pi \epsilon_0 (8.0 \times 10^{-2})} = 0$
- **A1**: $Q = 4.0 \times 10^{-9}$ C
- **B1**: $Q$ given with negative sign
</details>

### 常见陷阱

:::warning[常见陷阱]

- 距离必须用米（m），不是 cm
- 不要忘记 $\frac{1}{4\pi \epsilon_0} = 8.99 \times 10^9$ m F$^{-1}$
- 同号电荷 $F$ 为正（斥力），异号为负（引力）——但在只求大小时取绝对值
:::

---

## Question Type 3: Electric Field and Potential of Point Charges

### 如何识别

题目要求计算点电荷周围的电场强度或电势，或画 $E$-$r$ / $V$-$r$ 图。

### 标准解题方法

:::note[解题步骤]

1. 电场强度：$E = Q / (4\pi \epsilon_0 r^2)$
   - $E$ 是矢量，方向：正电荷向外，负电荷向内
2. 电势：$V = Q / (4\pi \epsilon_0 r)$
   - $V$ 是标量，正电荷为正，负电荷为负
3. 多个电荷的叠加：
   - $E$ 是矢量叠加（平行四边形法则）
   - $V$ 是代数叠加
4. 对于**球形导体**，外部场和电势等同于全部电荷集中在球心的点电荷
:::

### 完整原题

**Example 1 — 9702/41/M/J/20 Q5 (7 marks):**

> (a) State one similarity and one difference between the fields produced by an isolated point charge and an isolated point mass.
> (b) An isolated solid metal sphere A of radius R has charge +Q. Point P is distance 2R from the surface. Determine an expression for E at P.
> (c) A second sphere B with charge –Q is placed near A, centres separated by 6R. Point P lies midway. Explain why:
> (i) magnitude of E at P is given by the sum of magnitudes
> (ii) E at P is not equal to 2E (from part b) in practice.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **5(a) B1**: both obey inverse square law / both radial
- **5(a) B1**: electric field can be attractive or repulsive / gravitational field only attractive
- **5(b) A1**: distance from centre $= 3R$
- **5(b) A1**: $E = Q / (4\pi \epsilon_0 (3R)^2)$
- **5(c)(i) B1**: fields are in the same direction at P (so magnitudes add)
- **5(c)(ii) B1**: charge distribution on each sphere is affected by the other
- **5(c)(ii) B1**: they are not point charges / charges not uniformly distributed
</details>

**Example 2 — 9702/41/M/J/21 Q6(a) (3 marks):**

> An isolated metal sphere of radius r is charged so that E at its surface is $E_0$. On Fig. 6.1, sketch the variation of E with distance x from the centre from $x = 0$ to $x = 3r$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: $E = 0$ for $x < r$
- **B1**: $E \propto 1/x^2$ for $x > r$
- **B1**: curve starts at $E = E_0$ when $x = r$
</details>

### 常见陷阱

:::warning[常见陷阱]

- $E = Q/(4\pi \epsilon_0 r^2)$ 中的 $r$ 是从**球心**算起（不是从表面）
- 金属球**内部**电场强度为零（导体静电平衡）
- $E$-$r$ 图：$0 < r < R$ 为 0，$r > R$ 为 $1/r^2$ 衰减
- $V$-$r$ 图：$0 < r < R$ 为常数（等势体），$r > R$ 为 $1/r$ 衰减
:::

---

## Question Type 4: Uniform Electric Field (Parallel Plates)

### 如何识别

题目涉及平行板电容器、匀强电场、带电粒子在板间运动。

### 标准解题方法

:::note[解题步骤]

1. $E = \Delta V / \Delta d$（匀强电场）
2. 带电粒子在电场中受力：$F = qE$
3. 粒子的加速度：$a = F/m = qE/m$
4. 运动分析：
   - 沿电场方向：匀加速直线运动
   - 垂直电场方向：匀速运动
   - 轨迹：抛物线
:::

### 完整原题

**Example — 9702/41/O/N/22 Q4 (12 marks):**

> (a) State what is indicated by the direction of an electric field line.
> (b) Parallel metal plates with p.d. 2400 V, separation 4.6 cm.
> (i) Draw five lines to represent the electric field between the plates.
> (ii) Calculate the electric field strength.
> (c) A proton enters the region between the plates from the left.
> (i) Draw the path of the proton.
> (ii) A helium nucleus enters along the same path at same speed. Compare final speeds.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **4(a) B1**: direction of force on a positive charge
- **4(a) B1**: placed at that point in the field
- **4(b)(i) B1**: equally spaced parallel lines (between plates)
- **4(b)(i) B1**: arrows from + to –
- **4(b)(i) B1**: lines straight and not touching plates
- **4(b)(ii) C1**: $E = V/d = 2400 / 0.046$
- **4(b)(ii) A1**: $= 5.2 \times 10^4$ N C$^{-1}$
- **4(c)(i) B1**: curved path (parabolic) towards negative plate
- **4(c)(i) B1**: straight line after leaving field
- **4(c)(ii) B1**: helium nucleus has smaller final speed
- **4(c)(ii) B1**: helium has larger mass (so smaller acceleration)
- **4(c)(ii) B1**: charge/mass ratio is smaller
</details>

### 常见陷阱

:::warning[常见陷阱]

- 匀强电场中 $E = V/d$，$d$ 是板间距离（不是沿路径距离）
- 带电粒子在匀强电场中的轨迹是**抛物线**（不是直线或圆）
- $\alpha$ 粒子（$^4_2$He）的 $q/m$ 是质子的 $1/2$（不是相同）
:::
