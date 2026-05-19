---
title: 解题方法
sidebar_position: 4
---
# 解题方法 — Temperature

## Method 1: 比热容计算 ($Q = mc\Delta\theta$)

### When to use
物体吸收/放出热量导致温度变化，求热量、质量、比热容或温度变化。

### Steps
1. 确定初始温度和最终温度
2. 计算 $\Delta\theta$（注意：K 和 °C 数值变化相同）
3. 用 $Q = mc\Delta\theta$
4. 注意热量守恒：$Q_{\text{lost}} = Q_{\text{gained}}$（无热损失时）

### Formula
$$Q = mc\Delta\theta$$

### Mistakes to avoid
- 温度变化 $\Delta\theta$ 的单位 K 和 °C 数值相同
- 热量守恒方程中注意符号（失去为负，获得为正）

## Method 2: 热量守恒（混合法）

### When to use
两个不同温度的物体混合，达到热平衡。

### Steps
1. 高温物体放热：$Q_{\text{lost}} = m_1c_1(\theta_1 - \theta_f)$
2. 低温物体吸热：$Q_{\text{gained}} = m_2c_2(\theta_f - \theta_2)$
3. $Q_{\text{lost}} = Q_{\text{gained}}$（假设绝热）
4. 解出 $\theta_f$

### Formula
$$m_1c_1(\theta_1 - \theta_f) = m_2c_2(\theta_f - \theta_2)$$

### Mistakes to avoid
- 忽略容器（如烧杯）也会吸热
- 温度计本身也会吸热影响结果

## Method 3: 比潜热计算 ($Q = mL$)

### When to use
物质在相变（熔解/凝固、汽化/液化）过程中吸收/放出的热量。

### Steps
1. 判断相变类型（fusion 或 vaporisation）
2. $Q = mL$
3. 若同时有升温和相变，分步计算
4. 总热量 = 升温热量 + 相变潜热

### Formula
$$Q = mL$$
specific latent heat of fusion: 固-液相变
specific latent heat of vaporisation: 液-气相变

### Mistakes to avoid
- 相变过程中**温度不变**（潜热不改变温度）
- 识别 fusion 和 vaporisation
- 注意单位：$c$ 可能是 J g$^{-1}$ K$^{-1}$ 或 J kg$^{-1}$ K$^{-1}$
