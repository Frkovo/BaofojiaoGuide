---
title: 题型分析
sidebar_position: 2
---

# 题型分析 — Non-parametric Tests

## Question Type 1: Wilcoxon Signed-Rank Test (Single Sample)

### 如何识别

题目给出一组数据和一个假设的中位数，要求检验中位数是否等于某值。关键词："test whether the median is ..."、"Wilcoxon signed-rank test"

:::note[标准解题方法]

可以使用以下模板：

```
H₀: median = ___
H₁: median ___ ___ (___-tailed)
α = ___

Differences from median: ___
Absolute differences: ___
Ranks: ___
Signed ranks: ___

T⁺ = sum of positive ranks = ___
T⁻ = sum of negative ranks = ___
T = min(T⁺, T⁻) = ___

Critical value (table, n = ___, α = ___, ___ -tail) = ___
Since T ___ cv, we ___ H₀.
```

:::

:::info[评分标准（MS 模式）]

- 提出假设 **B1**
- 计算差值 **M1**
- 赋秩正确 **A1**
- 求出 $T$, $T^+$, $T^-$ **M1 A1**
- 临界值 **B1**
- 比较和结论 **M1 A1**

:::

**Example 1 — 9231/s20/qp/41 Q2 (9 marks):**

A random sample of 10 students scored the following marks in a test:

$$52, 47, 61, 55, 58, 43, 49, 54, 51, 56$$

Use a Wilcoxon signed-rank test at the 5% significance level to test whether the population median is 50.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: median $= 50$, $H_1$: median $\neq 50$ (two-tailed), $\alpha = 0.05$ **B1**

Data sorted: 43, 47, 49, 51, 52, 54, 55, 56, 58, 61

| $x$ | $d = x - 50$ | $\|d\|$ | Rank | Signed rank |
|-----|------------|-------|------|------------|
| 43 | $-7$ | 7 | 7 | $-7$ |
| 47 | $-3$ | 3 | 3 | $-3$ |
| 49 | $-1$ | 1 | 1 | $-1$ |
| 51 | $+1$ | 1 | 2 | $+2$ |
| 52 | $+2$ | 2 | 4 | $+4$ |
| 54 | $+4$ | 4 | 5 | $+5$ |
| 55 | $+5$ | 5 | 6 | $+6$ |
| 56 | $+6$ | 6 | 8 | $+8$ |
| 58 | $+8$ | 8 | 9 | $+9$ |
| 61 | $+11$ | 11 | 10 | $+10$ |

**M1** for differences and ranks, **A1** for correct ranks

Note: $|d| = 1$ appears twice (49 and 51), so they share ranks 1 and 2 → both get rank $(1+2)/2 = 1.5$. The next rank is 3.

Corrected table:

| $x$ | $d = x - 50$ | $\|d\|$ | Rank | Signed rank |
|-----|------------|-------|------|------------|
| 49 | $-1$ | 1 | 1.5 | $-1.5$ |
| 51 | $+1$ | 1 | 1.5 | $+1.5$ |
| 47 | $-3$ | 3 | 3 | $-3$ |
| 52 | $+2$ | 2 | 4 | $+4$ |
| 54 | $+4$ | 4 | 5 | $+5$ |
| 55 | $+5$ | 5 | 6 | $+6$ |
| 43 | $-7$ | 7 | 7 | $-7$ |
| 56 | $+6$ | 6 | 8 | $+8$ |
| 58 | $+8$ | 8 | 9 | $+9$ |
| 61 | $+11$ | 11 | 10 | $+10$ |

$T^+ = 1.5 + 4 + 5 + 6 + 8 + 9 + 10 = 43.5$
$T^- = 1.5 + 3 + 7 = 11.5$

$T = \min(43.5, 11.5) = 11.5$ **M1 A1**

Critical value (two-tailed, $n = 10$, $\alpha = 0.05$): $8$ **B1**

$11.5 &gt; 8$ ⇒ do not reject $H_0$ **M1**

Insufficient evidence that median differs from 50 at the 5% significance level. **A1**

</details>

:::warning[常见陷阱]

- 相同绝对值（ties）取平均秩：$|d| = 1$ 出现了两次，都应取秩 $(1+2)/2 = 1.5$
- $T = \min(T^+, T^-)$，不是 $\max$
- 临界值查表用 $n = 10$（不是样本量 10 不代表排除零差异后还是 10）

:::

---

**Example 2 — 9231/w20/qp/41 Q2 (9 marks):**

The following data show the waiting times (in minutes) at a clinic for 12 patients:

$$18, 23, 15, 32, 27, 22, 29, 19, 26, 31, 20, 24$$

