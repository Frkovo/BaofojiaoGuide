---
title: 常见错误
sidebar_position: 6
---
# 常见错误 — Ideal Gases

## 1. 温度未转换为开尔文

**错误**: 在 $pV = nRT$ 中使用摄氏度。

**正确**: 必须用 $T = \theta + 273.15$ 转换成开尔文。

**Fix**: 所有热力学方程中温度单位都是 K。

## 2. 混淆 $n$ 和 $N$

**错误**: $n$ 是分子数。

**正确**: $n$ 是**摩尔数**(number of moles)，$N$ 是**分子数**。$N = nN_A$，其中 $N_A = 6.02 \times 10^{23}$ mol$^{-1}$。

**Fix**: $pV = nRT$ 用摩尔数，$pV = NkT$ 用分子数。

## 3. 混淆 $\langle c^2\rangle$ 和 $c_{\text{r.m.s.}}$

**错误**: 认为 $\langle c^2\rangle$ 是 r.m.s. speed。

**正确**: $\langle c^2\rangle$ 是 mean-square speed（速度平方的平均值），$c_{\text{r.m.s.}} = \sqrt{\langle c^2\rangle}$ 才是 r.m.s. speed。

**Fix**: $\langle c^2\rangle$ 是平方后平均，r.m.s. 是开方后的值。

## 4. 理想气体分子内能

**错误**: 认为理想气体有分子势能。

**正确**: 理想气体分子间无作用力，所以**无势能**。内能 = 总动能。

**Fix**: 理想气体内能 $U = \frac32 NkT = \frac32 nRT$（单原子）。

## 5. 气体动理论假设遗漏

**错误**: 只列出1-2个假设。

**正确**: 需要至少列出3-4个基本假设：
- 分子做随机运动
- 碰撞完全弹性
- 分子间无作用力
- 分子体积可忽略
- 碰撞是瞬时的

**Fix**: 考试时列出4个假设确保满分。

## 6. 推导 $pV = \frac13 Nm\langle c^2\rangle$ 时混淆维度

**错误**: 认为 $\langle c^2\rangle = \langle c_x^2\rangle$。

**正确**: 三维中 $\langle c^2\rangle = \langle c_x^2\rangle + \langle c_y^2\rangle + \langle c_z^2\rangle = 3\langle c_x^2\rangle$。

**Fix**: 一维到三维的因子是 $\frac13$。
