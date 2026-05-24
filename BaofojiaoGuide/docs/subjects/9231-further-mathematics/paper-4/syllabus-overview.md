---
title: 考纲总览
sidebar_position: 3
---

# 考纲总览

## 板块 4.1: Continuous Random Variables（连续随机变量）

| 考纲点 | 内容 |
|--------|------|
| 4.1.1 | 理解连续随机变量的概念，理解概率密度函数（PDF）$f(x)$ 的性质：$f(x)\ge 0$ 且 $\int_{-\infty}^{\infty} f(x)\,dx=1$ |
| 4.1.2 | 掌握概率的计算：$P(a<X<b)=\int_a^b f(x)\,dx$ |
| 4.1.3 | 能够从 PDF 求出累积分布函数（CDF）$F(x)=\int_{-\infty}^x f(t)\,dt$，反之亦能由 CDF 求 PDF |
| 4.1.4 | 能够求期望值 $E(X)=\int xf(x)\,dx$ |
| 4.1.5 | 能够求 $E(g(X))=\int g(x)f(x)\,dx$，包括 $E(X^2)$ 和方差 $\operatorname{Var}(X)=E(X^2)-[E(X)]^2$ |
| 4.1.6 | 能够求中位数（median）$m$ 满足 $F(m)=0.5$，以及上下四分位数 |
| 4.1.7 | 能够求众数（mode），即最大化 $f(x)$ 的点 |
| 4.1.8 | 理解并应用线性变换：$E(aX+b)=aE(X)+b$，$\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$ |
| 4.1.9 | 理解并在简单情形下应用 PDF 的标准化变换 |
| 4.1.10 | 处理分段定义的 PDF 与 CDF |

## 板块 4.2: Inference using Normal and t-Distributions（正态与 t 分布推断）

| 考纲点 | 内容 |
|--------|------|
| 4.2.1 | 理解参数估计：点估计与区间估计 |
| 4.2.2 | 掌握样本均值 $\overline{X}$ 的抽样分布：$\overline{X}\sim N(\mu,\frac{\sigma^2}{n})$（总体正态）或 $n$ 大时近似正态 |
| 4.2.3 | 理解 t 分布的概念及与正态分布的关系（自由度越大越接近正态） |
| 4.2.4 | 在 $\sigma^2$ 未知时代入样本方差 $s^2$，使用 $T=\frac{\overline{X}-\mu}{s/\sqrt{n}}\sim t_{n-1}$ |
| 4.2.5 | 单样本 t 检验与置信区间 |
| 4.2.6 | 双样本 t 检验（独立样本，等方差假设）：$T=\frac{(\overline{X}_1-\overline{X}_2)-(\mu_1-\mu_2)}{s_p\sqrt{\frac1{n_1}+\frac1{n_2}}}\sim t_{n_1+n_2-2}$ |
| 4.2.7 | 合并方差 $s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}$ |
| 4.2.8 | 配对 t 检验（paired t-test）：$T=\frac{\overline{d}}{s_d/\sqrt{n}}\sim t_{n-1}$ 其中 $d$ 为配对差值 |
| 4.2.9 | z 检验（已知 $\sigma^2$ 或大样本）：$Z=\frac{\overline{X}-\mu}{\sigma/\sqrt{n}}\sim N(0,1)$ |
| 4.2.10 | 理解并应用单尾检验与双尾检验 |
| 4.2.11 | 理解显著性水平（$\alpha$）、$p$ 值、第一类错误与第二类错误 |
| 4.2.12 | 理解检验的势（power of test）的概念 |

## 板块 4.3: Chi-squared Tests（卡方检验）

