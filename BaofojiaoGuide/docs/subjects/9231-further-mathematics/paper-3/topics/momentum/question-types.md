---
title: 题型分析
sidebar_position: 4
---

# 题型分析 — Momentum

## Type 1：对心碰撞

> **Example 1:** Two particles A and B, of masses 2 kg and 3 kg respectively, move towards each other along the same straight line with speeds $4\ \text{m}\,\text{s}^{-1}$ and $2\ \text{m}\,\text{s}^{-1}$. The coefficient of restitution is $0.5$. Find the speeds of A and B after collision and the loss in kinetic energy.

<details>
<summary>📝 MS 展开查看</summary>

Take direction of A before collision as positive. **B1**

Momentum conservation:
$2 \times 4 + 3 \times (-2) = 2v_A + 3v_B$ **M1**
$8 - 6 = 2v_A + 3v_B$
$2 = 2v_A + 3v_B$ ... (1) **A1**

NEL: $e = \frac{v_B - v_A}{u_A - u_B} \Rightarrow 0.5 = \frac{v_B - v_A}{4 - (-2)}$ **M1**
$0.5 = \frac{v_B - v_A}{6}$
$v_B - v_A = 3$ ... (2) **A1**

From (1) and (2):
Sub (2) into (1): $2 = 2v_A + 3(v_A + 3)$ **M1**
$2 = 5v_A + 9$
$5v_A = -7 \Rightarrow v_A = -1.4\ \text{m}\,\text{s}^{-1}$ **A1**
$v_B = -1.4 + 3 = 1.6\ \text{m}\,\text{s}^{-1}$ **A1**

KE loss: $\Delta KE = \frac{1}{2}(2)(4^2) + \frac{1}{2}(3)(2^2) - \frac{1}{2}(2)(1.4^2) - \frac{1}{2}(3)(1.6^2)$
$= 16 + 6 - 1.96 - 3.84 = 16.2\ \text{J}$ **M1 A1**

[Total: 11]
</details>

> **Example 2:** A particle of mass $m$ moving with speed $u$ collides directly with a stationary particle of mass $km$. After the collision, the first particle is brought to rest. Find $k$ and the speed of the second particle. Given that the collision is perfectly elastic, find $e$.

<details>
<summary>📝 MS 展开查看</summary>

Momentum: $mu = m \times 0 + km \times v_2$ **M1**
$u = kv_2 \Rightarrow v_2 = \frac{u}{k}$ **A1**

First particle brought to rest: $v_1 = 0$. **B1**

NEL: $e = \frac{v_2 - v_1}{u_1 - u_2} = \frac{u/k - 0}{u - 0} = \frac{1}{k}$ **M1 A1**

For perfectly elastic, $e = 1 \Rightarrow k = 1$. **A1**

Speed of second: $v_2 = u$ **A1**

[Total: 6]
</details>

> **Example 3:** Two particles of masses 0.4 kg and 0.6 kg move towards each other along a straight line with speeds $5\ \text{m}\,\text{s}^{-1}$ and $3\ \text{m}\,\text{s}^{-1}$ respectively. The coefficient of restitution is $e$. After collision, the 0.4 kg particle reverses direction with speed $1\ \text{m}\,\text{s}^{-1}$. Find $e$ and the speed of the other particle.

<details>
<summary>📝 MS 展开查看</summary>

Take direction of 0.4 kg particle before collision as positive. **B1**

Momentum:
$0.4 \times 5 + 0.6 \times (-3) = 0.4 \times (-1) + 0.6v_2$ **M1**
$2 - 1.8 = -0.4 + 0.6v_2$
$0.2 = -0.4 + 0.6v_2$
$0.6v_2 = 0.6 \Rightarrow v_2 = 1\ \text{m}\,\text{s}^{-1}$ **A1**

NEL: $e = \frac{v_2 - v_1}{u_1 - u_2} = \frac{1 - (-1)}{5 - (-3)}$ **M1**
$e = \frac{2}{8} = 0.25$ **A1**

[Total: 6]
</details>

## Type 2：斜碰

> **Example 1:** A smooth sphere of mass $m$ moving with speed $u$ strikes a stationary sphere of mass $2m$. The line of centres makes an angle of $30^\circ$ with the direction of motion of the first sphere. The coefficient of restitution is $0.6$. Find the velocities after impact.

<details>
<summary>📝 MS 展开查看</summary>

Resolve along line of centres (direction of impact) and perpendicular. **B1**

