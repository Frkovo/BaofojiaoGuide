# Riemann Sums — Mark Scheme Patterns

## Mark Allocation Overview

| Question Type | Total Marks | M marks | A marks | B marks |
|---------------|-------------|---------|---------|---------|
| Upper bound (rectangles) | 4 | 2 | 2 | 0 |
| Lower bound (rectangles) | 4 | 2 | 2 | 0 |
| Both bounds (combined) | 8 | 4 | 4 | 0 |
| Stirling approximation | 8 | 4 | 4 | 0 |

## Pattern: Upper/Lower Bound Using Rectangles (4 marks each)

- **M1**: $\Delta x = \frac{b-a}{n}$ and correct endpoint identification
- **M1**: Form sum $\sum f(x_i)\Delta x$ with correct $x_i$
- **A1**: Correct sigma expression (unsimplified)
- **A1**: Correct simplified expression in terms of $n$

### 评分细节

| 步骤 | 标记 | 示例 |
|------|------|------|
| $\Delta x = \frac{1}{n}$ + 判断递增/递减 | **M1** | $\Delta x = \frac{1}{n}$, 递增用右端点 |
| $\sum_{i=1}^n f(x_i)\Delta x$ | **M1** | $\sum_{i=1}^n \left(\frac{i}{n}\right)^2 \cdot \frac{1}{n}$ |
| $\frac{1}{n^3}\sum i^2 = \frac{1}{n^3}\cdot\frac{n(n+1)(2n+1)}{6}$ | **A1** | 代入求和公式 |
| $\frac{(n+1)(2n+1)}{6n^2}$ | **A1** | 化简完成 |

## Pattern: Stirling Approximation (8 marks)

- **M1**: Express $\ln N! = \sum_{r=1}^N \ln r$
- **M1**: Set $f(x) = \ln x$, identify increasing function
- **M1**: Left endpoint inequality (lower bound for increasing function)
- **M1**: Right endpoint inequality (upper bound for increasing function)
- **A1**: Evaluate $\int_1^N \ln x\,dx = N\ln N - N + 1$
- **A1**: Correct lower bound inequality (may be for $\ln(N-1)!$)
- **A1**: Correct upper bound inequality
- **A1**: Final inequality for $\ln N!$

### 不等式的方向

对递增函数 $f(x) = \ln x$：

$$\text{左端点：} \sum_{r=1}^{N-1} \ln r \le \int_1^N \ln x\,dx \le \sum_{r=2}^N \ln r$$

$$\text{即 } \ln(N-1)! \le N\ln N - N + 1 \le \ln N!$$

:::warning[关键扣分点]
- 将左右端点弄反 → 扣 **M1**
- 求和下标范围错误（如从 $r=1$ 到 $N$ 而非 $N-1$）→ 扣 **A1**
- 最终不等式方向错误 → 扣 **A1**
:::

## Follow-Through Rules

- 如果求和公式用错（如 $\sum r^2$ 公式写错），后续使用可 **ft**
- 上下界判断错误但计算正确，最多扣 **M1**
- Stirling 近似中，积分计算错可 **ft** 后续不等式
