---
title: Question Types
sidebar_position: 2
---

# Question Types — Medical Physics

## Question Type 1: Specific acoustic impedance and intensity reflection coefficient

### 如何识别
题目给出密度 $\rho$ 和声速 $c$，要求计算 $Z = \rho c$ 和 intensity reflection coefficient $I_R / I_0$。

### 标准解题方法
:::note[标准解题方法]
1. $Z = \rho c$，单位 kg m$^{-2}$ s$^{-1}$
2. $\dfrac{I_R}{I_0} = \dfrac{(Z_{\text{介质1}} - Z_{\text{介质2}})^2}{(Z_{\text{介质1}} + Z_{\text{介质2}})^2}$
3. $Z$ 相近 → reflection 小（transmission 大）
4. $Z$ 相差大 → reflection 大
:::

### 评分标准
:::info[评分标准（MS 模式）]
- **C1**: 正确代入 $Z = \rho c$
- **C1**: 正确代入反射系数公式
- **A1**: 数值答案
- **B1**: 解释 gel 的作用
:::

### 完整原题

**Example 1 — 9702/s23/qp/41 Q8 (8 marks):**
> Table shows data for air, gel and tissue: air ($\rho = 1.29\text{ kg m}^{-3}$, $c = 340\text{ m s}^{-1}$), gel ($\rho = 1200\text{ kg m}^{-3}$, $c = 1400\text{ m s}^{-1}$), tissue ($\rho = 1090\text{ kg m}^{-3}$, $c = ?$). (a)(i) Show that specific acoustic impedance of gel is $1.68 \times 10^6\text{ kg m}^{-2}\text{ s}^{-1}$. (ii) Complete table. (b) Calculate intensity reflection coefficient for: (i) air-tissue boundary, (ii) gel-tissue boundary. (c) Explain why gel is applied to skin during ultrasound scanning.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **A1**: (a)(i) $Z_{\text{gel}} = 1200 \times 1400 = 1.68 \times 10^6\text{ kg m}^{-2}\text{ s}^{-1}$
- **A1**: (a)(ii) density of air $= 1.29$, speed in tissue $= 1540\text{ m s}^{-1}$
- **C1**: (b)(i) $I_R / I_0 = (Z_2 - Z_1)^2 / (Z_2 + Z_1)^2$ $= (1.68 \times 10^6 - 440)^2 / (1.68 \times 10^6 + 440)^2$
- **A1**: $= 0.999$
- **A1**: (b)(ii) $Z_{\text{gel}} \approx Z_{\text{tissue}}$, so $I_R / I_0 \approx 0$
- **B1**: (c) without gel, (almost) all ultrasound is reflected from skin
- **B1**: with gel, (almost) all ultrasound is transmitted into the body
</details>

**Example 2 — 9702/w21/qp/42 Q11 (8 marks):**
> (a) A piezoelectric transducer containing a quartz crystal is used to obtain diagnostic information about internal body structures using ultrasound. Describe how the reflected pulses provide diagnostic information. (b)(i) Define specific acoustic impedance. (ii) Describe how specific acoustic impedances affect the fraction of intensity reflected at a boundary.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a) pulses reflected at boundaries between different tissues
- **B1**: time delay gives depth/distance information
- **B1**: reflected intensity gives information about nature of boundary
- **M1**: (b)(i) $Z = \rho c$, product of density and speed of ultrasound in medium
- **A1**: correct definition
- **B1**: (b)(ii) greater difference in $Z$, greater fraction reflected
- **B1**: smaller difference in $Z$, greater fraction transmitted
</details>

**Example 3 — 9702/w22/qp/41 Q7(b) (4 marks):**
> (b) The alternating voltage is applied to a piezoelectric crystal in air. (i) Explain what happens to the air surrounding the crystal. (ii) A second piezoelectric crystal is placed in the air near to the first crystal. Explain the effect of the surrounding air on the second crystal.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (b)(i) (alternating p.d. makes) the crystal vibrate
- **B1**: vibrations (of crystal) cause air to vibrate
- **B1**: frequency is in ultrasound range
- **B1**: (b)(ii) (air makes) crystal vibrate, which causes an e.m.f. to be generated across the (second) crystal
</details>

---

## Question Type 2: X-ray production and attenuation

### 如何识别
题目涉及 X-ray tube、minimum wavelength、attenuation $I = I_0 e^{-\mu x}$、contrast 等。

