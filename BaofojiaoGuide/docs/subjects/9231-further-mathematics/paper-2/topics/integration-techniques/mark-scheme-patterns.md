# Integration Techniques — Mark Scheme Patterns

## Mark Allocation Overview

| Question Type | Total Marks | M marks | A marks | B marks |
|---------------|-------------|---------|---------|---------|
| Reduction formula derivation | 5–6 | 3 | 2–3 | 0 |
| Reduction formula evaluation | 2–3 | 1 | 1–2 | 0 |
| Reduction formula (combined) | 7–11 | 4 | 3–7 | 0 |
| Integration by parts | 3–4 | 1 | 1–2 | 1 |
| Integration by substitution | 3–4 | 1 | 1–2 | 1 |
| Rational function integration | 5 | 2 | 3 | 0 |

## Pattern: Reduction Formula Derivation (5–6 marks)

- **M1**: Split integrand (e.g. $(1-x^2)^{n/2} = (1-x^2)(1-x^2)^{(n-2)/2}$)
- **M1**: Express $I_n$ as sum of $I_{n-2}$ and another integral
- **M1**: Integration by parts with correct $u$, $dv$ selection
- **A1**: Correct working for the additional integral
- **A1**: Correct recurrence relation

:::warning[典型扣分]
- $u$、$dv$ 选反 → 无法得到递推关系 → 扣 **M1**
- 忘记处理积分上下限 → 扣 **A1**
:::

## Pattern: Reduction Formula Evaluation (2–3 marks)

- **M1**: Find boundary value $I_0$ or $I_1$
- **A1**: Correct iterative application (at least 2 steps shown)
- **A1**: Correct final value of $I_n$

:::info[常见边界值]
$$I_0 = \int_a^b 1\,dx = b-a$$

$$I_1 = \int_a^b f(x)\,dx \text{ (直接计算)}$$

$$\int_0^{\pi/2} \sin^0 x\,dx = \frac{\pi}{2}$$

$$\int_0^{\pi/2} \sin^1 x\,dx = 1$$
:::

## Pattern: Integration by Parts (3–4 marks)

- **M1**: Correct choice of $u$ and $dv$
- **A1**: Correct $uv - \int v\,du$ setup
- **A1**: Correct final answer
- *B1*: Correct integration of $dv$ (sometimes given separately)

## Pattern: Integration of Rational Functions (5 marks)

- **M1**: Set up partial fraction form
- **A1**: Correct coefficients
- **M1**: Split into separate integrals
- **A1**: Correct $\ln$ terms
- **A1**: Correct $\tan^{-1}$ or other terms

### 评分细节

| 步骤 | 标记 | 说明 |
|------|------|------|
| 设 $\frac{A}{x-1}+\frac{Bx+C}{x^2+1}$ | **M1** | 形式正确 |
| 解出 $A=2,B=1,C=0$ | **A1** | 系数正确 |
| 分成三项积分 | **M1** | 拆分方法正确 |
| $3\ln\|x-1\|$ | **A1** | $\ln$ 项正确 |
| $2\tan^{-1}x$ | **A1** | $\tan^{-1}$ 项正确 |

## Follow-Through Rules

- 递推公式推导中，若 $I_n$ 表达式写对但后续计算有算术错误，可 **ft**
- 边界值 $I_0$ 或 $I_1$ 计算错，后续递推可 **ft**
- 分部积分中 $u$ 和 $dv$ 选反但计算正确，最多扣 **M1**
