---
title: Capacitance — 考纲逐点解读
sidebar_position: 3
---

# Capacitance — 考纲逐点解读

## 19.1 Capacitors and capacitance

### 1. Define capacitance, as applied to both isolated spherical conductors and to parallel plate capacitors

- **Capacitance $C$**: 导体储存电荷能力的量度
- 定义：$C = \frac{Q}{V}$
  - $Q$：一个极板上的电荷量
  - $V$：两极板间的电势差
- 对**孤立球形导体**：$C = 4\pi \epsilon_0 R$（$R$ 为球半径）
- 对**平行板电容器**：$C = \frac{\epsilon_0 A}{d}$（$A$ 为板面积，$d$ 为板间距）
  - （注：此公式在 syllabus 中未明确要求记忆，但理解有助于解题）

### 2. Recall and use $C = Q / V$

- 单位：**farad (F)** = C V$^{-1}$
- 在实际电路中，常用 $\mu$F ($10^{-6}$ F)、nF ($10^{-9}$ F)、pF ($10^{-12}$ F)

### 3. Derive, using $C = Q / V$, formulae for the combined capacitance of capacitors in series and in parallel

- **并联**：$V$ 相同
  $$C = C_1 + C_2 + C_3 + \dots$$
- **串联**：$Q$ 相同
  $$\frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + \dots$$

### 4. Use the capacitance formulae for capacitors in series and in parallel

- 注意电容串并联公式与电阻串并联**相反**！

## 19.2 Energy stored in a capacitor

### 1. Determine the electric potential energy stored in a capacitor from the area under the potential–charge graph

- $V$-$Q$ 图是直线（$V = Q/C$），面积 = $\frac{1}{2} QV$
- 充电过程中，$V$ 从 0 线性增加到最终值，所以平均电压为 $V/2$

### 2. Recall and use $W = \frac{1}{2} QV = \frac{1}{2} CV^2$

- $$W = \frac{1}{2} QV = \frac{1}{2} CV^2 = \frac{1}{2} \frac{Q^2}{C}$$
- 注意三个公式的选择取决于已知量

## 19.3 Discharging a capacitor

### 1. Analyse graphs of variation with time of p.d., charge and current for a capacitor discharging through a resistor

- RC 放电时，$V$, $Q$, $I$ 都按指数规律衰减
- $V$-$t$ 图：指数衰减曲线（从 $V_0$ 趋于 0）
- $I$-$t$ 图：指数衰减曲线（从 $I_0 = V_0/R$ 趋于 0）
- $Q$-$t$ 图：指数衰减曲线（从 $Q_0 = CV_0$ 趋于 0）

### 2. Recall and use $\tau = RC$ for the time constant for a capacitor discharging through a resistor

- **Time constant $\tau = RC$** 的量纲是秒
- 物理意义：$t = \tau$ 时，$V = V_0 e^{-1} \approx 0.37 V_0$
- $\tau$ 越大，放电越慢

### 3. Use equations of the form $x = x_0 e^{-t/RC}$ where $x$ could represent current, charge or potential difference for a capacitor discharging through a resistor

- $$I = I_0 e^{-t/RC}, \quad Q = Q_0 e^{-t/RC}, \quad V = V_0 e^{-t/RC}$$
- 充电公式：$x = x_0 (1 - e^{-t/RC})$
- **半衰期**（选学但有用）：$t_{1/2} = RC \ln 2 \approx 0.693 RC$