### 标准解题方法
:::note[标准解题方法]
1. X-ray 产生：电子被加速撞击金属靶，减速产生 bremsstrahlung
2. $\lambda_{\min} = hc / eV$（$V$ 是加速电压）
3. 硬度 (hardness)：由加速电压控制（电压越高，X-ray 穿透力越强）
4. 强度 (intensity)：由灯丝电流控制（电流越大，X-ray 越多）
5. 衰减：$I = I_0 e^{-\mu x}$，$\mu$ 是 attenuation coefficient
6. Contrast：不同组织吸收差异大 → contrast 好
:::

### 评分标准
:::info[评分标准（MS 模式）]
- **B1**: 解释 X-ray 产生方式
- **C1**: $I = I_0 e^{-\mu x}$ 正确代入
- **A1**: 数值答案
- **B1**: 解释 contrast
:::

### 完整原题

**Example 1 — 9702/s21/qp/41 Q11 (7 marks):**
> (a) State how the intensity of the X-ray beam and its hardness are controlled. (b) A model of a limb consists of soft tissue (thickness 9.0 cm, $\mu = 0.92\text{ cm}^{-1}$) and bone (thickness 3.0 cm, $\mu = 2.90\text{ cm}^{-1}$). Calculate (i) transmitted intensity $I_S$ through soft tissue alone, (ii) transmitted intensity $I_C$ through soft tissue and bone. (c) Suggest with a reason whether good contrast would be obtained.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a) intensity: vary filament current / p.d. across filament
- **B1**: hardness: vary accelerating potential difference
- **C1**: (b)(i) $I_S = I_0 e^{-\mu x} = I_0 \exp(-0.92 \times 9.0)$
- **A1**: $I_S = 2.5 \times 10^{-4} I_0$
- **C1**: (b)(ii) $I_C = I_0 \exp(-0.92 \times 6.0) \times \exp(-2.9 \times 3.0)$
- **A1**: $I_C = 6.7 \times 10^{-7} I_0$
- **B1**: (c) $I_S \gg I_C$, so good contrast
</details>

**Example 2 — 9702/s22/qp/41 Q9 (8 marks):**
> (a)(i) Explain how X-rays are produced for use in medical diagnosis. (ii) State why X-ray images are taken of multiple sections during CT scanning. (b) An X-ray image is taken of a structure with bone ($\mu = 3.0\text{ cm}^{-1}$, thickness 2.0 cm) and soft tissue ($\mu = 0.70\text{ cm}^{-1}$, thickness 4.0 cm). Determine transmitted intensities in terms of $I_0$. (c) Explain whether good contrast is obtained.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a)(i) electrons accelerated (by high p.d.) hit metal target
- **B1**: (kinetic) energy lost by electrons emitted as X-ray photons
- **B1**: (a)(ii) to produce a 3D image
- **C1**: (b) $I_{\text{bone}} = I_0 \exp(-3.0 \times 2.0) = I_0 e^{-6}$
- **A1**: $= 2.5 \times 10^{-3} I_0$
- **C1**: $I_{\text{tissue}} = I_0 \exp(-0.70 \times 4.0) = I_0 e^{-2.8}$
- **A1**: $= 6.1 \times 10^{-2} I_0$
- **B1**: (c) large difference in intensities, so good contrast
</details>

**Example 3 — 9702/w21/qp/41 Q11(a) (5 marks):**
> (a) State, for an X-ray image, what is meant by: (i) contrast. (b) A parallel X-ray beam passes through 2.3 cm of soft body tissue. The intensity is reduced to 35% of the incident intensity. Calculate the linear attenuation coefficient $\mu$. (c) Suggest an advantage and a disadvantage of CT scanning compared with single X-ray imaging.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a) contrast is the difference in transmitted intensity from different structures / ability to distinguish between structures
- **C1**: (b) $I = I_0 e^{-\mu x}$, $0.35 = e^{-0.046\mu}$
- **A1**: $\mu = 23\text{ m}^{-1}$
- **B1**: (c) advantage: CT gives 3D image / more detail
- **B1**: disadvantage: higher radiation dose / more expensive
</details>

---

## Question Type 3: PET scanning and annihilation

### 如何识别
题目涉及 positron emission, annihilation, gamma-ray photons, tracer, PET scan。

### 标准解题方法
:::note[标准解题方法]
1. Tracer 是含有放射性核素的物质，通过 $\beta^+$ decay 发射 positron
2. Positron 与 tissue 中的 electron 发生 annihilation
3. Annihilation 产生两个 gamma-ray photons，能量 $E = mc^2$，方向相反
4. Photons 离开人体被检测器探测
5. 通过光子到达时间差确定位置
:::

