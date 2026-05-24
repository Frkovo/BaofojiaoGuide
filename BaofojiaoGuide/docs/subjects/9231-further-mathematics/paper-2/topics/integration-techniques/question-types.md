---
title: 题型分析
sidebar_position: 4
---

# 题型分析 — Integration Techniques

## Type 1: Reduction Formulae（递推公式）

### 整体认识

题目定义一个带参数 $n$ 的积分 $I_n$，要求：
- **(a)** 证明递推关系（5-6 分）
- **(b)** 求某个 $I_k$ 的值（2-3 分）
- 有时 **(c)** 求极限或进一步应用

### 两种推导方法

| 方法 | 适用场景 | 核心操作 |
|------|---------|---------|
| **分部积分法**（占 90%） | 被积函数可拆 $u \cdot dv$ | 选 $u$ 含 $n$，$dv$ 易积分 |
| **微分法** | 题目提示 "consider $\frac{d}{dx}(x \cdot \dots)$" | 求导后两边积分 |

---

#### 方法 A：分部积分法

**标准步骤：**

1. 被积函数拆成 $u \cdot dv$，$u$ 含 $n$（或 $n-1$），$dv$ 不含 $n$
2. $I_n = \int u\,dv = uv - \int v\,du$
3. 用恒等式（$\cos^2 x = 1 - \sin^2 x$ 等）将 $\int v\,du$ 写成 $I_n$ 和 $I_{n-2}$ 的组合
4. 整理得递推关系

:::info[分部积分选 u/dv 原则]
| 被积函数 | $u$（含 $n$） | $dv$ |
|----------|--------------|------|
| $\sin^n x$ | $\sin^{n-1}x$ | $\sin x\,dx$ |
| $\cos^n x$ | $\cos^{n-1}x$ | $\cos x\,dx$ |
| $x^n e^{ax}$ | $x^n$ | $e^{ax}dx$ |
| $(1-x^2)^{n/2}$ | 拆成 $(1-x^2)(1-x^2)^{(n-2)/2}$ | 对 $x$ 部分分部 |
| $(1-x)^n \sinh x$ | $(1-x)^n$ | $\sinh x\,dx$ |

原则：$u$ 微分后降次，$dv$ 积分后不变复杂。
:::

---

#### 方法 B：微分法

1. 题目引导："By considering $\frac{d}{dx}(x \cdot g(x))$ ..."
2. 求导 $\frac{d}{dx}[x \cdot g(x)]$
3. 两边从 $a$ 到 $b$ 积分
4. 左边得 $[x \cdot g(x)]_a^b$，右边拆成 $I_n$ 和 $I_{n-2}$

---

### 四大常见模式

#### 模式 1：$\sin^n x$ / $\cos^n x$ 型

$$
I_n = \int_0^{\pi/2} \sin^n x\,dx \quad\Rightarrow\quad nI_n = (n-1)I_{n-2}
$$

**关键**：$u = \sin^{n-1}x$，$dv = \sin x\,dx$，$\cos^2 x = 1 - \sin^2 x$

> **Example 1 — s21/23 Q6：** $I_n = \int_0^{\pi/2} \sin^n x\,dx$，$n \ge 2$
> (a) Show that $nI_n = (n-1)I_{n-2}$ [5]
> (b) Hence find $I_6$ [2]

<details>
<summary>📝 MS 展开查看</summary>

$I_n = \int_0^{\pi/2} \sin^{n-1}x \cdot \sin x\,dx$

$u = \sin^{n-1}x$，$dv = \sin x\,dx$ **M1**

$du = (n-1)\sin^{n-2}x\cos x\,dx$，$v = -\cos x$

$I_n = \big[-\sin^{n-1}x\cos x\big]_0^{\pi/2} + (n-1)\int_0^{\pi/2} \sin^{n-2}x\cos^2 x\,dx$ **M1**

$= 0 + (n-1)\int_0^{\pi/2} \sin^{n-2}x(1-\sin^2 x)\,dx$ **A1**

$= (n-1)(I_{n-2} - I_n)$

$nI_n = (n-1)I_{n-2}$ **A1**

$I_0 = \frac{\pi}{2}$，$I_1 = 1$ **B1**

$I_6 = \frac{5}{6} \cdot \frac{3}{4} \cdot \frac{1}{2} \cdot I_0 = \frac{5\pi}{32}$ **A1**
</details>

---

#### 模式 2：$(1-x^2)^{n/2}$ 型

$$
I_n = \int_0^1 (1-x^2)^{n/2}\,dx \quad\Rightarrow\quad (n+2)I_n = (n+1)I_{n-2}
$$

**关键**：拆 $(1-x^2)^{n/2} = (1-x^2)(1-x^2)^{(n-2)/2}$，分部中 $u = x$，$dv = x(1-x^2)^{(n-2)/2}dx$

