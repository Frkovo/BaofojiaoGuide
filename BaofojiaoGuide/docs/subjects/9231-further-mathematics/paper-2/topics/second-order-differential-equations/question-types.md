---
title: 题型分析
sidebar_position: 4
---

# 题型分析 — Second Order Differential Equations

## Type 1：常系数 ODE

> **Example 1 (w20/21 Q2):** Solve $9\frac{d^2y}{dx^2} + 6\frac{dy}{dx} + y = 3x^2 + 30x$.

<details>
<summary>📝 MS 展开查看</summary>

Auxiliary equation: $9m^2 + 6m + 1 = 0$ **M1**

$(3m + 1)^2 = 0 \Rightarrow m = -\frac{1}{3}$ (repeated) **A1**

CF: $y_c = (A + Bx)e^{-x/3}$ **A1**

For PI, try $y_p = \alpha x^2 + \beta x + \gamma$ **M1**

$y_p' = 2\alpha x + \beta$, $y_p'' = 2\alpha$

Substitute:

$9(2\alpha) + 6(2\alpha x + \beta) + (\alpha x^2 + \beta x + \gamma) = 3x^2 + 30x$

$\alpha x^2 + (12\alpha + \beta)x + (18\alpha + 6\beta + \gamma) = 3x^2 + 30x$ **M1**

Comparing coefficients:

$x^2$: $\alpha = 3$

$x$: $12\alpha + \beta = 30 \Rightarrow 36 + \beta = 30 \Rightarrow \beta = -6$

Const: $18\alpha + 6\beta + \gamma = 0 \Rightarrow 54 - 36 + \gamma = 0 \Rightarrow \gamma = -18$ **A1**

$y_p = 3x^2 - 6x - 18$

General solution: $y = (A + Bx)e^{-x/3} + 3x^2 - 6x - 18$ **A1**

[Total: 6+1]
</details>

> **Example 2 (s21/21 Q2):** Solve $\frac{d^2y}{dx^2} + 3\frac{dy}{dx} + 2y = 2x + 1$.

<details>
<summary>📝 MS 展开查看</summary>

AE: $m^2 + 3m + 2 = 0$ **M1**

$(m+1)(m+2) = 0 \Rightarrow m = -1, -2$ **A1**

CF: $y_c = Ae^{-x} + Be^{-2x}$ **A1**

PI: try $y_p = \alpha x + \beta$ **M1**

$y_p' = \alpha$, $y_p'' = 0$

$0 + 3\alpha + 2(\alpha x + \beta) = 2x + 1$

$2\alpha x + (3\alpha + 2\beta) = 2x + 1$ **M1**

$x$: $2\alpha = 2 \Rightarrow \alpha = 1$

Const: $3\alpha + 2\beta = 1 \Rightarrow 3 + 2\beta = 1 \Rightarrow \beta = -1$ **A1**

$y_p = x - 1$

General solution: $y = Ae^{-x} + Be^{-2x} + x - 1$ **A1**

[Total: 6+1]
</details>

> **Example 3 (s20/23 Q1):** Solve $\frac{d^2x}{dt^2} - 8\frac{dx}{dt} - 9x = 9e^{8t}$.

<details>
<summary>📝 MS 展开查看</summary>

AE: $m^2 - 8m - 9 = 0$ **M1**

$(m - 9)(m + 1) = 0 \Rightarrow m = 9, -1$ **A1**

CF: $x_c = Ae^{9t} + Be^{-t}$ **A1**

PI: try $x_p = Ce^{8t}$ **M1**

$\dot{x}_p = 8Ce^{8t}$, $\ddot{x}_p = 64Ce^{8t}$

Sub: $64Ce^{8t} - 8(8Ce^{8t}) - 9Ce^{8t} = 9e^{8t}$

$(64 - 64 - 9)C = 9$

$-9C = 9 \Rightarrow C = -1$ **A1**

$x_p = -e^{8t}$

General solution: $x = Ae^{9t} + Be^{-t} - e^{8t}$ **A1**

[Total: 6]
</details>

> **Example 4 (w20/22 Q6):** Solve $\frac{d^2x}{dt^2} + 8\frac{dx}{dt} + 15x = 102\cos 3t$.

<details>
<summary>📝 MS 展开查看</summary>

