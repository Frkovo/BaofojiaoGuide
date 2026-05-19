---
title: "Topic 21 — Question Types"
description: "9702 Physics 交流电题型分析"
---

# 题型分析 Question Types

## 类型 A: 峰值 → r.m.s. → 功率计算

从 r.m.s. 电压求峰值功率或平均功率。

<details>
<summary>📝 MS 展开查看</summary>

**Example 1** (9702_w22_qp_41 Q7a): r.m.s. 4.2 V, 50 kHz, 电阻 760 $\Omega$

- **B1** peak voltage $= 4.2 \times \sqrt{2} = 5.9$ V
- **A1** $P_{\text{max}} = V^2/R = 5.9^2 / 760 = 0.046$ W (46 mW)
- **B1** line symmetrical about 23 mW → mean power = 23 mW

**Example 2** (9702_w22_qp_41 Q7a(ii)): 画功率-时间图

- **B1** sketch shows peak(s) in power at 46 mW
- **B1** correct shape (sinusoidal wave sitting on $t$-axis)
- **B1** four cycles, $P = 0$ at 0, 10, 20, 30, 40 $\mu$s

**Example 3**: 证明平均功率是最大功率的一半

- **B1** $P = V^2/R = (V_0^2\sin^2\omega t)/R$
- **B1** mean of $\sin^2\omega t = 1/2$
- **B1** therefore $\langle P \rangle = V_0^2/(2R) = \frac12 P_{\text{max}}$

</details>

## 类型 B: 整流电路 Rectification

<details>
<summary>📝 MS 展开查看</summary>

**Example 1** (9702_s23_qp_41 Q5a): 半波整流电路

- **B1** correct circuit symbol for a diode shown correctly connected in series (1)
- **B1** smoothing — $V_{\text{OUT}}$ is smoothed (1)

**Example 2** (9702_s23_qp_41 Q5c): 改造成全波整流

- **B1** $V_{\text{IN}}$ has constant magnitude in both positive and negative directions (1)
- **B1** $V_{\text{OUT}}$ is (now) constant — $V_{\text{OUT}}$ does not vary with time (1)

**Example 3** (9702_w24_qp_41 Q6a): 整流类型区别

- **B1** conversion (from a.c.) to d.c. (1)
- **B1** half-wave: voltage in one direction is removed (1)
- **B1** full-wave: voltage in one direction is reversed (1)

</details>

## 类型 C: 电容平滑 Smoothing

<details>
<summary>📝 MS 展开查看</summary>

**Example 1** (9702_s23_qp_41 Q5b): 电容平滑电路中求时间常数

$V = V_0 e^{-t/RC}$, $\tau = RC$
$3.25 = 5.50 \exp(-0.020/\tau)$ → $\tau = 0.038$ s

- **C1** $V = V_0 \exp(-t/RC)$ and $\tau = RC$
- **A1** $\tau = 0.038$ s

**Example 2** (9702_s23_qp_41 Q5b(iii)): 求电容值

$\tau = RC = 0.038$ s, $R = 14$ k$\Omega$

- **C1** $C = \tau/R$
- **A1** $C = 0.038 / 14000 = 2.7 \times 10^{-6}$ F

**Example 3** (9702_w24_qp_41 Q6c): 电容放电计算电阻

$8.0 = 12.0 \exp(-0.010/RC)$ → $R = 43$ $\Omega$

- **C1** $E = \frac12CV^2$
- **A1** $C = 2 \times 0.041 / 12^2 = 570$ $\mu$F
- **C1** $8.0 = 12.0 \exp(-0.010/RC)$
- **A1** $R = 43$ $\Omega$

</details>
