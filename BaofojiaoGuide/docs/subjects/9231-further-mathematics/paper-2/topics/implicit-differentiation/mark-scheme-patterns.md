# Implicit Differentiation — Mark Scheme Patterns

## Mark Allocation Overview

| Question Type | Total Marks | M marks | A marks | B marks |
|---------------|-------------|---------|---------|---------|
| Find $\frac{dy}{dx}$ | 3 | 1 | 2 | 0 |
| Find $\frac{d^2y}{dx^2}$ | 5 | 2 | 3 | 0 |
| Values at a point (combined) | 8 | 3 | 5 | 0 |

## Pattern: First Derivative $\frac{dy}{dx}$ (3 marks)

- **M1**: Differentiate implicitly — must show evidence of chain rule on $y$ terms $\left(\frac{d}{dx}f(y) = f'(y)\frac{dy}{dx}\right)$ and product rule on $xy$ terms
- **A1**: Correct differentiated equation (all terms correct)
- **A1**: Correct expression for $\frac{dy}{dx}$ (fully simplified)

:::warning[扣分点]
- 对 $y^2$ 求导只得到 $2y$ 而非 $2y\frac{dy}{dx}$ → 扣 **M1**
- 乘积法则 $xy$ 只得到 $y$ 而非 $y + x\frac{dy}{dx}$ → 扣 **M1**
:::

## Pattern: Second Derivative $\frac{d^2y}{dx^2}$ (5 marks)

- **M1**: Attempt quotient rule on $\frac{dy}{dx}$ expression
- **M1**: Correctly differentiate $y$ terms in numerator/denominator (with $\frac{dy}{dx}$)
- **A1**: Correct unsimplified expression for $\frac{d^2y}{dx^2}$
- **A1**: Substitute expression for $\frac{dy}{dx}$ correctly
- **A1**: Correct simplified $\frac{d^2y}{dx^2}$ in terms of $x$ and $y$ only

:::info[简化技巧]
终态表达式应**不含** $\frac{dy}{dx}$，仅含 $x$ 和 $y$。可利用原方程进一步化简。
:::

## Pattern: Values at Specific Points (8 marks total)

**Part (a) — Find $\frac{dy}{dx}$** (3 marks):
- **M1**: Implicit differentiation
- **A1**: Correct derivative
- **A1**: Expression for $\frac{dy}{dx}$

**Part (b) — Tangent/Normal** (2 marks):
- **M1**: Substitute coordinates into $\frac{dy}{dx}$
- **A1**: Correct equation of tangent or normal

**Part (c) — Second derivative at point** (3 marks):
- **M1**: Differentiate $\frac{dy}{dx}$ again
- **M1**: Substitute coordinates and $\frac{dy}{dx}$ value
- **A1**: Correct numerical answer

:::tip[关键技巧]
求 $\frac{d^2y}{dx^2}$ 在特定点的值时，可在代入数值后再求导，而非先化简一般表达式再代入。有时代入后计算更简单（因为 $\frac{dy}{dx}=0$ 时大量项消失）。
:::

## Common MS Coding

| Code | Meaning |
|------|---------|
| **M1** | Method — implicit differentiation shown |
| **A1** | Accuracy — correct derivative expression |
| **A1** | Accuracy — correct simplified form |
| **ft** | Follow-through — accept error from part (a) |
| **AG** | Answer given — show full working |