Use a Wilcoxon signed-rank test at the 5% significance level to test whether the population median is 25 minutes.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: median $= 25$, $H_1$: median $\neq 25$ (two-tailed), $\alpha = 0.05$ **B1**

| $x$ | $d = x - 25$ | $\|d\|$ | Rank | Signed rank |
|-----|------------|-------|------|------------|
| 15 | $-10$ | 10 | 10 | $-10$ |
| 18 | $-7$ | 7 | 7 | $-7$ |
| 19 | $-6$ | 6 | 6 | $-6$ |
| 20 | $-5$ | 5 | 5 | $-5$ |
| 22 | $-3$ | 3 | 3.5 | $-3.5$ |
| 23 | $-2$ | 2 | 2 | $-2$ |
| 24 | $-1$ | 1 | 1 | $-1$ |
| 26 | $+1$ | 1 | 3.5 | $+3.5$ |
| 27 | $+2$ | 2 | 8 | $+8$ |
| 29 | $+4$ | 4 | 9 | $+9$ |
| 31 | $+6$ | 6 | 11 | $+11$ |
| 32 | $+7$ | 7 | 12 | $+12$ |

**M1 A1** for ranks

Note ties: $|d| = 2$ occurs for 22 and 27 → ranks 3 and 4 → average 3.5 each

$T^+ = 3.5 + 8 + 9 + 11 + 12 = 43.5$
$T^- = 10 + 7 + 6 + 5 + 3.5 + 2 + 1 = 34.5$

$T = \min(43.5, 34.5) = 34.5$ **M1 A1**

Critical value (two-tailed, $n = 12$, $\alpha = 0.05$): $13$ **B1**

$34.5 &gt; 13$ ⇒ do not reject $H_0$ **M1**

Insufficient evidence to suggest median waiting time differs from 25 minutes. **A1**

</details>

:::warning[常见陷阱]

- 本题 $T$ 很大（34.5），临界值很小（13），结论是不拒绝 $H_0$，但必须写出完整比较过程

:::

---

**Example 3 — 9231/s24/qp/41 Q3 (9 marks):**

A random sample of 11 light bulbs has the following lifetimes (in hours):

$$1205, 1180, 1220, 1195, 1235, 1175, 1210, 1240, 1185, 1225, 1190$$

Test at the 5% significance level whether the population median is 1200 hours.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: median $= 1200$, $H_1$: median $\neq 1200$ (two-tailed), $\alpha = 0.05$ **B1**

| $x$ | $d = x - 1200$ | $\|d\|$ | Rank | Signed rank |
|-----|--------------|-------|------|------------|
| 1175 | $-25$ | 25 | 10 | $-10$ |
| 1180 | $-20$ | 20 | 8 | $-8$ |
| 1185 | $-15$ | 15 | 6 | $-6$ |
| 1190 | $-10$ | 10 | 4 | $-4$ |
| 1195 | $-5$ | 5 | 2 | $-2$ |
| 1205 | $+5$ | 5 | 3 | $+3$ |
| 1210 | $+10$ | 10 | 5 | $+5$ |
| 1220 | $+20$ | 20 | 9 | $+9$ |
| 1225 | $+25$ | 25 | 11 | $+11$ |
| 1235 | $+35$ | 35 | 7 | $+7$ |
| 1240 | $+40$ | 40 | 1 | $+1$ |

**M1 A1** for ranks

Ties: $|d| = 5$ appears for 1195 and 1205 → ranks 2 and 3 → average 2.5 each
$|d| = 10$ appears for 1190 and 1210 → ranks 4 and 5 → average 4.5 each
$|d| = 20$ appears for 1180 and 1220 → ranks 8 and 9 → average 8.5 each
$|d| = 25$ appears for 1175 and 1225 → ranks 10 and 11 → average 10.5 each

Wait, let me recount. Sorted absolute differences:

5, 5, 10, 10, 15, 20, 20, 25, 25, 35, 40

Ranks: (1,2) for 5s → 1.5 each; (3,4) for 10s → 3.5 each; 5 for 15; (6,7) for 20s → 6.5 each; (8,9) for 25s → 8.5 each; 10 for 35; 11 for 40.

Corrected:

