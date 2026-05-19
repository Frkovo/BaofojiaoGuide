---
title: Capacitance — 解题方法
sidebar_position: 4
---

# Capacitance — 解题方法

## Method 1: Combined Capacitance

### 步骤

1. 识别串并联关系
   - 并联：两端直接连接，电压相同
   - 串联：首尾相连，电荷相同
2. 逐步化简复杂电路
   - 找到纯并联或纯串联的组合
   - 先化简最小单元的串/并联
   - 重复直到只剩一个电容
3. **注意**：电容的串并联公式与电阻相反

## Method 2: RC Discharge Calculations

### 步骤

1. 确定初始值：
   - $Q_0 = CV_0$
   - $I_0 = V_0 / R$
2. 时间常数：$\tau = RC$
3. 使用指数公式：
   - $x = x_0 e^{-t/\tau}$（$x$ = $Q$, $V$, 或 $I$）
4. 已知 $x$ 求 $t$：
   - $t = -\tau \ln(x/x_0)$
5. 已知 $t$ 求 $x$：
   - $x = x_0 e^{-t/\tau}$

## Method 3: Energy Stored

### 步骤

1. 根据已知量选择合适的公式：
   - 已知 $C$ 和 $V$：$W = \frac{1}{2} CV^2$
   - 已知 $Q$ 和 $V$：$W = \frac{1}{2} QV$
   - 已知 $Q$ 和 $C$：$W = \frac{1}{2} Q^2/C$
2. 注意单位：$C$ 的单位是 F，$V$ 是 V，$Q$ 是 C，$W$ 是 J

## Method 4: Switching/Charging and Discharging Circuits

### 步骤

1. 确定开关位置 → 确定是充电还是放电
2. 充电：$x = x_0 (1 - e^{-t/RC})$
3. 放电：$x = x_0 e^{-t/RC}$
4. 对反复充放电的电路：
   - 每次充电转移的电荷 $\Delta Q = CV$
   - 平均电流 $I_{\text{avg}} = \Delta Q \times f = fCV$
