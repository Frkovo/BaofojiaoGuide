---
title: 考前速通
sidebar_position: 4
---

# 考前速通

## 核心公式速查

### 4.1 CRV

$$f(x)\ge 0,\quad \int_{-\infty}^{\infty} f(x)\,dx = 1$$

$$F(x) = \int_{-\infty}^{x} f(t)\,dt, \quad f(x) = F'(x)$$

$$P(a < X < b) = \int_a^b f(x)\,dx = F(b) - F(a)$$

$$E(X) = \int x f(x)\,dx$$

$$E(g(X)) = \int g(x) f(x)\,dx$$

$$\operatorname{Var}(X) = E(X^2) - [E(X)]^2$$

$$F(m) = 0.5 \quad (\text{中位数})$$

$$f'(x) = 0 \quad (\text{众数})$$

$$E(aX+b) = aE(X) + b$$

$$\operatorname{Var}(aX+b) = a^2 \operatorname{Var}(X)$$

### 4.2 推断

$$T = \frac{\overline{X} - \mu}{s/\sqrt{n}} \sim t_{n-1}$$

$$s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$$

$$T = \frac{(\overline{X}_1 - \overline{X}_2) - (\mu_1-\mu_2)}{s_p \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}} \sim t_{n_1+n_2-2}$$

$$T = \frac{\overline{d}}{s_d/\sqrt{n}} \sim t_{n-1} \quad (\text{配对})$$

$$Z = \frac{\overline{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1)$$

$$\overline{X} \pm t_{\alpha/2,\,n-1} \times \frac{s}{\sqrt{n}} \quad (\text{CI})$$

### 4.3 卡方

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

$$\chi^2 = \sum \frac{(|O_i - E_i| - 0.5)^2}{E_i} \quad (\text{Yates})$$

$$E_{ij} = \frac{R_i \times C_j}{n} \quad (\text{列联表})$$

$$\text{df} = k-1 \quad (\text{拟合优度}), \quad \text{df} = (r-1)(c-1) \quad (\text{列联表})$$

### 4.4 非参数

**Wilcoxon 符号秩检验统计量：**

$$T = \min(T^+, T^-)$$

**Mann-Whitney U 检验：**

$$U = n_1 n_2 + \frac{n_1(n_1+1)}{2} - R_1$$

**正态近似（$n>10$）：**

$$Z = \frac{T - \frac{n(n+1)}{4}}{\sqrt{\frac{n(n+1)(2n+1)}{24}}}$$

$$Z = \frac{U - \frac{n_1 n_2}{2}}{\sqrt{\frac{n_1 n_2 (n_1+n_2+1)}{12}}}$$

### 4.5 PGF

$$G_X(t) = E(t^X) = \sum_x P(X=x)\,t^x$$

$$E(X) = G_X'(1)$$

$$E(X(X-1)) = G_X''(1)$$

$$\operatorname{Var}(X) = G_X''(1) + G_X'(1) - [G_X'(1)]^2$$

$$P(X=x) = \frac{G_X^{(x)}(0)}{x!}$$

$$G_{X+Y}(t) = G_X(t) \, G_Y(t) \quad (\text{独立和})$$

$$G_{S_N}(t) = G_N(G_X(t)) \quad (\text{随机和})$$

$$E(S_N) = E(N) \, E(X)$$

$$\operatorname{Var}(S_N) = E(N) \operatorname{Var}(X) + \operatorname{Var}(N) [E(X)]^2$$

## 看到 X 做 Y 速查表

| 看到... | 马上... |
|---------|---------|
| "probability density function" | 验证 $\int f = 1$，检查 $f(x) \ge 0$ |
| "cumulative distribution function" | 求导得 PDF，或从 PDF 积分 |
| "median" | 设 $F(m)=0.5$ 求解 $m$ |
| "mode" | 求 $f'(x)=0$（或分段比较） |
| "test the claim" / "test whether" | 写出 $H_0$, $H_1$，确定检验类型 |
| "known variance" | z 检验（$\sigma$ 已知） |
| "unknown variance" | t 检验（$s$ 估计） |
| "paired" / "matched" / "same individuals" | 配对 t 检验（差值 $d$） |
| "two independent samples" | 双样本 t 检验或 Mann-Whitney |
| "goodness-of-fit" | 卡方拟合优度检验 |
| "contingency table" / "association" | 卡方独立性检验 |
| "Yates" / "$2 \times 2$" | 使用连续性校正 |
| "expected frequency less than 5" | 合并相邻类别 |
| "Wilcoxon signed-rank" | 单样本/配对非参数检验 |
| "Mann-Whitney" | 双样本非参数检验 |
| "sign test" | 仅看符号忽略大小 |
| "probability generating function" | $G_X(t)=E(t^X)$ |
| "independent sum" | $G_{X+Y}=G_X G_Y$ |
| "random sum" | $G_{S_N}=G_N(G_X)$ |
| "show that $X \sim \text{Poisson}$" | 证明 $G_X(t) = e^{\lambda(t-1)}$ |
| "estimate" / "CI" | 构造置信区间 |
| "pooled estimate of variance" | $s_p^2$ 公式 |

## 时间分配表

| 分数段 | 可用时间 | 每分钟分值 |
|-------|---------|-----------|
| 50 分 | 90 分钟 | 1.8 分钟/分 |
| 每道 6 分题 | 约 10.8 分钟 | — |
| 每道 8 分题 | 约 14.4 分钟 | — |
| 每道 10 分题 | 约 18 分钟 | — |

## 卡住时的策略

| 情形 | 应对策略 |
|------|---------|
| 完全看不懂题目 | 先看最后一行问什么，反向定位所需方法 |
| 计算卡住 | 写出公式，代入已知量，标记未知数，检查是否漏条件 |
| 公式记不清 | 查阅 MF19（大部分关键公式已给出） |
| 时间不够 | 写出所有步骤框架（$H_0$, $H_1$, 检验公式），争取 **M1** 方法分 |
| $p$ 值无法查表 | 使用计算器直接计算（如有统计功能） |
| 自由度不确定 | 回到定义：样本数减约束数 |

:::tip[必背公式]
**MF19 中未给出**但必须记忆的公式：
- $s_p^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$
- $\operatorname{Var}(X) = G_X''(1) + G_X'(1) - [G_X'(1)]^2$
- $G_{S_N}(t) = G_N(G_X(t))$
- Yates 校正：$\frac{(|O-E|-0.5)^2}{E}$
:::

## 交卷前最终检查清单

- [ ] 每道题都写了题号
- [ ] 每个 $H_0$ 和 $H_1$ 都明确写出来了
- [ ] 自由度 df 正确
- [ ] 单尾/双尾选择正确
- [ ] 配对/独立判断正确
- [ ] 连续性校正是否应该使用
- [ ] 期望频数是否都已合并（$E\ge 5$）
- [ ] 所有概率在 0 到 1 之间
- [ ] 所有方差非负
- [ ] 最终结论有文字解释
- [ ] 答案有适当有效数字
