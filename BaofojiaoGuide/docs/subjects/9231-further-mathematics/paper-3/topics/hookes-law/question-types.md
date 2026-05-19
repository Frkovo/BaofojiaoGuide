---
title: 题型分析
sidebar_position: 4
---

# 题型分析 — Hooke's Law

## Type 1：弹性绳静态平衡

> **Example 1:** A light elastic string of natural length 0.5 m and modulus of elasticity $\lambda = 30\ \text{N}$ has one end fixed. A particle of mass 0.6 kg is attached to the other end and hangs in equilibrium. Find the extension of the string.

<details>
<summary>📝 MS 展开查看</summary>

Equilibrium: tension = weight **M1**
$T = mg = 0.6 \times 9.8 = 5.88\ \text{N}$ **A1**

Hooke's Law: $T = \frac{\lambda x}{L}$ **M1**
$5.88 = \frac{30x}{0.5}$
$x = \frac{5.88 \times 0.5}{30} = \frac{2.94}{30} = 0.098\ \text{m}$ **A1**

Extension $= 0.098\ \text{m}$ (or 9.8 cm) **A1**

[Total: 5]
</details>

> **Example 2:** An elastic string of natural length 2 m and modulus 40 N is stretched between two fixed points A and B, 3 m apart horizontally. A particle of mass 0.4 kg is attached to the midpoint of the string and hangs in equilibrium. Find the depth of the particle below AB.

<details>
<summary>📝 MS 展开查看</summary>

Let depth $= d$, half-length $= \sqrt{1.5^2 + d^2}$.

Extension of each half: $x = \sqrt{1.5^2 + d^2} - 1$ **M1 A1**

Tension in each half: $T = \frac{40x}{2} = \frac{40(\sqrt{2.25 + d^2} - 1)}{2} = 20(\sqrt{2.25 + d^2} - 1)$ **M1**

Vertical equilibrium: $2T\sin\theta = mg$, where $\sin\theta = \frac{d}{\sqrt{2.25 + d^2}}$ **M1**

$2 \times 20(\sqrt{2.25 + d^2} - 1) \times \frac{d}{\sqrt{2.25 + d^2}} = 0.4 \times 9.8$ **M1**

$40d\left(1 - \frac{1}{\sqrt{2.25 + d^2}}\right) = 3.92$

$d\left(1 - \frac{1}{\sqrt{2.25 + d^2}}\right) = 0.098$

Solve: $d = 0.45\ \text{m}$ (by trial or quadratic) **A1**

[Total: 7]
</details>

> **Example 3:** A light spring of natural length 0.3 m and modulus 25 N is attached to a fixed point. A particle of mass 0.8 kg is attached to the other end and is held at the same level as the fixed point with the spring unstretched. The particle is released. Find the maximum extension of the spring.

<details>
<summary>📝 MS 展开查看</summary>

Energy conservation: loss in GPE = gain in EPE **M1**

Let $x$ = maximum extension. The particle falls through distance $x$.

$mgx = \frac{\lambda x^2}{2L}$ **M1 M1**

$0.8 \times 9.8 \times x = \frac{25x^2}{2 \times 0.3}$

$7.84x = \frac{25x^2}{0.6}$ **M1**

$7.84x = 41.67x^2$

Either $x = 0$ (initial) or $x = \frac{7.84}{41.67} = 0.188\ \text{m}$ **A1**

Maximum extension $= 0.188\ \text{m}$ (3 s.f.) **A1**

[Total: 6]
</details>

## Type 2：能量法

> **Example 1:** An elastic string of natural length 1.2 m and modulus 50 N has one end fixed. A particle of mass 0.5 kg is attached to the other end and released from rest at the fixed point. Find the speed of the particle when the string is stretched to a length of 1.5 m.

<details>
<summary>📝 MS 展开查看</summary>

Extension $x = 1.5 - 1.2 = 0.3\ \text{m}$ **B1**

Energy conservation: loss in GPE = gain in KE + gain in EPE **M1**

