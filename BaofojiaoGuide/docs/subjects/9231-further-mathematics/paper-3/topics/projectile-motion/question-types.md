---
title: 题型分析
sidebar_position: 4
---

# 题型分析 — Projectile Motion

## Type 1：已知初速度和角度，求特定时刻或位置的参数

> **Example 1:** A particle is projected from point O with speed $20\ \text{m}\,\text{s}^{-1}$ at an angle of $30^\circ$ above the horizontal. Find:
> (i) the time taken to reach the highest point,
> (ii) the maximum height reached,
> (iii) the horizontal range.

<details>
<summary>📝 MS 展开查看</summary>

**M1** for resolving initial velocity:

$u_x = 20\cos 30^\circ = 10\sqrt{3}\ \text{m}\,\text{s}^{-1}$ **A1**
$u_y = 20\sin 30^\circ = 10\ \text{m}\,\text{s}^{-1}$ **A1**

(i) At highest point $v_y = 0$:
$0 = 10 - 9.8t$ **M1**
$t = \frac{10}{9.8} = 1.02\ \text{s}$ (3 s.f.) **A1**

(ii) $H = 10 \times 1.02 - \frac{1}{2} \times 9.8 \times 1.02^2$ **M1**
$H = 5.10\ \text{m}$ (3 s.f.) **A1**

(iii) Time of flight $T = 2 \times 1.02 = 2.04\ \text{s}$ **B1**
$R = 10\sqrt{3} \times 2.04 = 35.3\ \text{m}$ (3 s.f.) **M1 A1**

[Total: 9]
</details>

> **Example 2:** A particle P is projected from a point O with speed $25\ \text{m}\,\text{s}^{-1}$ at an angle $\alpha$ above the horizontal, where $\sin\alpha = \frac{3}{5}$ and $\cos\alpha = \frac{4}{5}$. Find the speed and direction of P when $t = 2$ seconds.

<details>
<summary>📝 MS 展开查看</summary>

$u_x = 25 \times \frac{4}{5} = 20\ \text{m}\,\text{s}^{-1}$ **B1**
$u_y = 25 \times \frac{3}{5} = 15\ \text{m}\,\text{s}^{-1}$ **B1**

$v_x = 20\ \text{m}\,\text{s}^{-1}$ (constant) **B1**
$v_y = 15 - 9.8 \times 2 = -4.6\ \text{m}\,\text{s}^{-1}$ **M1 A1**

Speed $v = \sqrt{20^2 + (-4.6)^2} = \sqrt{400 + 21.16} = 20.5\ \text{m}\,\text{s}^{-1}$ (3 s.f.) **M1 A1**

Direction: $\tan\theta = \frac{4.6}{20} \Rightarrow \theta = 13.0^\circ$ below horizontal **M1 A1**

[Total: 9]
</details>

> **Example 3:** A ball is projected from ground level with speed $u$ at an angle $\theta$ to the horizontal. At time $t = 1.5$ seconds, the ball is at point $(18, 6)$. Find $u$ and $\theta$.

<details>
<summary>📝 MS 展开查看</summary>

$x = u\cos\theta \cdot t$: $18 = u\cos\theta \times 1.5$ **M1**
$u\cos\theta = 12$ ... (1) **A1**

$y = u\sin\theta \cdot t - \frac{1}{2}gt^2$: $6 = u\sin\theta \times 1.5 - \frac{1}{2} \times 9.8 \times 1.5^2$ **M1**
$6 = 1.5u\sin\theta - 11.025$
$u\sin\theta = 11.35$ ... (2) **A1**

(2)/(1): $\tan\theta = \frac{11.35}{12} = 0.9458$ **M1**
$\theta = 43.4^\circ$ (3 s.f.) **A1**

$u = \frac{12}{\cos 43.4^\circ} = 16.5\ \text{m}\,\text{s}^{-1}$ (3 s.f.) **M1 A1**

[Total: 8]
</details>

## Type 2：轨迹方程推导与应用

> **Example 1:** A particle is projected with speed $V$ at an angle $\theta$ to the horizontal. Show that the equation of the trajectory is $y = x\tan\theta - \frac{gx^2}{2V^2\cos^2\theta}$.

