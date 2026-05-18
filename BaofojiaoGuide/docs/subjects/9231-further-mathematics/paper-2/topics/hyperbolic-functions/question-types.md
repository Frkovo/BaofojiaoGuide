---
title: 题型分析
sidebar_position: 3
---

# 题型分析 — Hyperbolic Functions

---

## Question Type 0: 必背基础 — 指数定义与图像

> **$\sinh x = \dfrac{e^x - e^{-x}}{2}$，$\cosh x = \dfrac{e^x + e^{-x}}{2}$**
>
> **$\cosh^2 x - \sinh^2 x \equiv 1$**
>
> **$\sinh 2x \equiv 2\sinh x\cosh x$，$\cosh 2x \equiv \cosh^2 x + \sinh^2 x$**

---

## Question Type 1: Proving hyperbolic identities

### 如何识别

题目出现 "Show that" 或 "Prove that" 后面跟一个双曲恒等式。

**关键词：** show that, prove, using the definitions of sinh and cosh in terms of exponentials

:::note[标准解题方法]

**方法A（指数形式）：**
1. 写成指数形式：$\sinh x = \frac{e^x - e^{-x}}{2}$，$\cosh x = \frac{e^x + e^{-x}}{2}$
2. 展开化简
3. 因式分解配到目标形式

**方法B（已知恒等式）：**
1. 从一边出发
2. 应用 $\cosh^2 x - \sinh^2 x = 1$、倍角公式等
3. 逐步推到另一边

:::

:::info[评分标准（MS 模式）]

- **M1**: 正确使用指数定义或恒等式
- **M1**: 正确的代数处理
- **A1**: 恒等式成功证明

:::

:::tip[涉及的主要恒等式]

$$
\cosh^2 x - \sinh^2 x \equiv 1
$$
$$
\sinh 2x \equiv 2\sinh x\cosh x
$$
$$
\cosh 2x \equiv \cosh^2 x + \sinh^2 x
$$
$$
\cosh 2x \equiv 2\cosh^2 x - 1 \equiv 2\sinh^2 x + 1
$$

:::

### 完整原题

**Example 1 — 9231/s22/qp/22 Q2(a) (3 marks):**

> (a) Starting from the definitions of $\cosh$ and $\sinh$ in terms of exponentials, prove that $\cosh 2x = 2\sinh^2 x + 1$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: writes $\cosh 2x = \frac12(e^{2x}+e^{-2x})$
- **M1**: uses $(e^x-e^{-x})^2 = e^{2x}-2+e^{-2x}$ to relate to $2\sinh^2 x$
- **A1**: AG

</details>

**Example 2 — 9231/s23/qp/22 Q3(a) (5 marks):**

> By considering the binomial expansion of $(z+z^{-1})^4$, where $z = \cos\theta + i\sin\theta$, use de Moivre's theorem to show that $\cos 4\theta = 8\cos^4\theta - 8\cos^2\theta + 1$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: $(z+z^{-1})^4 = z^4 + 4z^2 + 6 + 4z^{-2} + z^{-4}$
- **M1**: $z^n+z^{-n}=2\cos n\theta$
- **A1**: $=2\cos4\theta+8\cos2\theta+6$
- **M1**: uses $\cos2\theta=2\cos^2\theta-1$
- **A1**: AG

</details>

:::warning[常见陷阱]

- 混淆 $\cosh^2 x - \sinh^2 x = 1$ 与 $\cos^2 x + \sin^2 x = 1$（减号 vs 加号，完全不同）
- 只写结果不给过程——MS 给的是步骤分，光写答案得 0 分

:::

---

## Question Type 2: Graph sketching with asymptotes

### 如何识别

"Sketch $C_1$ and $C_2$ on the same diagram"

### 图像要点

- $y = \cosh x$：U 形，最低点 $(0,1)$，关于 $y$ 轴对称
- $y = \sinh x$：过 $(0,0)$，奇函数
- $y = \tanh x$：水平渐近线 $y = \pm 1$，过 $(0,0)$
- $y = \operatorname{sech} x$：过 $(0,1)$，$x\to\pm\infty$ 时 $y\to 0$

:::info[评分标准（MS 模式）]

- **B1**: $C_1$ 形状正确
- **B1**: $C_2$ 形状正确且有正确的交点

:::

### 完整原题

**Example 1 — 9231/s20/qp/22 Q5(b) (2 marks):**

> The curves $C_1: y = \cosh x$ and $C_2: y = \sinh^2 x$ intersect at $x = a$.
> (b) Sketch $C_1$ and $C_2$ on the same diagram.

**Example 2 — 9231/s22/qp/22 Q2(b) (3 marks):**

> Hence, or otherwise, solve the equation $2\sinh^2 x + 1 = 3$, giving your answer in logarithmic form.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: uses $\cosh2x=2\sinh^2x+1$ from (a) to rewrite as $\cosh2x=3$
- **M1**: $2x=\pm\cosh^{-1}3$ or exponential form
- **A1**: $x=\pm\frac12\ln(3+2\sqrt2)$

</details>

---

## Question Type 3: Solving hyperbolic equations using exponential form

### 如何识别

题目给出一个含 $\cosh x$、$\sinh x$ 的方程要求用**对数形式**表示解。

**关键词：** solve, logarithmic form, in terms of natural logarithms