$mgh = \frac{1}{2}mv^2 + \frac{\lambda x^2}{2L}$ **M1**

Here $h = 1.5\ \text{m}$ (distance fallen).

$0.5 \times 9.8 \times 1.5 = \frac{1}{2} \times 0.5 \times v^2 + \frac{50 \times 0.3^2}{2 \times 1.2}$ **M1**

$7.35 = 0.25v^2 + \frac{50 \times 0.09}{2.4}$
$7.35 = 0.25v^2 + 1.875$ **A1**

$0.25v^2 = 5.475$
$v^2 = 21.9$
$v = 4.68\ \text{m}\,\text{s}^{-1}$ (3 s.f.) **A1**

[Total: 7]
</details>

> **Example 2:** A particle of mass 0.3 kg is attached to one end of an elastic string of natural length 0.8 m and modulus 20 N. The other end is fixed. The particle is projected vertically downwards from the fixed point with speed $3\ \text{m}\,\text{s}^{-1}$. Find the greatest extension of the string.

<details>
<summary>📝 MS 展开查看</summary>

Let $x$ = greatest extension.

Energy: initial KE + initial GPE = final EPE + final GPE **M1**

Initial GPE at fixed point: 0 (reference level). **B1**

Final GPE at lowest point: $-mg(0.8 + x)$ **M1**

$\frac{1}{2}mv^2 + 0 = \frac{\lambda x^2}{2L} - mg(0.8 + x)$ **M1**

$\frac{1}{2} \times 0.3 \times 9 = \frac{20x^2}{2 \times 0.8} - 0.3 \times 9.8(0.8 + x)$ **M1**

$1.35 = \frac{20x^2}{1.6} - 2.352 - 2.94x$
$1.35 = 12.5x^2 - 2.352 - 2.94x$

$12.5x^2 - 2.94x - 3.702 = 0$ **A1**

$x = \frac{2.94 \pm \sqrt{2.94^2 + 4 \times 12.5 \times 3.702}}{2 \times 12.5}$
$x = \frac{2.94 \pm \sqrt{8.644 + 185.1}}{25}$
$x = \frac{2.94 \pm \sqrt{193.7}}{25} = \frac{2.94 \pm 13.92}{25}$ **M1**

$x = 0.674\ \text{m}$ (positive root) **A1**

[Total: 9]
</details>

> **Example 3:** A particle of mass $m$ is attached to the midpoint of an elastic string of natural length $2L$ and modulus $2\lambda$. The ends of the string are fixed at two points A and B at the same horizontal level, distance $2L$ apart. The particle is pulled down vertically and released. Show that the maximum speed occurs when the particle is at a depth $d = L\sqrt{\frac{mg}{2\lambda}}$ below AB.

<details>
<summary>📝 MS 展开查看</summary>

Let depth $= d$. Each half length $= \sqrt{L^2 + d^2}$, extension $x = \sqrt{L^2 + d^2} - L$ per half. **M1**

Total EPE: $2 \times \frac{2\lambda x^2}{2 \times L} = \frac{2\lambda x^2}{L}$ **M1**

Energy conservation: $\frac{2\lambda}{L}(\sqrt{L^2 + d^2} - L)^2 + \frac{1}{2}mv^2 = \text{constant} - mgd$ **M1**

Differentiate wrt $d$ and set $dv/dd = 0$ for max speed:
$\frac{d}{dd}(\text{EPE} + mgd) = 0$ at maximum speed (since KE is max when $\frac{d}{dd}(\text{total mechanical energy}) = 0$). **M1**

$\frac{d}{dd}\left[\frac{2\lambda}{L}(\sqrt{L^2 + d^2} - L)^2 + mgd\right] = 0$ **M1**

$\frac{2\lambda}{L} \cdot 2(\sqrt{L^2 + d^2} - L) \cdot \frac{d}{\sqrt{L^2 + d^2}} + mg = 0$

