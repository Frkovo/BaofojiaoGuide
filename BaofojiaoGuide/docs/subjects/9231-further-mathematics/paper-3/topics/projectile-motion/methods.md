---
title: 解题方法
sidebar_position: 3
---

# Solution Methods — Projectile Motion

## 方法一：分解法（标准解法）

适用于已知 $u$、$\theta$ 求任意时刻位置/速度。

:::info[Steps]

1. 分解初速度：$u_x = u\cos\theta$，$u_y = u\sin\theta$
2. 水平方向：$x = u_x t$，$v_x = u_x$
3. 竖直方向：$y = u_y t - \frac{1}{2}gt^2$，$v_y = u_y - gt$
4. 合速度大小：$v = \sqrt{v_x^2 + v_y^2}$
5. 速度方向：$\tan\phi = \frac{v_y}{v_x}$

:::

## 方法二：轨迹方程法

适用于已知落点条件反推初值。

:::info[Steps]

1. 写出轨迹方程：$y = x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$
2. 代入已知点 $(x,y)$
3. 整理得关于 $\tan\theta$ 或 $u$ 的方程
4. 求解

:::

## 方法三：斜面抛体

适用于抛体落在斜面上。

:::info[Steps]

1. 沿斜面和垂直斜面分解：将 $g$ 分解
2. 沿斜面方向：$s_{\parallel} = u_{\parallel}t + \frac{1}{2}g_{\parallel}t^2$
3. 垂直斜面方向：$s_{\perp} = u_{\perp}t + \frac{1}{2}g_{\perp}t^2$
4. 落点条件：$s_{\perp} = 0$ 或已知几何关系

:::

## 方法四：对称性法

利用抛物线对称性。

:::tip[Tips]

- 上升和下降时间相等（水平地面）
- 最高点 $v_y = 0$，$y = H$
- 落地时 $v_y = -u\sin\theta$

:::
