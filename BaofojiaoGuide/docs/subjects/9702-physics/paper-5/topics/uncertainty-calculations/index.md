---
title: Uncertainty Calculations
sidebar_position: 1
---

## 考纲要求

- Convert absolute uncertainty to fractional/percentage and vice versa
- Show uncertainty estimates beside every value in a table
- Calculate uncertainty estimates in derived quantities
- Estimate absolute uncertainty in gradient: |best - worst|
- Estimate absolute uncertainty in y-intercept
- Express a quantity as value, uncertainty and unit

## 常见题型

- [Derived Quantities](./question-types.md#question-type-1-uncertainty-in-derived-quantities-table) — ln, lg, reciprocal uncertainty propagation
- [Gradient Uncertainty](./question-types.md#question-type-2-gradient-uncertainty) — best and worst fit lines
- [Combined Uncertainty](./question-types.md#question-type-3-combined-uncertainty-in-final-constant) — error propagation in final answers

## 核心公式

- $\Delta(\ln x) = \frac{\Delta x}{x}$
- $\Delta(\lg x) = \frac{\Delta x}{x \ln 10} \approx 0.434\frac{\Delta x}{x}$
- $\Delta(1/x) = \frac{\Delta x}{x^2}$
- $\Delta(1/\sqrt{h}) = \frac{\Delta h}{2h^{3/2}}$
- Percentage: $\frac{\Delta x}{x} \times 100\%$
- Gradient uncertainty: $|\text{best} - \text{worst}|$

## 常见错误

- 忘记在表格中给每个 derived value 列出 uncertainty
- 梯度误差线画错（worst line 必须通过所有 error bars）
- 不确定度的有效数字位数不匹配