<details>
<summary>📝 MS 展开查看</summary>

$x = V\cos\theta \cdot t \Rightarrow t = \frac{x}{V\cos\theta}$ **M1**

$y = V\sin\theta \cdot t - \frac{1}{2}gt^2$ **M1**

Substitute $t$:
$y = V\sin\theta \cdot \frac{x}{V\cos\theta} - \frac{1}{2}g\left(\frac{x}{V\cos\theta}\right)^2$ **M1**

$y = x\tan\theta - \frac{gx^2}{2V^2\cos^2\theta}$ **A1**

[Total: 4]
</details>

> **Example 2:** A ball is thrown with speed $14\ \text{m}\,\text{s}^{-1}$ at an angle $\theta$ above the horizontal. The ball passes through a point $(8, 3.5)$. Find the two possible values of $\theta$.

<details>
<summary>📝 MS 展开查看</summary>

Trajectory: $y = x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$ **B1**

Using $1/\cos^2\theta = 1 + \tan^2\theta$:
$y = x\tan\theta - \frac{gx^2}{2u^2}(1 + \tan^2\theta)$ **M1**

Substitute $x = 8$, $y = 3.5$, $u = 14$, $g = 9.8$:
$3.5 = 8\tan\theta - \frac{9.8 \times 64}{2 \times 196}(1 + \tan^2\theta)$ **M1**
$3.5 = 8\tan\theta - \frac{627.2}{392}(1 + \tan^2\theta)$
$3.5 = 8\tan\theta - 1.6(1 + \tan^2\theta)$ **A1**

$3.5 = 8\tan\theta - 1.6 - 1.6\tan^2\theta$
$1.6\tan^2\theta - 8\tan\theta + 5.1 = 0$ **M1**

Solve quadratic: $\tan\theta = \frac{8 \pm \sqrt{64 - 4 \times 1.6 \times 5.1}}{2 \times 1.6}$ **M1**
$\tan\theta = \frac{8 \pm 5.36}{3.2}$
$\tan\theta = 4.175$ or $0.825$ **A1**
$\theta = 76.5^\circ$ or $39.5^\circ$ (3 s.f.) **A1**

[Total: 9]
</details>

> **Example 3:** A projectile is fired from the origin with speed $V$ at an angle $\alpha$ to the horizontal. It passes through the point $(a, b)$. Show that $V^2 = \frac{ga^2}{2(a\tan\alpha - b)\cos^2\alpha}$.

<details>
<summary>📝 MS 展开查看</summary>

Trajectory: $y = x\tan\alpha - \frac{gx^2}{2V^2\cos^2\alpha}$ **B1**

Substitute $(a, b)$:
$b = a\tan\alpha - \frac{ga^2}{2V^2\cos^2\alpha}$ **M1**

Rearrange:
$\frac{ga^2}{2V^2\cos^2\alpha} = a\tan\alpha - b$ **M1**

$2V^2\cos^2\alpha(a\tan\alpha - b) = ga^2$ **M1**

$V^2 = \frac{ga^2}{2(a\tan\alpha - b)\cos^2\alpha}$ **A1**

[Total: 5]
</details>

## Type 3：斜面抛体

> **Example 1:** A particle is projected from a point O on a plane inclined at $20^\circ$ to the horizontal. The initial speed is $15\ \text{m}\,\text{s}^{-1}$ at an angle of $45^\circ$ to the horizontal. Find the distance from O to where the particle lands on the plane.

<details>
<summary>📝 MS 展开查看</summary>

Set axes: $x$ along plane, $y$ perpendicular to plane.

$g_x = -g\sin 20^\circ = -3.352\ \text{m}\,\text{s}^{-2}$ **M1**
$g_y = -g\cos 20^\circ = -9.210\ \text{m}\,\text{s}^{-2}$ **M1**

Initial velocity components:
$u_x = 15\cos(45^\circ - 20^\circ) = 15\cos 25^\circ = 13.59\ \text{m}\,\text{s}^{-1}$ **A1**
$u_y = 15\sin(45^\circ - 20^\circ) = 15\sin 25^\circ = 6.339\ \text{m}\,\text{s}^{-1}$ **A1**

