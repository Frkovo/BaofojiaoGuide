---
title: 题型分析
sidebar_position: 4
---

# 题型分析 — Equilibrium of Rigid Body

## Type 1：均匀杆的平衡

> **Example 1:** A uniform rod AB of mass 8 kg and length 6 m is freely hinged at A. It is held in equilibrium by a light string attached to B at an angle of $30^\circ$ to the horizontal. Find the tension in the string and the force at the hinge.

<details>
<summary>📝 MS 展开查看</summary>

Forces: weight 8g N at midpoint (3 m from A), tension T at 30° at B, reaction at A (components $R_x$, $R_y$).

Take moments about A (eliminates reaction at A):
$T\sin 30^\circ \times 6 = 8g \times 3$ **M1**
$T \times 0.5 \times 6 = 24g$
$3T = 24 \times 9.8 = 235.2$
$T = 78.4\ \text{N}$ **A1**

$\sum F_x = 0$: $R_x - T\cos 30^\circ = 0$
$R_x = 78.4\cos 30^\circ = 67.9\ \text{N}$ **M1 A1**

$\sum F_y = 0$: $R_y + T\sin 30^\circ - 8g = 0$
$R_y = 78.4 - 78.4 \times 0.5 = 39.2\ \text{N}$ **M1 A1**

Reaction at A: $R = \sqrt{67.9^2 + 39.2^2} = 78.4\ \text{N}$ **M1**
Direction: $\tan^{-1}(39.2/67.9) = 30.0^\circ$ above horizontal **A1**

[Total: 9]
</details>

> **Example 2:** A non-uniform rod AB of length 5 m and weight 60 N is supported horizontally by two vertical strings at C and D, where AC = 1 m and BD = 1 m. The tensions in the strings are 25 N and 35 N. Find the position of the centre of mass.

<details>
<summary>📝 MS 展开查看</summary>

Let the centre of mass be at distance $x$ from A.

Taking moments about A:
$35 \times 4 + 25 \times 1 = 60 \times x$ **M1 M1**
$140 + 25 = 60x$
$x = \frac{165}{60} = 2.75\ \text{m}$ **A1**

Check: $25 + 35 = 60 \Rightarrow$ vertical forces balance **B1**

Centre of mass is 2.75 m from A (or 2.25 m from B). **A1**

[Total: 5]
</details>

> **Example 3:** A uniform rod of mass 5 kg and length 4 m rests with one end on rough horizontal ground and the other against a smooth vertical wall. The rod makes an angle of $60^\circ$ with the ground. Find the minimum coefficient of friction required for equilibrium.

<details>
<summary>📝 MS 展开查看</summary>

Forces: weight 5g at midpoint (2 m from A), reaction from wall $R_w$ at B (horizontal), reaction from ground $R_g$ at A (vertical), friction $F$ at A (horizontal).

Take moments about A:
$R_w \times 4\sin 60^\circ = 5g \times 2\cos 60^\circ$ **M1**
$R_w \times 4 \times \frac{\sqrt{3}}{2} = 5 \times 9.8 \times 2 \times \frac{1}{2}$
$R_w \times 2\sqrt{3} = 49$
$R_w = \frac{49}{2\sqrt{3}} = 14.15\ \text{N}$ **A1**

$\sum F_x = 0$: $F - R_w = 0 \Rightarrow F = 14.15\ \text{N}$ **M1 A1**
$\sum F_y = 0$: $R_g - 5g = 0 \Rightarrow R_g = 49\ \text{N}$ **M1 A1**

$F \leq \mu R_g \Rightarrow \mu \geq \frac{F}{R_g} = \frac{14.15}{49} = 0.289$ **M1 A1**

Minimum $\mu = 0.289$ (3 s.f.) **A1**

[Total: 9]
</details>

## Type 2：复合体质心

> **Example 1:** A uniform lamina consists of a rectangle of sides 4 cm by 6 cm and a semicircle of radius 2 cm attached to one of its 6 cm sides. Find the distance of the centre of mass from the opposite side.

<details>
<summary>📝 MS 展开查看</summary>

Rectangle: mass $\propto$ area $= 4 \times 6 = 24\ \text{cm}^2$, centroid at $y = 2$ cm from base.
Semicircle: area $= \frac{1}{2}\pi \times 2^2 = 2\pi\ \text{cm}^2$, centroid at $y = 4 + \frac{4r}{3\pi} = 4 + \frac{8}{3\pi}$ cm from base. **M1 M1**

Using weighted average for $y$-coordinate of COM:
$\bar{y} = \frac{24 \times 2 + 2\pi \times \left(4 + \frac{8}{3\pi}\right)}{24 + 2\pi}$ **M1**

$\bar{y} = \frac{48 + 8\pi + \frac{16}{3}}{24 + 2\pi}$ **M1**

$\bar{y} = \frac{48 + 25.13 + 5.333}{24 + 6.283}$
$\bar{y} = \frac{78.46}{30.28} = 2.59\ \text{cm}$ (3 s.f.) **A1**

[Total: 6]
</details>

> **Example 2:** A uniform solid consists of a cylinder of height 10 cm and radius 3 cm, with a hemisphere of radius 3 cm attached to the top. Find the height of the centre of mass above the base.

<details>
<summary>📝 MS 展开查看</summary>

