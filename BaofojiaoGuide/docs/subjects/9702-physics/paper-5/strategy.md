---
title: 详细策略
sidebar_position: 8
---

# 详细策略

## Q1 实验设计策略

### 1. Defining the Problem（约 2 分钟，**2** 分）

:::note[Key]

**M1** — 明确写出自变量和因变量。

**A1** — 写出至少两个控制变量。

:::

- **Independent variable（自变量）**: 你要改变的量。写出具体名称，并说明如何改变它。
- **Dependent variable（因变量）**: 你要测量的量。写出具体名称，并说明用什么仪器测量。
- **Control variables（控制变量）**: 需要保持恒定的量。至少列出 **$2$ 个**，并简要说明如何保持恒定。

**例句**:

> The **independent variable** is the length $L$ of the pendulum，which will be varied by using different lengths of string.
>
> The **dependent variable** is the period $T$ of oscillation，which will be measured using a stopwatch.
>
> The **control variables** are the mass of the bob (kept constant by using the same bob) and the amplitude of swing (kept small and constant).

### 2. Methods of Data Collection（约 15 分钟，**5** 分）

:::note[Key]

**M1** — 画出清晰标注的装置图。

**A1** — 描述实验步骤（改变 $IV$、测量 $DV$、保持 $CV$ 恒定）。

**B1** — 说明测量范围和间隔。

:::

#### 装置图要点

- 画出所有主要仪器
- 标注所有关键部件
- 显示 $IV$ 如何改变
- 显示 $DV$ 如何测量
- 可以使用简单线条，但要清晰

#### 步骤描述

1. **改变 $IV$**: 明确描述每一步如何改变自变量。例如："Vary the length $L$ by using strings of different lengths from $0.20\ \text{m}$ to $1.00\ \text{m}$ in increments of $0.10\ \text{m}$."
2. **测量 $DV$**: 具体描述测量方法。例如："Measure the time for $20$ oscillations using a stopwatch，then divide by $20$ to get the period $T$."
3. **保持 $CV$ 恒定**: 
   - 确保每次只改变一个变量
   - 例如："Use the same metal bob throughout to keep the mass constant."
   - "Ensure the amplitude is small ($\theta &lt; 10^\circ$) to maintain small-angle approximation."

#### 测量仪器参考

| 物理量 | 仪器 | 精度 |
|-------|------|------|
| 长度 | metre ruler / micrometer / vernier callipers | $\pm 0.001\ \text{m}$ / $\pm 0.0001\ \text{m}$ |
| 时间 | stopwatch / timer | $\pm 0.01\ \text{s}$ / $\pm 0.1\ \text{s}$ |
| 质量 | digital balance | $\pm 0.001\ \text{g}$ |
| 温度 | thermometer / thermocouple | $\pm 0.1^\circ\text{C}$ |
| 电流/电压 | ammeter / voltmeter / multimeter | $\pm 0.01\ \text{A}$ / $\pm 0.01\ \text{V}$ |
| 力 | newton meter / force sensor | $\pm 0.01\ \text{N}$ |
| 角度 | protractor | $\pm 0.5^\circ$ |

### 3. Method of Analysis（约 5 分钟，**3** 分）

:::note[Key]

**M1** — 说明要画什么图像。

**A1** — 说明直线证明关系。

**B1** — 给出用梯度/截距计算常数的公式。

:::

**写法模板**:

> A graph of $T^2$ against $L$ is plotted. If the relationship $T = 2\pi \sqrt{\frac{L}{g}}$ holds，the graph will be a straight line through the origin. The gradient of the line will be $\frac{4\pi^2}{g}$，so $g = \frac{4\pi^2}{\text{gradient}}$.

或者：

> A graph of $\ln V$ against $t$ is plotted. If $V = V_0 e^{-t/\tau}$，the graph will be a straight line. The gradient will be $-\frac{1}{\tau}$，so $\tau = -\frac{1}{\text{gradient}}$. The $y$-intercept will be $\ln V_0$.

### 4. Additional Detail & Safety（约 10 分钟，**5** 分）

:::note[Key]

**M1** — 重复测量。

**A1** — 数据范围。

**B1** — 安全措施。

:::

#### 重复测量

> Repeat each reading at least twice (or three times) and calculate the mean value of the dependent variable to reduce random errors and identify anomalous readings.

#### 数据范围

> Take readings at $5$-$6$ different values of the independent variable，covering as wide a range as possible to minimize percentage uncertainty.

#### 安全措施

根据实验场景选择适当的安全措施：

| 场景 | 安全措施 |
|------|---------|
| 电路 | "Switch off between readings to prevent overheating." |
| 光学实验 | "Do not look directly into the laser beam." |
| 悬挂重物 | "Wear safety goggles / secure clamp to prevent falling." |
| 加热 | "Use a heat-proof mat and tongs / keep flammable materials away." |
| 液体 | "Wipe up spills immediately." |

#### 额外确定常数的步骤

如果题目要求确定一个常数，除了主要测量外，可能还需要测量其他量：

