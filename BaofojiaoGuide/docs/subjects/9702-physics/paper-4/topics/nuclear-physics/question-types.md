---
title: Question Types
sidebar_position: 2
---

# Question Types — Nuclear Physics

## Question Type 1: Calculating binding energy and mass defect

### 如何识别
题目中出现 "binding energy", "mass defect", "energy released" 等关键词，通常给出核质量（以 u 或 kg 为单位）。

### 标准解题方法
:::note[标准解题方法]
1. 写出核反应方程式或确定核子组成
2. 计算质量亏损 $\Delta m = \sum m_{\text{初始}} - \sum m_{\text{终态}}$
3. 使用 $E = \Delta m c^2$ 转换为能量
4. 注意单位换算：$1\text{ u} = 1.66 \times 10^{-27}\text{ kg}$，$c = 3.00 \times 10^8\text{ m s}^{-1}$
5. $1\text{ MeV} = 1.60 \times 10^{-13}\text{ J}$
:::

### 评分标准
:::info[评分标准（MS 模式）]
- **C1**: 正确计算质量亏损 $\Delta m$
- **C1**: 代入 $E = \Delta m c^2$ 或使用 $E = \Delta m \times 931.5\text{ MeV u}^{-1}$
- **A1**: 正确答案（含单位）
- **B1**: 正确表述 binding energy 定义
:::

### 完整原题

**Example 1 — 9702/s24/qp/42 Q9(a)(b) (6 marks):**
> The mass of a nucleus of astatine-212 $({}^{212}_{85}\text{At})$ is 211.9907 u. (a) State what is meant by the binding energy of a nucleus. (b) The mass of a proton is 1.00728 u and the mass of a neutron is 1.00867 u. For ${}^{212}_{85}\text{At}$, calculate: (i) the mass defect $\Delta m$ in kg, (ii) the binding energy, (iii) the binding energy per nucleon.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: Binding energy is the energy required to separate a nucleus into its constituent protons and neutrons / energy released when nucleus is formed from its constituent protons and neutrons
- **C1**: mass defect = $(85 \times 1.00728 + 127 \times 1.00867) - 211.9907 = 1.8153\text{ u}$
- **C1**: $\Delta m = 1.8153 \times 1.66 \times 10^{-27} = 3.01 \times 10^{-27}\text{ kg}$
- **C1**: $E = 3.01 \times 10^{-27} \times (3.00 \times 10^8)^2$
- **A1**: $E = 2.71 \times 10^{-10}\text{ J}$
- **A1**: binding energy per nucleon $= 2.71 \times 10^{-10} / 212 = 1.28 \times 10^{-12}\text{ J}$
</details>

**Example 2 — 9702/s20/qp/41 Q11 (6 marks):**
> An electron, at rest, has mass $m$ and charge $-q$. A positron is a particle that, at rest, has mass $m$ and charge $+q$. A positron interacts with an electron. The electron and the positron may be considered to be at rest. The outcome of this interaction is that the electron and the positron become two gamma-ray photons, each having the same energy. (a) Calculate, for one of the gamma-ray photons: (i) the photon energy in J, (ii) its momentum. (b) State and explain the direction, relative to each other, in which the gamma-ray photons are emitted.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **C1**: $E = mc^2 = 9.11 \times 10^{-31} \times (3.0 \times 10^8)^2$
- **A1**: $E = 8.2 \times 10^{-14}\text{ J}$ per particle, so per photon $= 8.2 \times 10^{-14}\text{ J}$
- **C1**: $p = E / c = 8.2 \times 10^{-14} / (3.0 \times 10^8)$
- **A1**: $p = 2.7 \times 10^{-22}\text{ N s}$
- **B1**: total momentum before is zero, so momentum conserved requires photons to have equal and opposite momentum
- **B1**: photons emitted in opposite directions
</details>

