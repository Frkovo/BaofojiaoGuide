---
title: 方法框架
sidebar_position: 4
---

# 方法框架

## Overview

Paper 5 的不确定度计算分布在 Q1（实验设计）和 Q2（数据分析和结论）中。Q2 通常包含 3-4 个不确定度相关得分点。

---

## Method 1: Uncertainty in $\ln x$

:::note[推导]

$\Delta(\ln x) = \frac{d(\ln x)}{dx} \Delta x = \frac{1}{x} \Delta x$

:::

### 应用场景

Table 中需要计算 $\ln(x)$ 时。

**例子**：测量电压 $V$，计算 $\ln(V/\text{V})$。

- $V = 6.2$ V, $\Delta V = 0.2$ V
- $\ln(6.2) = 1.825$
- $\Delta(\ln V) = 0.2 / 6.2 = 0.0323$
- 结果: $1.825 \pm 0.032$

---

## Method 2: Uncertainty in $\lg x$

:::note[推导]

$\Delta(\lg x) = \frac{d(\lg x)}{dx} \Delta x = \frac{\Delta x}{x \ln 10} \approx 0.434 \frac{\Delta x}{x}$

:::

### 应用场景

Table 中需要计算 $\lg(x)$ 时。

**例子**：测量质量 $M$，计算 $\lg(M/10^{30})$。

- $M = 2.5 \times 10^{30}$ kg, $\Delta M = 0.1 \times 10^{30}$ kg
- $\lg(2.5) = 0.398$
- $\Delta(\lg M) = 0.434 \times (0.1/2.5) = 0.0174$
- 结果: $0.398 \pm 0.017$

---

## Method 3: Uncertainty in $1/x$

:::note[推导]

$\Delta(1/x) = \frac{d(1/x)}{dx} \Delta x = \frac{\Delta x}{x^2}$

:::

### 应用场景

Table 中需要计算 $1/x$ 或 $1/\sqrt{x}$ 时。

**例子**：测量距离 $d$，计算 $1/d$。

- $d = 0.200$ m, $\Delta d = 0.002$ m
- $1/d = 5.000$ m$^{-1}$
- $\Delta(1/d) = 0.002 / (0.200)^2 = 0.050$
- 结果: $5.00 \pm 0.05$ m$^{-1}$

---

## Method 4: Gradient Uncertainty (Best–Worst)

:::note[步骤]

1. 画 best fit line（直线通过数据点的"中心"）
2. 画 worst acceptable line
   - 所有 error bars 都必须被这条线穿过
   - 通常是最陡或最缓的合理直线
3. $\Delta \text{gradient} = |\text{gradient}_{\text{best}} - \text{gradient}_{\text{worst}}|$

:::

### 大三角形法

- 在 best fit line 上选两个远端点
- 两点在 x 轴上的距离要 &gt; 图中 x 范围的一半
- gradient = $\Delta y / \Delta x$
- worst line 也用同样方法

---

## Method 5: y-intercept Uncertainty

:::note[步骤]

1. 从 best fit line 读出 y-intercept（或延长线与 y 轴交点）
2. 从 worst acceptable line 读出 y-intercept
3. $\Delta \text{intercept} = |\text{intercept}_{\text{best}} - \text{intercept}_{\text{worst}}|$

:::

### 技巧

如果 x 轴不从 0 开始，需要延长 best/worst line 到 x = 0 处读取 y-intercept。

---

## Method 6: Percentage Uncertainty

$$
\text{Percentage uncertainty} = \frac{\Delta x}{x} \times 100\%
$$

### 组合百分比不确定度

| 运算 | 组合方式 |
|------|---------|
| 加减 | 绝对不确定度相加 |
| 乘除 | 百分比不确定度相加 |
| 幂次 | 百分比不确定度 $\times$ 指数 |

### 典型应用

从 gradient 和已知 constant 求最终常数的百分比不确定度：

$$
\frac{\Delta C}{C} = \frac{\Delta R}{R} + \frac{\Delta \text{gradient}}{\text{gradient}}
$$
