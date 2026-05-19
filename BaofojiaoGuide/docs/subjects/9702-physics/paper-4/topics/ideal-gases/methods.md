---
title: 解题方法
sidebar_position: 4
---
# 解题方法 — Ideal Gases

## Method 1: 理想气体状态方程 ($pV = nRT$ 或 $pV = NkT$)

### When to use
已知 $p$, $V$, $T$ 中部分量，求未知量。或求分子数 $N$、摩尔数 $n$。

### Steps
1. 确认温度是否已转换为开尔文(K)
2. 选择适合的形式：
   - 已知摩尔数 → $pV = nRT$
   - 已知分子数 → $pV = NkT$
3. 代入求解
4. 注意单位：$p$ in Pa, $V$ in m$^3$, $T$ in K

### Formula
$$pV = nRT$$
$$pV = NkT$$
$$k = \frac{R}{N_A} = 1.38 \times 10^{-23}\text{ J K}^{-1}$$

### Mistakes to avoid
- 温度必须用开尔文(K)：$T = \theta + 273.15$
- $n$ 是摩尔数，$N = nN_A$
- 体积单位：1 m$^3$ = $10^6$ cm$^3$

## Method 2: 气体动理论方程

### When to use
涉及分子均方根速度、压强与分子运动的关系。

### Steps
1. $pV = \frac13 Nm\langle c^2\rangle$
2. 若求 $c_{\text{r.m.s.}}$：$c_{\text{r.m.s.}} = \sqrt{\langle c^2\rangle}$
3. 结合 $pV = NkT$ 可消去 $pV$

### Formula
$$pV = \frac13 Nm\langle c^2\rangle$$
$$c_{\text{r.m.s.}} = \sqrt{\langle c^2\rangle}$$
$$\frac12 m\langle c^2\rangle = \frac32 kT$$

### Mistakes to avoid
- $\langle c^2\rangle$ 是 mean-**square** speed，不是 (mean speed)$^2$
- $m$ 是单个**分子**质量，不是总质量
- $N$ 是分子总数

## Method 3: 分子平均动能

### When to use
求分子平均动能、温度与分子速度的关系。

### Steps
1. 平均平动动能 $\langle E_K \rangle = \frac32 kT$
2. 每个分子：$\frac12 m\langle c^2\rangle = \frac32 kT$
3. 总内能（单原子理想气体）：$U = N \cdot \frac32 kT = \frac32 nRT$

### Formula
$$\langle E_K \rangle = \frac32 kT$$
$$U = \frac32 NkT = \frac32 nRT$$

### Mistakes to avoid
- $\frac32 kT$ 是每个分子的平均**平动**动能
- 单原子理想气体的内能只含动能
- $U = \frac32 nRT$ 只适用于单原子理想气体