### 评分标准
:::info[评分标准（MS 模式）]
- **B1**: 定义 tracer
- **B1**: $\beta^+$ decay 产生 positron
- **B1**: annihilation 过程
- **B1**: 两个 gamma photon 方向相反
- **B1**: 能量计算 $E = mc^2$
- **B1**: 光子探测和图像重建
:::

### 完整原题

**Example 1 — 9702/s20/qp/41 Q11 (6 marks):**
> An electron and positron at rest interact to become two gamma-ray photons of equal energy. (a) Calculate for one photon: (i) energy in J, (ii) momentum. (b) State and explain direction of photons relative to each other.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **C1**: (a)(i) $E = mc^2 = 9.11 \times 10^{-31} \times (3.0 \times 10^8)^2$
- **A1**: $E = 8.2 \times 10^{-14}\text{ J}$
- **C1**: (a)(ii) $p = E/c$
- **A1**: $p = 2.7 \times 10^{-22}\text{ N s}$
- **B1**: (b) total momentum before is zero, so momentum conserved
- **B1**: photons emitted in opposite directions
</details>

**Example 2 — 9702/w23/qp/42 Q9 (8 marks):**
> Fluorine-18 (${}^{18}\text{F}$) is a radioactive nuclide used as a tracer in PET scanning. (a)(i) State what is meant by a tracer. (ii) The decay is ${}^{18}_9\text{F} \rightarrow {}^{18}_8\text{O} + {}^{0}_{+1}\beta + {}^{0}_{0}\nu$. Identify particle X. (b)(i) Explain how the decay of fluorine-18 results in emission of gamma-ray photons detected during a PET scan.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a)(i) tracer is a substance containing radioactive nuclei that can be introduced into the body and is absorbed by the tissue being studied
- **B1**: (a)(ii) positron / $\beta^+$
- **B1**: (b)(i) positrons (emitted in the decay) and electrons annihilate
- **B1**: mass converted into energy in the form of gamma-ray photons
- **B1**: two gamma photons produced travelling in opposite directions
</details>

**Example 3 — 9702/w24/qp/41 Q9 (9 marks):**
> A sample contains positron-emitting nuclei of fluorine-18 (half-life 110 min). (a)(ii) Calculate decay constant. (iii) The mass of the tracer is $2.1 \times 10^{-12}\text{ kg}$. Calculate the initial activity. (b)(i) Explain how positrons from the decay lead to the production of an image in PET scanning.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **A1**: (a)(ii) $\lambda = \ln 2 / (110 \times 60) = 1.05 \times 10^{-4}\text{ s}^{-1}$
- **C1**: (a)(iii) $N = M / (18u) = 2.1 \times 10^{-12} / (18 \times 1.66 \times 10^{-27}) = 7.0 \times 10^{13}$
- **C1**: $A = \lambda N = 1.05 \times 10^{-4} \times 7.0 \times 10^{13}$
- **A1**: $A = 7.4 \times 10^9\text{ Bq}$
- **B1**: (b)(i) (pair) annihilation occurs
- **B1**: mass of the two particles is converted into energy
- **B1**: two gamma photons formed and travel in opposite directions / leave the body
- **B1**: difference in arrival times of photons (at detector) is processed
</details>

---

## Question Type 4: CT scanning principles

### 如何识别
题目出现 "CT scanning", "computed tomography", "3D image", "voxel"。

### 标准解题方法
:::note[标准解题方法]
1. CT 扫描：从多个角度拍摄同一截面的 X-ray 图像
2. 组合这些 2D 图像得到该截面的 2D 图像
3. 沿轴重复，得到多个截面的 2D 图像
4. 组合所有 2D 图像得到 3D 图像
:::

### 完整原题

**Example 1 — 9702/w20/qp/41 Q10 (8 marks):**
> (a) Describe how CT scanning produces a 3D image of an internal structure. (b) One section of a model is divided into four voxels K, L, M, N. The section is viewed from four directions D1-D4, with background reading 24. K=6, L=7, M=2, N=9. Determine the pixel numbers.

<details>
<summary>📝 MS 展开查看</summary>

**MS:**
- **B1**: (a) X-rays are used
- **B1**: section (of object) is scanned / scans taken at many angles
- **B1**: (images of) sections are combined
- **B1**: (to give) 3D image
- **B3**: (b) K=6, L=7, M=2, N=9 (all four correct = 3 marks)
</details>