Time of flight (when $y = 0$):
$0 = 6.339t - \frac{1}{2} \times 9.210 \times t^2$ **M1**
$t(6.339 - 4.605t) = 0$
$t = \frac{6.339}{4.605} = 1.377\ \text{s}$ (ignore $t = 0$) **A1**

Distance along plane:
$s_x = 13.59 \times 1.377 + \frac{1}{2} \times (-3.352) \times 1.377^2$ **M1**
$s_x = 18.71 - 3.177 = 15.5\ \text{m}$ (3 s.f.) **A1**

[Total: 8]
</details>

> **Example 2:** A ball is struck from a point O on a slope inclined at $15^\circ$ to the horizontal. The ball is projected with speed $12\ \text{m}\,\text{s}^{-1}$ at an angle $\beta$ to the slope. Find the maximum perpendicular height of the ball above the slope.

<details>
<summary>📝 MS 展开查看</summary>

Perpendicular component: $u_\perp = 12\sin\beta$ **B1**
Perpendicular acceleration: $g_\perp = g\cos 15^\circ = 9.467\ \text{m}\,\text{s}^{-2}$ **M1**

At max perpendicular height, $v_\perp = 0$:
$0 = (12\sin\beta)^2 - 2 \times 9.467 \times H_\perp$ **M1**

$H_\perp = \frac{144\sin^2\beta}{2 \times 9.467} = 7.60\sin^2\beta\ \text{m}$ **A1**

[Total: 4]
</details>

> **Example 3:** A particle is projected from a point on a horizontal plane with speed $u$ at an angle $\theta$ to the horizontal. The particle strikes a plane inclined at $30^\circ$ to the horizontal passing through the point of projection. Given that the particle strikes the inclined plane at right angles, find $\tan\theta$.

<details>
<summary>📝 MS 展开查看</summary>

Let $P = (X, Y)$ be the point of impact on the plane.
$Y = X\tan 30^\circ = X/\sqrt{3}$ **B1**

Impact at right angles: velocity is perpendicular to the plane.
Slope of plane $= \tan 30^\circ$, so velocity gradient $= -\cot 30^\circ = -\sqrt{3}$ **M1**
$\frac{v_y}{v_x} = -\sqrt{3}$ **M1**

$v_x = u\cos\theta$
$v_y = u\sin\theta - gt$
$\frac{u\sin\theta - gt}{u\cos\theta} = -\sqrt{3}$ ... (1) **A1**

Trajectory: $Y = X\tan\theta - \frac{gX^2}{2u^2\cos^2\theta}$ ... (2) **M1**

Time to reach $X$: $X = u\cos\theta \cdot t \Rightarrow t = \frac{X}{u\cos\theta}$

Sub into (1):
$\frac{u\sin\theta - g\frac{X}{u\cos\theta}}{u\cos\theta} = -\sqrt{3}$
$u\sin\theta - \frac{gX}{u\cos\theta} = -\sqrt{3}u\cos\theta$ **M1**

From (2) with $Y = X/\sqrt{3}$:
$\frac{X}{\sqrt{3}} = X\tan\theta - \frac{gX^2}{2u^2\cos^2\theta}$
Divide by $X$:
$\frac{1}{\sqrt{3}} = \tan\theta - \frac{gX}{2u^2\cos^2\theta}$ ... (3) **A1**

From (1) rearranged:
$\frac{gX}{u\cos\theta} = u\sin\theta + \sqrt{3}u\cos\theta$
$\frac{gX}{u^2\cos^2\theta} = \tan\theta + \sqrt{3}$ **A1**

Sub into (3):
$\frac{1}{\sqrt{3}} = \tan\theta - \frac{1}{2}(\tan\theta + \sqrt{3})$ **M1**
$\frac{1}{\sqrt{3}} = \tan\theta - \frac{1}{2}\tan\theta - \frac{\sqrt{3}}{2}$
$\frac{1}{\sqrt{3}} = \frac{1}{2}\tan\theta - \frac{\sqrt{3}}{2}$
$\frac{2}{\sqrt{3}} + \sqrt{3} = \tan\theta$
$\tan\theta = \frac{2}{\sqrt{3}} + \sqrt{3} = \frac{5}{\sqrt{3}}$ **A1**

[Total: 11]
</details>