> **Example 2 — s20/21 Q6：** $I_n = \int_0^1 (1-x^2)^{n/2}\,dx$，$n \ge 0$
> (a) Show that $(n+2)I_n = (n+1)I_{n-2}$ for $n \ge 2$ [5]
> (b) Evaluate $I_5$ [3]

<details>
<summary>📝 MS 展开查看</summary>

拆 $(1-x^2)^{n/2} = (1-x^2)(1-x^2)^{(n-2)/2}$ **M1**

$I_n = \int_0^1 (1-x^2)(1-x^2)^{(n-2)/2}\,dx$

$= I_{n-2} - \int_0^1 x \cdot x(1-x^2)^{(n-2)/2}\,dx$ **M1**

分部：$u = x$，$dv = x(1-x^2)^{(n-2)/2}dx$ **M1**

$du = dx$，$v = -\frac{1}{n}(1-x^2)^{n/2}$

$\int_0^1 x^2(1-x^2)^{(n-2)/2}dx = \big[-\frac{x}{n}(1-x^2)^{n/2}\big]_0^1 + \frac{1}{n}I_n = \frac{1}{n}I_n$ **A1**

$I_n = I_{n-2} - \frac{1}{n}I_n \Rightarrow \frac{n+1}{n}I_n = I_{n-2} \Rightarrow (n+2)I_n = (n+1)I_{n-2}$ **A1**

$I_0 = 1$，$I_1 = \frac{\pi}{4}$

$I_5 = \frac{6}{7}\cdot\frac{4}{5}\cdot\frac{\pi}{4} = \frac{6\pi}{35}$ **A1**
</details>

---

#### 模式 3：$x^n e^{ax}$ 型（步长 1）

$$
I_n = \int_a^b x^n e^{kx}\,dx \quad\Rightarrow\quad \text{与 } I_{n-1} \text{ 的递推}
$$

**关键**：$u = x^n$，$dv = e^{kx}dx$，每次降 1 次

> **Example 3 — s20/23 Q2：** $I_n = \int_0^1 x^n e^{-3x}\,dx$
> (a) Show that $3I_n = 1 - nI_{n-1}$，$n \ge 1$ [3]
> (b) Find $I_3$ [3]

<details>
<summary>📝 MS 展开查看</summary>

$u = x^n$，$dv = e^{-3x}dx$

$du = nx^{n-1}dx$，$v = -\frac{1}{3}e^{-3x}$ **M1**

$I_n = \big[-\frac{1}{3}x^n e^{-3x}\big]_0^1 + \frac{n}{3}\int_0^1 x^{n-1}e^{-3x}dx$ **M1**

$= -\frac{1}{3}e^{-3} + \frac{n}{3}I_{n-1}$

$3I_n = nI_{n-1} - e^{-3}$ **A1**

$I_0 = \frac{1}{3}(1-e^{-3})$ **B1**

$I_3 = \frac{2}{27} - \frac{26}{27}e^{-3}$ **A1**
</details>

---

#### 模式 4：双曲函数型（两次分部）

$$
I_n = \int_0^1 (1-x)^n \sinh x\,dx \quad\Rightarrow\quad I_n = -1 + n(n-1)I_{n-2}
$$

**关键**：两次分部（第一次 $u = (1-x)^n$，第二次 $u = (1-x)^{n-1}$）

> **Example 4 — s25/21 Q2：** $I_n = \int_0^1 (1-x)^n \sinh x\,dx$，$n \ge 2$
> (a) Show that $I_n = -1 + n(n-1)I_{n-2}$ [4]
> (b) Find $I_3$ [3]

<details>
<summary>📝 MS 展开查看</summary>

$u = (1-x)^n$，$dv = \sinh x\,dx$

$du = -n(1-x)^{n-1}dx$，$v = \cosh x$ **M1**

$I_n = \big[(1-x)^n\cosh x\big]_0^1 + n\int_0^1 (1-x)^{n-1}\cosh x\,dx$ **M1**

$= -1 + n\int_0^1 (1-x)^{n-1}\cosh x\,dx$

再分部：$u = (1-x)^{n-1}$，$dv = \cosh x\,dx$

$du = -(n-1)(1-x)^{n-2}dx$，$v = \sinh x$ **M1**

$\int_0^1 (1-x)^{n-1}\cosh x\,dx = \big[(1-x)^{n-1}\sinh x\big]_0^1 + (n-1)I_{n-2}$

$= (n-1)I_{n-2}$

所以 $I_n = -1 + n(n-1)I_{n-2}$ **A1**

$I_0 = \cosh 1 - 1$ **B1**

$I_1 = 1 - \sinh 1$ **A1**

$I_3 = 5 - 6\sinh 1$ **A1**
</details>

---

### 求具体 $I_k$ 的完整流程

1. **先求基础值**（$n=0$ 和 $n=1$）
   - $I_0$：去掉所有含 $n$ 的因子，通常可直接积
   - $I_1$：去掉高次幂，变成简单积分