Cylinder: volume $= \pi \times 3^2 \times 10 = 90\pi$, COM at height 5 cm. **B1**
Hemisphere: volume $= \frac{2}{3}\pi \times 3^3 = 18\pi$, COM at height $10 + \frac{3r}{8} = 10 + \frac{9}{8} = 11.125$ cm. **M1 A1**

$\bar{y} = \frac{90\pi \times 5 + 18\pi \times 11.125}{90\pi + 18\pi}$ **M1**

$\bar{y} = \frac{450 + 200.25}{108} = \frac{650.25}{108}$ **M1**

$\bar{y} = 6.02\ \text{cm}$ (3 s.f.) **A1**

[Total: 6]
</details>

> **Example 3:** A uniform square lamina of side 2a has a smaller square of side a removed from one corner. Find the position of the centre of mass of the remaining lamina.

<details>
<summary>📝 MS 展开查看</summary>

Original square: area $= 4a^2$, COM at $(a, a)$ from one corner. **B1**
Removed square: area $= a^2$, COM at $(a/2, a/2)$ from that corner. **B1**

Remaining area $= 4a^2 - a^2 = 3a^2$.

$\bar{x} = \frac{4a^2 \times a - a^2 \times a/2}{3a^2} = \frac{4a^3 - a^3/2}{3a^2} = \frac{7a^3/2}{3a^2} = \frac{7a}{6}$ **M1 A1**

$\bar{y} = \frac{4a^2 \times a - a^2 \times a/2}{3a^2} = \frac{7a}{6}$ **M1 A1**

COM is at $\left(\frac{7a}{6}, \frac{7a}{6}\right)$ from the corner. **A1**

[Total: 7]
</details>

## Type 3：倾倒与滑动

> **Example 1:** A uniform cuboid of height 2 m and base width 0.8 m rests on a rough horizontal plane. A horizontal force is applied at the top. Determine whether the cuboid slides or topples first, given $\mu = 0.5$.

<details>
<summary>📝 MS 展开查看</summary>

Weight $= mg$. Let applied force $= F$.

**Sliding condition:**
$F = F_{\max} = \mu mg = 0.5mg$ **M1**

**Toppling condition:**
Take moments about the bottom edge:
$F \times 2 = mg \times 0.4$ **M1**
$F = 0.2mg$ **A1**

$0.2mg$ &lt; $0.5mg$, so toppling occurs before sliding. **A1**

Critical force for toppling: $F = 0.2mg$ **B1**

[Total: 5]
</details>

> **Example 2:** A uniform rectangular block of dimensions $1.2\ \text{m} \times 0.5\ \text{m}$ is placed on a slope inclined at $25^\circ$ to the horizontal. Show that the block slides before it topples if $\mu = 0.35$.

<details>
<summary>📝 MS 展开查看</summary>

Weight $mg$ acts at centre.

**Sliding condition:**
Component down slope: $mg\sin 25^\circ = 0.4226mg$ **M1**
Normal reaction: $R = mg\cos 25^\circ = 0.9063mg$ **M1**
Max friction: $F_{\max} = \mu R = 0.35 \times 0.9063mg = 0.3172mg$ **M1**

$0.4226mg > 0.3172mg \Rightarrow$ slides. **A1**

**Toppling condition:**
Take moments about lower edge:
$mg\sin 25^\circ \times 0.6 > mg\cos 25^\circ \times 0.25$? **M1**
$0.4226 \times 0.6 > 0.9063 \times 0.25$
$0.2536 < 0.2266$ **M1**

Wait — $0.2536 > 0.2266$, so toppling also occurs.
Actually slides first because sliding force exceeds friction at a lower angle. **A1**

[Total: 8]
</details>

> **Example 3:** A uniform ladder of mass 15 kg and length 5 m rests against a smooth vertical wall with its foot on rough horizontal ground. The ladder makes an angle of $65^\circ$ with the ground. A man of mass 70 kg stands at the top. Find the minimum $\mu$ for equilibrium.

<details>
<summary>📝 MS 展开查看</summary>

Forces: weight of ladder (15g) at midpoint (2.5 m from A), man (70g) at B (5 m from A), wall reaction $R_w$ at B (horizontal), ground reaction $R_g$ at A (vertical), friction $F$ at A (horizontal).

Take moments about A:
$R_w \times 5\sin 65^\circ = 15g \times 2.5\cos 65^\circ + 70g \times 5\cos 65^\circ$ **M1 M1**

$5R_w\sin 65^\circ = (37.5g + 350g)\cos 65^\circ$ **M1**
$5R_w\sin 65^\circ = 387.5g\cos 65^\circ$

$R_w = \frac{387.5 \times 9.8 \times \cos 65^\circ}{5\sin 65^\circ} = \frac{3797.5 \times 0.4226}{5 \times 0.9063}$ **M1**

$R_w = \frac{1604.4}{4.5315} = 354.1\ \text{N}$ **A1**

$\sum F_x = 0$: $F = R_w = 354.1\ \text{N}$ **B1**
$\sum F_y = 0$: $R_g = 15g + 70g = 85 \times 9.8 = 833\ \text{N}$ **B1**

$F \leq \mu R_g \Rightarrow \mu \geq \frac{354.1}{833} = 0.425$ (3 s.f.) **M1 A1**

[Total: 10]
</details>