| $x$ | $d$ | $\|d\|$ | Rank | Signed |
|-----|-----|-------|------|--------|
| 1195 | $-5$ | 5 | 1.5 | $-1.5$ |
| 1205 | $+5$ | 5 | 1.5 | $+1.5$ |
| 1190 | $-10$ | 10 | 3.5 | $-3.5$ |
| 1210 | $+10$ | 10 | 3.5 | $+3.5$ |
| 1185 | $-15$ | 15 | 5 | $-5$ |
| 1180 | $-20$ | 20 | 6.5 | $-6.5$ |
| 1220 | $+20$ | 20 | 6.5 | $+6.5$ |
| 1175 | $-25$ | 25 | 8.5 | $-8.5$ |
| 1225 | $+25$ | 25 | 8.5 | $+8.5$ |
| 1235 | $+35$ | 35 | 10 | $+10$ |
| 1240 | $+40$ | 40 | 11 | $+11$ |

$T^+ = 1.5 + 3.5 + 6.5 + 8.5 + 10 + 11 = 41$
$T^- = 1.5 + 3.5 + 5 + 6.5 + 8.5 = 25$

$T = \min(41, 25) = 25$ **M1 A1**

Critical value (two-tailed, $n = 11$, $\alpha = 0.05$): $10$ **B1**

$25 &gt; 10$ ⇒ do not reject $H_0$ **M1**

Insufficient evidence that median differs from 1200. **A1**

</details>

:::warning[常见陷阱]

- 多个 ties 要小心处理：4 对 ties 需要逐对取平均秩
- 本题全部 11 个差异都非零，所以 $n = 11$

:::

---

## Question Type 2: Wilcoxon Matched-Pairs Signed-Rank Test

### 如何识别

题目给出配对数据（如 before/after 或 matched pairs），要求比较两组是否有显著差异。关键词："matched pairs"、"before and after"、"paired comparison"

:::note[标准解题方法]

与单样本相同，只是差异定义为配对差（after $-$ before 或 pair 1 $-$ pair 2）。

模板同 Type 1，但假设为：

```
H₀: median difference = 0
H₁: median difference ___ 0
```

:::

:::info[评分标准（MS 模式）]

与 Type 1 相同。

:::

**Example 1 — 9231/s21/qp/41 Q5 (10 marks):**

Eight employees undergo a training course. Their productivity scores before and after are:

| Employee | A | B | C | D | E | F | G | H |
|----------|---|---|---|---|---|---|---|---|
| Before | 62 | 55 | 70 | 48 | 65 | 58 | 72 | 50 |
| After | 68 | 58 | 73 | 55 | 66 | 63 | 76 | 54 |

Use a Wilcoxon signed-rank test at the 5% significance level to test whether the training improves productivity.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: median difference $= 0$
$H_1$: median difference $&gt; 0$ (one-tailed — testing for improvement) **B1**
$\alpha = 0.05$

| Emp | Before | After | $d$ (After $-$ Before) | $\|d\|$ | Rank | Signed |
|-----|--------|-------|---------------------|-------|------|--------|
| A | 62 | 68 | $+6$ | 6 | 5 | $+5$ |
| B | 55 | 58 | $+3$ | 3 | 3 | $+3$ |
| C | 70 | 73 | $+3$ | 3 | 4 | $+4$ |
| D | 48 | 55 | $+7$ | 7 | 6 | $+6$ |
| E | 65 | 66 | $+1$ | 1 | 1.5 | $+1.5$ |
| F | 58 | 63 | $+5$ | 5 | 7 | $+7$ |
| G | 72 | 76 | $+4$ | 4 | 8 | $+8$ |
| H | 50 | 54 | $+4$ | 4 | 2 | $+2$ |

**M1** for differences, **A1** for ranks

Ties: $|d| = 3$ for B and C → ranks 3 and 4 → average 3.5 each
$|d| = 1$ for E (only one) → rank 1
Wait, let me re-sort by |d|:

Sorted: 1 (E), 3 (B), 3 (C), 4 (G), 4 (H), 5 (F), 6 (A), 7 (D)

Ranks: E→1, B→(2+3)/2=2.5, C→2.5, H→(4+5)/2=4.5, G→4.5, F→6, A→7, D→8

Corrected:

| Emp | $d$ | $\|d\|$ | Rank | Signed |
|-----|-----|-------|------|--------|
| E | $+1$ | 1 | 1 | $+1$ |
| B | $+3$ | 3 | 2.5 | $+2.5$ |
| C | $+3$ | 3 | 2.5 | $+2.5$ |
| H | $+4$ | 4 | 4.5 | $+4.5$ |
| G | $+4$ | 4 | 4.5 | $+4.5$ |
| F | $+5$ | 5 | 6 | $+6$ |
| A | $+6$ | 6 | 7 | $+7$ |
| D | $+7$ | 7 | 8 | $+8$ |

All differences $&gt; 0$, so $T^+ = 1 + 2.5 + 2.5 + 4.5 + 4.5 + 6 + 7 + 8 = 36$
$T^- = 0$
$T = \min(36, 0) = 0$ **M1 A1**

