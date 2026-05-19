---
title: Oscillations — 题型分析
sidebar_position: 2
---

# Oscillations — 题型分析

## Question Type 1: Definition of SHM

### 如何识别

题目包含 "State what is meant by simple harmonic motion"。

### 标准解题方法

:::note[解题要点]

1. 加速度与位移**成正比**（proportional to displacement）
2. 加速度方向与位移**相反**（in opposite direction to displacement / directed towards equilibrium）
:::

### 评分标准

:::info[评分模式]

- **B1**: acceleration (directly) proportional to displacement
- **B1**: acceleration in opposite direction to displacement / directed towards equilibrium
:::

### 完整原题

**Example 1 — 9702/41/O/N/20 Q3(a) (2 marks):**

> State what is meant by simple harmonic motion.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: acceleration (directly) proportional to displacement
- **B1**: acceleration in opposite direction to displacement
</details>

**Example 2 — 9702/41/M/J/21 Q3(a) (2 marks):**

> State what is meant by simple harmonic motion.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: acceleration proportional to displacement
- **B1**: acceleration (directed) towards equilibrium / opposite to displacement
</details>

**Example 3 — 9702/41/O/N/22 Q3(a) (2 marks):**

> State the defining equation for simple harmonic motion. Identify the meaning of each of the symbols used to represent physical quantities.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: $a = -\omega^2 x$
- **B1**: $a$ = acceleration, $\omega$ = angular frequency, $x$ = displacement
</details>

### 常见陷阱

:::warning[常见陷阱]

- 必须同时提到"正比"和"相反方向"两个条件
- 只写 $a = -\omega^2 x$ 不够——还需要文字说明
:::

---

## Question Type 2: SHM Calculations

### 如何识别

题目给出振动参数（振幅、频率、质量等），求速度、加速度、力、能量等。

### 标准解题方法

:::note[解题步骤]

1. 确定振幅 $x_0$ 和角频率 $\omega$（或频率 $f$）
2. 最大速度：$v_0 = \omega x_0$
3. 最大加速度：$a_0 = \omega^2 x_0$
4. 最大力：$F_0 = m a_0 = m \omega^2 x_0$
5. 特定位置速度：$v = \pm \omega \sqrt{x_0^2 - x^2}$
6. 总能量：$E = \frac{1}{2} m \omega^2 x_0^2$
:::

### 评分标准

:::info[评分模式]

- **C1**: 写出正确公式（如 $v = \omega x_0$）
- **C1**: 正确代入数值（注意单位统一）
- **A1**: 最终答案（含单位）
:::

### 完整原题

**Example 1 — 9702/41/M/J/20 Q3 (9 marks):**

> The piston in the cylinder of a car engine moves with SHM. The distance moved between max and min height is 9.8 cm. Mass = 640 g. The piston completes 2700 oscillations in 1.0 minute. Determine:
> (a)(i) the amplitude
> (a)(ii) the frequency
> (a)(iii) the maximum speed
> (a)(iv) the speed when the top of the piston is 2.3 cm below its maximum height
> (b) the resultant force giving rise to its maximum acceleration

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **(a)(i) A1**: amplitude $= 9.8 / 2 = 4.9$ cm
- **(a)(ii) A1**: $f = 2700 / 60 = 45$ Hz
- **(a)(iii) C1**: $v_0 = \omega x_0$ or $v_0 = 2\pi f x_0$
- **(a)(iii) A1**: $v_0 = 2\pi \times 45 \times 0.049 = 13.9$ m s$^{-1}$
- **(a)(iv) C1**: $v = \omega \sqrt{x_0^2 - x^2}$ or $v^2 = \omega^2 (x_0^2 - x^2)$
- **(a)(iv) A1**: $v = 2\pi \times 45 \times \sqrt{0.049^2 - (0.049 - 0.023)^2} = 9.9$ m s$^{-1}$
- **(b) C1**: $a_0 = \omega^2 x_0$ or $a_0 = (2\pi f)^2 x_0$
- **(b) C1**: $F = ma_0$
- **(b) A1**: $F = 0.640 \times (2\pi \times 45)^2 \times 0.049 = 2.5 \times 10^3$ N
</details>

