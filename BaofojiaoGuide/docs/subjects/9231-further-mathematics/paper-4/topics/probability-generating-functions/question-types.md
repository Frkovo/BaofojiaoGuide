---
title: 题型分析
sidebar_position: 2
---

# 题型分析 — Probability Generating Functions

## Question Type 1: Constructing PGF from a Discrete Distribution

### 如何识别

题目给出一个离散随机变量的概率分布（可能以文字描述——如从袋中取球、掷骰子等），要求写出 $G(t) = \sum P(X = x)t^x$。

:::note[标准解题方法]

1. 确定随机变量 $X$ 的所有可能取值
2. 计算每个取值对应的概率 $P(X = x)$
3. 代入 $G(t) = \sum P(X = x)t^x$
4. 若有需要，化简合并同类项

:::

:::info[评分标准（MS 模式）]

- **M1** 列出所有 $x$ 并正确计算至少一个概率
- **A1** $G(t)$ 表达式完全正确（通常接受未化简形式）
- **B1** 特别标注的概率（如 $P(X = 0)$）

:::

**Example 1 (S20 Q4):** A bag contains 4 red balls and 2 blue balls. Two balls are drawn without replacement. Let $X$ be the number of blue balls drawn. Find the probability generating function of $X$.

<details>
<summary>📝 MS 展开查看</summary>

$X$ can take values 0, 1, 2.

$P(X = 0) = \frac{C^4_2}{C^6_2} = \frac{6}{15} = \frac{2}{5}$ **B1**

$P(X = 1) = \frac{C^4_1 \times C^2_1}{C^6_2} = \frac{8}{15}$ **M1**

$P(X = 2) = \frac{C^2_2}{C^6_2} = \frac{1}{15}$ **A1**

$G_X(t) = \frac{2}{5} + \frac{8}{15}t + \frac{1}{15}t^2$ **A1**

[Total: 4]
</details>

**Example 2 (W20 Q5):** A biased coin has probability $p$ of showing heads. It is tossed 3 times. Let $Y$ be the number of heads obtained. Find $G_Y(t)$.

<details>
<summary>📝 MS 展开查看</summary>

$Y \sim B(3, p)$

$P(Y = 0) = (1-p)^3$, $P(Y = 1) = 3p(1-p)^2$

$P(Y = 2) = 3p^2(1-p)$, $P(Y = 3) = p^3$ **M1 A1**

$G_Y(t) = (1-p)^3 + 3p(1-p)^2 t + 3p^2(1-p) t^2 + p^3 t^3$ **A1**

Alternatively: $G_Y(t) = (1-p + pt)^3$ **B1**

[Total: 4]
</details>

**Example 3 (S21 Q6):** A fair dice is rolled once. Let $Z$ be the score shown. Write down $G_Z(t)$.

<details>
<summary>📝 MS 展开查看</summary>

$Z$ takes values 1, 2, 3, 4, 5, 6 each with probability $\frac{1}{6}$. **M1**

$G_Z(t) = \frac{1}{6}(t + t^2 + t^3 + t^4 + t^5 + t^6)$ **M1 A1**

[Total: 3]
</details>

:::warning[常见陷阱]

- 不放回抽样时注意使用组合数，而非二项概率
- 区分 $X$ 的取值起点（0 还是 1）——几何分布有不同的定义
- 不要遗漏 $t^0 = 1$ 项（即常数项）

:::

---

## Question Type 2: Finding $E(X)$ and $\text{Var}(X)$ from PGF

### 如何识别

给出 $G(t)$（可能是多项式或有理函数），要求求 $E(X)$ 和 $\text{Var}(X)$，或直接给出一组概率表达式要求利用 PGF 求矩。

:::note[标准解题方法]

1. 对 $G(t)$ 求导得 $G'(t)$
2. 代入 $t = 1$ 得 $E[X] = G'(1)$
3. 求二阶导 $G''(t)$，代入 $t = 1$ 得 $E[X(X-1)] = G''(1)$
4. $\text{Var}(X) = G''(1) + G'(1) - [G'(1)]^2$

