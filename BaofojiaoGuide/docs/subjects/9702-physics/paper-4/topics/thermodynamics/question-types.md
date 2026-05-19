---
title: Thermodynamics — 题型分析
sidebar_position: 2
---

# Thermodynamics — 题型分析

## Question Type 1: Definition of Internal Energy

### 如何识别

题目包含 "State what is meant by the internal energy of a system" 或类似表述。

### 标准解题方法

:::note[解题要点]

1. 内能是系统内部所有分子**随机**动能和势能的总和
2. 内能由系统的**状态**（温度、压力、体积）决定
3. 温度升高 → 平均动能增加 → 内能增加（除非有相变）
:::

### 评分标准

:::info[评分模式]

- **B1**: sum of random distribution of kinetic and potential energies (of molecules)
- **B1**: of the molecules / of the system
:::

### 完整原题

**Example 1 — 9702/41/M/J/20 Q2(a) (2 marks):**

> State what is meant by the internal energy of a system.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: sum of (random) distribution of kinetic and potential energies (of molecules)
- **B1**: (of the molecules) in / of the system
</details>

**Example 2 — 9702/41/M/J/21 Q2(c)(i) (3 marks, context):**

> The average translational kinetic energy $E_K$ of a molecule of an ideal gas is given by $E_K = \frac{3}{2}kT$. Calculate the increase in internal energy $\Delta U$ of the gas during the expansion.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **C1**: number of molecules $N$ from earlier working ($1.4 \times 10^{23}$)
- **C1**: $\Delta U = \frac{3}{2} Nk\Delta T$
- **A1**: correct answer
</details>

### 常见陷阱

:::warning[常见陷阱]

- 不要只说"kinetic energy of molecules"——必须提 potential energy 也包含在内
- 不要忘记 "random" 一词——MS 通常会要求
- 对理想气体，内能只包含动能（无分子间势能）
:::

---

## Question Type 2: First Law of Thermodynamics Calculations

### 如何识别

题目给出 $q$、$W$、$\Delta U$ 中的两个，求第三个；或需要填表格；或给出 $p$-$V$ 图需要计算。

### 标准解题方法

:::note[解题步骤]

1. 确定符号约定：$\Delta U = q + W$
   - $+q$: 系统吸热（thermal energy transferred **to** system）
   - $+W$: 对系统做功（work done **on** system）
2. 如果是气体膨胀（$\Delta V > 0$），气体对外界做功 → $W$ 为负
3. 如果是气体压缩（$\Delta V < 0$），外界对气体做功 → $W$ 为正
4. 等体过程：$W = 0$，$\Delta U = q$
5. 循环过程：$\Delta U_{\text{cycle}} = 0$
6. $W = p\Delta V$ 仅在**等压**过程中直接使用
:::

### 评分标准

:::info[评分模式]

- **C1/M1**: 写出正确公式或表达式
- **C1**: 正确代入数值
- **A1**: 最终答案（含单位）
- 表格题通常逐行给 **B1**
:::

### 完整原题

**Example 1 — 9702/41/O/N/20 Q2 (9 marks):**

> (a) The first law of thermodynamics may be expressed as $\Delta U = (+q) + (+W)$. State the meaning of:
> - $+q$
> - $+W$
>
> (b) The variation with pressure $p$ of the volume $V$ of a fixed mass of an ideal gas is shown in Fig. 2.1. The gas undergoes a cycle of changes A to B to C to A.
> During A to B, the volume increases from $2.3 \times 10^{-3}$ m$^3$ to $3.8 \times 10^{-3}$ m$^3$.
> (i) Show that the magnitude of the work done during A to B is 390 J.
> (ii) State and explain the total change in internal energy during one complete cycle.
> (c) During A to B, 1370 J of thermal energy is transferred to the gas. During B to C, no thermal energy enters or leaves the gas. The work done on the gas during this change is 550 J. Complete Table 2.1.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **2(a) B1**: $+q$: thermal energy transfer to system
- **2(a) B1**: $+W$: work done on system
- **2(b)(i) A1**: $W = 2.6 \times 10^5 \times (3.8 - 2.3) \times 10^{-3} = 390$ J
- **2(b)(ii) B1**: no (total) change (in internal energy)
- **2(b)(ii) B1**: gas returns to its original temperature
- **2(c) B1**: A to B row all correct: (1370, –390, 980)
- **2(c) B1**: B to C row all correct: (0, 550, 550)
- **2(c) B1**: C to A row: $\Delta U$ adds to the other two $\Delta U$ values to give zero
- **2(c) B1**: C to A row: $w = 0$ and $q$ adds to $w$ to give $\Delta U$ value
</details>

**Example 2 — 9702/41/M/J/21 Q2(c)(ii) (2 marks):**

> The work done by the gas during the expansion is 76 J. Use your answer in (i) to explain whether thermal energy is transferred to or from the gas during the expansion.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: uses $\Delta U = q + W$ correctly (e.g. $q = \Delta U - W$)
- **A1**: conclusion consistent with sign of $q$ (thermal energy transferred to/from gas)
</details>

### 常见陷阱

:::warning[常见陷阱]

- $W = p\Delta V$ 中的 $\Delta V$ 有符号——膨胀为正，$W$（on gas）为负
- 区分 "work done by gas"（负值）和 "work done on gas"（正值）
- 循环过程 $\Delta U_{\text{total}} = 0$，因为初末状态相同
- 等体过程 $W = 0$，不是 $\Delta U = 0$
- $p$-$V$ 图面积 = 功的大小，方向由过程方向决定
:::

---

## Question Type 3: Kinetic Theory Explanation

### 如何识别

题目要求 "Use kinetic theory to explain why..." 涉及温度变化、压力变化等问题。

### 标准解题方法

:::note[解题思路]

1. 温度是分子平均动能的量度（$\frac{3}{2}kT = \frac{1}{2}m\langle c^2 \rangle$）
2. 膨胀时，分子与移动的活塞碰撞，速度减小（或：分子对活塞做功，损失动能）
3. 平均动能减小 → 温度降低
4. 压缩时相反：活塞对分子做功，动能增加 → 温度升高
:::

### 完整原题

**Example — 9702/41/M/J/21 Q2(b) (3 marks):**

> Use kinetic theory to explain why, when the piston is moved so that the gas expands, this causes a decrease in the temperature of the gas.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: temperature is related to (average) kinetic energy of molecules
- **B1**: (as gas expands) molecules do work on the piston (or: molecules collide with a receding piston)
- **B1**: molecules rebound with less speed (or: average kinetic energy decreases) → temperature decreases
</details>

### 常见陷阱

:::warning[常见陷阱]

- 不要只说 "gas expands → temperature drops" 而不解释分子层面的原因
- 必须提到 "molecules collide with moving piston" 或类似表述
- 用 "average kinetic energy" 而不是模糊的 "energy of molecules"
:::
