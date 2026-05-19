---
title: 题型分析
sidebar_position: 4
---

# 题型分析 — Linear Motion Under Variable Force

## Type 1：建立与求解微分方程

> **Example 1:** A particle of mass 0.5 kg moves in a straight line under the action of a force $F = 2 - 0.5v$ N, where $v$ is the speed. Initially the particle is at rest. Find an expression for $v$ in terms of $t$.

<details>
<summary>📝 MS 展开查看</summary>

$F = ma = m\frac{dv}{dt}$ **B1**

$0.5\frac{dv}{dt} = 2 - 0.5v$ **M1**

$\frac{dv}{dt} = 4 - v$

$\int \frac{1}{4 - v} dv = \int 1 dt$ **M1**

$-\ln|4 - v| = t + C$ **A1**

When $t = 0$, $v = 0$: $-\ln 4 = C$ **M1**

$-\ln(4 - v) = t - \ln 4$
$\ln(4 - v) = \ln 4 - t$
$4 - v = 4e^{-t}$ **M1**
$v = 4(1 - e^{-t})$ **A1**

[Total: 8]
</details>

> **Example 2:** A body of mass 2 kg moves under a force $F = 6 - 3x$ N, where $x$ is displacement from a fixed point O. When $x = 0$, velocity $v = 0$. Find $v$ as a function of $x$.

<details>
<summary>📝 MS 展开查看</summary>

$F = m\frac{dv}{dt} = mv\frac{dv}{dx}$ **M1**

$2v\frac{dv}{dx} = 6 - 3x$ **M1**

$\int 2v dv = \int (6 - 3x) dx$ **M1**

$v^2 = 6x - \frac{3}{2}x^2 + C$ **A1**

When $x = 0$, $v = 0 \Rightarrow C = 0$ **M1**

$v^2 = 6x - \frac{3}{2}x^2$
$v = \sqrt{6x - 1.5x^2}$ **A1**

[Total: 6]
</details>

> **Example 3:** A particle of mass $m$ moves along the $x$-axis under a force directed towards O of magnitude $\frac{mk}{x^3}$, where $k$ is a constant. Initially the particle is at $x = a$ with speed $v_0$ towards O. Find the speed when $x = a/2$.

<details>
<summary>📝 MS 展开查看</summary>

Force towards O: $F = -\frac{mk}{x^3}$ (negative since towards O) **M1**

$mv\frac{dv}{dx} = -\frac{mk}{x^3}$ **M1**

$\int v dv = -\int \frac{k}{x^3} dx$ **M1**

$\frac{1}{2}v^2 = \frac{k}{2x^2} + C$ **A1**

When $x = a$, $v = v_0$:
$\frac{1}{2}v_0^2 = \frac{k}{2a^2} + C \Rightarrow C = \frac{1}{2}v_0^2 - \frac{k}{2a^2}$ **M1**

When $x = a/2$:
$\frac{1}{2}v^2 = \frac{k}{2(a/2)^2} + \frac{1}{2}v_0^2 - \frac{k}{2a^2}$
$\frac{1}{2}v^2 = \frac{2k}{a^2} + \frac{1}{2}v_0^2 - \frac{k}{2a^2}$ **M1**
$\frac{1}{2}v^2 = \frac{1}{2}v_0^2 + \frac{3k}{2a^2}$
$v^2 = v_0^2 + \frac{3k}{a^2}$
$v = \sqrt{v_0^2 + \frac{3k}{a^2}}$ **A1**

[Total: 8]
</details>

## Type 2：空气阻力（$kv$ 形式）

> **Example 1:** A particle of mass 0.1 kg falls from rest under gravity, with air resistance proportional to velocity: $R = 0.2v$ N. Find the terminal velocity and the velocity after 2 seconds.

<details>
<summary>📝 MS 展开查看</summary>

$m\frac{dv}{dt} = mg - kv$, where $k = 0.2$ **M1**

Terminal velocity $v_T$: when $mg = kv$ **M1**
$0.1 \times 9.8 = 0.2v_T$
$v_T = \frac{0.98}{0.2} = 4.9\ \text{m}\,\text{s}^{-1}$ **A1**

$0.1\frac{dv}{dt} = 0.98 - 0.2v$
$\frac{dv}{dt} = 9.8 - 2v$

$\int \frac{dv}{9.8 - 2v} = \int dt$ **M1**

$-\frac{1}{2}\ln|9.8 - 2v| = t + C$ **A1**

At $t = 0$, $v = 0$: $-\frac{1}{2}\ln 9.8 = C$

$-\frac{1}{2}\ln(9.8 - 2v) = t - \frac{1}{2}\ln 9.8$
$\ln(9.8 - 2v) = -2t + \ln 9.8$
$9.8 - 2v = 9.8e^{-2t}$
$v = \frac{9.8}{2}(1 - e^{-2t})$ **M1**

At $t = 2$: $v = 4.9(1 - e^{-4}) = 4.9(1 - 0.0183) = 4.81\ \text{m}\,\text{s}^{-1}$ **A1**

[Total: 9]
</details>

> **Example 2:** A boat of mass 500 kg is moving at $8\ \text{m}\,\text{s}^{-1}$ when its engine is cut. The resistance is $50v$ N. Find the time taken for the speed to halve.

<details>
<summary>📝 MS 展开查看</summary>

$m\frac{dv}{dt} = -kv$, where $k = 50$ **M1**

$500\frac{dv}{dt} = -50v$
$\frac{dv}{dt} = -0.1v$ **A1**