:::

:::info[评分标准（MS 模式）]

- **M1** 对 $G(t)$ 求导（至少正确求出一阶导）
- **A1** $G'(1)$ 或 $E(X)$ 正确
- **M1** 求二阶导并代入
- **A1** $\text{Var}(X)$ 正确

:::

**Example 1 (W21 Q5):** The probability generating function of $X$ is $G_X(t) = \frac{1}{6}(t + t^2 + t^3 + t^4 + t^5 + t^6)$. Find $E(X)$ and $\text{Var}(X)$.

<details>
<summary>📝 MS 展开查看</summary>

$G_X'(t) = \frac{1}{6}(1 + 2t + 3t^2 + 4t^3 + 5t^4 + 6t^5)$ **M1**

$G_X'(1) = \frac{1}{6}(1 + 2 + 3 + 4 + 5 + 6) = \frac{21}{6} = 3.5$ **A1**

$G_X''(t) = \frac{1}{6}(2 + 6t + 12t^2 + 20t^3 + 30t^4)$ **M1**

$G_X''(1) = \frac{1}{6}(2 + 6 + 12 + 20 + 30) = \frac{70}{6} = \frac{35}{3}$

$\text{Var}(X) = G''(1) + G'(1) - [G'(1)]^2 = \frac{35}{3} + \frac{7}{2} - \left(\frac{7}{2}\right)^2$ **M1**

$\text{Var}(X) = \frac{35}{3} + \frac{7}{2} - \frac{49}{4} = \frac{140 + 42 - 147}{12} = \frac{35}{12} \approx 2.917$ **A1**

[Total: 6]
</details>

**Example 2 (S22 Q2):** $G_X(t) = \left(\frac{1}{2} + \frac{1}{2}t\right)^4$. Find $E(X)$ and $\text{Var}(X)$.

<details>
<summary>📝 MS 展开查看</summary>

$G_X'(t) = 4\left(\frac{1}{2} + \frac{1}{2}t\right)^3 \cdot \frac{1}{2} = 2\left(\frac{1}{2} + \frac{1}{2}t\right)^3$ **M1**

$G_X'(1) = 2\left(\frac{1}{2} + \frac{1}{2}\right)^3 = 2(1)^3 = 2$ **A1**

$G_X''(t) = 6\left(\frac{1}{2} + \frac{1}{2}t\right)^2 \cdot \frac{1}{2} = 3\left(\frac{1}{2} + \frac{1}{2}t\right)^2$ **M1**

$G_X''(1) = 3(1)^2 = 3$

$\text{Var}(X) = 3 + 2 - (2)^2 = 1$ **A1**

[Alternatively: $X \sim B(4, 0.5)$, $E(X) = 2$, $\text{Var}(X) = 1$]

[Total: 5]
</details>

**Example 3 (S24 Q4):** The probability generating function of $Y$ is $G_Y(t) = \frac{1}{8}(1 + t)^3$. Find $E(Y)$ and $\text{Var}(Y)$.

<details>
<summary>📝 MS 展开查看</summary>

$G_Y(t) = \frac{1}{8}(1 + 3t + 3t^2 + t^3)$

$G_Y'(t) = \frac{1}{8}(3 + 6t + 3t^2)$ **M1**

$G_Y'(1) = \frac{1}{8}(3 + 6 + 3) = \frac{12}{8} = 1.5$ **A1**

$G_Y''(t) = \frac{1}{8}(6 + 6t)$ **M1**

$G_Y''(1) = \frac{1}{8}(6 + 6) = \frac{12}{8} = 1.5$

$\text{Var}(Y) = 1.5 + 1.5 - (1.5)^2 = 3 - 2.25 = 0.75$ **A1**

[Alternatively: $Y \sim B(3, 0.5)$, $E(Y) = 1.5$, $\text{Var}(Y) = 0.75$]

