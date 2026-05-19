---
title: 方法框架
sidebar_position: 4
---

# 方法框架

## Overview

Constants and Conclusions 部分通常出现在 Q2 的 (d)-(f) 部分。核心任务是：用 gradient/intercept 求常数 → 扩展计算 → 得出结论。

---

## Method 1: From Gradient to Constant

:::note[步骤]

1. 写出线性化后的方程 $y = mx + c$
2. 从图上读出 gradient $m$（带单位）
3. 写出 $m = f(\text{constant})$ 的关系式
4. 反解 constant $= f^{-1}(m)$
5. 代入数值，给出答案 + 单位

:::

### Example

实验关系: $T = 2\pi \sqrt{\frac{L}{g}}$，线性化为 $T^2 = \frac{4\pi^2}{g} L$

- $y = T^2$, $x = L$, gradient $= 4\pi^2/g$
- $\Rightarrow g = \frac{4\pi^2}{\text{gradient}}$
- 代入 gradient $= 4.02$ s$^2$m$^{-1}$ $\Rightarrow g = \frac{4\pi^2}{4.02} = 9.82$ m s$^{-2}$

---

## Method 2: From y-intercept to Constant

:::note[步骤]

1. 从图上读出 y-intercept $c$（带单位）
2. 写出 $c = f(\text{constant})$ 的关系式
3. 注意对数形式需要取指数:
   - $\ln$ 形式: constant $= e^{\,c}$
   - $\lg$ 形式: constant $= 10^{\,c}$
4. 代入数值，给出答案 + 单位

:::

### Example

实验关系: $V = V_0 e^{-t/RC}$，线性化为 $\ln V = \ln V_0 - t/RC$

- y-intercept $= \ln V_0$
- $\Rightarrow V_0 = e^{\,\text{intercept}}$
- 代入 intercept $= 2.30$ $\Rightarrow V_0 = e^{2.30} = 9.97$ V

---

## Method 3: Extension Calculation

:::note[步骤]

1. 确认需要使用哪些之前求出的常数
2. 找到题目要求计算的物理量对应的公式
3. 代入所有已知值（题目给的 + 实验求出的）
4. 计算结果 + 单位
5. 如需要，计算不确定度

:::

### Flow

```
已知常数 C = 4.7 × 10⁻⁶ F
已知 V₀ = 10.0 V
求 Q₀ = V₀ × C = 10.0 × 4.7 × 10⁻⁶ = 4.7 × 10⁻⁵ C
```

---

## Method 4: Drawing Conclusions

:::note[步骤]

1. 确定要比较的值（实验值 vs 理论值/预期值）
2. 计算实验值的 range: $(\text{value} - \Delta\text{value}, \ \text{value} + \Delta\text{value})$
3. 判断预期值是否在该范围内
4. 给出结论（支持/不支持）

:::

### 标准回答模板

> "The theoretical value of $R = 4.7\ \Omega$ lies within the range $(4.5 \pm 0.3)\ \Omega$, i.e. from $4.2\ \Omega$ to $4.8\ \Omega$. Therefore the results support the suggested relationship within experimental uncertainty."

或者：

> "The expected value of $n = 2.0$ lies outside the range $1.6 \pm 0.2$, i.e. from $1.4$ to $1.8$. Therefore the results do not support the suggested relationship."

---

## Method 5: Unit Derivation

:::note[步骤]

1. 从 gradient 的单位出发
2. 代入常数表达式中各个量的单位
3. 化简得出常数的单位
4. 检查量纲是否合理

:::

### Example

- gradient $k$ 单位: s$^{-1}$（从 $\ln V$ 对 $t$ 的图）
- $C = -\frac{1}{Rk}$，$R$ 单位 $\Omega$
- $C$ 单位: $\frac{1}{\Omega \cdot \text{s}^{-1}} = \frac{\text{s}}{\Omega} = \text{F}$ ✓
