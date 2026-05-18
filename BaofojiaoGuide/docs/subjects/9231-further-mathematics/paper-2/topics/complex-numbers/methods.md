---
title: 解题方法
sidebar_position: 4
---

# Methods — Complex Numbers

## de Moivre's theorem

$$(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$$

## Key substitutions

$$\cos\theta = \frac{z + z^{-1}}{2},\quad \sin\theta = \frac{z - z^{-1}}{2i}$$
$$z^n + z^{-n} = 2\cos n\theta,\quad z^n - z^{-n} = 2i\sin n\theta$$

## Multiple angle method

1. Expand $(\cos\theta + i\sin\theta)^n$ using binomial theorem
2. Equate real parts → $\cos n\theta$, imaginary → $\sin n\theta$
3. Replace $\sin^2\theta = 1 - \cos^2\theta$ to express in terms of $\cos\theta$ only

## Power reduction

Use $\cos\theta = (z+z^{-1})/2$, $\sin\theta = (z-z^{-1})/(2i)$ with $z = e^{i\theta}$
Expand and group as $z^n + z^{-n} = 2\cos n\theta$, $z^n - z^{-n} = 2i\sin n\theta$

## $C + iS$ method

$C + iS = \sum e^{i\theta_r}$ (geometric series) → sum GP → separate real/imaginary

## $n$th roots of unity

$z_k = e^{2\pi i k/n}$ for $k = 0,1,\ldots,n-1$. Sum of all roots $= 0$.