Before impact:
$u_{1n} = u\cos 30^\circ = 0.866u$, $u_{1t} = u\sin 30^\circ = 0.5u$ **A1**
$u_{2n} = 0$, $u_{2t} = 0$ **B1**

Perpendicular direction (tangential): velocities unchanged.
$v_{1t} = 0.5u$, $v_{2t} = 0$ **M1 A1**

Along line of centres: momentum conservation.
$m \times 0.866u + 2m \times 0 = m v_{1n} + 2m v_{2n}$
$0.866u = v_{1n} + 2v_{2n}$ ... (1) **M1 A1**

NEL: $e = \frac{v_{2n} - v_{1n}}{u_{1n} - u_{2n}}$
$0.6 = \frac{v_{2n} - v_{1n}}{0.866u}$
$v_{2n} - v_{1n} = 0.5196u$ ... (2) **M1 A1**

From (1) and (2):
$v_{1n} = -0.0578u$, $v_{2n} = 0.4618u$ **A1**

Resultant velocities:
$v_1 = \sqrt{(-0.0578u)^2 + (0.5u)^2} = 0.503u$ at $\tan^{-1}(0.5/0.0578) \approx 83.4^\circ$ to line of centres **M1**
$v_2 = 0.462u$ along line of centres **A1**

[Total: 12]
</details>

> **Example 2:** A sphere A of mass $m$ moving with speed $4\ \text{m}\,\text{s}^{-1}$ strikes a stationary sphere B of mass $3m$. The line of centres is at $60^\circ$ to the direction of motion of A. The coefficient of restitution is $0.5$. Find the speeds of A and B after impact.

<details>
<summary>📝 MS 展开查看</summary>

Along line of centres:
$u_{An} = 4\cos 60^\circ = 2\ \text{m}\,\text{s}^{-1}$, $u_{At} = 4\sin 60^\circ = 3.464\ \text{m}\,\text{s}^{-1}$ **A1**
$u_{Bn} = 0$, $u_{Bt} = 0$ **B1**

Tangential: $v_{At} = 3.464\ \text{m}\,\text{s}^{-1}$, $v_{Bt} = 0$ **M1 A1**

Line of centres momentum:
$m \times 2 + 3m \times 0 = m v_{An} + 3m v_{Bn}$
$2 = v_{An} + 3v_{Bn}$ ... (1) **A1**

NEL: $0.5 = \frac{v_{Bn} - v_{An}}{2 - 0}$
$v_{Bn} - v_{An} = 1$ ... (2) **A1**

From (1) and (2):
$v_{An} = -0.25\ \text{m}\,\text{s}^{-1}$, $v_{Bn} = 0.75\ \text{m}\,\text{s}^{-1}$ **A1**

$v_A = \sqrt{(-0.25)^2 + 3.464^2} = \sqrt{0.0625 + 12} = \sqrt{12.0625} = 3.47\ \text{m}\,\text{s}^{-1}$ **M1 A1**
$v_B = 0.75\ \text{m}\,\text{s}^{-1}$ **A1**

[Total: 10]
</details>

> **Example 3:** A smooth sphere of mass $2m$ moving with speed $V$ strikes a stationary sphere of mass $m$. After the collision, the $2m$ sphere moves at $30^\circ$ to its original direction. Find the velocity of each sphere after impact, given $e = 0.4$.

<details>
<summary>📝 MS 展开查看</summary>

Let line of centres be at angle $\theta$ to original direction. **M1**

Before impact:
$u_{1n} = V\cos\theta$, $u_{1t} = V\sin\theta$
$u_{2n} = 0$, $u_{2t} = 0$ **B1**

Tangential: $v_{1t} = V\sin\theta$ **B1**

Line of centres momentum:
$2m \cdot V\cos\theta = 2m v_{1n} + m v_{2n}$
$2V\cos\theta = 2v_{1n} + v_{2n}$ ... (1) **A1**

NEL: $0.4 = \frac{v_{2n} - v_{1n}}{V\cos\theta}$
$v_{2n} - v_{1n} = 0.4V\cos\theta$ ... (2) **A1**

After collision: $2m$ sphere moves at $30^\circ$ to original direction.
$\tan 30^\circ = \frac{v_{1t}}{v_{1n}} = \frac{V\sin\theta}{v_{1n}}$ **M1**
$v_{1n} = \frac{V\sin\theta}{\tan 30^\circ} = V\sin\theta \cdot \sqrt{3}$ **A1**