**Example 3 — 9702/w23/qp/41 Q9(d) (4 marks):**
> A nucleus Z undergoes nuclear fission to form strontium-93 (${}^{93}_{38}\text{Sr}$) and xenon-139 (${}^{139}_{54}\text{Xe}$). The binding energies are: ${}^{93}\text{Sr} = 1.25 \times 10^{-10}\text{ J}$, ${}^{139}\text{Xe} = 1.81 \times 10^{-10}\text{ J}$. The fission of 1.00 mol of Z releases $1.77 \times 10^{13}\text{ J}$ of energy. Determine the binding energy per nucleon, in MeV, of Z.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **C1**: energy released per nucleus $= 1.77 \times 10^{13} / 6.02 \times 10^{23} = 2.94 \times 10^{-11}\text{ J}$
- **C1**: binding energy of Z $= (1.25 + 1.81) \times 10^{-10} - 2.94 \times 10^{-11} = 2.77 \times 10^{-10}\text{ J}$
- **C1**: number of nucleons in Z $= 93 + 139 = 232$
- **A1**: binding energy per nucleon $= 2.77 \times 10^{-10} / (232 \times 1.60 \times 10^{-13}) = 7.46\text{ MeV}$
</details>

---

## Question Type 2: Radioactive decay calculations ($A = \lambda N$, $x = x_0 e^{-\lambda t}$)

### 如何识别
题目涉及 activity、half-life、decay constant、number of undecayed nuclei，要求计算时间、数量或 activity。

### 标准解题方法
:::note[标准解题方法]
1. 确定已知量和未知量：$A$, $\lambda$, $N$, $t$, $t_{1/2}$
2. 使用 $A = \lambda N$ 关联 activity 和 number of nuclei
3. 使用 $\lambda = 0.693 / t_{1/2}$ 转换 half-life
4. 使用 $N = N_0 e^{-\lambda t}$ 或 $A = A_0 e^{-\lambda t}$ 计算衰变过程
5. 注意时间单位一致
:::

### 评分标准
:::info[评分标准（MS 模式）]
- **C1**: 正确使用 $A = \lambda N$ 或 $\lambda = \ln 2 / t_{1/2}$
- **C1**: 正确代入指数衰变公式
- **A1**: 正确答案（含单位）
:::

### 完整原题

**Example 1 — 9702/w20/qp/41 Q12 (9 marks):**
> Iodine-131 (${}^{131}_{53}\text{I}$) is a radioactive isotope with a decay constant of $9.9 \times 10^{-7}\text{ s}^{-1}$. (a) State what is meant by: (i) radioactive, (ii) decay constant. (b) Some water becomes contaminated with iodine-131. The activity of the iodine-131 in 1.0 kg of water is 560 Bq. Determine the number of iodine-131 atoms in 1.0 kg of water. (c) Regulations require that the activity of iodine-131 in 1.0 kg of water is to be less than 170 Bq. Calculate the time, in days, for the activity of the contaminated water to be reduced to 170 Bq.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a)(i) unstable nucleus emits ionising radiation / decays spontaneously
- **M1**: (a)(ii) probability of decay (of a nucleus) per unit time
- **A1**: (a)(ii) correct definition
- **C1**: (b) $A = \lambda N$, so $560 = 9.9 \times 10^{-7} \times N$
- **A1**: $N = 5.7 \times 10^8$
- **C1**: (c) $A = A_0 e^{-\lambda t}$, $170 = 560 \exp(-9.9 \times 10^{-7} \times t)$
- **C1**: $t = 1.2 \times 10^6\text{ s}$
- **A1**: $t = 14\text{ days}$
</details>

**Example 2 — 9702/s20/qp/41 Q12 (6 marks):**
> A radioactive isotope X has a half-life of 1.4 hours. Initially, a pure sample of this isotope X has an activity of $3.6 \times 10^5\text{ Bq}$. (a) Explain what is meant by the decay being: (i) random, (ii) spontaneous. (b) Determine the activity of the isotope X in the sample after a time of 2.0 hours.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a)(i) time at which a nucleus will decay cannot be predicted / constant probability of decay
- **B1**: (a)(ii) decay not affected by environmental factors
- **C1**: (b) $A = A_0 e^{-\lambda t}$ and $\lambda = \ln 2 / t_{1/2}$
- **C1**: $A = 3.6 \times 10^5 \times \exp[-(2 \times \ln 2) / 1.4]$ or $A = A_0 \times 0.5^{N}$ where $N = 2 / 1.4$
- **A1**: $A = 1.3 \times 10^5\text{ Bq}$
</details>

