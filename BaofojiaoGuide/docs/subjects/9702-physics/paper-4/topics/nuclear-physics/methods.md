---
title: Solution Methods
sidebar_position: 4
---

# Solution Methods — Nuclear Physics

## Method 1: Binding energy calculation

### 步骤
1. **确定反应物和生成物** — 写出核反应方程式
2. **计算质量亏损 $\Delta m$**：
   - $\Delta m = \sum m_{\text{反应前}} - \sum m_{\text{反应后}}$（释放能量时 $\Delta m > 0$）
   - 对于单个核：$\Delta m = Z m_p + (A - Z) m_n - m_{\text{核}}$
3. **质能转换**：
   - $E = \Delta m c^2$
   - 若 $\Delta m$ 以 u 为单位：$E(\text{J}) = \Delta m \times 1.66 \times 10^{-27} \times (3.00 \times 10^8)^2$
   - 或 $E(\text{MeV}) = \Delta m \times 931.5$
4. **per nucleon**: $E / A$

### 易错点
- 质量亏损是 反应前减反应后，不是绝对值
- 注意区分 atomic mass 和 nuclear mass（电子质量有时需要扣除）

## Method 2: Radioactive decay

### 步骤
1. **确定使用哪个公式**：
   - $A = \lambda N$ — activity 与数量关系
   - $\lambda = \ln 2 / t_{1/2}$ — decay constant 与 half-life
   - $N = N_0 e^{-\lambda t}$ — 数量随时间变化
   - $A = A_0 e^{-\lambda t}$ — activity 随时间变化
2. **统一时间单位**
3. **使用自然对数求解时间**：
   - $\ln(N / N_0) = -\lambda t$
4. **从 graph 求 $\lambda$**：
   - $\ln N = \ln N_0 - \lambda t$，斜率 $= -\lambda$
   - 半对数坐标纸使用

## Method 3: Binding energy per nucleon graph

### 关键分析
1. **曲线形状**：轻核急剧上升 → 铁（$A \approx 56$）峰值 $\approx 8.8\text{ MeV}$ → 重核缓慢下降
2. **最稳定**：binding energy per nucleon 最大 → $^{56}\text{Fe}$
3. **能量释放条件**：反应物在曲线较低位置，生成物在较高位置
4. **Fusion**：轻核结合→移动到峰值左边→增加→释放能量
5. **Fission**：重核分裂→移动到峰值右边→增加→释放能量
