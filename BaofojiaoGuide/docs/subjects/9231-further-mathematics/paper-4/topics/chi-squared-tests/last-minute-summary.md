---
title: 考前总结
sidebar_position: 7
---

# 考前总结 — Chi-squared Tests

## 核心公式速记

| 公式 | 用途 |
|------|------|
| $\chi^2 = \sum \dfrac{(O - E)^2}{E}$ | 所有卡方检验 |
| $E_{\text{GOF}} = n \times P(X = x)$ | 拟合优度期望 |
| $E_{\text{ind}} = \dfrac{R_i \times C_j}{T}$ | 独立性期望 |
| $\nu_{\text{GOF}} = k - 1 - m$ | GOF 自由度 |
| $\nu_{\text{ind}} = (r - 1)(c - 1)$ | 独立性自由度 |

## 解题五步法

1. **Identify**：确定是 GOF 还是 Independence
2. **Expected**：计算期望频数（注意参数估计和 $E \geq 5$）
3. **Chi-squared**：计算 $\chi^2 = \sum (O-E)^2/E$
4. **df**：计算自由度
5. **Conclusion**：查表 → 比较 → 结论

## Binomial GOF 特别提醒

- $\hat{p} = \dfrac{\sum x f_x}{n \sum f_x}$，注意 $n$ 是每次试验的次数
- 最后 $P(X \geq r)$ 合并为一项
- $\mathrm{df} = k - 1 - 1$（估计 $p$）

## Poisson GOF 特别提醒

- $\hat{\lambda} = \bar{x}$
- $P(X = x) = e^{-\lambda} \lambda^x / x!$
- $P(X \geq r) = 1 - \sum_{x=0}^{r-1} P(X = x)$
- $\mathrm{df} = k - 1 - 1$（估计 $\lambda$）

## 独立性检验特别提醒

- $E_{ij}$ 保留分数或至少 2 位小数
- 先检查 $E_{ij}$ 再决定是否合并
- $2 \times 2$ 表：$\mathrm{df} = 1$
- 临界值从 $\chi^2$ 分布表查（右尾）

## 考试中常见陷阱

- ❌ 忘记 $E \geq 5$
- ❌ 自由度忘记减 $m$
- ❌ 独立性用错自由度
- ❌ 忘记乘 $n$ 得到 $E$
- ✅ $\chi^2$ 检验永远**右尾检验**