[Total: 5]
</details>

:::warning[常见陷阱]

- $G'(1) = E[X]$，不是 $E[X^2]$
- $\text{Var}(X) = G''(1) + G'(1) - [G'(1)]^2$，忘记加 $G'(1)$ 是典型错误
- 展开多项式时注意合并同类项；若 $G(t)$ 是 $(a+bt)^n$ 形式，直接用链式法则

:::

---

## Question Type 3: Sum of Independent Random Variables

### 如何识别

题目给出两个或多个独立随机变量（有时是同分布），要求求 $X+Y$ 的 PGF，或由和的 PGF 求概率分布。

:::note[标准解题方法]

1. 写出每个变量的 PGF：$G_X(t)$ 和 $G_Y(t)$
2. 乘积得和 PGF：$G_{X+Y}(t) = G_X(t) \cdot G_Y(t)$
3. 展开多项式（或幂级数），$t^k$ 的系数即为 $P(X + Y = k)$

:::

:::info[评分标准（MS 模式）]

- **B1** 正确写出每个变量的 PGF
- **M1** $G_X \cdot G_Y$ 乘积
- **A1** 乘积表达式正确
- **M1** 从展开系数提取概率
- **A1** 最终概率值正确

:::

**Example 1 (S20 Q6):** $X \sim B(3, 0.4)$ and $Y \sim B(2, 0.4)$ are independent. Find $P(X + Y = 3)$ using PGFs.

<details>
<summary>📝 MS 展开查看</summary>

$G_X(t) = (0.6 + 0.4t)^3$ **B1**

$G_Y(t) = (0.6 + 0.4t)^2$ **B1**

$G_{X+Y}(t) = (0.6 + 0.4t)^3 \cdot (0.6 + 0.4t)^2 = (0.6 + 0.4t)^5$ **M1**

$P(X+Y = 3) = \binom{5}{3}(0.4)^3(0.6)^2$ **M1**

$P(X+Y = 3) = 10 \times 0.064 \times 0.36 = 0.2304$ **A1**

[Total: 5]
</details>

**Example 2 (W22 Q4):** $X$ and $Y$ are independent discrete random variables with $G_X(t) = \frac{1}{2}(1 + t)$ and $G_Y(t) = \frac{1}{4}(1 + t)^2$. Find $P(X + Y = 2)$.

<details>
<summary>📝 MS 展开查看</summary>

$G_{X+Y}(t) = G_X(t) \cdot G_Y(t) = \frac{1}{2}(1 + t) \cdot \frac{1}{4}(1 + t)^2$ **M1**

$G_{X+Y}(t) = \frac{1}{8}(1 + t)^3$ **A1**

$\frac{1}{8}(1 + t)^3 = \frac{1}{8}(1 + 3t + 3t^2 + t^3)$ **M1**

$P(X + Y = 2) = \frac{3}{8}$ **A1**

[Total: 4]
</details>

**Example 3 (W23 Q5):** $X_1, X_2, \dots, X_5$ are independent identically distributed random variables with $G_X(t) = \frac{1}{3}(1 + t + t^2)$. Let $S = X_1 + X_2 + \cdots + X_5$. Find $P(S = 2)$.

<details>
<summary>📝 MS 展开查看</summary>

$G_S(t) = [G_X(t)]^5 = \left[\frac{1}{3}(1 + t + t^2)\right]^5$ **M1**

$P(S = 2)$ is coefficient of $t^2$ in $\left(\frac{1}{3}\right)^5(1 + t + t^2)^5$ **M1**

Consider $(1 + t + t^2)^5$. To get $t^2$, possibilities:
- Two $t$'s and three $1$'s: $\binom{5}{2} = 10$ ways
- One $t^2$ and four $1$'s: $\binom{5}{1} = 5$ ways

Coefficient of $t^2 = 10 + 5 = 15$ **M1**

$P(S = 2) = 15 \times \left(\frac{1}{3}\right)^5 = \frac{15}{243} = \frac{5}{81}$ **A1**