| 考纲点 | 内容 |
|--------|------|
| 4.3.1 | 理解 $\chi^2$ 分布的概念，掌握自由度对分布形状的影响 |
| 4.3.2 | 拟合优度检验（goodness-of-fit test）：检验观测频数是否符合某个理论分布 |
| 4.3.3 | 计算期望频数 $E_i$，计算检验统计量 $\chi^2=\sum\frac{(O_i-E_i)^2}{E_i}$ |
| 4.3.4 | 确定自由度：$\text{df}=k-1$（$k$ 为类别数），或 $k-1-p$（$p$ 为从数据估计的参数个数） |
| 4.3.5 | 列联表独立性检验（contingency table test of independence）：$H_0$ 为两变量独立 |
| 4.3.6 | 列联表期望频数：$E_{ij}=\frac{R_i\times C_j}{n}$ |
| 4.3.7 | 列联表自由度：$\text{df}=(r-1)(c-1)$（$r$ 为行数，$c$ 为列数） |
| 4.3.8 | 期望频数合并规则：若期望频数 $E<5$ 的格子超过 20%，需合并相邻类别 |
| 4.3.9 | 期望频数合并：若超过 20% 格子 $E&lt;5$，合并相邻类别 |
| 4.3.10 | 理解卡方检验的适用条件和局限性 |

## 板块 4.4: Non-parametric Tests（非参数检验）

| 考纲点 | 内容 |
|--------|------|
| 4.4.1 | 理解非参数检验与参数检验的区别（不依赖总体分布假设） |
| 4.4.2 | 符号检验（sign test）：基于正负号个数的检验 |
| 4.4.3 | Wilcoxon 单样本符号秩检验（signed-rank test）：考虑符号及秩 |
| 4.4.4 | Wilcoxon 双样本检验（Mann-Whitney U test）：比较两个独立样本 |
| 4.4.5 | 能查非参数检验的临界值表 |
| 4.4.6 | 在大样本下使用正态近似计算检验统计量 |
| 4.4.7 | 理解非参数检验在数据不满足正态分布时的优势 |
| 4.4.8 | 零值处理（ties）及打结时的修正方法 |

## 板块 4.5: Probability Generating Functions（概率生成函数）

| 考纲点 | 内容 |
|--------|------|
| 4.5.1 | 理解 PGF 的定义：$G_X(t)=E(t^X)=\sum_{x}P(X=x)t^x$ |
| 4.5.2 | 能求出标准分布的 PGF：包括 Bernoulli、Binomial、Poisson、Geometric |
| 4.5.3 | 利用 PGF 求期望和方差：$E(X)=G_X'(1)$，$\operatorname{Var}(X)=G_X''(1)+G_X'(1)-[G_X'(1)]^2$ |
| 4.5.4 | 理解 $P(X=x)=\frac{G_X^{(x)}(0)}{x!}$（在 $t=0$ 处的 $x$ 阶导数） |
| 4.5.5 | 独立随机变量之和的 PGF：$G_{X+Y}(t)=G_X(t)G_Y(t)$ |
| 4.5.6 | 随机和（random sum）$S_N=X_1+X_2+\cdots+X_N$ 的 PGF：$G_{S_N}(t)=G_N(G_X(t))$ |
| 4.5.7 | 利用 PGF 求随机和的期望和方差 |
| 4.5.8 | 应用 PGF 识别分布 |

## Assessment Objectives（评估目标）

| AO | 描述 | 权重 |
|----|------|------|
| AO1 | 知识理解与应用：准确回忆并应用标准统计方法与公式 | 约 **50%** |
| AO2 | 数学推理与论证：构建逻辑推理链，解释统计结论 | 约 **25%** |
| AO3 | 问题解决与建模：将实际问题转化为统计模型，选择合适方法 | 约 **25%** |

## 先修知识要求（Prior Knowledge）

9231 Further Mathematics 以 9709（Cambridge International A Level Mathematics）为基础。Paper 4 特别依赖以下内容：

| 9709 试卷 | 关联内容 |
|-----------|---------|
| Paper 1: Pure Mathematics 1 | 基本代数、微积分（尤其是积分的计算）、函数 |
| Paper 3: Pure Mathematics 3 | 进一步微积分技巧（分步积分、换元法） |
| Paper 5: Probability & Statistics 1 | 基本概率、离散与连续分布、期望方差、正态分布基础 |
| Paper 6: Probability & Statistics 2 | 泊松分布、抽样分布、假设检验初步、卡方分布初步 |

其中 **9709 Paper 5** 与 **Paper 6** 是最直接的先修要求，缺乏其基础将难以应对 9231 Paper 4。

:::warning[常见陷阱]
很多学生在 9231 Paper 4 中因为 **9709 积分能力不足**而失分。CRV 的 PDF/CDF 计算需要熟练的积分技巧，请在备考初期确保微积分基础扎实。
:::
