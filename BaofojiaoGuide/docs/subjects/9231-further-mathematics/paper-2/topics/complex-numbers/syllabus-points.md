---
title: 考纲要点
sidebar_position: 2
---

# Complex Numbers — 考纲要点

## 1. de Moivre 定理
$(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$（整数 $n$）

## 2. 归纳法证明
Base $n=1$ → 假设 $n=k$ → 乘 $(\cos\theta+i\sin\theta)$ → 和角公式 → $n=k+1$

## 3. 倍角公式
展开 $(\cos\theta+i\sin\theta)^n$ → 实部得 $\cos n\theta$，虚部得 $\sin n\theta$

## 4. 降幂
设 $z = e^{i\theta}$，$\cos\theta = \frac{z+z^{-1}}{2}$，$\sin\theta = \frac{z-z^{-1}}{2i}$
展开后用 $z^n \pm z^{-n} = 2\cos n\theta$ 或 $2i\sin n\theta$ 归并

## 5. $C+iS$ 求和
$C+iS = \sum e^{i\theta_r}$ → 等比数列求和 → 分离实部虚部

## 6. $n$ 次单位根
$z_k = e^{2\pi i k/n}$，$k=0,1,\ldots,n-1$
所有根之和 $= 0$，所有根之积 $= (-1)^{n-1}$