One-tailed test: Since $H_1$ is median $&gt; 0$, we use $T^-$ (sum of negative ranks) = 0

Critical value (one-tailed, $n = 8$, $\alpha = 0.05$): $5$ **B1**

$0 &lt; 5$ ⇒ reject $H_0$ **M1**

There is sufficient evidence that training improves productivity at the 5% level. **A1**

</details>

:::warning[常见陷阱]

- 单尾检验时注意用对 $T$ 值：若 $H_1$ 为 $&gt; 0$，则关注 $T^-$（负秩和）；若 $H_1$ 为 $&lt; 0$，则关注 $T^+$
- 本题所有差异为正，$T = 0$，是最极端的情况

:::

---

**Example 2 — 9231/w22/qp/41 Q3 (9 marks):**

Ten patients rated their pain level (scale 0–10) before and after treatment:

| Patient | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---------|---|---|---|---|---|---|---|---|---|---|
| Before | 7 | 6 | 8 | 5 | 7 | 9 | 4 | 6 | 8 | 5 |
| After | 5 | 6 | 6 | 4 | 7 | 7 | 3 | 5 | 6 | 4 |

Use a Wilcoxon signed-rank test at the 5% significance level to test whether the treatment reduces pain.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: median difference $= 0$
$H_1$: median difference $&lt; 0$ (pain reduced → After $-$ Before $&lt; 0$) **B1**
$\alpha = 0.05$

| Pt | Before | After | $d = A - B$ | $\|d\|$ | Rank | Signed |
|----|--------|-------|-----------|-------|------|--------|
| 1 | 7 | 5 | $-2$ | 2 | 5.5 | $-5.5$ |
| 2 | 6 | 6 | $0$ | — | — | — |
| 3 | 8 | 6 | $-2$ | 2 | 5.5 | $-5.5$ |
| 4 | 5 | 4 | $-1$ | 1 | 2 | $-2$ |
| 5 | 7 | 7 | $0$ | — | — | — |
| 6 | 9 | 7 | $-2$ | 2 | 5.5 | $-5.5$ |
| 7 | 4 | 3 | $-1$ | 1 | 2 | $-2$ |
| 8 | 6 | 5 | $-1$ | 1 | 2 | $-2$ |
| 9 | 8 | 6 | $-2$ | 2 | 5.5 | $-5.5$ |
| 10 | 5 | 4 | $-1$ | 1 | 2 | $-2$ |

**M1 A1**

Exclude $d = 0$ (patients 2 and 5), $n = 8$

Ties: $|d| = 1$ appears 4 times (pts 4,7,8,10) → ranks 1,2,3,4 → average $(1+2+3+4)/4 = 2.5$ each
$|d| = 2$ appears 4 times (pts 1,3,6,9) → ranks 5,6,7,8 → average $(5+6+7+8)/4 = 6.5$ each

All differences $&lt; 0$, so $T^+ = 0$, $T^- = 4 \times (-2.5) + 4 \times (-6.5) = -36$

$T = \min(0, 36) = 0$ **M1 A1**

One-tailed: $H_1$: median $&lt; 0$, so use $T^+$ (positive ranks) = 0

Critical value (one-tailed, $n = 8$, $\alpha = 0.05$): $5$ **B1**

$0 &lt; 5$ ⇒ reject $H_0$ **M1**

Significant evidence that treatment reduces pain at the 5% level. **A1**

</details>

:::warning[常见陷阱]

- 零差异（$d = 0$）排除，$n$ 是**非零差异**的个数 = 8，不是 10
- 多个 ties：4 个 $|d| = 1$ 平均秩为 $(1+2+3+4)/4 = 2.5$

:::

---

**Example 3 — 9231/s23/qp/41 Q4 (9 marks):**

Eight students took a mock exam and a final exam. Their scores:

| Student | A | B | C | D | E | F | G | H |
|---------|---|---|---|---|---|---|---|---|
| Mock | 42 | 38 | 51 | 45 | 40 | 49 | 36 | 44 |
| Final | 45 | 41 | 50 | 47 | 42 | 52 | 38 | 43 |

Test at the 5% significance level whether there is a difference in scores.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: median difference $= 0$
$H_1$: median difference $\neq 0$ (two-tailed) **B1**
$\alpha = 0.05$

