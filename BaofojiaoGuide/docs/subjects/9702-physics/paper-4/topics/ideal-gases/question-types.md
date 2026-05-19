---
title: 题型分析
sidebar_position: 2
---
# 题型分析 — Ideal Gases

## Question Type 1: 气体状态方程计算 ($pV = nRT$ / $pV = NkT$)

### 如何识别
给出 $p$, $V$, $T$ 中部分量，求分子数 $N$、摩尔数 $n$ 或未知量。

### 标准解题方法
:::note[步骤]
1. 确认温度已转 K
2. 选择 $pV = nRT$（求摩尔数）或 $pV = NkT$（求分子数）
3. 代入求解
4. $N = nN_A$，$k = R/N_A$
:::

### 评分标准
:::info[评分要点]
- **C1**: 正确公式 $pV = nRT$ 或 $pV = NkT$
- **C1**: 正确代入数值
- **A1**: 答案
:::

### 完整原题

**Example 1 — 9702_s21_qp_41 (2 marks):**
> An ideal gas has volume $1.8 \times 10^{-3}$ m$^3$, pressure $3.3 \times 10^5$ Pa, temperature 310 K. Show that the number of gas molecules is $1.4 \times 10^{23}$.

<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $pV = NkT$
- **C1**: $N = (1.8 \times 10^{-3} \times 3.3 \times 10^5)/(1.38 \times 10^{-23} \times 310)$
- **A1**: $N = 1.4 \times 10^{23}$
</details>

**Example 2 — 9702_s23_qp_41 (4 marks):**
> A gas cylinder of volume $4.5 \times 10^{-2}$ m$^3$ contains 2.4 mol of an ideal gas at a pressure of $1.3 \times 10^5$ Pa. Calculate the temperature of the gas.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $pV = nRT$
- **C1**: $T = pV/(nR) = (1.3 \times 10^5 \times 4.5 \times 10^{-2})/(2.4 \times 8.31)$
- **A1**: $T = 293$ K
</details>

**Example 3 — 9702_s24_qp_41 (3 marks):**
> A fixed mass of an ideal gas has a volume of $3.6 \times 10^{-3}$ m$^3$ at a pressure of $2.0 \times 10^5$ Pa and a temperature of 300 K. Calculate the number of moles of gas.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $pV = nRT$
- **C1**: $n = pV/(RT) = (2.0 \times 10^5 \times 3.6 \times 10^{-3})/(8.31 \times 300)$
- **A1**: $n = 0.29$ mol
</details>

### 常见陷阱
:::warning[注意]
- 温度必须用 K：$T = \theta + 273.15$
- 区分 $n$（摩尔数）和 $N$（分子数）
- 单位一致性：$p$ in Pa, $V$ in m$^3$
:::

## Question Type 2: 气体动理论假设与气压解释

### 如何识别
"State the basic assumptions of kinetic theory" 或 "Explain how molecular movement causes pressure"。

### 标准解题方法
:::note[基本假设]
1. Molecules are in (continuous) random motion.
2. All collisions (between molecules and with walls) are (perfectly) elastic.
3. No intermolecular forces (except during collisions).
4. Volume of molecules is negligible compared with volume of gas.
5. Collisions are instantaneous.

气压解释：molecules collide with walls → momentum change → force on wall → many molecules → pressure
:::

### 评分标准
:::info[评分规则]
- 每个假设 **B1**（通常列出3-4个可得满分）
- 气压解释：每个关键步骤 **B1**
:::

### 完整原题

**Example 1 — 9702_w24_qp_41 (6 marks):**
> (a) State three basic assumptions of the kinetic theory of gases.
> (b) Explain how the movement of molecules causes a pressure exerted by a gas.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **B1**: molecules are in (continuous) random motion
- **B1**: (all) collisions between molecules are (perfectly) elastic
- **B1**: no forces between molecules (except during collisions)
- 或 volume of molecules negligible / collisions instantaneous
- **B1**: molecules collide with (walls of) container
- **B1**: momentum of molecule changes during collision (with walls)
- **B1**: change in momentum is caused by force on molecule by wall
- **B1**: molecule experiences force from wall so molecule exerts force on wall
- **B1**: many molecules exerting force across the area of the wall leads to pressure
</details>

**Example 2 — 9702_s21_qp_41 (3 marks):**
> Use kinetic theory to explain why, when the piston is moved so that the gas expands, this causes a decrease in the temperature of the gas.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **B1**: speed of molecule decreases on impact with moving piston
- **B1**: mean-square speed (directly) proportional to (thermodynamic) temperature
- **B1**: kinetic energy (of molecules) decreases (so temperature decreases)
</details>

### 常见陷阱
:::warning[注意]
- 假设要列出**至少3条**
- "elastic collisions" 指总动能守恒
- 解释气压要讲全过程：碰撞 → 动量变化 → 力 → 压强
:::

## Question Type 3: 分子平均动能与推导

### 如何识别
"Deduce that average KE = $\frac32 kT$" 或求分子 $c_{\text{r.m.s.}}$。

### 标准解题方法
:::note[推导]
比较 $pV = \frac13 Nm\langle c^2\rangle$ 和 $pV = NkT$：
$NkT = \frac13 Nm\langle c^2\rangle$
$\frac12 m\langle c^2\rangle = \frac32 kT$
:::

### 评分标准
:::info[评分]
- **M1**: 联立两个公式
- **A1**: 得出 $\frac12 m\langle c^2\rangle = \frac32 kT$
:::

### 完整原题

**Example 1 — 9702_s21_qp_41 (3 marks):**
> The average translational kinetic energy $E_K$ of a molecule of an ideal gas is given by $E_K = \frac32 kT$. Calculate the increase in internal energy $\Delta U$ of the gas during expansion. Number of molecules $= 1.4 \times 10^{23}$, temperature changes from 310 K to 288 K.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $\Delta U = \frac32 Nk\Delta T$
- **C1**: $= \frac32 \times 1.4 \times 10^{23} \times 1.38 \times 10^{-23} \times (288 - 310)$
- **A1**: $\Delta U = -64$ J
</details>

**Example 2 — 9702_w23_qp_41 (4 marks):**
> (a) State the meaning of $N$, $m$ and $\langle c^2\rangle$ in $pV = \frac13 Nm\langle c^2\rangle$.
> (b) Use $pV = \frac13 Nm\langle c^2\rangle$ and $pV = NkT$ to show that $\frac12 m\langle c^2\rangle = \frac32 kT$.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **B1**: $N$ = number of molecules (of the gas)
- **B1**: $m$ = mass of one molecule (of the gas)
- **B1**: $\langle c^2\rangle$ = mean-square speed (of molecules)
- **M1**: $pV = \frac13 Nm\langle c^2\rangle$ and $pV = NkT$
- **A1**: $NkT = \frac13 Nm\langle c^2\rangle$ → $\frac12 m\langle c^2\rangle = \frac32 kT$
</details>

### 常见陷阱
:::warning[注意]
- 推导中消去 $N$ 和 $pV$
- $\frac12 m\langle c^2\rangle$ 是平均动能，不是总动能
- $c_{\text{r.m.s.}} = \sqrt{\langle c^2\rangle} = \sqrt{3kT/m}$
- 理想气体内能变化 $\Delta U = \frac32 Nk\Delta T$
:::
