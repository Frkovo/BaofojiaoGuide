---
title: "Topic 21 — Methods"
description: "9702 Physics 交流电解题方法"
---

# 解题方法 Solution Methods

## 1. 峰值与 r.m.s. 转换

$$V_0 = V_{\text{r.m.s.}} \times \sqrt{2}, \quad I_0 = I_{\text{r.m.s.}} \times \sqrt{2}$$

## 2. 功率计算

$$P_{\text{max}} = \frac{V_0^2}{R}, \quad \langle P \rangle = \frac{V_{\text{r.m.s.}}^2}{R} = \frac12 P_{\text{max}}$$

## 3. 整流电路分析

- **半波整流**: 单个二极管串联，只允许正半周通过
- **全波整流**: 四个二极管（桥式），负半周翻转成正半周
- **平滑**: 电容并联在负载两端，在峰值时充电，在下降时通过 $R$ 放电

## 4. 时间常数与指数放电

$$\tau = RC$$

$$V = V_0 e^{-t/\tau}$$

- $\tau$ 越大（更大的 $R$ 或 $C$）→ 放电越慢 → 平滑效果越好
- 但 $\tau$ 太大会导致放电不完全（无法跟踪峰值变化）

## 5. 从示波器图读频率

$$T = \text{每个周期的时间}, \quad f = \frac{1}{T}$$
