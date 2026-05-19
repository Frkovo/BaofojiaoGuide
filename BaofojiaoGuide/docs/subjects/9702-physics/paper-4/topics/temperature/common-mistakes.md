---
title: 常见错误
sidebar_position: 6
---
# 常见错误 — Temperature

## 1. $\Delta T$ 和 $\Delta\theta$ 的关系

**错误**: 认为 $\Delta T$（K）和 $\Delta\theta$（°C）数值不同。

**正确**: **数值相同**，因为开尔文和摄氏度的刻度大小相同，只是零点不同。$T/K = \theta/°C + 273.15$ 但 $\Delta T/K = \Delta\theta/°C$。

**Fix**: 温度变化值在 K 和 °C 中一样。

## 2. 比热容定义混淆

**错误**: "specific heat capacity is the heat capacity per unit mass"（循环定义）。

**正确**: "energy per unit mass per unit temperature change" 或 "$Q = mc\Delta\theta$ where $c$ is specific heat capacity"。

**Fix**: 必须包含 energy/thermal energy, per unit mass, per unit temperature change。

## 3. 相变温度不变

**错误**: 认为熔解或汽化过程中温度也在升高。

**正确**: 相变过程中能量用于克服分子间作用力，温度**保持不变**。

**Fix**: 潜热不改变温度，能量用于改变分子的势能。

## 4. 比潜热 vs 比热容

**错误**: 混淆 $Q = mc\Delta\theta$ 和 $Q = mL$。

**正确**: 
- 温度变化 → 比热容 $c$
- 相变（温度不变）→ 比潜热 $L$

**Fix**: 看是否有温度变化。

## 5. 摄氏度与开尔文混淆

**错误**: 在 $pV = nRT$ 中使用摄氏度。

**正确**: 所有热力学公式中的温度必须用**开尔文(K)**。

**Fix**: 代入前先将 °C 转换为 K：$T = \theta + 273.15$。

## 6. 热量守恒忽略系统组件

**错误**: 只考虑主要物体的热量交换，忽略容器、温度计等。

**正确**: 容器（如烧杯）和温度计也参与热量交换。

**Fix**: 题目中提示 negligible heat capacity 时可以忽略，否则要考虑。
