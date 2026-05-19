---
title: 考纲要点
sidebar_position: 3
---

# 考纲要点

## 1. 不确定度的基本转换

### 绝对 → 分数/百分比

- Fractional uncertainty: $\frac{\Delta x}{x}$
- Percentage uncertainty: $\frac{\Delta x}{x} \times 100\%$

### 分数/百分比 → 绝对

- $\Delta x = \frac{\text{percentage}}{100} \times x$

## 2. 表格中的不确定度

### 要求

每个 derived quantity 必须在表格中列出对应的 absolute uncertainty

### 常见派生量公式

| 派生量 $Y$ | $\Delta Y$ 公式 |
|-----------|----------------|
| $\ln x$ | $\frac{\Delta x}{x}$ |
| $\lg x$ | $\frac{\Delta x}{x \ln 10} \approx 0.434\frac{\Delta x}{x}$ |
| $1/x$ | $\frac{\Delta x}{x^2}$ |
| $1/\sqrt{x}$ | $\frac{\Delta x}{2x^{3/2}}$ |
| $x^n$ | $n x^{n-1} \Delta x$ |

## 3. 梯度不确定度

### 方法

1. 画 best fit line（最佳拟合直线）
2. 画 worst acceptable line（最差可接受直线 — 通过所有 error bars 的最陡/最缓线）
3. $\Delta \text{gradient} = |\text{gradient}_{\text{best}} - \text{gradient}_{\text{worst}}|$

### 大三角形法

用坐标轴上的两个远端点计算 gradient，保证三角形尽可能大（&gt; 一半图幅）。

## 4. y-intercept 不确定度

### 方法

1. best fit line 的 y-intercept
2. worst acceptable line 的 y-intercept
3. $\Delta \text{intercept} = |\text{intercept}_{\text{best}} - \text{intercept}_{\text{worst}}|$

## 5. 组合不确定度

| 运算 | 误差传播 |
|------|---------|
| $Z = A + B$ | $\Delta Z = \Delta A + \Delta B$ |
| $Z = A - B$ | $\Delta Z = \Delta A + \Delta B$ |
| $Z = A \times B$ | $\frac{\Delta Z}{Z} = \frac{\Delta A}{A} + \frac{\Delta B}{B}$ |
| $Z = A / B$ | $\frac{\Delta Z}{Z} = \frac{\Delta A}{A} + \frac{\Delta B}{B}$ |
| $Z = A^n$ | $\frac{\Delta Z}{Z} = n \frac{\Delta A}{A}$ |

## 6. 表达最终结果

格式: $\text{value} \pm \text{uncertainty}$（带单位）

- uncertainty 一般给 1 位有效数字
- value 的小数位数与 uncertainty 对齐