AE: $m^2 + 8m + 15 = 0$ **M1**

$(m+3)(m+5) = 0 \Rightarrow m = -3, -5$ **A1**

CF: $x_c = Ae^{-3t} + Be^{-5t}$ **A1**

PI: try $x_p = C\cos 3t + D\sin 3t$ **M1**

$\dot{x}_p = -3C\sin 3t + 3D\cos 3t$

$\ddot{x}_p = -9C\cos 3t - 9D\sin 3t$

Sub:

$(-9C\cos 3t - 9D\sin 3t) + 8(-3C\sin 3t + 3D\cos 3t) + 15(C\cos 3t + D\sin 3t)$

$= 102\cos 3t$ **M1**

$\cos 3t$: $-9C + 24D + 15C = 6C + 24D = 102$

$\sin 3t$: $-9D - 24C + 15D = 6D - 24C = 0$ **M1**

From $\sin 3t$: $6D = 24C \Rightarrow D = 4C$

From $\cos 3t$: $6C + 24(4C) = 6C + 96C = 102C = 102 \Rightarrow C = 1$ **A1**

$D = 4$

$x_p = \cos 3t + 4\sin 3t$ **A1**

General solution: $x = Ae^{-3t} + Be^{-5t} + \cos 3t + 4\sin 3t$ **A1**

[Total: 11]
</details>

> **Example 5 (s25/21 Q5):** Solve $6\frac{d^2x}{dt^2} + 3\frac{dx}{dt} + 6x = e^{-t}$.

<details>
<summary>📝 MS 展开查看</summary>

AE: $6m^2 + 3m + 6 = 0$ **M1**

$2m^2 + m + 2 = 0$

$m = \frac{-1 \pm \sqrt{1 - 16}}{4} = \frac{-1 \pm i\sqrt{15}}{4}$ **A1**

CF: $x_c = e^{-t/4}\left(A\cos\frac{\sqrt{15}}{4}t + B\sin\frac{\sqrt{15}}{4}t\right)$ **A1**

PI: try $x_p = Ce^{-t}$ **M1**

$\dot{x}_p = -Ce^{-t}$, $\ddot{x}_p = Ce^{-t}$

Sub: $6(Ce^{-t}) + 3(-Ce^{-t}) + 6(Ce^{-t}) = e^{-t}$

$(6 - 3 + 6)C = 1 \Rightarrow 9C = 1 \Rightarrow C = \frac{1}{9}$ **A1**

$x_p = \frac{1}{9}e^{-t}$

General solution: $x = e^{-t/4}\left(A\cos\frac{\sqrt{15}}{4}t + B\sin\frac{\sqrt{15}}{4}t\right) + \frac{1}{9}e^{-t}$ **A1**

[Total: 10]
</details>

## Type 2：Euler-Cauchy 方程

> **Example 1 (s20/21 Q7):** By using the substitution $x = t^3y$, transform $t^3\frac{d^2y}{dt^2} + \cdots$ into a constant coefficient equation.

<details>
<summary>📝 MS 展开查看</summary>

Given $x = t^3y$, we have $y = xt^{-3}$.

First, express derivatives:

$y = t^{-3}x$

$\frac{dy}{dt} = -3t^{-4}x + t^{-3}\frac{dx}{dt}$ **M1**

$\frac{d^2y}{dt^2} = 12t^{-5}x - 6t^{-4}\frac{dx}{dt} + t^{-3}\frac{d^2x}{dt^2}$ **M1**

Substitute into original ODE and simplify.

The substitution transforms it into a constant coefficient equation in $x$:

$\frac{d^2x}{dt^2} + P\frac{dx}{dt} + Qx = R(t)$ **A1**

(Continued with solving the transformed equation...) **M1 A1**

[Total: 4+7]
</details>

> **Example 2:** Solve the Euler-Cauchy equation $t^2\frac{d^2y}{dt^2} - 2t\frac{dy}{dt} + 2y = t^3$.

<details>
<summary>📝 MS 展开查看</summary>

This is an Euler-Cauchy equation of the form $at^2y'' + bty' + cy = f(t)$.

Use substitution $t = e^u$ or try $y = t^m$.

For homogeneous: $t^2y'' - 2ty' + 2y = 0$

