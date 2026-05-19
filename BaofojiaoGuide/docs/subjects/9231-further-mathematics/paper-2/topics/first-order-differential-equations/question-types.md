---
title: 题型分析
sidebar_position: 4
---

# 题型分析 — First Order Differential Equations

## Type 1：积分因子法

> **Example 1 (s20/21 Q1):** Solve $\frac{dy}{dx} + 5y = e^{-7x}$, given that $y = 0$ when $x = 0$.

<details>
<summary>📝 MS 展开查看</summary>

$P(x) = 5$, $Q(x) = e^{-7x}$ **B1**

Integrating factor: $I = e^{\int 5\,dx} = e^{5x}$ **M1**

Multiply both sides:
$e^{5x}\frac{dy}{dx} + 5e^{5x}y = e^{5x}e^{-7x} = e^{-2x}$

LHS = $\frac{d}{dx}(ye^{5x})$ **M1**

$\frac{d}{dx}(ye^{5x}) = e^{-2x}$

$ye^{5x} = \int e^{-2x}\,dx = -\frac{1}{2}e^{-2x} + C$ **A1**

$y = -\frac{1}{2}e^{-7x} + Ce^{-5x}$

Using $y(0) = 0$: $0 = -\frac{1}{2} + C \Rightarrow C = \frac{1}{2}$ **M1**

$y = \frac{1}{2}(e^{-5x} - e^{-7x})$ **A1**

[Total: 6]
</details>

> **Example 2 (w20/22 Q4):** Solve $x\frac{dy}{dx} + 2y = e^x$, given that $y = 3$ when $x = 1$.

<details>
<summary>📝 MS 展开查看</summary>

Rewrite in standard form:
$\frac{dy}{dx} + \frac{2}{x}y = \frac{e^x}{x}$ **M1**

$P(x) = \frac{2}{x}$, $Q(x) = \frac{e^x}{x}$ **B1**

$I = e^{\int \frac{2}{x}\,dx} = e^{2\ln x} = x^2$ **M1**

Multiply: $x^2\frac{dy}{dx} + 2xy = xe^x$

LHS = $\frac{d}{dx}(x^2 y)$ **M1**

$x^2 y = \int xe^x\,dx$

Integration by parts: $\int xe^x\,dx = xe^x - e^x + C$ **M1**

$x^2 y = xe^x - e^x + C$

$y = \frac{e^x(x - 1)}{x^2} + \frac{C}{x^2}$ **A1**

Using $y(1) = 3$: $3 = \frac{e(0)}{1} + C \Rightarrow C = 3$ **M1**

$y = \frac{e^x(x - 1)}{x^2} + \frac{3}{x^2}$ **A1**

[Total: 8]
</details>

> **Example 3 (s20/23 Q7):** Solve $(x^2+1)\frac{dy}{dx} + y\sqrt{x^2+1} = x^2 - x\sqrt{x^2+1}$.

<details>
<summary>📝 MS 展开查看</summary>

Rewrite in standard form:
$\frac{dy}{dx} + \frac{\sqrt{x^2+1}}{x^2+1}y = \frac{x^2 - x\sqrt{x^2+1}}{x^2+1}$ **M1**

$P(x) = \frac{1}{\sqrt{x^2+1}}$ (since $\frac{\sqrt{x^2+1}}{x^2+1} = \frac{1}{\sqrt{x^2+1}}$) **A1**

$I = e^{\int \frac{1}{\sqrt{x^2+1}}\,dx} = e^{\sinh^{-1}x}$ **M1 A1**

Note: $e^{\sinh^{-1}x} = x + \sqrt{x^2+1}$ **B1**

Multiply: $(x+\sqrt{x^2+1})\frac{dy}{dx} + \frac{x+\sqrt{x^2+1}}{\sqrt{x^2+1}}y = \frac{x+\sqrt{x^2+1}}{x^2+1}(x^2 - x\sqrt{x^2+1})$

LHS = $\frac{d}{dx}[(x+\sqrt{x^2+1})y]$ **M1**

RHS simplifies to $\frac{x^2}{x+\sqrt{x^2+1}} - x$ **A1**

