---
title: 解题方法
sidebar_position: 4
---

# 解题方法 — Non-parametric Tests

## 方法一：Wilcoxon Signed-Rank Test（单样本）

### 标准解题模板

```
H₀: median = ___
H₁: median ___ ___ (___-tailed)
α = ___

Data: [list]
Differences from median: ___
Zero differences excluded: n = ___

Absolute differences (excluding 0): ___
Ranks (smallest = 1): ___
Signed ranks: ___

T⁺ = sum of positive ranks = ___
T⁻ = sum of negative ranks = ___
T = min(T⁺, T⁻) = ___

Critical value (table, n = ___, α = ___, ___ -tail) = ___
Since T ___ cv, we ___ H₀.

Conclusion: At the ___% significance level, there is ___ evidence that the median ___ ___.
```

### 步骤详解

1. 对每个观测值计算差异 $d_i = X_i - m_0$
2. 排除 $d_i = 0$ 的观测值，$n$ = 非零差异个数
3. 取绝对值 $|d_i|$，从小到大排序
4. 赋予秩：最小 $|d_i|$ 得秩 1，次小得秩 2，依此类推
5. 若绝对值相等（ties），取平均秩
6. 将原始符号（正/负）赋回各秩
7. $T^+ = \sum$ 正秩，$T^- = \sum$ 负秩，$T = \min(T^+, T^-)$
8. 查 Wilcoxon signed-rank 临界值表
9. 若 $T \leq$ 临界值，拒绝 $H_0$

## 方法二：Wilcoxon Matched-Pairs Signed-Rank Test

### 标准解题模板

```
H₀: median difference = 0
H₁: median difference ___ 0 (___-tailed)
α = ___

Pairs: [list of before/after]
Differences (after - before): ___
Zero differences excluded: n = ___

Absolute differences: ___
Ranks: ___
Signed ranks: ___

T⁺ = sum of positive ranks = ___
T⁻ = sum of negative ranks = ___
T = min(T⁺, T⁻) = ___

Critical value (table, n = ___, α = ___, ___ -tail) = ___
Since T ___ cv, we ___ H₀.
```

### 步骤详解

与单样本完全相同，只是差异定义为配对差（如 after $-$ before）

## 方法三：Wilcoxon Rank-Sum Test（两独立样本）

### 标准解题模板

```
H₀: The two populations are identical / have the same distribution
H₁: The two populations differ (___-tailed)
α = ___

Sample 1 (n₁ = ___): [list]
Sample 2 (n₂ = ___): [list]

Combine and rank all N = n₁ + n₂ observations:
[show ranked table]

R₁ = sum of ranks for Sample 1 = ___
(or R₂ = sum of ranks for Sample 2 = ___)

Test statistic W = R₁ = ___

Critical value (table, n₁ = ___, n₂ = ___, α = ___, ___ -tail):
Lower cv = ___, Upper cv = ___

Since W is [between / outside] the critical region, we ___ H₀.
```

### 步骤详解

1. 合并两个样本，所有数据从小到大排序
2. 赋予秩：最小值得秩 1，次小得秩 2，依此类推
3. 相同值取平均秩
4. 计算第一个样本的秩和 $R_1$（或两个样本的秩和，用较小的那个）
5. 检验统计量 $W = R_1$
6. 查 Wilcoxon rank-sum 临界值表（或 Mann-Whitney 表）
7. 若 $W \leq$ 下临界值 或 $W \geq$ 上临界值，拒绝 $H_0$

## 方法四：Sign Test

### 标准解题模板

```
H₀: median = ___
H₁: median ___ ___ (___-tailed)
α = ___

Signs (data - median):
+ : ___ (X > m₀)
- : ___ (X < m₀)
0 : ___ (X = m₀, excluded)

n = number of non-zero signs = ___
S = number of ___ signs = ___

Under H₀, S ~ B(n, 0.5)

P(S ___ ___) = ___ [calculate using binomial]
Since p-value ___ α, we ___ H₀.
```

### 步骤详解

1. 计算每个数据与中位数的差
2. 记录符号（+、-、0）
3. 排除 0，记 $n$ = 非零符号数
4. $S$ = 较少出现的符号数
5. 计算 $P(S \leq s)$ 或 $2P(S \leq s)$（双尾）
6. 用 $B(n, 0.5)$ 计算 p-value
7. 若 p-value $&lt;$ $\alpha$，拒绝 $H_0$

## 方法五：正态近似

### Signed-Rank 正态近似

当 $n &gt; 20$ 时使用：

$$\mu_T = \frac{n(n+1)}{4}$$
$$\sigma_T = \sqrt{\frac{n(n+1)(2n+1)}{24}}$$
$$z = \frac{T + 0.5 - \mu_T}{\sigma_T} \quad \text{或} \quad z = \frac{T - 0.5 - \mu_T}{\sigma_T}$$

符号取决于检验方向。对比标准正态临界值。

### Rank-Sum 正态近似

当 $n_1, n_2 &gt; 10$ 时使用：

$$\mu_W = \frac{n_1(n_1 + n_2 + 1)}{2}$$
$$\sigma_W = \sqrt{\frac{n_1 n_2 (n_1 + n_2 + 1)}{12}}$$
$$z = \frac{W \pm 0.5 - \mu_W}{\sigma_W}$$

:::note[连续性校正方向]

- 下尾检验：$z = \dfrac{W + 0.5 - \mu}{\sigma}$
- 上尾检验：$z = \dfrac{W - 0.5 - \mu}{\sigma}$
- 双尾检验：用 $W$ 与 $\mu$ 比较，较小一侧用相应校正

:::
