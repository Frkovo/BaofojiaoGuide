---
title: Chi-squared Tests
sidebar_position: 1
---

# Chi-squared Tests（卡方检验）

## 考纲要求

1. 理解 $\chi^2$ 检验的基本原理：比较观测频数（O）与期望频数（E）的差异
2. **拟合优度检验（Goodness of Fit）**：检验一组观测数据是否来自某个指定的理论分布（Binomial、Poisson 或其他给定 PDF）
3. **独立性检验（Test for Independence）**：使用列联表（contingency table）判断两个分类变量是否独立
4. 正确计算期望频数：
   - GOF：$E = n \times P(X = x)$ 或 $E = n \times \text{PDF}(x)$
   - 独立性：$E_{ij} = \dfrac{R_i \times C_j}{T}$
5. 自由度计算：
   - GOF：$\mathrm{df} = k - 1 - m$（$k$ = 类别数，$m$ = 从数据中估计的参数个数）
   - 独立性：$\mathrm{df} = (r - 1)(c - 1)$
6. **期望频数 ≥ 5 规则**：任何 $E &lt; 5$ 的单元格必须与相邻单元格合并
7. **不要求 Yates 连续性校正**（考纲明确说明不考）

## 常见题型

| 题型 | 识别关键词 | 分值占比 |
|------|-----------|---------|
| Binomial 拟合优度 | "test whether Binomial model fits"、"expected frequencies from Binomial" | 8–10 marks |
| Poisson 拟合优度 | "test whether Poisson model fits"、"test for randomness" | 8–10 marks |
| 独立性检验 | "test for association/independence"、"contingency table" | 8–12 marks |
| 给定 PDF 拟合优度 | "given probability density function"、"test" | 8–10 marks |

## 核心公式

| 公式 | 说明 |
|------|------|
| $\chi^2 = \sum \dfrac{(O - E)^2}{E}$ | 检验统计量，所有单元格求和 |
| $E = n \times P(X = x)$ | GOF 期望频数（理论分布） |
| $E_{ij} = \dfrac{R_i \times C_j}{T}$ | 独立性期望频数（$R_i$ = 行和，$C_j$ = 列和，$T$ = 总数） |
| $\nu = k - 1 - m$ | GOF 自由度 |
| $\nu = (r - 1)(c - 1)$ | 独立性自由度 |

## 常见错误

- 自由度算错：独立性检验用 $\mathrm{df} = (r-1)(c-1)$，**不是** $r \times c$
- 忘记合并 $E &lt; 5$ 的单元格
- 参数估计后忘记减去自由度中的 $m$
- 使用 Yates 校正（考纲不要求）
- 混淆单尾/双尾：$\chi^2$ 检验总是右尾检验
