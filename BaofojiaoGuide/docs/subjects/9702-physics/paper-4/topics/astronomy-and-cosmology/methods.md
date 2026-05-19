---
title: Solution Methods
sidebar_position: 4
---

# Solution Methods — Astronomy and Cosmology

## Method 1: Luminosity, flux, and distance

### 步骤
1. **确定已知量**：$L$, $F$, $d$ 中任意两个
2. **使用 inverse square law**：$F = L / (4\pi d^2)$
3. **求第三个量**：
   - $L = F \times 4\pi d^2$
   - $d = \sqrt{L / (4\pi F)}$

## Method 2: Stellar radius estimation

### 步骤
1. **Wien's law**：$\lambda_{\max} T = 2.9 \times 10^{-3}\text{ m K}$
   - 已知 $\lambda_{\max}$ → 求 $T$
   - 已知 $T$ → 求 $\lambda_{\max}$
2. **Stefan-Boltzmann law**：$L = 4\pi\sigma r^2 T^4$
   - 已知 $L$ 和 $T$ → 求 $r$
   - 已知 $r$ 和 $T$ → 求 $L$
   - 已知 $L$ 和 $r$ → 求 $T$
3. **结合使用**：有时需先用 $F = L / (4\pi d^2)$ 求 $L$

## Method 3: Redshift and Hubble constant

### 步骤
1. **计算 redshift**：$z = \Delta\lambda / \lambda = (\lambda_{\text{obs}} - \lambda_{\text{emit}}) / \lambda_{\text{emit}}$
2. **求 recessional speed**：$v \approx z \times c$
3. **Hubble's law**：$v = H_0 d$，求 $H_0$ 或 $d$
4. **宇宙年龄估计**：$t \approx 1 / H_0$

## Method 4: Standard candle

### 步骤
1. 确认天体是 standard candle（已知 $L$）
2. 在地球测量 $F$
3. 计算距离 $d = \sqrt{L / (4\pi F)}$