Try $y = t^m$: $t^2(m(m-1)t^{m-2}) - 2t(mt^{m-1}) + 2t^m = 0$

$m(m-1) - 2m + 2 = 0$

$m^2 - 3m + 2 = 0$ **M1**

$(m-1)(m-2) = 0 \Rightarrow m = 1, 2$ **A1**

CF: $y_c = At + Bt^2$ **A1**

For PI with RHS $t^3$, try $y_p = Ct^3$ **M1**

$y_p' = 3Ct^2$, $y_p'' = 6Ct$

Sub: $t^2(6Ct) - 2t(3Ct^2) + 2(Ct^3) = t^3$

$6Ct^3 - 6Ct^3 + 2Ct^3 = 2Ct^3 = t^3$ **M1**

$2C = 1 \Rightarrow C = \frac{1}{2}$ **A1**

$y_p = \frac{1}{2}t^3$

General solution: $y = At + Bt^2 + \frac{1}{2}t^3$ **A1**

[Total: 8]
</details>

> **Example 3:** Solve $t^2\frac{d^2y}{dt^2} + t\frac{dy}{dt} + y = \ln t$.

<details>
<summary>📝 MS 展开查看</summary>

Euler-Cauchy with $a=1, b=1, c=1$.

Try $y = t^m$: $m(m-1) + m + 1 = 0$

$m^2 + 1 = 0 \Rightarrow m = \pm i$ **M1 A1**

CF: $y_c = A\cos(\ln t) + B\sin(\ln t)$ **A1**

For PI, use substitution $t = e^u$, so $u = \ln t$.

$\frac{dy}{dt} = \frac{dy}{du}\cdot\frac{1}{t}$, $\frac{d^2y}{dt^2} = \frac{1}{t^2}\left(\frac{d^2y}{du^2} - \frac{dy}{du}\right)$ **M1**

$\frac{d^2y}{du^2} + y = u$ **M1**

AE: $m^2 + 1 = 0 \Rightarrow m = \pm i$

CF (in $u$): $y_c = A\cos u + B\sin u$ **A1**

PI (in $u$): try $y_p = \alpha u$

$0 + \alpha u = u \Rightarrow \alpha = 1$

$y_p = u = \ln t$ **A1**

General solution: $y = A\cos(\ln t) + B\sin(\ln t) + \ln t$ **A1**

[Total: 9]
</details>

## Type 3：耦合系统（拓展）

> **Example 1:** Solve the coupled system $\frac{dx}{dt} = 3x + 4y$, $\frac{dy}{dt} = 2x + y$.

<details>
<summary>📝 MS 展开查看</summary>

Matrix form: $\begin{pmatrix}\dot{x} \\ \dot{y}\end{pmatrix} = \begin{pmatrix}3 & 4 \\ 2 & 1\end{pmatrix}\begin{pmatrix}x \\ y\end{pmatrix}$ **B1**

Find eigenvalues of $A = \begin{pmatrix}3 & 4 \\ 2 & 1\end{pmatrix}$:

$\det(A - \lambda I) = (3-\lambda)(1-\lambda) - 8 = 0$

$\lambda^2 - 4\lambda - 5 = 0 \Rightarrow \lambda = 5, -1$ **M1 A1**

For $\lambda = 5$: $\begin{pmatrix}-2 & 4 \\ 2 & -4\end{pmatrix}\begin{pmatrix}a \\ b\end{pmatrix} = 0 \Rightarrow a = 2b$, eigenvector $\begin{pmatrix}2 \\ 1\end{pmatrix}$ **M1**

For $\lambda = -1$: $\begin{pmatrix}4 & 4 \\ 2 & 2\end{pmatrix}\begin{pmatrix}a \\ b\end{pmatrix} = 0 \Rightarrow a = -b$, eigenvector $\begin{pmatrix}1 \\ -1\end{pmatrix}$ **M1**

General solution:

$\begin{pmatrix}x \\ y\end{pmatrix} = C_1\begin{pmatrix}2 \\ 1\end{pmatrix}e^{5t} + C_2\begin{pmatrix}1 \\ -1\end{pmatrix}e^{-t}$ **A1**

$x = 2C_1e^{5t} + C_2e^{-t}$
$y = C_1e^{5t} - C_2e^{-t}$

[Total: 8]
</details>
