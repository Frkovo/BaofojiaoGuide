---
title: 题型分析
sidebar_position: 2
---
# 题型分析 — Temperature

## Question Type 1: 温标与测温性质

### 如何识别
问 thermometric property 的例子，或解释为什么某种温度计不能测量 thermodynamic temperature。

### 标准解题方法
:::note[概念要点]
Thermometric property: a physical property that varies with temperature.
Examples: density of liquid, volume of gas at constant pressure, resistance of metal, e.m.f. of thermocouple.

Thermodynamic temperature: independent of the property of any particular substance.
:::

### 评分标准
:::info[评分]
- **B1/B2**: 列举测温性质（每个1分）
- **B1**: depends on properties of real substance
- **B1**: 0 °C is not absolute zero
:::

### 完整原题

**Example 1 — 9702_w22_qp_41 (5 marks):**
> (a) State two other physical properties of materials, apart from the density of a liquid, that can be used for measuring temperature.
> (c)(i) Explain why the thermometer does not provide a direct measurement of thermodynamic temperature.
> (ii) Name the type of substance for which $T$ is proportional to the product of pressure and volume.

<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **B1**: resistance of a metal
- **B1**: volume of a gas at constant pressure / e.m.f. of a thermocouple
- **B1**: depends on properties of a real substance
- **B1**: 0 °C is not absolute zero
- **B1**: ideal gas
</details>

**Example 2 — 9702_s24_qp_41 (4 marks):**
> (a)(i) State the magnitude and unit of absolute zero on the thermodynamic temperature scale.
> (ii) Explain why temperature measured using a laboratory liquid-in-glass thermometer does not give a direct measurement of thermodynamic temperature.
> (b)(iii) Suggest a type of thermometer suitable for measuring a rapidly changing temperature.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **B1**: 0 K
- **B1**: -273 °C
- **B1**: depends on property of liquid / depends on property of a real substance
- **B1**: thermocouple
</details>

### 常见陷阱
:::warning[注意]
- 列举测温性质时不要重复
- "ideal gas" 是 thermodynamic temperature 的标准物质
- 温度计测量需要达到热平衡（需要时间）
:::

## Question Type 2: 比热容计算

### 如何识别
给出加热功率、质量、温度变化，求比热容。

### 标准解题方法
:::note[方法]
1. $Q = Pt$（电能转化为热能）
2. $Q = mc\Delta\theta$
3. 联立求解
4. 注意热损失对结果的影响
:::

### 评分标准
:::info[评分]
- **C1**: $Q = Pt$ 或 $Q = mc\Delta\theta$
- **C1**: $Q_{\text{lost}} = Q_{\text{gained}}$
- **A1**: 数值正确
:::

### 完整原题

**Example 1 — 9702_s23_qp_41 (8 marks):**
> A beaker of mass 42 g and specific heat capacity 0.84 J g$^{-1}$ K$^{-1}$ contains 180 g of liquid. An electrical heater of power 810 W heats the liquid. The temperature rises from 22.5 °C to 35.0 °C in 28 s. Determine the specific heat capacity of the liquid.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $Q = Pt = 810 \times 28$
- **C1**: $= 22680$ J
- **C1**: $Q = m_l c_l \Delta\theta + m_b c_b \Delta\theta$
- **C1**: $22680 = 180 \times c_l \times 12.5 + 42 \times 0.84 \times 12.5$
- **A1**: $c_l = 10.1 - 0.352 = 9.8$ J g$^{-1}$ K$^{-1}$ (需约 4 s.f.)
- **B1**: 最终答案带单位
</details>

**Example 2 — 9702_w22_qp_41 (4 marks):**
> A mercury thermometer initially at 23.0 °C is inserted into water at 37.4 °C. Mass of water = 18.7 g, specific heat capacity of water = 4.18 J g$^{-1}$ K$^{-1}$. Mass of mercury = 6.94 g, specific heat capacity of mercury = 0.140 J g$^{-1}$ K$^{-1}$. The glass has negligible heat capacity. Calculate the final steady temperature.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **C1**: $Q = mc\Delta\theta$
- **C1**: $Q_{\text{lost by water}} = Q_{\text{gained by mercury}}$
- **C1**: $18.7 \times 4.18 \times (37.4 - T) = 6.94 \times 0.140 \times (T - 23.0)$
- **A1**: $T = 37.1$ °C
</details>

### 常见陷阱
:::warning[注意]
- 容器也吸热！
- 温度变化 $\Delta\theta$ 在 K 和 °C 中数值相同
- 注意单位一致：J g$^{-1}$ K$^{-1}$ 还是 J kg$^{-1}$ K$^{-1}$
- 热损失导致计算值偏小
:::

## Question Type 3: 比潜热

### 如何识别
涉及相变（熔解、汽化）的热量计算。

### 标准解题方法
:::note[方法]
1. 相变时温度不变
2. $Q = mL$
3. 如包含升温和相变，分两步
:::

### 评分标准
:::info[评分]
- **B1**: definition: energy per unit mass (during change of state)
- **C1**: $Q = mL$
- **A1**: 数值正确
:::

### 完整原题

**Example 1 — 9702_s22_qp_42 (4 marks):**
> (a) Define specific latent heat of vaporisation.
> (b) The specific latent heat of vaporisation of water at atmospheric pressure is $2.3 \times 10^6$ J kg$^{-1}$. Calculate the thermal energy required to vaporise 0.015 kg of water at 100 °C.
<details>
<summary>📝 MS 展开查看</summary>
**MS:**
- **M1**: energy per unit mass
- **A1**: during change of state (at constant temperature)
- **C1**: $Q = mL$
- **C1**: $= 0.015 \times 2.3 \times 10^6$
- **A1**: $= 3.45 \times 10^4$ J
</details>

### 常见陷阱
:::warning[注意]
- 相变时温度不变
- 区分 fusion（固液）和 vaporisation（液气）
- 定义题必须包含 "during change of state" 或 "at constant temperature"
:::