2. **沿递推逐步上行**
   - 步长 2（$n \to n-2$）：分奇偶两条链
   - 步长 1（$n \to n-1$）：逐次下降
3. **约分化简** — 连乘要仔细，答案往往含 $\pi$、$e$ 或 $\ln$

:::tip[奇偶分离技巧（步长 2）]
$nI_n = (n-1)I_{n-2}$：

**偶数链**：$I_0 \to I_2 \to I_4 \to I_6$
$I_{2k} = \frac{(2k-1)(2k-3)\cdots 1}{(2k)(2k-2)\cdots 2} \cdot I_0$

**奇数链**：$I_1 \to I_3 \to I_5 \to I_7$
$I_{2k+1} = \frac{(2k)(2k-2)\cdots 2}{(2k+1)(2k-1)\cdots 3} \cdot I_1$
:::

### 常见陷阱

:::warning[常见陷阱]
1. **$u$/$dv$ 选反**：含 $n$ 的因子做 $u$（微分后降次），不是 $dv$
2. **恒等式代错**：$\cos^2 x = 1 - \sin^2 x$，不是 $\cos^2 x = 1 + \sin^2 x$
3. **边界项忘代**：$[uv]_a^b$ 要代两个端点
4. **基础值 $I_0$/$I_1$ 算错**：最常见的失分点
5. **步长 2 的递推试图一步到位**：$n=5$ 必须 $5\to3\to1$
6. **符号**：分部积分是 $+\int v\,du$，不是 $-$
:::

---

## Type 2: Integration by Parts / Substitution (3–4 marks)

> **Example 1: s20/23 Q2** — Evaluate $\int_0^1 x^2 e^{2x}\,dx$.

<details>
<summary>📝 MS 展开查看</summary>

Let $u = x^2$, $dv = e^{2x}dx$

$du = 2x\,dx$, $v = \frac{1}{2}e^{2x}$

$\int x^2 e^{2x}\,dx = \frac{1}{2}x^2e^{2x} - \int \frac{1}{2}e^{2x} \cdot 2x\,dx = \frac{1}{2}x^2e^{2x} - \int xe^{2x}\,dx$

For $\int xe^{2x}\,dx$: $u = x$, $dv = e^{2x}dx$

$= \frac{1}{2}xe^{2x} - \frac{1}{4}e^{2x}$

So $\int x^2 e^{2x}\,dx = \frac{1}{2}x^2e^{2x} - \frac{1}{2}xe^{2x} + \frac{1}{4}e^{2x} + C$

$\int_0^1 x^2 e^{2x}\,dx = \big[\frac{1}{2}x^2e^{2x} - \frac{1}{2}xe^{2x} + \frac{1}{4}e^{2x}\big]_0^1$

$= \big(\frac{1}{2}e^2 - \frac{1}{2}e^2 + \frac{1}{4}e^2\big) - \frac{1}{4} = \frac{1}{4}(e^2 - 1)$

**M1** — Correct first integration by parts
**A1** — Correct $\int xe^{2x}dx$
**A1** — Correct final answer $\frac{1}{4}(e^2 - 1)$
</details>

---

## Type 3: Integration of Rational Functions (5 marks)

> **Example 1: s23/21 Q4** — Find $\int \frac{2x^2 + 3x + 1}{(x-1)(x^2 + 1)}\,dx$.

<details>
<summary>📝 MS 展开查看</summary>

Partial fractions:

$$\frac{2x^2 + 3x + 1}{(x-1)(x^2+1)} = \frac{A}{x-1} + \frac{Bx + C}{x^2+1}$$

Multiplying: $2x^2 + 3x + 1 = A(x^2+1) + (Bx + C)(x-1)$

$= (A+B)x^2 + (-B+C)x + (A-C)$

Compare coefficients:

$x^2$: $A + B = 2$
$x$: $-B + C = 3$
Constant: $A - C = 1$

Solving: $A=3$, $B=-1$, $C=2$

$$\frac{2x^2+3x+1}{(x-1)(x^2+1)} = \frac{3}{x-1} - \frac{x}{x^2+1} + \frac{2}{x^2+1}$$

Integrate:

$$\int \frac{3}{x-1}\,dx = 3\ln|x-1|$$

$$\int \frac{x}{x^2+1}\,dx = \frac{1}{2}\ln(x^2+1)$$

$$\int \frac{2}{x^2+1}\,dx = 2\tan^{-1}x$$

Answer: $3\ln|x-1| - \frac{1}{2}\ln(x^2+1) + 2\tan^{-1}x + C$

**M1** — Correct partial fraction form
**A1** — Correct coefficients $A=3$, $B=-1$, $C=2$
**M1** — Separate into standard integrals
**A1** — Correct $\ln$ terms
**A1** — Correct $\tan^{-1}$ term
</details>