$\frac{4\lambda d}{L\sqrt{L^2 + d^2}}(\sqrt{L^2 + d^2} - L) + mg = 0$ **A1**

At small $d$ approximation, or for maximum speed:
$\frac{4\lambda d}{L} \cdot \frac{d}{2L} \approx mg$ (using $\sqrt{L^2 + d^2} \approx L + \frac{d^2}{2L}$)

$\frac{2\lambda d^2}{L^2} = mg \Rightarrow d = L\sqrt{\frac{mg}{2\lambda}}$ **A1**

[Total: 8]
</details>

## Type 3：弹性绳与斜面

> **Example 1:** A particle of mass 0.5 kg is on a rough inclined plane at $30^\circ$ to the horizontal. It is attached to one end of an elastic string of natural length 0.6 m and modulus 15 N, with the other end fixed at the top of the plane. The coefficient of friction is 0.2. Find the equilibrium extension.

<details>
<summary>📝 MS 展开查看</summary>

Forces down the plane: $mg\sin 30^\circ - F$ (if about to move up) **B1**

Normal reaction: $R = mg\cos 30^\circ = 0.5 \times 9.8 \times 0.8660 = 4.243\ \text{N}$ **M1 A1**

Friction: $F = \mu R = 0.2 \times 4.243 = 0.8486\ \text{N}$ **M1 A1**

Equilibrium (acting up the plane): $T = mg\sin 30^\circ - F$ (if particle would slide down without string) **M1**
$T = 0.5 \times 9.8 \times 0.5 - 0.8486$
$T = 2.45 - 0.8486 = 1.601\ \text{N}$ **A1**

Hooke's Law: $T = \frac{15x}{0.6}$
$x = \frac{1.601 \times 0.6}{15} = \frac{0.9606}{15} = 0.0640\ \text{m}$ **A1**

[Total: 9]
</details>

> **Example 2:** A particle of mass $m$ is on a smooth inclined plane at angle $\theta$ to the horizontal. An elastic string of natural length $L$ and modulus $\lambda$ connects the particle to the top of the plane. The particle is held at the top with the string unstretched and released. Show that the maximum speed occurs when $x = \frac{mgL\sin\theta}{\lambda}$.

<details>
<summary>📝 MS 展开查看</summary>

Let $x$ be extension down the plane.
Energy: $\frac{1}{2}mv^2 = mgx\sin\theta - \frac{\lambda x^2}{2L}$ **M1 M1**

For maximum speed, $\frac{d}{dx}(v^2) = 0$:
$\frac{d}{dx}\left(2gx\sin\theta - \frac{\lambda x^2}{mL}\right) = 0$ **M1**

$2g\sin\theta - \frac{2\lambda x}{mL} = 0$ **M1**

$x = \frac{mgL\sin\theta}{\lambda}$ **A1**

[Total: 5]
</details>

> **Example 3:** A particle P of mass 0.2 kg is attached to one end of a light elastic string of natural length 0.5 m and modulus 8 N. The other end is fixed at point O. P is held at O and released. Find the speed of P when it has fallen 0.8 m.

<details>
<summary>📝 MS 展开查看</summary>

After falling 0.8 m: string is taut if $0.8 > 0.5$, so extension $x = 0.8 - 0.5 = 0.3\ \text{m}$. **B1**

Energy: loss in GPE = gain in KE + gain in EPE **M1**

$mgh = \frac{1}{2}mv^2 + \frac{\lambda x^2}{2L}$ **M1**

$0.2 \times 9.8 \times 0.8 = \frac{1}{2} \times 0.2 \times v^2 + \frac{8 \times 0.3^2}{2 \times 0.5}$ **M1**

$1.568 = 0.1v^2 + \frac{8 \times 0.09}{1.0}$
$1.568 = 0.1v^2 + 0.72$ **A1**

$0.1v^2 = 0.848$
$v^2 = 8.48$
$v = 2.91\ \text{m}\,\text{s}^{-1}$ (3 s.f.) **A1**

[Total: 7]
</details>