$\int \frac{dv}{v} = -\int 0.1 dt$ **M1**

$\ln v = -0.1t + C$ **A1**

At $t = 0$, $v = 8$: $\ln 8 = C$

$\ln v = -0.1t + \ln 8$
$\ln\left(\frac{v}{8}\right) = -0.1t$ **M1**

When $v = 4$: $\ln(0.5) = -0.1t$
$t = -10\ln(0.5) = 10\ln 2 = 6.93\ \text{s}$ (3 s.f.) **A1**

[Total: 7]
</details>

> **Example 3:** A particle of mass $m$ is projected vertically upwards with speed $u$ in a medium where the resistance is $mkv$. Find the maximum height reached.

<details>
<summary>📝 MS 展开查看</summary>

Equation of motion (upward positive): $-mg - mkv = m\frac{dv}{dt}$ **M1**

Using $a = v\frac{dv}{dx}$: $v\frac{dv}{dx} = -g - kv$ **M1**

$v\frac{dv}{dx} = -(g + kv)$

$\frac{v}{g + kv} dv = -dx$ **M1**

$\int \frac{v}{g + kv} dv = -\int dx$

Rewrite: $\frac{v}{g + kv} = \frac{1}{k} - \frac{g}{k(g + kv)}$ **M1**

$\int \left(\frac{1}{k} - \frac{g}{k(g + kv)}\right) dv = -\int dx$

$\frac{v}{k} - \frac{g}{k^2}\ln(g + kv) = -x + C$ **A1**

When $x = 0$, $v = u$:
$C = \frac{u}{k} - \frac{g}{k^2}\ln(g + ku)$ **M1**

At max height, $v = 0$:
$0 - \frac{g}{k^2}\ln g = -H + \frac{u}{k} - \frac{g}{k^2}\ln(g + ku)$

$H = \frac{u}{k} - \frac{g}{k^2}\ln\left(\frac{g + ku}{g}\right)$ **A1**

[Total: 9]
</details>

## Type 3：空气阻力（$kv^2$ 形式）

> **Example 1:** A particle falls from rest under gravity with air resistance $0.5v^2$ N per unit mass. Find the terminal velocity and the velocity after falling a distance $x$.

<details>
<summary>📝 MS 展开查看</summary>

Per unit mass: $\frac{dv}{dt} = g - 0.5v^2$ **M1**

Terminal velocity: $g = 0.5v_T^2 \Rightarrow v_T = \sqrt{2g} = \sqrt{19.6} = 4.43\ \text{m}\,\text{s}^{-1}$ **M1 A1**

Using $v\frac{dv}{dx} = g - 0.5v^2$ **M1**

$\int \frac{v}{g - 0.5v^2} dv = \int dx$ **M1**

$-\ln(g - 0.5v^2) = x + C$ (up to constant factor) **A1**

At $x = 0$, $v = 0$: $-\ln g = C$

$-\ln(g - 0.5v^2) = x - \ln g$
$\ln\left(\frac{g}{g - 0.5v^2}\right) = x$
$g - 0.5v^2 = ge^{-x}$
$v^2 = 2g(1 - e^{-x})$
$v = \sqrt{2g(1 - e^{-x})}$ **A1**

[Total: 7]
</details>

> **Example 2:** A projectile of mass $m$ is fired vertically upwards with speed $u$ in a medium where resistance is $mkv^2$. Show that the time to reach the highest point is $\frac{1}{\sqrt{kg}}\tan^{-1}\left(u\sqrt{\frac{k}{g}}\right)$.

<details>
<summary>📝 MS 展开查看</summary>

Upward motion: $m\frac{dv}{dt} = -mg - mkv^2$ **M1**
$\frac{dv}{dt} = -g - kv^2$

$\int \frac{dv}{g + kv^2} = -\int dt$ **M1**

$\frac{1}{\sqrt{kg}}\tan^{-1}\left(v\sqrt{\frac{k}{g}}\right) = -t + C$ **A1**

At $t = 0$, $v = u$:
$C = \frac{1}{\sqrt{kg}}\tan^{-1}\left(u\sqrt{\frac{k}{g}}\right)$ **M1**

At highest point, $v = 0$:
$0 = -t + \frac{1}{\sqrt{kg}}\tan^{-1}\left(u\sqrt{\frac{k}{g}}\right)$ **M1**

$t = \frac{1}{\sqrt{kg}}\tan^{-1}\left(u\sqrt{\frac{k}{g}}\right)$ **A1**

[Total: 6]
</details>

> **Example 3:** A particle moves in a straight line under a force $F = -kv^2$ (retarding force). Initially $v = V$. Find the distance travelled before the speed reduces to $V/2$.

<details>
<summary>📝 MS 展开查看</summary>

$m\frac{dv}{dt} = -kv^2$ **M1**

Using $a = v\frac{dv}{dx}$: $mv\frac{dv}{dx} = -kv^2$ **M1**

$\int \frac{m}{v} dv = -\int k dx$ **M1**

$m\ln v = -kx + C$ **A1**

At $x = 0$, $v = V$: $C = m\ln V$

$m\ln v = -kx + m\ln V$
$\ln\left(\frac{v}{V}\right) = -\frac{kx}{m}$ **M1**

When $v = V/2$:
$\ln\left(\frac{1}{2}\right) = -\frac{kx}{m}$
$x = \frac{m\ln 2}{k}$ **A1**

[Total: 6]
</details>
