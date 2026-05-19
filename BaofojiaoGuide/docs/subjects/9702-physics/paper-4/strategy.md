---
title: 详细策略
sidebar_position: 9
---

# 详细策略

## 前 5 分钟

1. **快速浏览所有 11–12 道题**，在每个题号旁标注对应 Topic（用铅笔）
2. **识别计算题和"Show that"题**——这些通常有明确方法分，先做
3. **标出定义题**——快速拿分，只需 1–2 句话
4. **识别解释题**——想想要用什么物理原理
5. **检查试卷最后是否附有公式表**——有时需要自己翻到最后看

## 各 Topic 具体答题策略

### 12 Motion in a Circle
- **核心思路**：任何圆周运动问题，先列 $F = mr\omega^2$ 或 $F = mv^2/r$
- **常见陷阱**：线速度和角速度不混淆；注意向心力不是独立力，是合力
- **第一步**：确定给出的是 $v$ 还是 $\omega$，如果是转速（rev/s）则 $\omega = 2\pi f$

### 13 Gravitational Fields
- **核心思路**：卫星/行星问题，写 $GMm/r^2 = mr\omega^2$（万有引力提供向心力）
- **地球同步卫星**：$T = 24\text{ h}$，在赤道正上方，轨道半径 fixed
- **引力势**：$\phi = -GM/r$，负号不能漏；$\phi$ 随 $r$ 增大而增大（从很负到接近零）
- **比较 $g$ 在两个天体表面**：$g_1/g_2 = (M_1/M_2)(r_2/r_1)^2$

### 14 Temperature
- **核心思路**：比热容 $mc\Delta T$，潜热 $ml$
- **注意**：能量守恒——放热 = 吸热
- **温标**：热力学温标单位 K，与摄氏温标的关系 $T(K) = \theta(^\circ C) + 273.15$

### 15 Ideal Gases
- **核心思路**：$pV = nRT = NkT$ 是基础；分子运动论公式 $pV = \frac13 Nm\langle c^2 \rangle$
- **r.m.s. 速度**：$c_{rms} = \sqrt{\langle c^2 \rangle} = \sqrt{\frac{3kT}{m}}$
- **平均动能**：$\frac12 m\langle c^2 \rangle = \frac32 kT$（**只与温度有关，与气体种类无关**）
- **注意**：区分 $\langle c^2 \rangle$（均方速度）和 $\langle c \rangle^2$（平均速度的平方），两者不相等

### 16 Thermodynamics
- **核心思路**：$\Delta U = q + W$，$W = p\Delta V$
- **正负号**：系统吸热 $q > 0$，系统放热 $q < 0$；系统对外做功 $W < 0$，外界对系统做功 $W > 0$
- **等温过程**：$\Delta U = 0$，所以 $q = -W$
- **等容过程**：$\Delta V = 0$，$W = 0$，所以 $\Delta U = q$
- **绝热过程**：$q = 0$，所以 $\Delta U = W$

### 17 Oscillations
- **核心思路**：SHM 一切从 $a = -\omega^2 x$ 出发
- **找 $\omega$**：通常从 $T = 2\pi\sqrt{m/k}$ 或 $T = 2\pi\sqrt{L/g}$ 得到
- **能量**：总能量 $E = \frac12 m\omega^2 x_0^2$，$E = KE + PE$
- **阻尼**：轻阻尼→振幅指数衰减；临界阻尼→最快回到平衡
- **共振**：驱动力频率 = 系统固有频率时振幅最大

### 18 Electric Fields
- **核心思路**：类比引力场（$F = Q_1Q_2/4\pi\epsilon_0 r^2$ 类似 $F = Gm_1m_2/r^2$）
- **匀强电场**：$E = \Delta V/\Delta d$，带电粒子在平行板间的运动用 $F = qE$ 结合运动学
- **点电荷**：$E = Q/4\pi\epsilon_0 r^2$（径向），$V = Q/4\pi\epsilon_0 r$（标量）
- **电势能**：$E_p = qV$，$E_p = Qq/4\pi\epsilon_0 r$

