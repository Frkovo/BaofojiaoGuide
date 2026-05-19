---
title: Capacitance — 题型分析
sidebar_position: 2
---

# Capacitance — 题型分析

## Question Type 1: Definition of Capacitance

### 如何识别

题目包含 "Define capacitance" 或 "State what is meant by the capacitance of a capacitor"。

### 标准解题方法

:::note[解题要点]

- **Capacitance** = charge per unit potential difference
- 需明确是 "charge on **one** plate" 和 "potential difference **across the plates**"
:::

### 评分标准

:::info[评分模式]

- **M1**: charge per unit potential (difference)
- **A1**: charge on one plate and p.d. across the plates
:::

### 完整原题

**Example 1 — 9702/41/O/N/20 Q6(a)(i) (2 marks):**

> Define the capacitance of a parallel plate capacitor.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: charge per unit potential (difference)
- **A1**: charge on one plate and potential difference across the plates
</details>

**Example 2 — 9702/41/M/J/21 Q7(a) (2 marks):**

> State what is meant by the capacitance of a parallel plate capacitor.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: charge per unit potential (difference)
- **A1**: (charge stored) on one plate / p.d. across the capacitor
</details>

### 常见陷阱

:::warning[常见陷阱]

- 只说 "charge per unit potential difference" 可能不够——需要提 "on one plate"
- 不是 "charge on both plates"——正负电荷分别在两个板上
:::

---

## Question Type 2: Combined Capacitance Calculations

### 如何识别

题目给出多个电容，要求计算总电容。

### 标准解题方法

:::note[解题步骤]

1. 串联：$\frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2} + \dots$
2. 并联：$C = C_1 + C_2 + \dots$
3. 注意：电容串并联公式与**电阻相反**！
4. 复杂电路：先找纯并联或纯串联的部分，逐步化简
:::

### 评分标准

:::info[评分模式]

- **C1**: 写出正确的公式/计算部分组合
- **A1**: 最终答案（含单位）
:::

### 完整原题

**Example 1 — 9702/41/O/N/20 Q6(b) (2 marks):**

> A student has four capacitors, each 24 $\mu$F. They are connected as shown — three in series (two parallel branches with two capacitors) between X and Y. Calculate the combined capacitance.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **C1**: series combination: $1/C = 1/24 + 1/24 + 1/24$ → $C = 8$ $\mu$F
- **A1**: total $C = 8 + 24 = 32$ $\mu$F
</details>

**Example 2 — 9702/41/M/J/21 Q7(b)(ii) (2 marks):**

> A capacitor of capacitance C is connected into the circuit shown. For V = 150 V and f = 60 Hz, the average current is 4.8 $\mu$A. Calculate the capacitance in pF.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **C1**: $I = fCV$
- **C1**: $C = I/(fV) = 4.8 \times 10^{-6} / (60 \times 150)$
- **A1**: $= 5.3 \times 10^{-10}$ F $= 530$ pF
</details>

### 常见陷阱

:::warning[常见陷阱]

- 电容串联公式与电阻**相反**：串联 $\frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2}$，并联 $C = C_1 + C_2$
- 两个相同电容串联：$C = C_1/2$，不是 $C_1/4$
- 单位：1 $\mu$F $= 10^{-6}$ F, 1 pF $= 10^{-12}$ F
:::

---

## Question Type 3: Energy Stored in a Capacitor

### 如何识别

题目要求计算电容器储存的能量，或使用 $W = \frac{1}{2}QV$。

### 标准解题方法

:::note[解题步骤]

1. 从 $V$-$Q$ 图，面积 = $\frac{1}{2} QV$ = 储能
2. 公式：$W = \frac{1}{2} QV = \frac{1}{2} CV^2 = \frac{1}{2} Q^2 / C$
3. 选择最方便的公式（取决于已知量）
:::

### 常见陷阱

:::warning[常见陷阱]