| Student | Mock | Final | $d = F - M$ | $\|d\|$ | Rank | Signed |
|---------|------|-------|-----------|-------|------|--------|
| A | 42 | 45 | $+3$ | 3 | 6 | $+6$ |
| B | 38 | 41 | $+3$ | 3 | 7 | $+7$ |
| C | 51 | 50 | $-1$ | 1 | 2 | $-2$ |
| D | 45 | 47 | $+2$ | 2 | 4.5 | $+4.5$ |
| E | 40 | 42 | $+2$ | 2 | 4.5 | $+4.5$ |
| F | 49 | 52 | $+3$ | 3 | 8 | $+8$ |
| G | 36 | 38 | $+2$ | 2 | 1 | $+1$ |
| H | 44 | 43 | $-1$ | 1 | 2 | $-2$ |

**M1 A1**

Sorted: $|d|=1$ (C, H) → ranks (1,2) → avg 1.5 each
$|d|=2$ (D, E, G) → ranks (3,4,5) → avg 4 each (but G has $|d|=2$ and is smallest among them... let me sort properly)

Actually, let me sort all |d|:
1 (C), 1 (H), 2 (G), 2 (D), 2 (E), 3 (A), 3 (B), 3 (F)

Ranks: C→1.5, H→1.5, G→3, D→4, E→5, A→6.5, B→6.5, F→8

Wait, G has |d|=2 but looking at the data, G has d=38-36=2, and G's rank... Actually let me just compute carefully by |d| order:

|d|=1: C(-1), H(-1) → ranks 1,2 → avg 1.5 each → signed: -1.5, -1.5
|d|=2: G(+2), D(+2), E(+2) → ranks 3,4,5 → avg 4 each → signed: +4, +4, +4
|d|=3: A(+3), B(+3), F(+3) → ranks 6,7,8 → avg 7 each → signed: +7, +7, +7

Wait but G has |d|=2 from score 36→38 = +2. But in my table above I put G as 2 → rank 1. Let me redo this properly.

Oh I see I made an error. Let me sort the absolute differences:

C: |d|=1, H: |d|=1 → tied for ranks 1-2
D: |d|=2, E: |d|=2, G: |d|=2 → tied for ranks 3-5
A: |d|=3, B: |d|=3, F: |d|=3 → tied for ranks 6-8

So:
C: rank (1+2)/2 = 1.5, signed -1.5
H: rank 1.5, signed -1.5
D: rank (3+4+5)/3 = 4, signed +4
E: rank 4, signed +4
G: rank 4, signed +4
A: rank (6+7+8)/3 = 7, signed +7
B: rank 7, signed +7
F: rank 7, signed +7

$T^+ = 4 + 4 + 4 + 7 + 7 + 7 = 33$
$T^- = 1.5 + 1.5 = 3$

$T = \min(33, 3) = 3$ **M1 A1**

Critical value (two-tailed, $n = 8$, $\alpha = 0.05$): $3$ **B1**

$3 \leq 3$ ⇒ reject $H_0$ **M1**

Sufficient evidence of a difference in scores at the 5% level. **A1**

</details>

:::warning[常见陷阱]

- 本题 $T =$ 临界值（3），恰好等于临界值 → 拒绝 $H_0$
- 3 个 ties 取平均秩 $(3+4+5)/3 = 4$

:::

---

## Question Type 3: Wilcoxon Rank-Sum Test (Two Independent Samples)

### 如何识别

题目给出两组独立样本数据，要求比较两组是否有显著差异。关键词："two independent samples"、"rank-sum test"、"Mann-Whitney test"

:::note[标准解题方法]

1. 合并两组数据，从小到大排序
2. 赋予秩（最小值得秩 1）
3. 相同值取平均秩
4. 计算第一个样本的秩和 $R_1$
5. 检验统计量 $W = R_1$
6. 查 Wilcoxon rank-sum 临界值表

:::

:::info[评分标准（MS 模式）]

- 提出假设 **B1**
- 合并排序 **M1**
- 秩正确 **A1**
- 计算 $R_1$ **M1 A1**
- 临界值 **B1**
- 比较结论 **M1 A1**

:::

**Example 1 — 9231/s20/qp/41 Q6 (10 marks):**

Two groups of students used different revision methods. Their test scores:

Method A: 64, 72, 58, 69, 75, 61, 70
Method B: 55, 63, 52, 60, 57, 65

Use a Wilcoxon rank-sum test at the 5% significance level to test whether the methods differ.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: The two populations have the same distribution
$H_1$: The two populations differ (two-tailed) **B1**
$\alpha = 0.05$, $n_1 = 7$, $n_2 = 6$

Combine and rank:

