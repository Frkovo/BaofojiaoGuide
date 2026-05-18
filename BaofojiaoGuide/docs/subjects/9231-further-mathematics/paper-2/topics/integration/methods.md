---
title: 解题方法
sidebar_position: 4
---

# Methods — Integration

## Standard inverse integrals

$$\int\frac{dx}{\sqrt{a^2-x^2}} = \sin^{-1}\frac{x}{a} + C$$
$$\int\frac{dx}{a^2+x^2} = \frac{1}{a}\tan^{-1}\frac{x}{a} + C$$
$$\int\frac{dx}{\sqrt{x^2+a^2}} = \sinh^{-1}\frac{x}{a} + C$$
$$\int\frac{dx}{\sqrt{x^2-a^2}} = \cosh^{-1}\frac{x}{a} + C$$

## Common substitution choices

| Integrand contains | Try substitution |
|--------------------|-----------------|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ |
| $\sqrt{x^2 + a^2}$ | $x = a\sinh u$ |
| $\sqrt{x^2 - a^2}$ | $x = a\cosh u$ |
| $x^2 + a^2$ | $x = a\tan\theta$ |

## Reduction formulae

Integration by parts → $I_n$ in terms of $I_{n-1}$ or $I_{n-2}$

## Arc length

Cartesian: $s = \int_a^b \sqrt{1 + (\frac{dy}{dx})^2}\,dx$

Parametric: $s = \int_{t_1}^{t_2} \sqrt{(\frac{dx}{dt})^2 + (\frac{dy}{dt})^2}\,dt$

## Surface area of revolution

$$S = 2\pi\int_a^b y\sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx$$

Don't forget the extra $2\pi y$ factor!

## Rectangle bounds

Upper bound (right rectangles): $\frac{1}{n}\sum_{r=1}^n f(\frac{r}{n})$
Lower bound (left rectangles): $\frac{1}{n}\sum_{r=0}^{n-1} f(\frac{r}{n})$
