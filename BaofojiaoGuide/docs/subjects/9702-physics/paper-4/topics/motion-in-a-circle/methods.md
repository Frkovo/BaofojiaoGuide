---
title: 解题方法
sidebar_position: 4
---
# 解题方法 — Motion in a Circle

## Method 1: 计算向心加速度和向心力

### When to use
已知圆周运动半径 $r$、角速度 $\omega$ 或线速度 $v$，求加速度或力。

### Steps
1. 确定已知量：$r$, $\omega$ 或 $v$, 以及 $T$ 或 $f$
2. 若给 $T$，用 $\omega = 2\pi / T$ 求 $\omega$
3. 用 $a = r\omega^2$ 或 $a = v^2 / r$ 求加速度
4. 用 $F = ma$ 得向心力
5. 注意核对方向：指向圆心

### Formula
$$a = r\omega^2 = \frac{v^2}{r}$$
$$F = mr\omega^2 = \frac{mv^2}{r}$$

### Mistakes to avoid
- 向心力是合力(resultant force)，不是额外力
- 不要忘记单位换算：cm 转 m

## Method 2: 竖直面圆周运动

### When to use
物体在竖直圆周中运动，如过山车、摆锤在最低点。

### Steps
1. 分析各点受力
2. 最低点：$T - mg = mv^2/r$ 或 $N - mg = mv^2/r$
3. 最高点：$T + mg = mv^2/r$ 或 $N + mg = mv^2/r$
4. 临界条件：最高点 $N = 0$ 时，$mg = mv^2/r$

### Formula
$$F_{\text{net}} = \frac{mv^2}{r}$$（指向圆心方向）

### Mistakes to avoid
- 忘记重力贡献
- 方向搞反

## Method 3: 角速度与线速度转换

### When to use
已知周期 $T$ 或频率 $f$，求角速度或线速度。

### Steps
1. $\omega = 2\pi / T$ 或 $\omega = 2\pi f$
2. $v = r\omega$
3. 注意弧度制

### Formula
$$\omega = \frac{2\pi}{T} = 2\pi f$$
$$v = r\omega$$

### Mistakes to avoid
- $\omega$ 不等于 $f$，差 $2\pi$ 倍
