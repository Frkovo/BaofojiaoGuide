---
title: 题型分析
sidebar_position: 4
---

# 题型分析 — Circular Motion

## Type 1：水平圆周运动

> **Example 1:** A particle of mass 0.5 kg is attached to one end of a light inextensible string of length 0.8 m. The other end is fixed. The particle moves in a horizontal circle with constant speed, making 3 revolutions per second. Find the tension in the string and the angle it makes with the vertical.

<details>
<summary>📝 MS 展开查看</summary>

Angular speed: $\omega = 3 \times 2\pi = 6\pi\ \text{rad}\,\text{s}^{-1}$ **M1 A1**

Let $\theta$ be angle with vertical.
Radius of circle: $r = 0.8\sin\theta$ **M1**

Vertical: $T\cos\theta = mg = 0.5 \times 9.8 = 4.9$ **(1)** **M1 A1**
Horizontal: $T\sin\theta = m\omega^2 r = 0.5 \times (6\pi)^2 \times 0.8\sin\theta$ **(2)** **M1**

From (2): $T\sin\theta = 0.5 \times 36\pi^2 \times 0.8\sin\theta$
$T = 14.4\pi^2 = 142.1\ \text{N}$ (if $\sin\theta \neq 0$) **A1**

From (1): $\cos\theta = \frac{4.9}{142.1} = 0.03448$
$\theta = 88.0^\circ$ (3 s.f.) **M1 A1**

[Total: 10]
</details>

> **Example 2:** A car of mass 1200 kg travels around a banked track of radius 50 m at a constant speed. The track is banked at an angle $\theta$ such that there is no lateral friction at a speed of $15\ \text{m}\,\text{s}^{-1}$. Find $\theta$.

<details>
<summary>📝 MS 展开查看</summary>

No lateral friction $\Rightarrow$ reaction force $R$ is perpendicular to track. **B1**

Horizontal (centripetal): $R\sin\theta = m\frac{v^2}{r}$ **M1**
Vertical: $R\cos\theta = mg$ **M1**

Divide: $\tan\theta = \frac{v^2}{rg}$ **M1**

$\tan\theta = \frac{15^2}{50 \times 9.8} = \frac{225}{490} = 0.4592$ **A1**

$\theta = 24.7^\circ$ (3 s.f.) **A1**

[Total: 6]
</details>

> **Example 3:** A conical pendulum consists of a particle of mass 0.2 kg attached to a fixed point by a light string of length 1.2 m. The particle moves in a horizontal circle with angular speed $\omega$. Given that the tension in the string is 3 N, find $\omega$ and the angle the string makes with the vertical.

<details>
<summary>📝 MS 展开查看</summary>

Let $\theta$ be angle with vertical.
Vertical: $T\cos\theta = mg \Rightarrow \cos\theta = \frac{0.2 \times 9.8}{3} = \frac{1.96}{3} = 0.6533$ **M1 A1**
$\theta = 49.2^\circ$ (3 s.f.) **A1**

Radius: $r = 1.2\sin\theta = 1.2\sin 49.2^\circ = 1.2 \times 0.7571 = 0.9085\ \text{m}$ **M1 A1**

Horizontal: $T\sin\theta = m\omega^2 r$
$3\sin 49.2^\circ = 0.2 \times \omega^2 \times 0.9085$ **M1**
$3 \times 0.7571 = 0.1817\omega^2$
$2.271 = 0.1817\omega^2$
$\omega^2 = 12.50 \Rightarrow \omega = 3.54\ \text{rad}\,\text{s}^{-1}$ (3 s.f.) **A1**

[Total: 8]
</details>

## Type 2：竖直圆周运动

> **Example 1:** A particle of mass 0.3 kg is attached to a light rod of length 0.6 m and rotates in a vertical circle. At the lowest point, the speed is $5\ \text{m}\,\text{s}^{-1}$. Find the tension in the rod at the lowest point and at the highest point.

<details>
<summary>📝 MS 展开查看</summary>

At lowest point:
$T_L - mg = m\frac{v_L^2}{r}$ **M1**
$T_L = 0.3 \times 9.8 + 0.3 \times \frac{5^2}{0.6}$ **M1**
$T_L = 2.94 + 12.5 = 15.44\ \text{N}$ **A1**

Energy conservation to find speed at highest point:
$\frac{1}{2}mv_L^2 = \frac{1}{2}mv_H^2 + 2mgr$ **M1**
$\frac{1}{2} \times 5^2 = \frac{1}{2}v_H^2 + 2 \times 9.8 \times 0.6$
$12.5 = \frac{1}{2}v_H^2 + 11.76$
$\frac{1}{2}v_H^2 = 0.74 \Rightarrow v_H^2 = 1.48$ **A1**

At highest point:
$T_H + mg = m\frac{v_H^2}{r}$ **M1**
$T_H + 2.94 = 0.3 \times \frac{1.48}{0.6} = 0.74$
$T_H = -2.2\ \text{N}$ (negative means rod is in compression) **A1**