$(x+\sqrt{x^2+1})y = \int \left(\frac{x^2}{x+\sqrt{x^2+1}} - x\right)dx = \cdots$

$(x+\sqrt{x^2+1})y = x - \ln|x+\sqrt{x^2+1}| + C$ **A1**

$y = \frac{x - \ln(x+\sqrt{x^2+1}) + C}{x+\sqrt{x^2+1}}$ **A1**

[Total: 11]
</details>

> **Example 4 (w21/21 Q7):** Find the integrating factor for $\frac{dy}{dx} + \frac{x}{\sqrt{x^2-1}}\,y = \frac{1}{\sqrt{x^2-1}}$, and hence solve for $y$.

<details>
<summary>📝 MS 展开查看</summary>

$P(x) = \frac{x}{\sqrt{x^2-1}}$ **B1**

$I = e^{\int \frac{x}{\sqrt{x^2-1}}\,dx}$ **M1**

Let $u = x^2-1$, $du = 2x\,dx$

$\int \frac{x}{\sqrt{x^2-1}}\,dx = \frac{1}{2}\int u^{-1/2}\,du = \sqrt{x^2-1}$ **A1**

$I = e^{\sqrt{x^2-1}}$ **A1**

[4 marks for IF]

Multiplying: $\frac{d}{dx}(ye^{\sqrt{x^2-1}}) = \frac{e^{\sqrt{x^2-1}}}{\sqrt{x^2-1}}$ **M1**

$ye^{\sqrt{x^2-1}} = \int \frac{e^{\sqrt{x^2-1}}}{\sqrt{x^2-1}}\,dx$

Let $u = \sqrt{x^2-1}$, then $du = \frac{x}{\sqrt{x^2-1}}\,dx$ ... alternative approach needed.

Alternatively, note IF can be written as $x + \sqrt{x^2-1}$ since:

$e^{\sqrt{x^2-1}} = x + \sqrt{x^2-1}$ can be verified by squaring. **B1**

$\frac{d}{dx}[(x+\sqrt{x^2-1})y] = \frac{x+\sqrt{x^2-1}}{\sqrt{x^2-1}}$ **M1**

$(x+\sqrt{x^2-1})y = \int \frac{x}{\sqrt{x^2-1}} + 1\,dx$

$= \sqrt{x^2-1} + x + C$ **A1**

$y = \frac{\sqrt{x^2-1} + x + C}{x+\sqrt{x^2-1}}$ **A1**

[Total: 4+7]
</details>

> **Example 5 (w22/21 Q8):** Solve $\frac{dy}{d\theta} + y\cot\theta = \cos\theta$.

<details>
<summary>📝 MS 展开查看</summary>

$P(\theta) = \cot\theta$, $Q(\theta) = \cos\theta$ **B1**

$I = e^{\int \cot\theta\,d\theta} = e^{\ln\sin\theta} = \sin\theta$ **M1 A1**

Multiply: $\sin\theta\frac{dy}{d\theta} + y\cos\theta = \sin\theta\cos\theta$

LHS = $\frac{d}{dx}(y\sin\theta)$ **M1**

$\frac{d}{dx}(y\sin\theta) = \frac{1}{2}\sin 2\theta$

$y\sin\theta = \frac{1}{2}\int \sin 2\theta\,d\theta = -\frac{1}{4}\cos 2\theta + C$ **M1 A1**

$y\sin\theta = -\frac{1}{4}(1 - 2\sin^2\theta) + C = \frac{1}{2}\sin^2\theta - \frac{1}{4} + C$ **M1**

$y = \frac{1}{2}\sin\theta - \frac{1}{4}\csc\theta + C\csc\theta$ **A1**

Alternatively: $y = \frac{1}{2}\sin\theta + K\csc\theta$ where $K = C - \frac{1}{4}$ **A1**

[Total: 11]
</details>

> **Example 6 (s25/21 Q7):** Solve $\frac{dy}{dx} + \frac{x+5}{x^2+10x+61}\,y = \frac{1}{x^2+10x+61}$.

