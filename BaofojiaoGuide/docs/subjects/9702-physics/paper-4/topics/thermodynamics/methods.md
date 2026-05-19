---
title: Thermodynamics — 解题方法
sidebar_position: 4
---

# Thermodynamics — 解题方法

## Method 1: First Law Sign Convention

### 步骤

1. 确定问题中的 $q$ 和 $W$ 的符号
   - $q$: 系统吸热 → $+$；系统放热 → $-$
   - $W$: 对系统做功 → $+$；系统对外做功 → $-$
2. 代入 $\Delta U = q + W$
3. 解出未知量

### 记忆技巧

- "GAS" rule: **G**as **A**dds to **S**ystem = $+$ sign
- 如果系统在膨胀（volume increases），气体对 piston 做功，所以 $W$ 是负的
- 如果系统被压缩（volume decreases），piston 对气体做功，所以 $W$ 是正的

## Method 2: Work Done from $p$-$V$ Graph

### 步骤

1. 确定过程是否等压（水平线）
   - 如果 $p$ 不变，$W = p\Delta V$
2. 如果 $p$ 变化，计算图形面积
   - 矩形：$\text{area} = p\Delta V$
   - 三角形：$\text{area} = \frac{1}{2}\Delta p \Delta V$
   - 其他形状：分割求和
3. 确定符号
   - 右移（$V$ 增大）：气体对外做功 → $W$ 负
   - 左移（$V$ 减小）：外界对气体做功 → $W$ 正

## Method 3: Internal Energy Change for Ideal Gas

### 步骤

1. 对理想气体，$U$ 只取决于温度
   $$\Delta U = \frac{3}{2} Nk \Delta T = \frac{3}{2} nR \Delta T$$
2. 如果温度不变 → $\Delta U = 0$
3. 循环过程 → $\Delta U_{\text{total}} = 0$

## Method 4: Complete the Table Questions

### 步骤

1. 逐行填写已知值
2. 对每一行，用 $\Delta U = q + W$ 求未知值
3. 检查：循环过程中所有行的 $\Delta U$ 之和 = 0
4. 检查：循环过程中所有行的 $q$ 之和 = -（所有行的 $W$ 之和）
