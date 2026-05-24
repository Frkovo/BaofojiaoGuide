---
title: Inference Using Normal and t-Distributions
sidebar_position: 1
---

# Inference Using Normal and t-Distributions（正态分布与t分布推断）

## 考纲要求

根据 CAIE 9231 Further Mathematics Paper 4  Syllabus（Topic 4.2）：

- 对总体均值进行假设检验：当方差未知且样本量较小时使用 **t 检验**
- 从两个样本计算 **合并方差**（pooled estimate of population variance）
- **双样本 t 检验**（two-sample t-test）与 **配对样本 t 检验**（paired sample t-test）
- 使用 **正态分布**（大样本情形）进行检验
- 构造总体均值的 **置信区间**（t 分布）
- 构造总体均值之差的 **置信区间**

## 常见题型

| 题型 | 知识点 | 常见方法 |
|------|--------|----------|
| 单样本 t 检验 | $H_0: \mu = \mu_0$，小样本，$\sigma^2$ 未知 | $t = \frac{\bar{x} - \mu_0}{\sqrt{s^2/n}} \sim t(n-1)$ |
| 单样本置信区间（t） | 基于 t 分布的区间估计 | $\bar{x} \pm t_{\alpha/2}(n-1) \cdot \sqrt{s^2/n}$ |
| 双样本合并 t 检验 | $H_0: \mu_1 = \mu_2$，等方差假设 | $s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$ |
| 配对样本 t 检验 | 同一被试前后两次测量 | $t = \frac{\bar{d} - d_0}{\sqrt{s_d^2/n}} \sim t(n-1)$ |
| 双样本 z 检验 | 大样本（$n_1, n_2 \ge 30$） | $z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}} \sim N(0,1)$ |
| 均值差置信区间 | 两总体均值之差估计 | $(\bar{x}_1-\bar{x}_2) \pm z \cdot \sqrt{s_1^2/n_1 + s_2^2/n_2}$ |

## 核心公式

### 单样本 t 统计量

$$t = \frac{\bar{x} - \mu_0}{\sqrt{s^2/n}}, \quad \text{df} = n - 1$$

### 合并方差（双样本等方差假设）

$$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_p^2\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}, \quad \text{df} = n_1 + n_2 - 2$$

### 配对 t 统计量

$$d_i = x_i - y_i, \quad t = \frac{\bar{d} - d_0}{\sqrt{s_d^2/n}}, \quad \text{df} = n - 1$$

### 置信区间（均值）

$$\bar{x} \pm t_{\alpha/2}(n-1) \cdot \sqrt{\frac{s^2}{n}}$$

### 置信区间（均值差）

$$(\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2}(\nu) \cdot \sqrt{s_p^2\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}$$

### 大样本 z 统计量

$$z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} \quad \text{或} \quad z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

## 常见错误

1. **混淆配对与独立样本** — 同一对象前后测量使用配对，不同对象使用独立
2. **自由度错误** — 配对检验忘记 df = n-1（差异个数减 1），合并检验忘记 df = n₁+n₂-2
3. **小样本误用 z 检验** — 方差未知且样本量小时必须使用 t 分布
4. **忘记说明正态性假设** — 审题时必须写出 "Assume the population(s) are normally distributed"
5. **单尾/双尾判断错误** — 仔细审查 $H_1$ 的符号（$\neq$ 双尾，$&lt;$ 或 $&gt;$ 单尾）
6. **计算方差时忘记平方** — 标准差的平方才是方差
