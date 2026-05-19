---
title: Thermodynamics — 考纲逐点解读
sidebar_position: 3
---

# Thermodynamics — 考纲逐点解读

## 16.1 Internal energy

### 1. Understand that internal energy is determined by the state of the system and that it can be expressed as the sum of a random distribution of kinetic and potential energies associated with the molecules of a system

- **Internal energy** 是系统内部所有分子随机运动的**动能**和分子间相互作用的**势能**的总和
- 内能是**状态函数**（state function）——只取决于系统的当前状态（$T$、$p$、$V$），与路径无关
- "Random distribution" 强调分子的运动是随机的、无规则的
- 内能的变化 $\Delta U$ 只取决于初末状态，与过程无关

### 2. Relate a rise in temperature of an object to an increase in its internal energy

- 温度升高 → 分子平均动能增大 → 内能增大
- 注意：相变（如熔化、沸腾）时温度不变，但内能仍增加（因为分子势能增加）
- 对**理想气体**：$U = \frac{3}{2}NkT$，只与温度有关（无分子间势能）

## 16.2 The first law of thermodynamics

### 1. Recall and use $W = p\Delta V$ for the work done when the volume of a gas changes at constant pressure and understand the difference between the work done by the gas and the work done on the gas

- $W = p\Delta V$ 仅在**等压过程**（constant pressure）中适用
- **Work done by gas**（气体对外做功）：气体膨胀 $\Delta V > 0$，气体对活塞做功
- **Work done on gas**（外界对气体做功）：气体压缩 $\Delta V < 0$，活塞对气体做功
- 在 $p$-$V$ 图上，曲线下方的面积 = 功的大小
- 对非等压过程，功 = $\int p\,dV$（$p$-$V$ 图面积）

### 2. Recall and use the first law of thermodynamics $\Delta U = q + W$ expressed in terms of the increase in internal energy, the heating of the system (energy transferred to the system by heating) and the work done on the system

- $\Delta U = q + W$ 是能量守恒在热力学中的表述
- **符号约定**：
  - $+q$：系统**吸收**热量（thermal energy **to** system）
  - $-q$：系统**放出**热量
  - $+W$：对系统**做功**（work done **on** system）
  - $-W$：系统对外界**做功**
- **常见特殊情况**：
  - 等体过程（isochoric）：$V$ 不变 → $W = 0$ → $\Delta U = q$
  - 等压过程（isobaric）：$p$ 不变 → $W = p\Delta V$（注意符号）
  - 等温过程（isothermal）：$T$ 不变 → $\Delta U = 0$ → $q = -W$
  - 绝热过程（adiabatic）：$q = 0$ → $\Delta U = W$
  - 循环过程（cyclic）：返回初态 → $\Delta U = 0$ → $q = -W$
