---
title: Oscillations — 考纲逐点解读
sidebar_position: 3
---

# Oscillations — 考纲逐点解读

## 17.1 Simple harmonic oscillations

### 1. Understand and use displacement, amplitude, period, frequency, angular frequency and phase difference in context of oscillations; express period in terms of both frequency and angular frequency

- **Displacement $x$**: 从平衡位置到当前位置的位移
- **Amplitude $x_0$**: 最大位移大小
- **Period $T$**: 完成一次完整振动所需时间（单位：s）
- **Frequency $f$**: 单位时间内振动次数（单位：Hz）
  $$f = \frac{1}{T}$$
- **Angular frequency $\omega$**: 角频率
  $$\omega = 2\pi f = \frac{2\pi}{T}$$
- **Phase difference**: 两个振动在时间上的偏移（单位：rad 或 $\pi$）

### 2. Understand that SHM occurs when acceleration is proportional to displacement from a fixed point and in the opposite direction

- SHM 的定义条件：
  $$a \propto -x$$
- 比例常数是 $\omega^2$：
  $$a = -\omega^2 x$$

### 3. Use $a = -\omega^2 x$ and $x = x_0 \sin \omega t$

- $x = x_0 \sin \omega t$ 是微分方程 $a = -\omega^2 x$ 的解
- 当 $t = 0$ 时 $x = 0$（从平衡位置开始），速度最大
- 如果 $t = 0$ 时 $x = x_0$（从极端位置开始），用 $x = x_0 \cos \omega t$

### 4. Use $v = v_0 \cos \omega t$ and $v = \pm \omega \sqrt{x_0^2 - x^2}$

- $v_0 = \omega x_0$（最大速度出现在平衡位置）
- $v = v_0 \cos \omega t = \omega x_0 \cos \omega t$（当 $x = x_0 \sin \omega t$）
- $v = \pm \omega \sqrt{x_0^2 - x^2}$ 不依赖时间

### 5. Analyse and interpret graphical representations of $x$, $v$, $a$ for SHM

- $x$-$t$ 图：正弦/余弦曲线
- $v$-$t$ 图：余弦（相位领先 $x$ 为 $\pi/2$）
- $a$-$t$ 图：负正弦（与 $x$ 反相，领先 $v$ 为 $\pi/2$）
- $v$-$x$ 图：椭圆
- 关键关系：
  - $x$ 最大 → $v = 0$ → $a$ 最大（反向）
  - $x = 0$ → $v$ 最大 → $a = 0$

## 17.2 Energy in simple harmonic motion

### 1. Describe the interchange between kinetic and potential energy during SHM

- **平衡位置** ($x = 0$)：$E_K$ 最大，$E_P = 0$
- **极端位置** ($x = \pm x_0$)：$E_K = 0$，$E_P$ 最大
- 过程中 $E_K$ 和 $E_P$ 相互转换，**总能量守恒**

### 2. Recall and use $E = \frac{1}{2} m \omega^2 x_0^2$ for total energy

- 总能量 $E = E_{K,\max} = \frac{1}{2} m v_0^2 = \frac{1}{2} m \omega^2 x_0^2$
- 任意位置：$E = \frac{1}{2} m v^2 + \frac{1}{2} m \omega^2 x^2$

## 17.3 Damped and forced oscillations, resonance

### 1. Understand that a resistive force acting on an oscillating system causes damping

- Damping 是**阻力**（resistive force）导致的能量耗散
- 阻尼使振幅逐渐减小，机械能转化为内能

### 2. Understand and use terms light, critical and heavy damping; sketch displacement–time graphs

- **Light damping**: 振幅指数衰减，周期略长
- **Critical damping**: 最快回到平衡位置，不振荡
- **Heavy damping**: 缓慢回到平衡位置（可能不回到），不振荡

### 3. Understand that resonance involves maximum amplitude; occurs when an oscillating system is forced to oscillate at its natural frequency

- **Natural frequency $f_0$**: 系统自由振荡的频率
- **Forced oscillations**: 外力驱动系统振动
- **Resonance**: $f_{\text{driving}} = f_0$ 时振幅最大
- 阻尼越小，共振峰越尖锐