### 19 Capacitance
- **核心思路**：$C = Q/V$、电容器储能 $W = \frac12 CV^2$
- **串并联**：与电阻规则相反
- **RC 放电**：$x = x_0 e^{-t/RC}$，时间常数 $\tau = RC$
- **图像**：$Q-t$、$V-t$、$I-t$ 都是指数衰减

### 20 Magnetic Fields
- **核心思路**：$F = BIL\sin\theta$ 和 $F = BQv\sin\theta$ 是两大基本公式
- **力的方向**：弗莱明左手定则（电流/正电荷方向）
- **霍尔效应**：$V_H = BI/(ntq)$，用 Hall probe 测量磁场
- **电磁感应**：
  - $\Phi = BA\cos\theta$（$\theta$ 是 $B$ 与法线夹角）
  - 法拉第定律：$E = -N d\Phi/dt$
  - 楞次定律：感应电流的方向总是阻碍磁通量的变化

### 21 Alternating Currents
- **核心思路**：$x = x_0\sin\omega t$，$\omega = 2\pi f$
- **有效值**：$I_{rms} = I_0/\sqrt{2}$，$V_{rms} = V_0/\sqrt{2}$
- **整流**：半波整流（1 个二极管）vs 全波桥式整流（4 个二极管）
- **平滑**：并联电容减小纹波

### 22 Quantum Physics
- **核心思路**：$E = hf = hc/\lambda$，$p = h/\lambda$
- **光电效应**：$hf = \Phi + KE_{\max}$；$\Phi = hf_0$（$f_0$ 是阈值频率）
- **波粒二象性**：电子衍射验证了电子的波动性
- **能级**：$hf = E_1 - E_2$；高能级 $E_1$ 跃迁到低能级 $E_2$ 发射光子

### 23 Nuclear Physics
- **核心思路**：质量亏损 → 结合能（$\Delta E = \Delta m c^2$）
- **放射性衰变**：$A = \lambda N$，$A = A_0 e^{-\lambda t}$，$t_{1/2} = \ln2/\lambda$
- **计算**：取 ln 解指数方程
- **单位**：$A$（Bq）、$\lambda$（s$^{-1}$）、$t_{1/2}$（s）

### 24 Medical Physics
- **超声波**：
  - 压电换能器产生和接收超声波
  - $Z = \rho c$，$I_r/I_0 = (Z_1 - Z_2)^2/(Z_1 + Z_2)^2$
  - $I = I_0 e^{-\mu x}$
- **X 射线**：$I = I_0 e^{-\mu x}$，CT 扫描用多角度 X 射线重建 3D 图像
- **PET 扫描**：$\beta^+$ 示踪剂 → 湮灭 → 产生两个能量 511 keV 的 $\gamma$ 光子 → 同时探测定位

### 25 Astronomy and Cosmology
- **标准烛光**：已知 $L$，测 $F$ 得距离 $d = \sqrt{L/(4\pi F)}$
- **恒星半径**：结合维恩位移（$T$）和斯特藩-玻尔兹曼（$L$），$r = \sqrt{L/(4\pi\sigma T^4)}$
- **红移和哈勃定律**：$v \approx H_0 d$，$\Delta\lambda/\lambda \approx v/c$
- **宇宙膨胀**：红移与距离成正比（哈勃定律）

## 最后 10 分钟检查清单

- [ ] 题目有没有漏做（看看答题纸上每道题都有内容）
- [ ] 所有计算题答案都写了单位
- [ ] 有效数字是否合理（至少 2–3 位）
- [ ] "Show that" 题有没有完整的推导
- [ ] 作图题有没有标注坐标轴
- [ ] 定义题是否包含关键公式
- [ ] 检查有没有抄错数字（看清指数 $10^3$ 还是 $10^{-3}$）
- [ ] 有没有可用的 ecf 修正前面错误