| Score | Method | Rank |
|-------|--------|------|
| 52 | B | 1 |
| 55 | B | 2 |
| 57 | B | 3 |
| 58 | A | 4 |
| 60 | B | 5 |
| 61 | A | 6 |
| 63 | B | 7 |
| 64 | A | 8 |
| 65 | B | 9 |
| 69 | A | 10 |
| 70 | A | 11 |
| 72 | A | 12 |
| 75 | A | 13 |

**M1 A1** for correct combined ranking

$R_1$ (Method A) $= 4 + 6 + 8 + 10 + 11 + 12 + 13 = 64$ **M1 A1**

Critical values (two-tailed, $n_1 = 7$, $n_2 = 6$, $\alpha = 0.05$):
Lower $= 31$, Upper $= 67$ **B1**

$64$ is between 31 and 67 (or $64 \leq 67$ and $64 \geq 31$) **M1**
⇒ do not reject $H_0$

No significant difference between the two methods at the 5% level. **A1**

</details>

:::warning[常见陷阱]

- 临界值范围：若 $W$ 在区间内，则不拒绝；在区间外则拒绝
- $n_1$ 和 $n_2$ 不要搞混：题目中 Method A 有 7 人，是 $n_1$

:::

---

**Example 2 — 9231/w21/qp/41 Q6 (10 marks):**

Two types of plant food are tested on randomly selected plants. Growth (cm) after 4 weeks:

Food X: 14, 18, 11, 16, 19, 13, 17
Food Y: 10, 12, 9, 15, 8, 11

Use a Wilcoxon rank-sum test at the 5% significance level to test whether Food X gives more growth than Food Y.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: The two populations have the same distribution
$H_1$: Food X has more growth than Food Y (one-tailed) **B1**
$\alpha = 0.05$, $n_1 = 7$ (X), $n_2 = 6$ (Y)

Combine and rank:

| Score | Food | Rank |
|-------|------|------|
| 8 | Y | 1 |
| 9 | Y | 2 |
| 10 | Y | 3 |
| 11 | X | 4.5 |
| 11 | Y | 4.5 |
| 12 | Y | 6 |
| 13 | X | 7 |
| 14 | X | 8 |
| 15 | Y | 9 |
| 16 | X | 10 |
| 17 | X | 11 |
| 18 | X | 12 |
| 19 | X | 13 |

**M1 A1** — tie: score 11 appears for both X and Y → ranks 4 and 5 → average 4.5

$R_1$ (Food X) $= 4.5 + 7 + 8 + 10 + 11 + 12 + 13 = 65.5$ **M1 A1**

One-tailed critical value ($n_1 = 7$, $n_2 = 6$, $\alpha = 0.05$):
Upper $= 64$ (for one-tailed test) **B1**

$65.5 &gt; 64$ ⇒ reject $H_0$ **M1**

Food X gives significantly more growth than Food Y at the 5% significance level. **A1**

</details>

:::warning[常见陷阱]

- 单尾检验的临界值与双尾不同。双尾用 $\alpha/2$ 的临界值
- 本题是"greater than"的单尾检验，只需看上临界值

:::

---

## Question Type 4: Sign Test

### 如何识别

题目要求使用符号检验，只需计数正负号而不考虑大小。关键词："sign test"、"ignore magnitude"

:::note[标准解题方法]

1. 记录每项符号（+、-、0）
2. 排除 0，$n$ = 非零符号数
3. $S$ = 较少符号的个数
4. 在 $H_0$ 下，$S \sim B(n, 0.5)$
5. 计算 p-value（双尾 $\times 2$）

:::

:::info[评分标准（MS 模式）]

- 提出假设 **B1**
- 符号计数 **M1**
- $S$ 和 $n$ 正确 **A1**
- 二项概率计算 **M1**
- p-value 正确 **A1**
- 比较结论 **M1 A1**

:::

**Example 1 — 9231/s24/qp/41 Q2 (7 marks):**

A company claims that its new packaging increases customer satisfaction. 12 customers rate their satisfaction (1-10) before and after:

| Customer | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|----------|---|---|---|---|---|---|---|---|---|---|---|---|
| Before | 6 | 5 | 7 | 4 | 8 | 5 | 6 | 7 | 3 | 6 | 5 | 7 |
| After | 7 | 5 | 8 | 6 | 7 | 6 | 8 | 8 | 5 | 7 | 6 | 7 |

Use a sign test at the 5% significance level to test whether satisfaction has increased.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: $P(\text{After} &gt; \text{Before}) = P(\text{After} &lt; \text{Before}) = 0.5$ (no difference)
$H_1$: $P(\text{After} &gt; \text{Before}) &gt; 0.5$ (one-tailed) **B1**
$\alpha = 0.05$