From (1) and (2):
$v_{2n} = 0.4V\cos\theta + v_{1n}$
$2V\cos\theta = 2v_{1n} + 0.4V\cos\theta + v_{1n}$
$2V\cos\theta - 0.4V\cos\theta = 3v_{1n}$
$1.6V\cos\theta = 3 \times \sqrt{3}V\sin\theta$ **M1**
$\tan\theta = \frac{1.6}{3\sqrt{3}} = 0.3079$
$\theta = 17.1^\circ$ **A1**

$v_1 = \sqrt{v_{1n}^2 + v_{1t}^2}$ etc. **M1**

[Total: 12]
</details>

## Type 3：碰撞固定面

> **Example 1:** A ball strikes a smooth vertical wall with speed $8\ \text{m}\,\text{s}^{-1}$ at an angle of $40^\circ$ to the normal. The coefficient of restitution is $0.6$. Find the speed and direction of the ball after impact.

<details>
<summary>📝 MS 展开查看</summary>

Normal component before: $u_n = 8\cos 40^\circ = 6.128\ \text{m}\,\text{s}^{-1}$ **A1**
Tangential component before: $u_t = 8\sin 40^\circ = 5.142\ \text{m}\,\text{s}^{-1}$ **A1**

Tangential component unchanged: $v_t = 5.142\ \text{m}\,\text{s}^{-1}$ **B1**

Normal after: $v_n = -e u_n = -0.6 \times 6.128 = -3.677\ \text{m}\,\text{s}^{-1}$ **M1 A1**

Speed after: $v = \sqrt{3.677^2 + 5.142^2} = \sqrt{13.52 + 26.44} = \sqrt{39.96} = 6.32\ \text{m}\,\text{s}^{-1}$ **M1 A1**

Angle to normal: $\tan\theta = \frac{5.142}{3.677} = 1.398 \Rightarrow \theta = 54.4^\circ$ **M1 A1**

[Total: 9]
</details>

> **Example 2:** A ball is projected towards a smooth vertical wall with speed $12\ \text{m}\,\text{s}^{-1}$ at an angle of $30^\circ$ to the horizontal. The coefficient of restitution is $0.5$. Find the distance from the wall where the ball lands.

<details>
<summary>📝 MS 展开查看</summary>

Before impact: $u_x = 12\cos 30^\circ = 10.39\ \text{m}\,\text{s}^{-1}$ (towards wall), $u_y = 12\sin 30^\circ = 6\ \text{m}\,\text{s}^{-1}$ upward. **A1**

After impact: $v_x = -e u_x = -0.5 \times 10.39 = -5.196\ \text{m}\,\text{s}^{-1}$ (away from wall) **M1 A1**
$v_y = 6\ \text{m}\,\text{s}^{-1}$ (unchanged) **B1**

Time of flight after impact:
$0 = 6t - \frac{1}{2} \times 9.8 \times t^2$
$t(6 - 4.9t) = 0 \Rightarrow t = 1.225\ \text{s}$ (ignore $t = 0$) **M1 A1**

Distance from wall: $x = v_x \times t = 5.196 \times 1.225 = 6.36\ \text{m}$ **M1 A1**

[Total: 8]
</details>

> **Example 3:** A small smooth sphere strikes a smooth plane surface with speed $V$ at an angle $\theta$ to the normal. The coefficient of restitution is $e$. Show that $\tan\phi = \frac{\tan\theta}{e}$, where $\phi$ is the angle the rebound velocity makes with the normal.

<details>
<summary>📝 MS 展开查看</summary>

Before: $u_n = V\cos\theta$, $u_t = V\sin\theta$ **B1**

After: $v_n = -eV\cos\theta$ (normal component reverses and reduces) **M1 A1**
$v_t = V\sin\theta$ (unchanged) **B1**

Angle $\phi$ to normal: $\tan\phi = \frac{|v_t|}{|v_n|} = \frac{V\sin\theta}{eV\cos\theta} = \frac{\tan\theta}{e}$ **M1 A1**

[Total: 5]
</details>

## Type 4：连续碰撞

> **Example 1:** Three particles A, B, C of masses $m$, $2m$, $m$ respectively lie at rest in a straight line on a smooth horizontal table. A is projected towards B with speed $u$. The coefficient of restitution between each pair is $e$. Find the speeds after all collisions have taken place.

<details>
<summary>📝 MS 展开查看</summary>

**First collision: A and B**
Momentum: $mu = mv_A + 2mv_B$ **M1**
$u = v_A + 2v_B$ ... (1)

NEL: $e = \frac{v_B - v_A}{u - 0}$ **M1**
$eu = v_B - v_A$ ... (2)

