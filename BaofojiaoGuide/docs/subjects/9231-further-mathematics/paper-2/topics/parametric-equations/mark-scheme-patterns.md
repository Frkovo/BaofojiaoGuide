# Parametric Equations — Mark Scheme Patterns

## Mark Allocation Overview

| Question Type | Total Marks | M marks | A marks | B marks |
|---------------|-------------|---------|---------|---------|
| First derivative $\frac{dy}{dx}$ | 2–3 | 1 | 1–2 | 0 |
| Second derivative $\frac{d^2y}{dx^2}$ | 3 | 1–2 | 1–2 | 0 |
| Parametric differentiation combined | 5 | 2 | 3 | 0 |
| Arc length | 5–6 | 2–3 | 3 | 0 |

## Pattern: First Derivative (2–3 marks)

- **M1**: Find $\frac{dx}{dt}$ and $\frac{dy}{dt}$ correctly
- **A1**: Correct $\frac{dy}{dx}$ expression (may be unsimplified)
- *A1*: Correct simplified form (if required)

:::warning[常见扣分]
若 $\frac{dy}{dx}$ 未简化到最简形式，可能丢 **A1**。如 $\frac{t^2}{2t}$ 应简化为 $\frac{t}{2}$。
:::

## Pattern: Second Derivative (3 marks, often part of a larger question)

- **M1**: Differentiate $\frac{dy}{dx}$ with respect to $t$
- **A1**: Correct $\frac{d}{dt}\left(\frac{dy}{dx}\right)$
- **A1**: Correct $\frac{d^2y}{dx^2}$ (divide by $\frac{dx}{dt}$)

:::info[评分标志]
**M1** 仅给到"对 $t$ 求导"这一步。如果直接用 $\frac{\ddot{y}}{\ddot{x}}$ 则不得分——必须展示除以 $\frac{dx}{dt}$ 的步骤。
:::

## Pattern: Arc Length (5–6 marks)

- **M1**: Find $\frac{dx}{dt}$ and $\frac{dy}{dt}$
- **M1**: Form $\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2$
- **A1**: Simplify integrand (e.g. $8(1-\cos t)$ or $16\sin^2(t/2)$)
- **M1**: Set up arc length integral $L = \int \sqrt{(\dot{x}^2 + \dot{y}^2)}\,dt$
- **A1**: Correct square root simplification
- **A1**: Correct final answer

### 评分关键点
| 步骤 | 得分点 | 常见错误 |
|------|--------|---------|
| $\frac{dx}{dt}$, $\frac{dy}{dt}$ | **M1** | 导数计算错误 |
| 平方和 | **M1** | 漏项或展开错误 |
| 化简 | **A1** | 未用半角公式 |
| 积分设置 | **M1** | 积分变量写错 |
| 开方 | **A1** | 忽略绝对值 |
| 最终答案 | **A1** | 数值或代数错误 |

## Follow-Through Rules

- 如果 $\frac{dx}{dt}$ 或 $\frac{dy}{dt}$ 错一个，后续的 $\frac{dy}{dx}$ 可 **ft**
- 弧长问题中，平方和化简错则后续不得分
- $\frac{d^2y}{dx^2}$ 中，$\frac{dy}{dx}$ 的错可 **ft**，但方法必须正确