| Customer | Before | After | Sign |
|----------|--------|-------|------|
| 1 | 6 | 7 | + |
| 2 | 5 | 5 | 0 |
| 3 | 7 | 8 | + |
| 4 | 4 | 6 | + |
| 5 | 8 | 7 | − |
| 6 | 5 | 6 | + |
| 7 | 6 | 8 | + |
| 8 | 7 | 8 | + |
| 9 | 3 | 5 | + |
| 10 | 6 | 7 | + |
| 11 | 5 | 6 | + |
| 12 | 7 | 7 | 0 |

**M1**

$+$ : 9, $-$ : 1, $0$ : 2
$n = 12 - 2 = 10$ (non-zero signs) **A1**
$S = 1$ (number of $-$ signs, the less frequent)

Under $H_0$, $S \sim B(10, 0.5)$

$P(S \leq 1) = P(S = 0) + P(S = 1)$
$= \binom{10}{0}(0.5)^{10} + \binom{10}{1}(0.5)^{10}$
$= (1 + 10) \times 0.5^{10} = 11 \times 0.0009766 = 0.01074$

**M1 A1**

One-tailed test: p-value $= 0.01074$ **A1**

$0.01074 &lt; 0.05$ ⇒ reject $H_0$ **M1**

There is sufficient evidence that satisfaction has increased. **A1**

</details>

:::warning[常见陷阱]

- 零差异排除后 $n = 10$（不是 12）
- 单尾检验，p-value 不需 $\times 2$
- 本题用较少符号数（$S = 1$）而非较多符号数

:::

---

**Example 2 — 9231/s25/qp/41 Q5 variation (8 marks):**

A taste test compares two cola brands. 15 tasters each pick their preferred brand:

Prefer A: 11, Prefer B: 4

Use a sign test at the 5% significance level to test whether there is a preference.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: $P(\text{prefer A}) = P(\text{prefer B}) = 0.5$ (no preference)
$H_1$: There is a preference (two-tailed) **B1**
$\alpha = 0.05$

$n = 15$ (all tasters expressed a preference, no ties)
$S = 4$ (the smaller count) **M1 A1**

Under $H_0$, $S \sim B(15, 0.5)$

$P(S \leq 4) = \sum_{r=0}^4 \binom{15}{r}(0.5)^{15}$
$= (1 + 15 + 105 + 455 + 1365) \times 0.5^{15}$
$= 1941 \times 0.00003052 = 0.0592$ **M1 A1**

Two-tailed: p-value $= 2 \times 0.0592 = 0.1184$ **A1**

$0.1184 &gt; 0.05$ ⇒ do not reject $H_0$ **M1**

No significant preference for either brand at the 5% level. **A1**

</details>

:::warning[常见陷阱]

- 双尾检验 p-value 需要 $\times 2$
- 本题没有零差异（所有 taster 都选了），所以 $n = 15$

:::

---

## Question Type 5: Normal Approximation for Wilcoxon Tests

### 如何识别

样本量较大（signed-rank: $n &gt; 20$，rank-sum: $n_1, n_2 &gt; 10$），题目要求使用正态近似。关键词："normal approximation"、"large sample"、"use a suitable approximation"

:::note[标准解题方法]

**Signed-rank:**
$$\mu_T = \frac{n(n+1)}{4}, \quad \sigma_T = \sqrt{\frac{n(n+1)(2n+1)}{24}}$$
$$z = \frac{T \pm 0.5 - \mu_T}{\sigma_T}$$

**Rank-sum:**
$$\mu_W = \frac{n_1(n_1+n_2+1)}{2}, \quad \sigma_W = \sqrt{\frac{n_1 n_2 (n_1+n_2+1)}{12}}$$
$$z = \frac{W \pm 0.5 - \mu_W}{\sigma_W}$$

:::

:::info[评分标准（MS 模式）]

- 计算 $\mu$：**B1**
- 计算 $\sigma$：**M1 A1**
- 计算 $z$ 含连续性校正：**M1 A1**
- 比较 $|z|$ 与 $z_{\text{crit}}$：**M1**
- 结论：**A1**

:::

**Example 1 — 9231/s22/qp/41 Q6 (10 marks):**

A sample of 30 households recorded their monthly electricity bills ($). The differences from the national average of $120 were calculated for a Wilcoxon signed-rank test. The sum of positive ranks $T^+ = 312$.

Use a normal approximation at the 5% significance level to test whether the population median differs from $120.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: median $= 120$
$H_1$: median $\neq 120$ (two-tailed) **B1**
$\alpha = 0.05$, $n = 30$ (assume no zero differences)

$T^+ = 312$, total sum of ranks $= \frac{30 \times 31}{2} = 465$
$T^- = 465 - 312 = 153$
$T = \min(312, 153) = 153$

