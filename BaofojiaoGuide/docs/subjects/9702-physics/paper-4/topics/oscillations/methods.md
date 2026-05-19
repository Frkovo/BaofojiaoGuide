---
title: Oscillations — 解题方法
sidebar_position: 4
---

# Oscillations — 解题方法

## Method 1: Extracting Parameters from Graphs

### 从 $x$-$t$ 图

- 振幅 $x_0$ = 峰值
- 周期 $T$ = 相邻两峰值的时间间隔
- $\omega = 2\pi / T$

### 从 $v$-$t$ 图

- 最大速度 $v_0$ = 峰值
- $v_0 = \omega x_0$

### 从 $v$-$x$ 图

- 椭圆长轴 = $v_0$，短轴 = $x_0$
- 或长轴 = $x_0$，短轴 = $v_0$（取决于坐标轴）
- 斜率在 $(x=0, v=v_0)$ 处为零

### 从 $E_P$-$x$ 图

- 最大势能 = 总能量
- $E_{P,\max} = \frac{1}{2} m \omega^2 x_0^2$
- 通过 $E_{P,\max}$ 和 $x_0$ 可求 $m\omega^2$

## Method 2: SHM Calculation Sequence

### 步骤

1. 确定 $x_0$ 和 $f$（或 $\omega$ 或 $T$）
2. 计算 $\omega = 2\pi f$
3. 需要时计算：
   - $v_0 = \omega x_0$
   - $a_0 = \omega^2 x_0$
   - $F_0 = m\omega^2 x_0$
   - $E = \frac{1}{2} m \omega^2 x_0^2$
4. 特定位置的速度：$v = \omega \sqrt{x_0^2 - x^2}$

## Method 3: Finding Mass/Spring Constant from $a$-$x$ Relation

### 弹簧-质量系统

- $F = -kx$（Hooke's law）
- $ma = -kx$
- $a = -(k/m)x$
- 对比 $a = -\omega^2 x$ → $\omega^2 = k/m$
- $T = 2\pi \sqrt{m/k}$

### 单摆

- $a = -(g/L)x$（小角度近似）
- $\omega^2 = g/L$
- $T = 2\pi \sqrt{L/g}$

## Method 4: Damping Graph Sketching

### 步骤

1. 先画出无阻尼正弦波（参考）
2. **Light damping**: 振幅逐渐减小（包络线指数衰减），周期基本不变
3. **Critical damping**: 从初位移直接回到零（不越过平衡位置），最快
4. **Heavy damping**: 从初位移缓慢趋于零（比临界阻尼慢）