[Total: 5]
</details>

:::warning[常见陷阱]

- 和的 PGF 是乘积（$G_X \cdot G_Y$）而非和（$G_X + G_Y$）
- 展开多项式时注意大型系数，可考虑组合解释而非完全展开
- 多个独立同分布变量的 PGF 是 $[G_X(t)]^n$，不要误写为 $n \cdot G_X(t)$

:::

---

## Question Type 4: Working Backwards from Sum-PGF

### 如何识别

给出 $S = X_1 + X_2 + \cdots + X_n$ 的 PGF（如 $G_S(t) = [G_X(t)]^n$ 形式），要求反推单个变量 $X_i$ 的 PGF 或概率分布。

:::note[标准解题方法]

1. 写出 $G_S(t) = [G_X(t)]^n$
2. 两边同时开 $n$ 次方：$G_X(t) = [G_S(t)]^{1/n}$
3. 展开或通过系数匹配求 $P(X = x)$

:::

:::info[评分标准（MS 模式）]

- **M1** 识别 $G_S(t) = [G_X(t)]^2$ 或 $n$ 次方关系
- **M1** 开方运算
- **A1** $G_X(t)$ 正确
- **M1/A1** 由 $G_X(t)$ 系数得出概率分布

:::

**Example 1 (W25 Q7):** $S = X_1 + X_2$ where $X_1, X_2$ are independent and identically distributed. Given $G_S(t) = \frac{1}{4}(1 + t)^2$, find the distribution of $X_1$.

<details>
<summary>📝 MS 展开查看</summary>

$G_S(t) = [G_X(t)]^2$ **M1**

$[G_X(t)]^2 = \frac{1}{4}(1 + t)^2$ **M1**

$G_X(t) = \frac{1}{2}(1 + t)$ (positive root) **A1**

Hence $X_1$ takes values 0 and 1, each with probability $\frac{1}{2}$. **A1**

[Total: 4]
</details>

**Example 2 (S23 Q5):** $Y_1, Y_2, Y_3$ are independent and identically distributed. Given $G_{Y_1+Y_2+Y_3}(t) = \frac{1}{27}(1 + t + t^2)^3$, find $G_{Y_1}(t)$ and $P(Y_1 = 1)$.

<details>
<summary>📝 MS 展开查看</summary>

$G_{Y_1+Y_2+Y_3}(t) = [G_{Y_1}(t)]^3$ **M1**

$[G_{Y_1}(t)]^3 = \frac{1}{27}(1 + t + t^2)^3$ **M1**

$G_{Y_1}(t) = \frac{1}{3}(1 + t + t^2)$ **A1**

$P(Y_1 = 1) =$ coefficient of $t^1$ in $G_{Y_1}(t) = \frac{1}{3}$ **A1**

[Total: 4]
</details>

**Example 3 (S25 Q6):** $S = X_1 + X_2$ where $X_1, X_2$ are i.i.d. with unknown distribution. $G_S(t) = \frac{1}{16}(1 + t)^4$. Find $G_X(t)$ and $P(X = 2)$.

<details>
<summary>📝 MS 展开查看</summary>

$G_S(t) = [G_X(t)]^2 = \frac{1}{16}(1 + t)^4 = \left[\frac{1}{4}(1 + t)^2\right]^2$ **M1**

$G_X(t) = \frac{1}{4}(1 + t)^2$ **A1**

$G_X(t) = \frac{1}{4}(1 + 2t + t^2)$ **M1**

$P(X = 2) = \frac{1}{4}$ **A1**

[Total: 4]
</details>

:::warning[常见陷阱]

- 开平方/开 $n$ 次方时只取正根（概率非负）
- 注意区分 $G_S(t) = [G_X(t)]^n$ 和 $G_S(t) = [G_X(t)]^n$ 的不同 $n$ 值
- 开方后检查各项系数是否在 $[0, 1]$ 范围内

:::