$\mu_T = \frac{n(n+1)}{4} = \frac{30 \times 31}{4} = 232.5$ **B1**

$\sigma_T = \sqrt{\frac{n(n+1)(2n+1)}{24}} = \sqrt{\frac{30 \times 31 \times 61}{24}} = \sqrt{\frac{56730}{24}} = \sqrt{2363.75} = 48.62$ **M1 A1**

$z = \frac{T + 0.5 - \mu_T}{\sigma_T} = \frac{153 + 0.5 - 232.5}{48.62} = \frac{-79}{48.62} = -1.625$ **M1 A1**

Two-tailed critical value: $z_{0.025} = 1.960$ **M1**

$|z| = 1.625 &lt; 1.960$ ⇒ do not reject $H_0$ **M1**

No evidence that median bill differs from $120 at the 5% level. **A1**

</details>

:::warning[常见陷阱]

- $T = \min(T^+, T^-)$，因为双尾检验
- 连续性校正：$T + 0.5$（因为 $T &lt; \mu$，下尾校正）
- $\sigma_T$ 公式中有 $2n+1$，不要写成 $2n$ 或 $2n-1$

:::

---

**Example 2 — 9231/w23/qp/41 Q6 (10 marks):**

A Wilcoxon signed-rank test on 25 pairs of data (matched pairs) gave $T^+ = 198$ and $T^- = 127$.

Use a normal approximation at the 5% significance level to test whether there is a difference.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: median difference $= 0$
$H_1$: median difference $\neq 0$ (two-tailed) **B1**
$\alpha = 0.05$, $n = 25$

$T = \min(198, 127) = 127$

$\mu_T = \frac{n(n+1)}{4} = \frac{25 \times 26}{4} = 162.5$ **B1**

$\sigma_T = \sqrt{\frac{n(n+1)(2n+1)}{24}} = \sqrt{\frac{25 \times 26 \times 51}{24}} = \sqrt{\frac{33150}{24}} = \sqrt{1381.25} = 37.17$ **M1 A1**

$z = \frac{T + 0.5 - \mu_T}{\sigma_T} = \frac{127 + 0.5 - 162.5}{37.17} = \frac{-35}{37.17} = -0.942$ **M1 A1**

$z_{0.025} = 1.960$ **M1**

$|z| = 0.942 &lt; 1.960$ ⇒ do not reject $H_0$ **M1**

No evidence of a significant difference at the 5% level. **A1**

</details>

:::warning[常见陷阱]

- $n = 25$ 是排除零差异后的样本量，如果原数据有零差异需先排除
- 连续性校正符号：$T &lt; \mu$ 时用 $T + 0.5$

:::

---

**Example 3 — 9231/w25/qp/41 Q4 (9 marks):**

A Wilcoxon rank-sum test comparing two groups with $n_1 = 14$ and $n_2 = 16$ gave $R_1 = 289$ as the rank sum for the first group.

Use a normal approximation at the 5% significance level to test whether the two groups differ.

<details>
<summary>📝 展开查看完整解法 + MS</summary>

$H_0$: The two populations are identical
$H_1$: The two populations differ (two-tailed) **B1**
$n_1 = 14$, $n_2 = 16$, $W = R_1 = 289$
$\alpha = 0.05$

$\mu_W = \frac{n_1(n_1 + n_2 + 1)}{2} = \frac{14 \times (14 + 16 + 1)}{2} = \frac{14 \times 31}{2} = 217$ **B1**

$\sigma_W = \sqrt{\frac{n_1 n_2 (n_1 + n_2 + 1)}{12}} = \sqrt{\frac{14 \times 16 \times 31}{12}} = \sqrt{\frac{6944}{12}} = \sqrt{578.67} = 24.06$ **M1 A1**

$W = 289$ is greater than $\mu_W = 217$, so upper tail:
$z = \frac{W - 0.5 - \mu_W}{\sigma_W} = \frac{289 - 0.5 - 217}{24.06} = \frac{71.5}{24.06} = 2.972$ **M1 A1**

$z_{0.025} = 1.960$ **M1**

$2.972 &gt; 1.960$ ⇒ reject $H_0$ **M1**

Significant evidence of a difference between the two groups at the 5% level. **A1**

</details>

:::warning[常见陷阱]

- Rank-sum 的正态近似 $\mu$ 和 $\sigma$ 公式与 signed-rank 不同，不要混淆
- 上尾检验用 $W - 0.5$（因为 $W &gt; \mu$），下尾检验用 $W + 0.5$（因为 $W &lt; \mu$）

:::