> Also measure the diameter $d$ of the wire using a micrometer to calculate the cross-sectional area $A = \pi d^2/4$.

---

## Q2 数据分析策略

### Part (a): 线性化表达式（约 3 分钟，**1** 分）

:::note[Key]

**M1** — 正确写出线性化后的斜率和截距表达式。

:::

**步骤**:

1. 从题目给出的公式出发
2. 将其变形为 $y = mx + c$ 的形式
3. 确定 $x$ 轴和 $y$ 轴各放什么量
4. 写出梯度 $m$ 和截距 $c$ 对应什么

**示例**:

题目给出 $T = 2\pi \sqrt{\frac{l}{g}}$，要求验证 $T \propto \sqrt{l}$。

> $$T = 2\pi \sqrt{\frac{l}{g}} \implies T^2 = \frac{4\pi^2}{g} l$$
>
> Plot $T^2$ on $y$-axis against $l$ on $x$-axis.
>
> Gradient $m = \frac{4\pi^2}{g}$，so $g = \frac{4\pi^2}{m}$.
>
> $y$-intercept $c = 0$ (through origin).

### Part (b): 表格计算（约 5 分钟，**2** 分）

:::note[Key]

**M1** — 正确计算衍生量。

**A1** — 正确计算不确定度。

:::

#### 衍生量计算

根据 Part (a) 的结论，计算所需的衍生量，如 $\lg x$、$\ln y$、$1/x$、$x^2$、$\sqrt{x}$ 等。

#### 不确定度传播

| 原始量 | 衍生量 | 不确定度 |
|-------|-------|---------|
| $x \pm \Delta x$ | $\ln x$ | $\displaystyle \Delta(\ln x) = \frac{\Delta x}{x}$ |
| $x \pm \Delta x$ | $1/x$ | $\displaystyle \Delta(1/x) = \frac{\Delta x}{x^2}$ |
| $x \pm \Delta x$ | $x^2$ | $\displaystyle \Delta(x^2) = 2x \cdot \Delta x$ |
| $x \pm \Delta x$ | $\sqrt{x}$ | $\displaystyle \Delta(\sqrt{x}) = \frac{\Delta x}{2\sqrt{x}}$ |
| $x \pm \Delta x$ | $\lg x$ | $\displaystyle \Delta(\lg x) = \frac{\Delta x}{x \ln 10}$ |

#### 有效数字

不确定度一般保留 **$1$ 位有效数字**，衍生量与不确定度对齐小数位数。

### Part (c): 图表（约 15 分钟，**6** 分）

:::note[Key]

**M1** — 正确描点。

**A1** — 合理画误差棒。

**B1** — 最佳拟合线和最差线。

**Gradient 计算和不确定度**。

:::

#### 描点

- 用 $\times$ 标记数据点
- 精确到半小格以内
- 选择合适的坐标轴比例，使数据点大致占据图纸的 $50\%$ 以上

#### 误差棒（Error Bars）

- 对称误差棒
- 长度 = $2 \times$ 不确定度
- 如果两个变量都有不确定度，两端都需要误差棒

#### 最佳拟合线（Best Fit Line）

- 直线应穿过所有误差棒
- 数据点大致均匀分布在直线两侧（不要强行通过所有点）
- 用透明直尺画线

#### 最差线（Worst Acceptable Line）

- 在最佳线的基础上旋转，直到触碰到误差棒的边界
- 有两种可能：最陡（steepest）和最缓（shallowest），选择偏差更大的那个

#### 梯度计算

$$m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$

- 在线上选取两个点，相距 $&gt;$ 线段长度的一半
- 用三角形标记所选点
- 标出 $\Delta y$ 和 $\Delta x$

#### 梯度不确定度

$$\Delta m = |m_{\text{best}} - m_{\text{worst}}|$$

对最佳线和最差线分别计算梯度，取差值绝对值。

#### $y$ 截距

从公式 $y = mx + c$ 推导，**不要直接从图线读取**：

$$c = y_1 - m x_1$$

其中 $(x_1, y_1)$ 为线上任一点。

### Part (d): 计算常数（约 6 分钟，**4** 分）

:::note[Key]

**M1** — 正确代入梯度/截距。

**A1** — 正确写出单位和不确定度。

:::

使用 Part (a) 的表达式，将 Part (c) 得到的梯度/截距代入。

**示例**:

$$g = \frac{4\pi^2}{m} = \frac{4\pi^2}{4.02} = 9.82\ \text{m s}^{-2}$$

不确定度传播：

$$\frac{\Delta g}{g} = \frac{\Delta m}{m} \implies \Delta g = g \times \frac{\Delta m}{m}$$

最终结果：

$$g = 9.82 \pm 0.05\ \text{m s}^{-2}$$

### Part (e): 拓展部分（约 3 分钟，**2** 分）

使用你的常数和给定的方程，完成题目要求的额外计算。通常是用公式计算新的物理量，或者估计某个值。

**技巧**: 有时这一问会要求你使用与 Part (d) 不同的常数表达式（如使用 $y$ 截距而非梯度），注意读题。
