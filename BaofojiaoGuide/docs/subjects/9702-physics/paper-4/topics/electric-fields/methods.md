---
title: Electric Fields — 解题方法
sidebar_position: 4
---

# Electric Fields — 解题方法

## Method 1: Calculating Electric Field Strength

### 点电荷

$$E = \frac{Q}{4\pi \epsilon_0 r^2}$$

1. 确定 $r$（从电荷中心到点 P 的距离）
2. 代入 $Q$（注意符号——只影响方向）
3. 使用 $\frac{1}{4\pi \epsilon_0} = 8.99 \times 10^9$
4. 方向：正电荷发出，负电荷吸入

### 平行板匀强电场

$$E = \frac{V}{d}$$

1. $V$ 是板间电势差
2. $d$ 是板间距（单位 m）
3. 方向：从正极板指向负极板

### 多个点电荷的叠加

- $E$ 是矢量：先求每个电荷在 P 点的 $E$（大小 + 方向），然后矢量相加
- 如果所有 $E$ 在同一直线上 → 代数加减
- 如果不在同一直线上 → 用平行四边形法则（或分量法）

## Method 2: Calculating Electric Potential

### 点电荷

$$V = \frac{Q}{4\pi \epsilon_0 r}$$

1. 确定 $r$
2. 代入 $Q$（**注意符号**：正电荷→正电势，负电荷→负电势）
3. 多个电荷的 $V$ 是**代数叠加**（标量）

### 从 $V$ 求 $E$

$$E = -\frac{dV}{dr} \quad \text{或} \quad E = \frac{\Delta V}{\Delta d}$$

## Method 3: Motion of Charged Particles in Uniform Electric Field

### 步骤

1. 受力：$F = qE$
2. 加速度：$a = \frac{qE}{m}$
3. 运动分析：
   - 平行电场方向：$s = ut + \frac{1}{2}at^2$
   - 垂直电场方向：$s = vt$
4. 偏转量：与 $q/m$ 成正比，与 $v^2$ 成反比

## Method 4: Coulomb's Law Problems

### 步骤

1. 写出 $F = \frac{Q_1 Q_2}{4\pi \epsilon_0 r^2}$
2. 注意 $\frac{1}{4\pi \epsilon_0} = 8.99 \times 10^9$
3. $r$ 必须是中心到中心的距离
4. 力的方向：同号相斥，异号相吸
5. 当多个力存在时，矢量叠加
