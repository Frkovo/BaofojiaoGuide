---
title: 考前速通
sidebar_position: 10
---

# 考前速通

## Q1 实验设计速查

### 1. Defining the Problem（$2$ 分）

| 项目 | 关键写法 |
|------|---------|
| **Independent variable** | 写下 "The **independent variable** is \_\_\_\_\_\_，which will be varied by \_\_\_\_\_\_." |
| **Dependent variable** | 写下 "The **dependent variable** is \_\_\_\_\_\_，which will be measured by \_\_\_\_\_\_." |
| **Control variables** | 至少列出 $2$ 个控制变量，如温度、长度、质量等 |

### 2. Methods of Data Collection（$5$ 分）

| 要点 | 关键短语 |
|------|---------|
| 装置图 | "A labelled diagram showing \_\_\_\_\_\_" |
| 改变 IV | "The $IV$ is varied by \_\_\_\_\_\_" |
| 测量 DV | "$DV$ is measured using a \_\_\_\_\_\_ (instrument)" |
| 保持 CV 恒定 | "$CV$ is kept constant by \_\_\_\_\_\_" |
| 测量范围 | "Measurements are taken over a range of \_\_\_\_\_\_" |

### 3. Method of Analysis（$3$ 分）

| 要点 | 关键写法 |
|------|---------|
| 图像类型 | "A graph of \_\_\_\_\_\_ is plotted" |
| 期待结果 | "If the relationship holds，the graph will be a straight line" |
| 常数公式 | "The constant can be found from the gradient/intercept = \_\_\_\_\_\_" |

### 4. Additional Detail / Safety（$5$ 分）

| 要点 | 关键写法 |
|------|---------|
| 重复测量 | "Repeat each reading \_\_\_\_ times and calculate the mean" |
| 数据点数量 | "At least $5$-$6$ readings over the range" |
| 安全措施 | "安全短语同下" |
| 额外确定步骤 | "Also measure \_\_\_\_\_\_ to calculate the constant" |

### 常见安全措施

| 场景 | 安全措施 |
|------|---------|
| 电路 | "Turn off power supply between readings to avoid overheating" |
| 重物/悬挂 | "Wear safety goggles to protect eyes" |
| 高温 | "Use heat-proof mat and tongs" |
| 液体 | "Wipe spills immediately" |
| 光学 | "Do not look directly at laser" |

### 画图要点

- 仪器必须标注名称
- 显示如何测量 $IV$ 和 $DV$
- 显示如何保持 $CV$ 恒定
- 比例合理，连接清晰

---

## Q2 数据分析速查

### 线性化公式

常见关系与线性化方式：

| 原始关系 | 线性化 |
|---------|--------|
| $y = ax^n$ | $\lg y = \lg a + n \lg x$ |
| $y = ae^{kx}$ | $\ln y = \ln a + kx$ |
| $y = a + \frac{b}{x}$ | $y = a + b \left(\frac{1}{x}\right)$ |
| $y = a\sqrt{x} + b$ | $y = a\sqrt{x} + b$ |

### 不确定度传播公式

| 运算 | 不确定度 |
|------|---------|
| $\Delta(\ln x)$ | $\displaystyle \frac{\Delta x}{x}$ |
| $\Delta(1/x)$ | $\displaystyle \frac{\Delta x}{x^2}$ |
| $\Delta(x^2)$ | $2x \cdot \Delta x$ |
| $\Delta(\sqrt{x})$ | $\displaystyle \frac{\Delta x}{2\sqrt{x}}$ |

### 梯度计算

- **Best fit line gradient**: 在线上选取两个相距较远的点（$>$ 线段长度的一半）
- **Worst acceptable line**: 通过所有误差棒的最陡/最缓直线
- **Gradient uncertainty** = $|\text{gradient}_{\text{best}} - \text{gradient}_{\text{worst}}|$

### $y$ 截距

:::caution

不要从图中直接读取 $y$ 截距！从 $y = mx + c$ 推导：

$$c = \bar{y} - m\bar{x}$$

:::

使用线上任意一点 $(x_1, y_1)$：

$$c = y_1 - mx_1$$

---

## Time Plan

| 时间 | 任务 |
|------|------|
| $0$ - $5$ min | 阅读两题，理解实验与数据 |
| **Q1** | |
| $5$ - $10$ min | **Definitions** — 写 $IV$、$DV$、$CV$ |
| $10$ - $25$ min | **Methods** — 画图 + 详细步骤 |
| $25$ - $30$ min | **Analysis** — 图像类型 + 常数公式 |
| $30$ - $40$ min | **Details / Safety** — 重复 + 安全 |
| **Q2** | |
| $40$ - $45$ min | **Expressions** — 线性化 |
| $45$ - $50$ min | **Table** — 计算 + 不确定度 |
| $50$ - $65$ min | **Graph** — 描点 + 画线 + 求梯度 |
| $65$ - $71$ min | **Constants** — 常数 + 不确定度 |
| $71$ - $75$ min | **Extension** — 最终计算 |

:::tip

如果时间不够，优先保证 Q1 的 **Definitions**（$2$ 分易得）和 **Methods**（$5$ 分），以及 Q2 的 **Graph**（$6$ 分最多）。这些是性价比最高的部分。

:::
