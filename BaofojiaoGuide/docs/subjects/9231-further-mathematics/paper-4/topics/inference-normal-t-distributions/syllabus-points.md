---
title: 大纲要点
sidebar_position: 3
---

# Syllabus Points — Inference Using Normal and t-Distributions

## 核心知识点

### 1. 单样本 t 检验（One-Sample t-Test）

- 用于检验总体均值是否等于某定值 $\mu_0$
- 条件：总体服从正态分布，方差未知，样本量小
- 统计量：$t = \dfrac{\bar{x} - \mu_0}{\sqrt{s^2/n}} \sim t(n-1)$
- 自由度 $\text{df} = n - 1$

### 2. 双样本合并 t 检验（Two-Sample Pooled t-Test）

- 用于比较两个独立总体的均值
- 条件：两总体均服从正态分布，方差相等（但未知），样本独立
- 合并方差：$s_p^2 = \dfrac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1 + n_2 - 2}$
- 统计量：$t = \dfrac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_p^2(1/n_1 + 1/n_2)}} \sim t(n_1+n_2-2)$
- 自由度 $\text{df} = n_1 + n_2 - 2$

### 3. 配对 t 检验（Paired t-Test）

- 用于同一组对象在两种条件下的均值比较
- 先计算每对差值 $d_i = x_i - y_i$
- 统计量：$t = \dfrac{\bar{d} - d_0}{\sqrt{s_d^2/n}} \sim t(n-1)$
- 自由度 $\text{df} = n - 1$（$n$ 为对数）
- **关键假设：差值服从正态分布**

### 4. 大样本 z 检验（Large-Sample z-Test）

- 样本量足够大（$n \ge 30$）时使用
- 统计量：$z = \dfrac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$ 或 $z = \dfrac{\bar{x}_1 - \bar{x}_2}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}}$
- 参照标准正态分布 $N(0,1)$

### 5. 置信区间（t 分布）

- 单样本均值：$\bar{x} \pm t_{\alpha/2}(n-1) \cdot \sqrt{s^2/n}$
- 均值差（合并）：$(\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2}(n_1+n_2-2) \cdot \sqrt{s_p^2(1/n_1 + 1/n_2)}$
- 均值差（配对）：$\bar{d} \pm t_{\alpha/2}(n-1) \cdot \sqrt{s_d^2/n}$
- 大样本均值差：$(\bar{x}_1 - \bar{x}_2) \pm z_{\alpha/2} \cdot \sqrt{s_1^2/n_1 + s_2^2/n_2}$

### 6. 假设检验的基本框架

1. 建立原假设 $H_0$ 和备择假设 $H_1$
2. 确定显著性水平 $\alpha$
3. 计算检验统计量
4. 确定拒绝域（临界值法）
5. 作出统计结论（拒绝/不拒绝 $H_0$）
6. 在问题背景下解释结论

### 7. 正态性假设

- 单样本 t 检验：假设总体服从正态分布
- 双样本合并 t 检验：假设两总体均服从正态分布
- 配对 t 检验：假设差值服从正态分布
- 大样本 z 检验：由中心极限定理保证，无需正态假设

### 8. 单尾与双尾检验

- $H_1: \mu \neq \mu_0$ → 双尾检验，临界值 $t_{\alpha/2}$
- $H_1: \mu &gt; \mu_0$ → 右单尾检验，临界值 $t_{\alpha}$
- $H_1: \mu &lt; \mu_0$ → 左单尾检验，临界值 $-t_{\alpha}$