[Total: 8]
</details>

> **Example 2:** A bead slides on a smooth circular wire of radius 0.5 m fixed in a vertical plane. The bead is released from rest at a point A, where the radius makes an angle of $60^\circ$ with the downward vertical. Find the speed of the bead at the lowest point and the reaction of the wire at that point.

<details>
<summary>📝 MS 展开查看</summary>

Energy conservation: $\frac{1}{2}mv^2 = mg(r - r\cos 60^\circ) = mgr(1 - \cos 60^\circ)$ **M1 M1**

$v^2 = 2gr(1 - \cos 60^\circ) = 2 \times 9.8 \times 0.5 \times (1 - 0.5)$ **M1**
$v^2 = 9.8 \times 0.5 = 4.9$
$v = 2.21\ \text{m}\,\text{s}^{-1}$ (3 s.f.) **A1**

At lowest point:
$R - mg = m\frac{v^2}{r}$ **M1**
$R = m\left(g + \frac{v^2}{r}\right) = m\left(9.8 + \frac{4.9}{0.5}\right) = m(9.8 + 9.8) = 19.6m\ \text{N}$ **A1**

[Total: 6]
</details>

> **Example 3:** A particle P of mass 0.4 kg is attached to one end of a light inextensible string of length 0.8 m. The other end is fixed. P is held at the same height as the fixed point with the string taut, then released. Find the speed of P when the string makes an angle of $30^\circ$ with the vertical, and the tension in the string at that instant.

<details>
<summary>📝 MS 展开查看</summary>

Initial: height above lowest point $= 0.8\ \text{m}$ (horizontal). **B1**

When string is at $30^\circ$ to vertical, drop in height:
$h = 0.8 - 0.8\cos 30^\circ = 0.8(1 - \cos 30^\circ) = 0.8(1 - 0.8660) = 0.1072\ \text{m}$ **M1 A1**

Energy: $\frac{1}{2}mv^2 = mgh$
$v^2 = 2 \times 9.8 \times 0.1072 = 2.101$ **M1**
$v = 1.45\ \text{m}\,\text{s}^{-1}$ (3 s.f.) **A1**

Tension: $T - mg\cos 30^\circ = m\frac{v^2}{r}$ **M1**
$T = 0.4 \times 9.8 \times 0.8660 + 0.4 \times \frac{2.101}{0.8}$ **M1**
$T = 3.395 + 1.051 = 4.45\ \text{N}$ (3 s.f.) **A1**

[Total: 9]
</details>

## Type 3：完成竖直圆周的条件

> **Example 1:** A particle is attached to a light rod of length $L$ and rotates in a vertical circle. Find the minimum speed at the lowest point needed for the particle to complete the circle.

<details>
<summary>📝 MS 展开查看</summary>

For complete circle, the particle must reach the highest point.

At highest point, minimum speed $v_H \to 0$ (for a rod, it can support compression). **M1**

Energy: $\frac{1}{2}mv_L^2 = \frac{1}{2}mv_H^2 + 2mgL$ **M1**
With $v_H = 0$:
$\frac{1}{2}mv_L^2 = 2mgL$ **M1**
$v_L^2 = 4gL$
$v_L = 2\sqrt{gL}$ **A1**

[Total: 4]
</details>

> **Example 2:** A particle is attached to a light inextensible string of length $L$ and rotates in a vertical circle. Find the minimum speed at the lowest point for the particle to complete the circle.

<details>
<summary>📝 MS 展开查看</summary>

For a string, the particle must have $v_H \geq \sqrt{gL}$ at the highest point to maintain tension. **M1**

Energy: $\frac{1}{2}mv_L^2 = \frac{1}{2}mv_H^2 + 2mgL$ **M1**

With $v_H^2 = gL$:
$\frac{1}{2}mv_L^2 = \frac{1}{2}m(gL) + 2mgL$ **M1**
$v_L^2 = gL + 4gL = 5gL$
$v_L = \sqrt{5gL}$ **A1**

[Total: 4]
</details>

> **Example 3:** A bead of mass 0.2 kg slides on a smooth circular wire of radius 0.3 m fixed in a vertical plane. It is projected from the lowest point with speed $v$. Find the minimum $v$ for the bead to reach the highest point.

<details>
<summary>📝 MS 展开查看</summary>

For a bead on a wire, the bead can reach the highest point even at $v_H = 0$ (the wire provides support). **B1**

Energy: $\frac{1}{2}mv^2 = \frac{1}{2}mv_H^2 + mg \times 2r$ **M1**

With $v_H = 0$:
$\frac{1}{2}mv^2 = mg \times 2 \times 0.3$
$v^2 = 4 \times 9.8 \times 0.3 = 11.76$ **M1**
$v = 3.43\ \text{m}\,\text{s}^{-1}$ (3 s.f.) **A1**

[Total: 4]
</details>
