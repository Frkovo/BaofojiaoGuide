---
title: Common Mistakes
sidebar_position: 6
---

# Common Mistakes — Medical Physics

## Mistake 1: 混淆 ultrasound 和 X-ray 的产生方式

**错误**：认为 ultrasound 和 X-ray 都是用电子轰击靶产生。

**正确**：
- **Ultrasound**: piezoelectric crystal 在交变电压下机械振动产生
- **X-ray**: 电子被高电压加速后轰击金属靶产生

## Mistake 2: 忘记 gel 的作用原理

**错误**：认为 gel 用于润滑或冷却。

**正确**：gel 的 acoustic impedance 与人体组织相近，减少 ultrasound 在空气-皮肤界面的反射，使更多 ultrasound 进入体内。

## Mistake 3: $Z = \rho c$ 单位错误

**错误**：使用 kg m$^{-3}$ 作为 acoustic impedance 单位。

**正确**：$Z = \rho c$ 单位是 kg m$^{-2}$ s$^{-1}$（或 Rayl）。

## Mistake 4: 衰减公式指数符号错误

**错误**：$I = I_0 e^{\mu x}$（忘记负号）。

**正确**：$I = I_0 e^{-\mu x}$，强度随厚度指数衰减。

## Mistake 5: PET 中混淆 $\beta^+$ 和 $\beta^-$ 衰变

**错误**：认为 PET 使用 $\beta^-$ 衰变。

**正确**：PET 使用 $\beta^+$ 衰变（positron emission）。Positron 与 electron 发生 annihilation。

## Mistake 6: CT 和 PET 概念混淆

**错误**：认为 CT 和 PET 使用相同的物理原理。

**正确**：
- **CT**: 使用 X-ray 透射成像，从多角度扫描
- **PET**: 使用正电子湮灭产生的 gamma photon，检测符合事件

## Mistake 7: X-ray 硬度和强度控制混淆

**错误**：认为灯丝电流控制硬度，电压控制强度。

**正确**：
- **硬度 (hardness)**：由加速电压控制（电压越高，穿透力越强）
- **强度 (intensity)**：由灯丝电流控制（电流越大，光子越多）

## Mistake 8: 计算多层衰减时顺序错误

**错误**：直接使用总厚度乘以平均 $\mu$。

**正确**：$I = I_0 e^{-\mu_1 x_1} \times e^{-\mu_2 x_2} \times ...$，每层分别计算后相乘。
