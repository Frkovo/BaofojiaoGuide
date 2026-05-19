---
title: 解题方法
sidebar_position: 4
---
# 解题方法 — Gravitational Fields

## Method 1: 引力场强度计算

### When to use
已知天体质量 $M$ 和半径 $R$（或距离 $r$），求引力场强度 $g$。

### Steps
1. 确认 $M$ 为质量，$r$ 为距**中心**的距离
2. 用 $g = GM/r^2$
3. 若在地球表面附近，$g \approx 9.81$ N kg$^{-1}$
4. 若高度 $h \ll R$，可用 $g \approx g_0(1 - 2h/R)$ 近似

### Formula
$$g = \frac{GM}{r^2}$$

### Mistakes to avoid
- $r$ 是从中心到点的距离，不是表面到点的距离
- $G$ 是引力常数 $6.67 \times 10^{-11}$，不是 $g$

## Method 2: 卫星轨道分析

### When to use
卫星或行星绕中心天体做圆周运动。

### Steps
1. 引力提供向心力：$GMm/r^2 = mv^2/r = mr\omega^2$
2. 消去卫星质量 $m$：$GM/r^2 = v^2/r = r\omega^2$
3. 代入 $v = 2\pi r/T$ 得：$GM/r^2 = 4\pi^2 r/T^2$
4. 整理得开普勒第三定律：$T^2 = (4\pi^2/GM)r^3$

### Formula
$$\frac{GMm}{r^2} = \frac{mv^2}{r} = mr\omega^2$$
$$T^2 = \frac{4\pi^2}{GM}r^3$$

### Mistakes to avoid
- 卫星质量 $m$ 在推导中消去
- $r$ 为轨道半径（从中心算起）

## Method 3: 引力势能与逃逸

### When to use
计算将物体从某点移到无穷远所需的功。

### Steps
1. 引力势 $\phi = -GM/r$
2. 引力势能 $E_P = m\phi = -GMm/r$
3. 逃逸所需能量 $\Delta E = 0 - (-GMm/r) = GMm/r$
4. 逃逸速度：$\frac12 mv^2 = GMm/r \Rightarrow v = \sqrt{2GM/r}$

### Formula
$$\phi = -\frac{GM}{r}$$
$$E_P = -\frac{GMm}{r}$$
$$v_{\text{esc}} = \sqrt{\frac{2GM}{r}}$$

### Mistakes to avoid
- 势能是负的！数值越大（越接近0）能量越高
- 逃逸速度公式中的 $r$ 是起始位置到中心的距离
