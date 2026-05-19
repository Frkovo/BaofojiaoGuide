---
title: 考前速通
sidebar_position: 7
---

# 考前速通

## Key Relations: Gradient/Intercept to Constants

| Linearized form | Gradient | y-intercept |
|----------------|----------|-------------|
| $y = mx + c$ | $m$ | $c$ |
| $\ln y = bx + \ln a$ | $b$ | $\ln a \Rightarrow a = e^{\,c}$ |
| $\lg y = n \lg x + \lg a$ | $n$ | $\lg a \Rightarrow a = 10^{\,c}$ |
| $y = a(1/x) + b$ | $a$ | $b$ |
| $1/f = \frac{4}{v}L + \frac{4c}{v}$ | $4/v \Rightarrow v = 4/m$ | $4c/v \Rightarrow c = cv/4$ |

## Constant from Gradient Workflow

```
read gradient m from graph
find formula: m = expression
rearrange: constant = f(m)
substitute numbers
add units
```

## Constant from y-intercept Workflow

```
read intercept c from graph
find formula: c = expression
if ln/c -> constant = e^(c)
if lg/c -> constant = 10^(c)
otherwise constant = c
add units
```

## Conclusion Template

> "The theoretical value of $X = \_\_\_$ lies **within / outside** the experimental range $(X_{\text{exp}} \pm \Delta X) = (\_\_\_ \text{ to } \_\_\_)$. Therefore the results **support / do not support** the suggested relationship within experimental uncertainty."

## Red Flags

| 信号 | 可能的问题 |
|------|-----------|
| y-intercept from $\ln$ graph | 必须取 $e^{\text{intercept}}$ |
| y-intercept from $\lg$ graph | 必须取 $10^{\text{intercept}}$ |
| gradient 为负 | 检查常数是否应为正 |
| 题目给了已知常数 | 必须代入（如 $k = 1.38 \times 10^{-23}$） |
| 答案没有单位 | 必扣分 |
| 理论值比较 | 必须提及 uncertainty range |
| 扩展计算 | 用精确值，不要用四舍五入值 |

## Quick Checklist

### Part (d)(i): Calculate constant from gradient
- [ ] Correct expression linking gradient to constant
- [ ] Numerical substitution correct
- [ ] Units derived and stated

### Part (d)(ii): Uncertainty in constant
- [ ] Error propagation formula correct
- [ ] All contributing terms included
- [ ] Answer: value $\pm$ uncertainty with units

### Part (e): Extension calculation
- [ ] Correct formula used
- [ ] Previously calculated constant used correctly
- [ ] Final answer with unit

### Part (f): Conclusion
- [ ] Experimental range stated (value $\pm$ uncertainty)
- [ ] Theoretical/expected value stated
- [ ] Compared correctly
- [ ] Clear "supports" or "does not support" with reasoning

:::tip

从 y-intercept 求常数时，务必判断是否需要取指数！$\ln a \rightarrow a = e^{\text{intercept}}$，$\lg a \rightarrow a = 10^{\text{intercept}}$。

:::
