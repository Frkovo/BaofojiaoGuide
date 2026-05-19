# Maclaurin Series — Mark Scheme Patterns

## Mark Allocation Overview

| Question Type | Total Marks | M marks | A marks | B marks |
|---------------|-------------|---------|---------|---------|
| First principles (3 terms) | 5 | 1 | 4 | 0 |
| First principles (4 terms) | 6–7 | 1–2 | 4–5 | 0 |
| Substitution / composite | 4–5 | 1 | 2–3 | 1 |
| Integral approximation | 2 | 1 | 1 | 0 |

## Pattern: First Principles (5–7 marks)

- **M1**: Attempt to differentiate (at least 2 derivatives, correct method)
- **A1**: $f(0)$ correct
- **A1**: $f'(0)$ correct
- **A1**: $f''(0)$ correct and $\frac{f''(0)}{2!}x^2$ term
- **A1**: $f'''(0)$ correct and $\frac{f'''(0)}{3!}x^3$ term
- *Optional A1*: $f^{(4)}(0)$ correct

:::warning[关键]
如果导数计算正确但忘记除以阶乘（如 $f''(0)x^2$ 而非 $f''(0)x^2/2!$），通常扣 1 分。
:::

## Pattern: Substitution into Standard Series (4–5 marks)

- **B1**: Correctly states standard series (e.g. $e^u = 1+u+u^2/2!+\cdots$)
- **M1**: Substitutes $u = g(x)$ into standard series
- **A1**: Correct first non-zero term
- **A1**: Correct second non-zero term
- *A1*: Correct third term (if required)

## Pattern: Composite Functions (4–5 marks)

- **M1**: Recognise need for $\ln(1+u)$ expansion or equivalent
- **A1**: Correct inner expansion (e.g. $\cosh x$ or $e^x$)
- **A1**: Correct first term
- **A1**: Correct second term

:::info[评分规律]
对于 $\ln(\cosh x)$ 类型：
- 展开 $\cosh x$ 获 **B1**
- 代入 $\ln(1+u)$ 获 **M1**
- 每正确一项得 **A1**
:::

## Pattern: Integral Approximation (2 marks)

- **M1**: Integrates series term-by-term (at least 2 terms)
- **A1**: Correct numerical answer (usually given to 3 or 4 s.f.)

:::note[注意]
积分近似通常为压轴小题，只需 2 分。不必展开太多项，只需足够得到精度要求。
:::

## Common MS Coding

| Code | Meaning |
|------|---------|
| **M1** | Method mark — correct differentiation or substitution |
| **A1** | Accuracy mark — correct term/coefficient |
| **B1** | Independent mark — stating standard series |
| **ft** | Follow-through — accept error from earlier step |
| **AG** | Answer given — must show full working |
