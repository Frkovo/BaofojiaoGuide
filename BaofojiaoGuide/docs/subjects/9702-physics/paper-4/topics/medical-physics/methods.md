---
title: Solution Methods
sidebar_position: 4
---

# Solution Methods — Medical Physics

## Method 1: Acoustic impedance and reflection

### 步骤
1. **计算 $Z$**：$Z = \rho c$
   - $\rho$ = density (kg m$^{-3}$)
   - $c$ = speed of sound (m s$^{-1}$)
   - 单位：kg m$^{-2}$ s$^{-1}$
2. **计算反射系数**：
   - $\dfrac{I_R}{I_0} = \dfrac{(Z_2 - Z_1)^2}{(Z_2 + Z_1)^2}$
   - 值在 0（完全透射）到 1（完全反射）之间
3. **解释 gel 的作用**：
   - 无 gel：空气 ($Z \approx 400$) vs 皮肤 ($Z \approx 1.6 \times 10^6$)，$Z$ 相差巨大 → 几乎完全反射
   - 有 gel：gel 的 $Z$ 与组织相近 → 几乎完全透射

## Method 2: X-ray attenuation

### 步骤
1. **衰减公式**：$I = I_0 e^{-\mu x}$
   - $I_0$ = incident intensity
   - $\mu$ = linear attenuation coefficient
   - $x$ = thickness
2. **多层结构**：$I = I_0 e^{-\mu_1 x_1} \times e^{-\mu_2 x_2} \times ...$
3. **CT 原理**：
   - 多个角度扫描同一截面
   - 计算机重建 2D 截面图像
   - 沿轴移动重复，组合成 3D

## Method 3: PET scanning

### 步骤
1. **Tracer**：含有 $\beta^+$ 衰变核素的物质
2. **Annihilation**：$e^+ + e^- \rightarrow \gamma + \gamma$
3. **能量**：$E_{\text{photon}} = m_e c^2 = 8.2 \times 10^{-14}\text{ J}$
4. **动量守恒**：两个 gamma photon 方向相反
5. **探测**：检测器记录 photon 到达时间 → 确定 annihilation 位置 → 重建图像