:::note[标准解题方法]

1. 代入：
   $\cosh x = \dfrac{e^x + e^{-x}}{2}$
   $\sinh x = \dfrac{e^x - e^{-x}}{2}$
2. 化简得到关于 $e^x$ 的方程
3. 两边乘 $e^x$ 得到关于 $e^x$ 的二次方程
4. 解 $e^x$，取正值（因为 $e^x > 0$）
5. $x = \ln(\text{正根})$

:::

### 完整原题

**Example 1 — 9231/w22/qp/22 Q4:**

> Solve the equation $\cosh x - 3\sinh x = 4$, giving your answer in logarithmic form.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: writes $\frac{e^x+e^{-x}}{2} - \frac{3(e^x-e^{-x})}{2} = 4$
- **M1**: simplifies to $-2e^x + 4e^{-x} = 8$
- **M1**: multiplies by $e^x$ $\to$ $2e^{2x} + 8e^x - 4 = 0$
- **A1**: $e^x = -2 + \sqrt{6}$ (positive root)
- **A1**: $x = \ln(\sqrt{6} - 2)$

</details>

**Example 2 — 9231/s20/qp/22 Q5(a) (4 marks):**

> The curves $C_1: y = \cosh x$ and $C_2: y = \sinh^2 x$ intersect at the point where $x = a$.
> (a) Find the exact value of $a$, giving your answer in logarithmic form.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: $\cosh a = \sinh^2 a$
- **M1**: uses $\cosh^2 a - \sinh^2 a = 1$ to get $\cosh^2 a - \cosh a - 1 = 0$
- **M1**: solves quadratic: $\cosh a = \frac{1+\sqrt5}{2}$
- **A1**: $a = \ln\left(\frac12 + \frac{\sqrt5}{2}\right)$

</details>

:::warning[常见陷阱]

- 忘记 $e^x > 0$，把两个二次根都取了 log
- 正负号错误：$\cosh x - 3\sinh x$ 展开时 $-3\sinh x$ 变成 $-\dfrac{3e^x - 3e^{-x}}{2}$

:::

---

## Question Type 4: Logarithmic form of inverse hyperbolic functions

### 必须背熟的三个公式

$$
\sinh^{-1} x = \ln\left(x + \sqrt{x^2 + 1}\right)
$$
$$
\cosh^{-1} x = \ln\left(x + \sqrt{x^2 - 1}\right),\quad x \ge 1
$$
$$
\tanh^{-1} x = \frac{1}{2}\ln\left(\frac{1+x}{1-x}\right),\quad |x| < 1
$$

### 完整原题

**Example 1 — 9231/s20/qp/22 Q5(a) (4 marks):**

> The curves $C_1: y = \cosh x$ and $C_2: y = \sinh^2 x$ intersect at $x = a$.
> (a) Find the exact value of $a$, giving your answer in logarithmic form.

**Example 2 — 标准题型：直接应用公式：**

> Express $\sinh^{-1} 2$ in the form $\ln(a+\sqrt{b})$, where $a$ and $b$ are integers.

**解题：** $\sinh^{-1} 2 = \ln(2 + \sqrt{2^2+1}) = \ln(2+\sqrt{5})$

**Example 3 — 标准题型：反双曲函数的积分应用：**

> Evaluate $\displaystyle\int_0^3 \frac{dx}{\sqrt{x^2+16}}$, giving your answer in logarithmic form.

**解题：** $\displaystyle\int_0^3 \frac{dx}{\sqrt{x^2+16}} = \left[\sinh^{-1}\frac{x}{4}\right]_0^3 = \sinh^{-1}\frac34 - 0 = \ln\left(\frac34 + \sqrt{\frac{9}{16}+1}\right) = \ln\left(\frac{3+\sqrt{25}}{4}\right) = \ln 2$

:::note[解题思路]

1. $\cosh a = \sinh^2 a$
2. $\cosh a = \cosh^2 a - 1$（用 $\cosh^2 - \sinh^2 = 1$）
3. $\cosh^2 a - \cosh a - 1 = 0$
4. $\cosh a = \dfrac{1+\sqrt{5}}{2}$（取正值）
5. $a = \cosh^{-1}\left(\dfrac{1+\sqrt{5}}{2}\right) = \ln\left(\dfrac{1}{2} + \dfrac{1}{2}\sqrt{5}\right)$

:::

---

## Question Type 5: Integration using hyperbolic substitution

### 代换选择表

| 被积函数含 | 设 | $dx$ | 恒等式 |
|-----------|-----|------|--------|
| $\sqrt{x^2 + a^2}$ | $x = a\sinh u$ | $a\cosh u\,du$ | $\cosh^2 u - \sinh^2 u = 1$ |
| $\sqrt{x^2 - a^2}$ | $x = a\cosh u$ | $a\sinh u\,du$ | $\cosh^2 u - \sinh^2 u = 1$ |
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $a\cos\theta\,d\theta$ | $1-\sin^2\theta = \cos^2\theta$ |

:::warning[常见陷阱]

- 忘了换 $dx$：$x = \sinh u$ → $dx = \cosh u\,du$，不是 $du$
- 定积分忘了换限：$x=0 \to u=0$，$x=1 \to u=\sinh^{-1}1$
- 回代搞反：$u = \sinh^{-1} x$，不是 $u = \sinh x$

:::