**Example 3 — 9702/w22/qp/41 Q10 (10 marks):**
> Carbon-15 (${}^{15}_{6}\text{C}$) undergoes radioactive decay to nitrogen-15 (${}^{15}_{7}\text{N}$). (a) State what is meant by: (i) random, (ii) spontaneous. (b) A small sample of carbon-15 decays. The mass M of carbon-15 in the sample decreases with time t. Fig 10.1 shows the variation with t of ln(M / 10^{-16} g). (i) State how Fig. 10.1 demonstrates that radioactive decay is random. (iii) Show that the decay constant $\lambda$ of carbon-15 is given by the magnitude of the gradient of your line. (iv) Use your line to determine $\lambda$. (v) Calculate the half-life of carbon-15.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a)(i) cannot predict when a (particular) nucleus will decay
- **B1**: (a)(ii) not affected by external / environmental factors
- **B1**: (b)(i) line fluctuates
- **B1**: (b)(iii) $M = M_0 \exp(-\lambda t)$ so $\ln M = \ln M_0 - \lambda t$, gradient $= -\lambda$
- **C1**: (b)(iv) gradient $= (8.0 - 4.8) / (11.6 - 0)$
- **A1**: $\lambda = 0.28\text{ s}^{-1}$
- **A1**: (b)(v) half-life $= 0.693 / 0.28 = 2.5\text{ s}$
</details>

---

## Question Type 3: Binding energy per nucleon graph (fusion and fission)

### 如何识别
题目给出 binding energy per nucleon vs nucleon number 图表，要求标注 fusion/fission 区域，或解释能量释放。

### 标准解题方法
:::note[标准解题方法]
1. 曲线形状：先上升（轻核），在 $A \approx 56$（铁）处达到最大值，然后缓慢下降（重核）
2. Fusion：轻核结合→生成物 binding energy per nucleon 更大→释放能量
3. Fission：重核分裂→生成物 binding energy per nucleon 更大→释放能量
4. 能量释放 = 反应后总 binding energy - 反应前总 binding energy
:::

### 评分标准
:::info[评分标准（MS 模式）]
- **B1**: binding energy per nucleon 最大的核最稳定（铁附近）
- **B1**: fusion 和 fission 都导致 binding energy per nucleon 增加
- **B1**: 曲线正确标注 fusion 区域（轻核端）和 fission 区域（重核端）
:::

### 完整原题

**Example 1 — 9702/w23/qp/41 Q9(b)(c) (4 marks):**
> (b) On Fig. 9.1, sketch the variation of binding energy per nucleon with nucleon number A for stable nuclei. (c) Label with (i) a point X that could represent a nucleus that undergoes nuclear fission, (ii) a point Y that could represent a nucleus that undergoes nuclear fusion.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: correct shape (steep rise from low A, broad peak around A = 50-60, gradual decrease for high A)
- **B1**: line does not return to 0 binding energy
- **B1**: point X on right-hand side (high A) of peak
- **B1**: point Y on left-hand side (low A) of peak
</details>

**Example 2 — 9702/s24/qp/42 Q9(c) (4 marks):**
> (c)(i) On Fig. 9.1, sketch the variation with nucleon number A of binding energy per nucleon. (ii) State what the graph indicates about the stability of nuclei. (iii) Polonium-212 is radioactive and undergoes alpha-decay. Explain why energy is released in this decay with reference to the binding energy per nucleon of the nuclei involved.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: correct sketch shape
- **B1**: binding energy per nucleon is greatest for intermediate nucleon numbers (most stable at A ≈ 56)
- **B1**: polonium-212 (high A) has lower binding energy per nucleon
- **B1**: decay products have greater binding energy per nucleon, so energy is released
</details>

---

## Question Type 4: Defining terms (half-life, decay constant, random, spontaneous)

### 如何识别
直接问 "State what is meant by..." 各种核物理术语。

### 标准答案模板
:::note[定义模板]
- **Half-life**: time for activity / number of undecayed nuclei to decrease to half its initial value
- **Decay constant**: probability of decay of a nucleus per unit time
- **Random**: cannot predict when a particular nucleus will decay / constant probability of decay
- **Spontaneous**: not affected by external / environmental factors
- **Binding energy**: energy required to separate a nucleus into its constituent protons and neutrons
- **Mass defect**: difference between the mass of a nucleus and the sum of the masses of its constituent nucleons
:::

### 完整原题

**Example 1 — 9702/w20/qp/41 Q12(a) (4 marks):**
> (a) State what is meant by: (i) radioactive, (ii) decay constant.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a)(i) unstable nucleus emits ionising radiation / decays spontaneously
- **M1**: (a)(ii) probability of decay (of a nucleus)
- **A1**: per unit time
</details>

**Example 2 — 9702/s23/qp/41 Q9(a) (1 mark):**
> (a) Define half-life.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: time for activity (of sample) to halve
</details>
