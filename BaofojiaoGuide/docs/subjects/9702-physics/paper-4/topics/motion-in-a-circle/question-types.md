---
title: 题型分析
sidebar_position: 2
---
# 题型分析 — Motion in a Circle

## Question Type 1: 弧度定义与角速度计算

### 如何识别
直接问 define the radian 或计算 $\omega$、$T$、$f$。

### 标准解题方法
:::note[定义题]
radian: angle subtended at centre of circle when arc length equals radius.
必须包含 arc length = radius 或 angle subtended when arc length = radius。
:::

### 评分标准
:::info[评分要点]
- **B1**: arc length = radius 两个要素齐全
- **C1**: $\omega = 2\pi/T$ 公式正确
- **A1**: 数值正确，单位 rad s$^{-1}$
:::

### 完整原题

**Example 1 — 9702_s24_qp_42 (2 marks):**
> Define the radian.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **B1**: angle (subtended) at the centre of a circle
- **B1**: (when) arc length = radius
</details>

**Example 2 — 9702_w23_qp_42 (4 marks):**
> The minute hand of a clock revolves at constant angular speed around the face of the clock. The tip of the minute hand is at a distance of 2.8 cm from the centre of the clock face. A small piece of modelling clay is attached to the tip of the minute hand.
> (i) Calculate the angular speed $\omega$ of the minute hand.
> (ii) Calculate the magnitude of the centripetal acceleration of the piece of modelling clay.

<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $\omega = 2\pi/T$
- **C1**: $T = 60 \times 60 = 3600$ s
- **A1**: $\omega = 1.75 \times 10^{-3}$ rad s$^{-1}$
- **C1**: $a = r\omega^2$
- **A1**: $a = 2.8 \times 10^{-2} \times (1.75 \times 10^{-3})^2 = 8.6 \times 10^{-8}$ m s$^{-2}$
</details>

**Example 3 — 9702_s20_qp_41 (2 marks):**
> The period of rotation of the stars is 44.2 years. Calculate the angular velocity $\omega$.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $\omega = 2\pi/T$
- **C1**: $T = 44.2 \times 365 \times 24 \times 3600$
- **A1**: $\omega = 4.5 \times 10^{-9}$ rad s$^{-1}$
</details>

### 常见陷阱
:::warning[常见陷阱]
- $\omega$ 单位必须是 rad s$^{-1}$，不是 Hz
- 周期 $T$ 的单位必须是秒(s)
- 年转秒：乘以 $365 \times 24 \times 3600$
:::

## Question Type 2: 向心加速度与向心力计算

### 如何识别
给出 $m$, $r$, $v$ 或 $\omega$，求力或加速度。

### 标准解题方法
:::note[计算步骤]
1. 写出公式 $F = mv^2/r$ 或 $F = mr\omega^2$
2. 代入数值（注意单位）
3. 得出结果
:::

### 评分标准
:::info[评分要点]
- **C1**: 写出正确公式
- **C1**: 正确代入
- **A1**: 正确答案 + 单位
:::

### 完整原题

**Example 1 — 9702_w21_qp_41 (4 marks):**
> (a) With reference to velocity and acceleration, describe uniform circular motion.
> (b) An object of mass 0.35 kg is attached to one end of a string. The object moves in a horizontal circle of radius 0.62 m at constant speed. The string makes an angle of 30° with the vertical. Calculate:
> (i) the centripetal acceleration
> (ii) the tension in the string
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **B1**: speed is constant
- **B1**: direction (of velocity) changes continuously
- **B1**: acceleration (directed) towards centre of circle
- **C1**: $T\sin\theta = mv^2/r$ or $T\sin30 = ma$
- **C1**: $T\cos30 = mg$, so $T = 0.35 \times 9.81 / \cos30 = 3.96$ N
- **C1**: $a = T\sin30 / m = 3.96 \times 0.5 / 0.35$
- **A1**: $a = 5.7$ m s$^{-2}$
</details>

**Example 2 — 9702_s23_qp_41 (4 marks):**
> A sphere of mass 0.15 kg is attached to a string and moves in a horizontal circle at constant speed. The centripetal acceleration is $a = 7.2$ m s$^{-2}$. The radius is 0.45 m. Determine:
> (i) the speed of the sphere
> (ii) the period of the circular motion
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $a = v^2/r$
- **C1**: $v = \sqrt{ar} = \sqrt{7.2 \times 0.45} = 1.8$ m s$^{-1}$
- **A1**: $v = 1.8$ m s$^{-1}$
- **C1**: $\omega = v/r = 1.8/0.45 = 4.0$ rad s$^{-1}$, $T = 2\pi/\omega$
- **A1**: $T = 1.57$ s
</details>

### 常见陷阱
:::warning[常见陷阱]
- 向心力是**合力**，不是独立力
- 注意 $v = r\omega$ 中 $r$ 必须是运动半径
- 张力不等于向心力（除非水平且无重力）
:::

## Question Type 3: 竖直圆周运动

### 如何识别
物体在竖直圆轨道上运动，最低点/最高点的力分析。

### 标准解题方法
:::note[方法]
最低点：$N - mg = mv^2/r$，所以 $N = mg + mv^2/r$
最高点：$N + mg = mv^2/r$，所以 $N = mv^2/r - mg$
临界条件（刚好过最高点）：$N = 0, v = \sqrt{gr}$
:::

### 评分标准
:::info[评分规则]
- **B1**: 确定力的方向
- **C1**: 牛顿第二定律方程
- **C1**: 代入
- **A1**: 答案
:::

### 完整原题

**Example 1 — 9702_w22_qp_42 (5 marks):**
> An object of mass 0.20 kg moves in a vertical circle of radius 0.80 m. At the top of the circle, the speed is 3.0 m s$^{-1}$. 
> (i) Determine the centripetal acceleration of the object.
> (ii) Describe how the two forces acting on the object give rise to this centripetal acceleration.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $a = v^2/r = 3.0^2/0.80$
- **A1**: $a = 11.25$ m s$^{-2}$
- **B1**: weight (downwards) and contact/normal force (downwards)
- **B1**: both forces act towards centre
- **B1**: resultant of these two forces = centripetal force
</details>

### 常见陷阱
:::warning[注意]
- 最高点重力和法向力都指向圆心（同向）
- 最低点法向力减去重力等于向心力
- 若速度太小，物体在最高点会掉下来
:::