<details>
<summary>📝 MS 展开查看</summary>

$P(x) = \frac{x+5}{x^2+10x+61}$ **B1**

Complete square: $x^2+10x+61 = (x+5)^2 + 36$ **M1**

$I = e^{\int \frac{x+5}{(x+5)^2+36}\,dx}$ **M1**

Let $u = (x+5)^2$, $du = 2(x+5)dx$

$\int \frac{x+5}{(x+5)^2+36}\,dx = \frac{1}{2}\ln[(x+5)^2 + 36]$ **A1**

$I = e^{\frac{1}{2}\ln[(x+5)^2+36]} = \sqrt{x^2+10x+61}$ **A1**

Multiply: $\sqrt{x^2+10x+61}\frac{dy}{dx} + \frac{x+5}{\sqrt{x^2+10x+61}}y = \frac{1}{\sqrt{x^2+10x+61}}$

LHS = $\frac{d}{dx}(y\sqrt{x^2+10x+61})$ **M1**

$y\sqrt{x^2+10x+61} = \int \frac{1}{\sqrt{x^2+10x+61}}\,dx$

$= \int \frac{1}{\sqrt{(x+5)^2+36}}\,dx = \sinh^{-1}\left(\frac{x+5}{6}\right) + C$ **M1 A1**

$y = \frac{\sinh^{-1}\left(\frac{x+5}{6}\right) + C}{\sqrt{x^2+10x+61}}$ **A1**

[Total: 10]
</details>

## Type 2：可分离变量方程

> **Example 1:** Solve $\frac{dy}{dx} = \frac{x}{y}$, given $y(1) = 2$.

<details>
<summary>📝 MS 展开查看</summary>

Separate variables: $y\,dy = x\,dx$ **M1**

$\int y\,dy = \int x\,dx$ **M1**

$\frac{1}{2}y^2 = \frac{1}{2}x^2 + C$ **A1**

$y^2 = x^2 + 2C$

$y^2 - x^2 = K$ where $K = 2C$

Using $y(1) = 2$: $4 - 1 = 3 = K$ **M1**

$y^2 - x^2 = 3$ **A1**

$y = \pm\sqrt{x^2 + 3}$

Since $y(1) = 2 &gt; 0$: $y = \sqrt{x^2 + 3}$ **A1**

[Total: 6]
</details>

> **Example 2:** Solve $\frac{dy}{dx} = xy^2$, given $y(0) = \frac{1}{2}$.

<details>
<summary>📝 MS 展开查看</summary>

Separate: $y^{-2}\,dy = x\,dx$ **M1**

$\int y^{-2}\,dy = \int x\,dx$

$-y^{-1} = \frac{1}{2}x^2 + C$ **A1**

$y = -\frac{1}{\frac{1}{2}x^2 + C}$ **M1**

Using $y(0) = \frac{1}{2}$: $\frac{1}{2} = -\frac{1}{C} \Rightarrow C = -2$ **M1**

$y = -\frac{1}{\frac{1}{2}x^2 - 2} = \frac{2}{4 - x^2}$ **A1**

[Total: 5]
</details>

## Type 3：初值问题

> **Example 1:** Solve the initial value problem $x\frac{dy}{dx} + y = x^3$, $y(1) = 2$.

<details>
<summary>📝 MS 展开查看</summary>

Standard form: $\frac{dy}{dx} + \frac{1}{x}y = x^2$ **M1**

$P(x) = \frac{1}{x}$, $Q(x) = x^2$ **B1**

$I = e^{\int \frac{1}{x}\,dx} = e^{\ln x} = x$ **M1**

$\frac{d}{dx}(xy) = x \cdot x^2 = x^3$ **M1**

$xy = \int x^3\,dx = \frac{x^4}{4} + C$ **A1**

$y = \frac{x^3}{4} + \frac{C}{x}$

Using $y(1) = 2$: $2 = \frac{1}{4} + C \Rightarrow C = \frac{7}{4}$ **M1**

$y = \frac{x^3}{4} + \frac{7}{4x}$ **A1**

[Total: 7]
</details>
