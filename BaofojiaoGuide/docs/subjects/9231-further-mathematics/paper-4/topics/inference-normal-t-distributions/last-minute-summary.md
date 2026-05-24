---
title: 考前速记
sidebar_position: 7
---

# 考前速记 — Inference Using Normal and t-Distributions

## 核心公式速查

### 单样本 t 检验

$$t = \frac{\bar{x} - \mu_0}{\sqrt{s^2/n}}, \quad \text{df} = n-1$$

### 双样本合并 t 检验

$$s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$$

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_p^2(1/n_1 + 1/n_2)}}, \quad \text{df} = n_1+n_2-2$$

### 配对 t 检验

$$d_i = x_i - y_i, \quad t = \frac{\bar{d} - d_0}{\sqrt{s_d^2/n}}, \quad \text{df} = n-1$$

### 大样本 z 检验

$$z = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}} \sim N(0,1)$$

### 置信区间

| 情形 | 公式 |
|------|------|
| 单样本（t） | $\bar{x} \pm t_{\alpha/2}(n-1) \cdot \sqrt{s^2/n}$ |
| 双样本合并（t） | $(\bar{x}_1 - \bar{x}_2) \pm t_{\alpha/2}(n_1+n_2-2) \cdot \sqrt{s_p^2(1/n_1 + 1/n_2)}$ |
| 配对（t） | $\bar{d} \pm t_{\alpha/2}(n-1) \cdot \sqrt{s_d^2/n}$ |
| 大样本（z） | $(\bar{x}_1 - \bar{x}_2) \pm z_{\alpha/2} \cdot \sqrt{s_1^2/n_1 + s_2^2/n_2}$ |

## 自由度一览

| 检验 | df |
|------|----|
| 单样本 t | $n-1$ |
| 双样本合并 t | $n_1+n_2-2$ |
| 配对 t | $n-1$（$n$ = 对数） |
| z 检验 | $\infty$（正态表） |

## 临界值速记

| $\alpha$ | $z_{\alpha/2}$（双尾） | $z_{\alpha}$（单尾） |
|----------|----------------------|---------------------|
| 0.10 | 1.645 | 1.282 |
| 0.05 | 1.960 | 1.645 |
| 0.01 | 2.576 | 2.326 |

t 临界值需查表（记住 df 依赖）。

## 区分要点

### 配对 vs 独立

| 特征 | 配对 | 独立 |
|------|------|------|
| 对象 | 同一组对象测量两次 | 两组不同对象 |
| 数据 | 成对出现 | 两组独立 |
| 方法 | 计算差值 | 合并方差 |
| df | 对数 - 1 | $n_1+n_2-2$ |

### t 分布 vs 正态分布

| 条件 | 使用 |
|------|------|
| 方差已知 | 正态分布 $z$ |
| 方差未知，$n$ 小 | t 分布 |
| 方差未知，$n$ 大 | 正态分布 $z$（用 $s$ 代替 $\sigma$） |

## 正态假设措辞模板

- 单样本："Assume the population is normally distributed"
- 双样本合并："Assume both populations are normally distributed with equal variance"
- 配对："Assume the differences are normally distributed"

## 答题步骤模板

**假设检验**：
1. $H_0: \mu = \mu_0$，$H_1: \mu \neq \mu_0$
2. $\alpha = 0.05$
3. $t = (\bar{x} - \mu_0)/\sqrt{s^2/n} = \dots$
4. Critical value: $t_{\alpha/2}(n-1) = \dots$
5. Since $|t| \; ( &gt; / &lt; ) \; t_{\text{crit}}$，we reject/do not reject $H_0$
6. In context: There is sufficient/insufficient evidence that...

## 易错点（考场 30 秒回顾）

- **df**：配对 $n-1$（对数），合并 $n_1+n_2-2$，单样本 $n-1$
- **单尾 vs 双尾**：$\neq$ → 双尾，$&gt;$ 或 $&lt;$ → 单尾
- **配对 vs 独立**：同一人群两次 → 配对，不同人群 → 独立
- **正态假设**：t 检验必须写明，z 检验不需
- **$s^2$ vs $s$**：方差是标准差的平方
- **结论措辞**：不说 "accept"，说 "do not reject"
- **有效数字**：最终答案 3 s.f.

## 常考题型索引

| 题型 | 文件位置 | 典型真题 |
|------|----------|----------|
| 单样本 t 检验 | Question Type 1 | S20 Q4, W20 Q1, S21 Q1, W21 Q1, S22 Q1, W22 Q1, S23 Q1, W23 Q1, S24 Q1, S25 Q1, W25 Q1 |
| 单样本置信区间 | Question Type 2 | S20 Q5, W20 Q4, S21 Q4, W22 Q6, S23 Q2, W23 Q3, S24 Q6, S25 Q4, W25 Q3 |
| 双样本合并 t 检验 | Question Type 3 | S21 Q4, W21 Q4, S22 Q5, W22 Q6, S23 Q2, W23 Q3, S24 Q6, W25 Q6 |
| 配对 t 检验 | Question Type 4 | S20 Q4, W20 Q4, S22 Q1, W23 Q1, S25 Q1 |
| 双样本 z 检验 | Question Type 5 | S21 Q1, W21 Q4, S22 Q5, W25 Q6, S25 Q4 |
| 均值差置信区间 | Question Type 6 | S20 Q5, W20 Q4, S21 Q4, W22 Q6, S23 Q2, W23 Q3, S24 Q6, S25 Q4, W25 Q3 |
