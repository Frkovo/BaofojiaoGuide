---
title: 考前速记
sidebar_position: 7
---

# 考前速记 — Linear Motion Under Variable Force

## 核心公式

| 公式 | 说明 |
|------|------|
| $F = ma = m\frac{dv}{dt}$ | Newton 第二定律 |
| $a = v\frac{dv}{dx}$ | 加速度（位移变量） |
| $v_T = \frac{mg}{k}$ | 极限速度（$kv$ 阻力） |
| $v_T = \sqrt{\frac{mg}{k}}$ | 极限速度（$kv^2$ 阻力） |

## 常用积分结果

| 情况 | 结果 |
|------|------|
| $\frac{dv}{dt} = g - kv$ | $v = \frac{g}{k}(1 - e^{-kt})$ |
| $\frac{dv}{dt} = -kv$ | $v = v_0 e^{-kt}$ |
| $\frac{dv}{dx} = -\frac{k}{m}v$ | $v = v_0 - \frac{kx}{m}$ |

## 易错点

- 积分后要加常数
- 阻力方向与运动方向相反
- 极限速度时 $a = 0$
- $a = v dv/dx$ 用于求 $v(x)$

## 解题策略

1. 写 $F = ma$
2. 选合适形式（$dv/dt$ 或 $v dv/dx$）
3. 分离变量
4. 积分 + 初始条件