From (1) and (2):
$v_B = \frac{u(1 + e)}{3}$, $v_A = \frac{u(1 - 2e)}{3}$ **A1**

**Second collision: B and C** (if $v_B > 0$)
Momentum: $2m v_B = 2m v_B' + m v_C$ **M1**
$2v_B = 2v_B' + v_C$ ... (3)

NEL: $e = \frac{v_C - v_B'}{v_B - 0}$ **M1**
$ev_B = v_C - v_B'$ ... (4)

From (3) and (4):
$v_C = \frac{4ev_B}{3} + \frac{2v_B}{3}?$

Solve:
(4): $v_C = v_B' + ev_B$
Sub into (3): $2v_B = 2v_B' + v_B' + ev_B$
$2v_B = 3v_B' + ev_B$
$v_B' = \frac{(2 - e)v_B}{3}$ **A1**
$v_C = \frac{(2 - e)v_B}{3} + ev_B = \frac{(2 + 2e)v_B}{3}$ **A1**

Substituting $v_B = \frac{u(1 + e)}{3}$:
$v_C = \frac{2(1 + e)}{3} \times \frac{u(1 + e)}{3} = \frac{2u(1 + e)^2}{9}$ **A1**

[Total: 11]
</details>

> **Example 2:** A small sphere of mass $m$ moving with speed $4u$ collides directly with a sphere of mass $2m$ moving in the same direction with speed $u$. The coefficient of restitution is $0.5$. Find the speeds after collision. If the first sphere then collides with a stationary sphere of mass $m$, find the speed of the stationary sphere.

<details>
<summary>📝 MS 展开查看</summary>

**Collision 1:**
Momentum: $m \times 4u + 2m \times u = mv_1 + 2mv_2$
$4u + 2u = v_1 + 2v_2$
$6u = v_1 + 2v_2$ ... (1) **M1 A1**

NEL: $0.5 = \frac{v_2 - v_1}{4u - u}$
$1.5u = v_2 - v_1$ ... (2) **M1 A1**

From (1) and (2):
$v_1 = u$, $v_2 = 2.5u$ **A1**

**Collision 2: sphere 1 ($v_1 = u$) strikes stationary sphere of mass $m$:**
Momentum: $m \times u + m \times 0 = m v_1' + m v_3$
$u = v_1' + v_3$ ... (3) **M1 A1**

NEL: $0.5 = \frac{v_3 - v_1'}{u - 0}$
$0.5u = v_3 - v_1'$ ... (4) **M1 A1**

From (3) and (4):
$v_3 = 0.75u$, $v_1' = 0.25u$ **A1**

Speed of stationary sphere after collision: $0.75u$ **A1**

[Total: 12]
</details>

> **Example 3:** Particles P, Q, R of masses $m$, $m$, $3m$ lie at rest in a straight line on a smooth horizontal surface, with Q between P and R. P is projected towards Q with speed $V$. The coefficient of restitution between each pair is $1$ (perfectly elastic). Find the final speeds of all particles.

<details>
<summary>📝 MS 展开查看</summary>

**Collision 1: P and Q**
Momentum: $mV = mv_1 + mv_2 \Rightarrow V = v_1 + v_2$ **M1**
NEL $e = 1$: $1 = \frac{v_2 - v_1}{V - 0} \Rightarrow V = v_2 - v_1$ **M1**

Solving: $v_1 = 0$, $v_2 = V$ **A1**

**Collision 2: Q (now speed $V$) and R (at rest)**
Momentum: $m \times V + 3m \times 0 = m v_2' + 3m v_3$
$V = v_2' + 3v_3$ ... (1) **M1**

NEL: $1 = \frac{v_3 - v_2'}{V - 0}$
$V = v_3 - v_2'$ ... (2) **M1**

From (1) and (2):
$v_3 = V/2$, $v_2' = -V/2$ **A1**

**Collision 3: P (at rest) and Q (now $-V/2$, moving towards P)**
Momentum: $m \times (-V/2) + m \times 0 = m v_1' + m v_2''$
$-V/2 = v_1' + v_2''$ ... (3) **M1**

NEL: $1 = \frac{v_2'' - v_1'}{-V/2 - 0} \Rightarrow -V/2 = v_2'' - v_1'$ ... (4) **M1**

From (3) and (4): $v_1' = -V/2$, $v_2'' = 0$ **A1**

Final speeds: P: $V/2$ (direction opposite to original), Q: $0$, R: $V/2$ (same direction as original P) **A1**

[Total: 12]
</details>