**Example 2 — 9702/41/O/N/22 Q3 (11 marks):**

> An object oscillates vertically with SHM. Fig. 3.2 shows $v$-$x$ graph. Fig. 3.3 shows $E_P$-$x$ graph.
> (i) Determine the amplitude $x_0$
> (ii) Show that $\omega = 1.7$ rad s$^{-1}$
> (iii) Determine the mass $M$ of the object

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **(i) A1**: $x_0 = 0.10$ m (from graph)
- **(ii) C1**: $v_0 = 0.17$ m s$^{-1}$ (from graph), $v_0 = \omega x_0$
- **(ii) C1**: $\omega = 0.17 / 0.10 = 1.7$ rad s$^{-1}$
- **(iii) C1**: $E_{P,\max} = \frac{1}{2} m \omega^2 x_0^2$ or $E_{K,\max} = \frac{1}{2} m v_0^2$
- **(iii) A1**: $m = 2 \times 0.050 / (1.7^2 \times 0.10^2) = 3.5$ kg
</details>

### 常见陷阱

:::warning[常见陷阱]

- 振幅是总位移的一半（不是总位移）
- 角频率 $\omega$ 和频率 $f$ 不要混淆：$\omega = 2\pi f$
- 速度最大的位置在平衡位置（$x = 0$），加速度最大在极端位置（$x = \pm x_0$）
- $v$-$x$ 图是椭圆，$v$-$t$ 图是正弦/余弦
:::

---

## Question Type 3: Damping and Resonance

### 如何识别

题目涉及 "damped oscillations"、"light/critical/heavy damping"、"resonance"、"forced oscillations" 等关键词。

### 标准解题方法

:::note[解题要点]

- **Light damping**: 振幅逐渐减小，周期略增（仍可振荡多次）
- **Critical damping**: 最快回到平衡位置（不振荡）
- **Heavy damping**: 缓慢回到平衡位置（甚至不回），不振荡
- **Resonance**: 驱动力频率 = 系统自然频率时，振幅最大
- 如果给定频率下振幅恒定 → 存在**阻尼**（否则无阻尼时振幅会无限增大）
:::

### 完整原题

**Example — 9702/41/M/J/21 Q3(c) (3 marks):**

> The oscillator is switched on. The frequency is varied, keeping amplitude constant. The amplitude of oscillation of the trolley is a maximum at the frequency calculated in (b).
> (i) State the name of the effect giving rise to this maximum.
> (ii) At any given frequency, the amplitude of oscillation of the trolley is constant. Explain how this indicates that there are resistive forces opposing the motion.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **(i) B1**: resonance
- **(ii) B1**: without resistive forces the amplitude would continue to increase
- **(ii) B1**: constant amplitude shows energy input = energy dissipated
</details>

### 常见陷阱

:::warning[常见陷阱]

- 共振条件是驱动频率 = **自然频率**（不是其他频率）
- 轻阻尼 ≠ 无阻尼——轻阻尼振幅仍会缓慢减小
- 临界阻尼是"最快回到平衡"（not "最快停止"）
- 画 $x$-$t$ 图时注意：轻阻尼是逐渐减小的正弦波；临界阻尼是快速回到零（不越过）；重阻尼是缓慢趋于零
:::

---

## Question Type 4: Energy in SHM — Graph Sketching

### 如何识别

要求 sketch 能量（$E_K$, $E_P$, $E_{total}$）随位移或时间的变化图。

### 标准解题方法

:::note[图形要点]

- $E_K$-$x$: 开口向下抛物线（$x=0$ 最大，$x=\pm x_0$ 为零）
- $E_P$-$x$: 开口向上抛物线（$x=0$ 为零，$x=\pm x_0$ 最大）
- $E_{total}$: 水平线（常数）
- $E_K$-$t$ 和 $E_P$-$t$: 正弦平方曲线（频率是振动频率的 2 倍）
:::

### 常见陷阱

:::warning[常见陷阱]

- 总能量不变（守恒），不是动能或势能不变
- $E_K$ 和 $E_P$ 的相位差 $\pi/2$（时间上差 $T/4$）
- 能量转换频率是振动频率的 2 倍（因为每个周期动能两次最大）
:::