- 能量不是 $QV$，而是 $\frac{1}{2} QV$（因为充电过程中 $V$ 从 0 增加到最终值）
- $W = \frac{1}{2} CV^2$ 中的 $V$ 是最终电压，不是变化量
:::

---

## Question Type 4: RC Discharge — Graphs and Calculations

### 如何识别

题目给出 RC 放电电路，要求计算时间常数、电流、电荷等，或 sketch 放电曲线。

### 标准解题方法

:::note[解题步骤]

1. **初始值**（$t = 0$）：
   - $Q_0 = CV_0$
   - $I_0 = V_0 / R$
2. **时间常数**：$\tau = RC$（单位：s）
3. **放电公式**：
   - $Q = Q_0 e^{-t/RC}$
   - $V = V_0 e^{-t/RC}$
   - $I = I_0 e^{-t/RC}$
4. **$t = RC$ 时**：$x = x_0 e^{-1} \approx 0.37 x_0$
5. **半衰期**：$t_{1/2} = RC \ln 2 \approx 0.693 RC$
:::

### 评分标准

:::info[评分模式]

- **C1**: 写出 $Q = CV$ 或 $I = V/R$ 求初始值
- **C1**: $\tau = RC$ 或指数公式
- **A1**: 正确答案（含单位）
- **作图**：**B1** 指数衰减形状 + **B1** 标注初始值或时间常数
:::

### 完整原题

**Example 1 — 9702/41/O/N/22 Q5 (11 marks):**

> A capacitor of 470 $\mu$F is connected to a 24 V battery. Switch S is moved to Y so the capacitor discharges through wire P (5.6 k$\Omega$).
> (a)(i) Calculate the charge on the capacitor at t = 0.
> (a)(ii) Calculate the current in wire P at t = 0.
> (a)(iii) Calculate the time constant of the discharge circuit.
> (a)(iv) On Fig. 5.2, sketch the variation of I with t.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **(a)(i) C1**: $Q = CV$
- **(a)(i) A1**: $= 470 \times 10^{-6} \times 24 = 1.13 \times 10^{-2}$ C
- **(a)(ii) A1**: $I = V/R = 24 / 5600 = 4.3 \times 10^{-3}$ A
- **(a)(iii) C1**: $\tau = RC$
- **(a)(iii) A1**: $= 5600 \times 470 \times 10^{-6} = 2.6$ s
- **(a)(iv) B1**: exponential decay starting at $I_0$
- **(a)(iv) B1**: correct shape approaching zero asymptotically
</details>

**Example 2 — 9702/41/M/J/23 Q5 (9 marks, part)**

> Fig. 5.2 shows the variation of $V_{IN}$ with t. Fig. 5.3 shows $V_{OUT}$ with t. Show that the time constant $\tau$ for the discharge of the capacitor through the resistor is 0.038 s. Calculate the capacitance C.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **(b)(ii) C1**: $V_{OUT} = V_0 e^{-t/RC}$
- **(b)(ii) C1**: $0.50 = 7.5 e^{-t/RC}$ or reads time from graph
- **(b)(ii) A1**: shows that $\tau = 0.038$ s
- **(b)(iii) C1**: $C = \tau / R = 0.038 / 14000$
- **(b)(iii) A1**: $= 2.7 \times 10^{-6}$ F (unit required)
</details>

### 常见陷阱

:::warning[常见陷阱]

- 放电是 $x = x_0 e^{-t/RC}$（指数衰减），不是 $x = x_0 (1 - e^{-t/RC})$（这是充电公式）
- 时间常数 $\tau = RC$，$R$ 和 $C$ 都用 SI 单位（$\Omega$ 和 F），结果才是秒
- 放电时电流方向与充电时相反
- $t = RC$ 时 $x / x_0 = e^{-1} \approx 0.37$，不是 $0.5$
- 半衰期 $t_{1/2} = RC \ln 2 \approx 0.693 RC$
:::
