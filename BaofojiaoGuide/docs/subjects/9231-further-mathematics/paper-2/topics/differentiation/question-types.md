---
title: 题型分析
sidebar_position: 3
---

# 题型分析 — Differentiation

---

## Question Type 1: Differentiating inverse trig/hyperbolic functions

### 必须记忆的导数

| $f(x)$ | $f'(x)$ | 易错成 |
|--------|---------|--------|
| $\sin^{-1} x$ | $\dfrac{1}{\sqrt{1-x^2}}$ | — |
| $\cos^{-1} x$ | $-\dfrac{1}{\sqrt{1-x^2}}$ | $+\dfrac{1}{\sqrt{1-x^2}}$ ✗ |
| $\tan^{-1} x$ | $\dfrac{1}{1+x^2}$ | — |
| $\sinh^{-1} x$ | $\dfrac{1}{\sqrt{1+x^2}}$ | $\dfrac{1}{\sqrt{x^2-1}}$ ✗ |
| $\cosh^{-1} x$ | $\dfrac{1}{\sqrt{x^2-1}}$ | $\dfrac{1}{\sqrt{1+x^2}}$ ✗ |
| $\tanh^{-1} x$ | $\dfrac{1}{1-x^2}$ | $\dfrac{1}{1+x^2}$ ✗ |
| $\sinh x$ | $\cosh x$ | — |
| $\cosh x$ | $\sinh x$ | $-\sinh x$ ✗ |

:::warning[常见陷阱]

- $\dfrac{d}{dx}\cos^{-1}x = -\dfrac{1}{\sqrt{1-x^2}}$（**负号！**）
- $\dfrac{d}{dx}\tanh^{-1}x = \dfrac{1}{1-x^2}$，不是 $\dfrac{1}{1+x^2}$（$\dfrac{1}{1+x^2}$ 是 $\tan^{-1}x$）
- 别忘了链式法则：$\dfrac{d}{dx}\sinh^{-1}(2x) = \dfrac{2}{\sqrt{1+4x^2}}$

:::

### 完整原题

**Example 1 — 标准题型：直接求导**

> Differentiate $\sinh^{-1}(2x)$ with respect to $x$.

**解题：** $\frac{d}{dx}\sinh^{-1}(2x) = \frac{1}{\sqrt{1+(2x)^2}} \cdot 2 = \frac{2}{\sqrt{1+4x^2}}$

**Example 2 — 标准题型：链式法则**

> Find $\frac{dy}{dx}$ where $y = \cos^{-1}(x^3)$.

**解题：** $\frac{dy}{dx} = -\frac{1}{\sqrt{1-(x^3)^2}} \cdot 3x^2 = -\frac{3x^2}{\sqrt{1-x^6}}$

**Example 3 — 标准题型：乘积 + 反函数**

> Differentiate $x^2\sinh^{-1}x$.

**解题：** $\frac{d}{dx}[x^2\sinh^{-1}x] = 2x\sinh^{-1}x + x^2\cdot\frac{1}{\sqrt{1+x^2}}$

---

## Question Type 2: Implicit differentiation

### 标准方法

1. 两边对 $x$ 求导
2. 牢记：$\dfrac{d}{dx}(y) = \dfrac{dy}{dx}$，$\dfrac{d}{dx}(y^2) = 2y\dfrac{dy}{dx}$，$\dfrac{d}{dx}(xy) = y + x\dfrac{dy}{dx}$
3. 把所有 $\dfrac{dy}{dx}$ 项移到一边，提出并解出
4. 代已知点坐标
5. 求 $\dfrac{d^2y}{dx^2}$：对 $\dfrac{dy}{dx}$ 表达式再隐函数微分

### 完整原题

**Example 1 — 9231/w20/qp/22 Q5 (8 marks):**

> $y^2 + (xy+1)^2 = 5$，求 $(1,1)$ 处的 $\dfrac{dy}{dx}$ 和 $\dfrac{d^2y}{dx^2}$。

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **B1**: $2y\frac{dy}{dx} + 2(xy+1)(y + x\frac{dy}{dx}) = 0$
- **B1**: substitutes $(1,1)$
- **B1**: $6\frac{dy}{dx} = -4$ → $-\frac{2}{3}$ AG

**MS (b):**
- **A1**: $\frac{d^2y}{dx^2} = \frac{19}{27}$

</details>

**Example 2 — 9231/w22/qp/22 Q2 (6 marks):**

> 曲线方程为 $(x+1)y + y^2 = 2$。
> (a) 证明在 $(0,-2)$ 处 $\dfrac{dy}{dx} = -\dfrac{2}{3}$。 [3]
> (b) 求 $(0,-2)$ 处 $\dfrac{d^2y}{dx^2}$ 的值。 [3]

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **B1**: $(x+1)\frac{dy}{dx} + y + 2y\frac{dy}{dx} = 0$
- **B1**: substitutes $(0,-2)$
- **B1**: $\frac{dy}{dx} - 2 - 4\frac{dy}{dx} = 0$ → $-3\frac{dy}{dx}=2$ → $-\frac{2}{3}$ AG

**MS (b):**
- **B1**: differentiates again
- **M1**: substitutes $x=0,y=-2,\frac{dy}{dx}=-\frac{2}{3}$
- **A1**: $\frac{d^2y}{dx^2} = -\frac{10}{27}$

