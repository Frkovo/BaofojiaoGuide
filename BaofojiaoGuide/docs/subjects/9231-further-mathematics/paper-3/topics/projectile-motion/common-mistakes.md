---
title: 常见错误
sidebar_position: 6
---

# 常见错误 — Projectile Motion

## 错误 1：最高点速度为 0

**错误想法**：最高点时速度为零。

**正解**：$v_y = 0$，但 $v_x = u\cos\theta$ 保持不变。

## 错误 2：符号处理

**错误**：竖直方向位移或速度正负号混乱。

**正解**：向上为正方向，则 $a_y = -g$，$v_y = u\sin\theta - gt$。

## 错误 3：轨迹方程公式

**错误**：$y = x\tan\theta - \frac{gx^2}{2u^2\cos^2\theta}$ 当作 $y = x\tan\theta - \frac{gx^2}{2u^2}$。

**正解**：分母有 $\cos^2\theta$，不是简单的 $u^2$。

## 错误 4：斜面抛体不分 $g$

**错误**：直接用标准 $g$ 而不分解。

**正解**：将 $g$ 分解为沿斜面和垂直斜面两个分量。

## 错误 5：忘记 $\cos^2\theta$ 与 $1 + \tan^2\theta$ 的关系

**正解**：$\frac{1}{\cos^2\theta} = 1 + \tan^2\theta$，用于化简轨迹方程。
