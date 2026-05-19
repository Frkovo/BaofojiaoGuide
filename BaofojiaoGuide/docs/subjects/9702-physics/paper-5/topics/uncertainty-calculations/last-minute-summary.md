---
title: 考前速通
sidebar_position: 7
---

# 考前速通

## Propagation Formulas (Must Know)

| Original $Y$ | $\Delta Y$ |
|-------------|-----------|
| $\ln x$ | $\Delta x / x$ |
| $\lg x$ | $0.434 \times \Delta x / x$ |
| $1/x$ | $\Delta x / x^2$ |
| $1/\sqrt{x}$ | $\Delta x / (2x^{3/2})$ |
| $x^n$ | $n x^{n-1} \Delta x$ |
| $\sqrt{x}$ | $\Delta x / (2\sqrt{x})$ |

## Gradient Uncertainty Workflow

```
best fit line → gradient_best
worst line through all error bars → gradient_worst
Δgradient = |gradient_best - gradient_worst|
Answer: gradient ± Δgradient
```

## Combined Uncertainty Workflow

```
Identify formula for constant C
Find all contributing uncertainties (ΔR, Δk, Δintercept, etc.)
Sum fractional/percentage uncertainties
ΔC = C × (sum of fractional uncertainties)
Answer: C ± ΔC (with units)
```

## Red Flags

| 信号 | 可能的问题 |
|------|-----------|
| 看到 $\ln$ | $\Delta(\ln x) = \Delta x / x$，无 0.434 |
| 看到 $\lg$ | 必须用 0.434 因子 |
| 看到 $1/x$ | $\Delta(1/x) = \Delta x / x^2$ |
| Table 中 $Y$ | 每个值旁必须有 uncertainty 列 |
| 题目要求 gradient | 必须画 worst line |
| error bars 在图上 | worst line 必须通过所有 error bars |
| y-intercept | 从 x = 0 处读取，延长线可能需要 |

## Quick Checklist

### Part (b): Table with derived quantities
- [ ] All derived values calculated correctly
- [ ] Uncertainty formula stated
- [ ] Each value has uncertainty beside it
- [ ] Significant figures consistent

### Part (c)(iii): Gradient uncertainty
- [ ] Best fit line drawn
- [ ] Large triangle used for best gradient
- [ ] Worst acceptable line drawn through all error bars
- [ ] Large triangle used for worst gradient
- [ ] $\Delta$gradient = |best - worst| calculated
- [ ] Final answer in form gradient $\pm$ uncertainty

### Part (c)(iv): y-intercept uncertainty
- [ ] Best fit y-intercept read
- [ ] Worst fit y-intercept read
- [ ] $\Delta$intercept = |best - worst| calculated

### Part (d)(ii): Combined uncertainty
- [ ] Fractional uncertainty formula correct
- [ ] Each contributing term included
- [ ] Final answer: value $\pm$ uncertainty with units
- [ ] uncertainty to 1 s.f., value aligned

:::tip

表格中 uncertainty 保留 1 位有效数字，derived quantity 的小数位数与之对齐。

:::