</details>

---

## Question Type 3: Parametric differentiation

### 公式

$$
\frac{dy}{dx} = \frac{dy/dt}{dx/dt},\qquad
\frac{d^2y}{dx^2} = \frac{d}{dt}\left(\frac{dy}{dx}\right) \bigg/ \frac{dx}{dt}
$$

:::danger[最常见的错误]

$\displaystyle\frac{d^2y}{dx^2} \neq \frac{d^2y/dt^2}{d^2x/dt^2}$！

:::

### 完整原题

**Example 1 — 9231/w23/qp/22 Q2 (7 marks):**

> $x = 1 + \dfrac{1}{t}$，$y = te^t$。(a) Show $\dfrac{dy}{dx} = -e^t(t^3 + t^2)$。(b) Find $\dfrac{d^2y}{dx^2}$.

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **M1**: $\frac{dx}{dt} = -\frac{1}{t^2}$, $\frac{dy}{dt} = e^t + te^t = e^t(1+t)$
- **M1**: $\frac{dy}{dx} = \frac{e^t(1+t)}{-1/t^2} = -e^t t^2(1+t)$
- **A1**: $= -e^t(t^3+t^2)$ AG

**MS (b):**
- **M1**: $\frac{d}{dt}(\frac{dy}{dx}) = -[e^t(t^3+t^2) + e^t(3t^2+2t)]$
- **M1**: $= -e^t(t^3+4t^2+2t)$
- **M1**: $\frac{d^2y}{dx^2} = \frac{-e^t(t^3+4t^2+2t)}{-1/t^2}$
- **A1**: $= e^t t^2(t^3+4t^2+2t) = e^t(t^5+4t^4+2t^3)$

</details>

**Example 2 — 9231/s24/qp/22 Q3 (7 marks):**

> $x = \sin^{-1} t$，$y = t\cos^{-1} t$。(a) Show $\dfrac{dy}{dx} = -t + \sqrt{1-t^2}\cos^{-1} t$。(b) Find $\dfrac{d^2y}{dx^2}$.

<details>
<summary>📝 MS 展开查看</summary>

**MS (a):**
- **M1**: $\frac{dx}{dt} = \frac{1}{\sqrt{1-t^2}}$, $\frac{dy}{dt} = \cos^{-1}t - \frac{t}{\sqrt{1-t^2}}$
- **M1**: $\frac{dy}{dx} = \frac{dy}{dt} / \frac{dx}{dt} = \sqrt{1-t^2}\cos^{-1}t - t$
- **A1**: AG

**MS (b):**
- **M1**: differentiate $\frac{dy}{dx}$ wrt $t$
- **M1**: divide by $\frac{dx}{dt}$
- **A1**: correct $\frac{d^2y}{dx^2}$

</details>

---

## Question Type 4: Maclaurin series expansion

### 公式

$$
f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots
$$

### 标准方法

1. 计算 $f(0)$
2. 逐次求导，每次在 $x=0$ 取值
3. 代入公式，化简系数

### 完整原题

**Example 1 — 9231/w20/qp/22 Q1 (5 marks):**

> Find the Maclaurin series for $\tan\left(\dfrac{\pi}{4} + x\right)$ up to $x^2$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: $f(0)=1$
- **M1**: $f'(x)$ correct
- **M1**: $f'(0)=2$
- **M1**: $f''(0)=4$
- **A1**: $1+2x+2x^2$

</details>

**Example 2 — 9231/s24/qp/22 Q2 (4 marks):**

> Find the Maclaurin series for $e^{1+x^2} + e^{1-x}$ up to and including the term in $x^2$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: $e^{1+x^2} = e \cdot e^{x^2} = e(1+x^2+\frac{x^4}{2!}+\cdots)$
- **M1**: $e^{1-x} = e \cdot e^{-x} = e(1-x+\frac{x^2}{2!}-\frac{x^3}{3!}+\cdots)$
- **M1**: adds, keeping only terms up to $x^2$
- **A1**: $f(x) = 2e - ex + \frac{3e}{2}x^2 + \cdots$

</details>

**Example 3 — 9231/w23/qp/22 Q1 (5 marks):**

> Find the Maclaurin series for $\ln(x+2) + \ln(x^2+5)$ up to and including the term in $x^2$.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **M1**: $\ln(x+2) = \ln2 + \ln(1+\frac{x}{2})$
- **M1**: $\ln(x^2+5) = \ln5 + \ln(1+\frac{x^2}{5})$
- **M1**: expands $\ln(1+u) = u - \frac{u^2}{2} + \cdots$ for both
- **A1**: $\ln2+\ln5 + \frac{x}{2} - \frac{x^2}{8} + \frac{x^2}{5} + \cdots$
- **A1**: $= \ln10 + \frac{x}{2} + \frac{3x^2}{40} + \cdots$

</details>

:::warning[常见陷阱]

- 导数在 $x=0$ 取值，不是在原来的 $x$ 处
- 别忘了阶乘分母：$\dfrac{f''(0)}{2!}x^2$，不是 $f''(0)x^2$
- 系数要化简：$\dfrac{4}{2!} = 2$

:::
