---
title: 解题方法
sidebar_position: 4
---

# 解题方法 — Chi-squared Tests

## 方法一：拟合优度检验（一般流程）

### 步骤

1. 确定理论分布，提出假设
2. 若分布参数未知，从样本估计
3. 计算每类的理论概率 $p_i$
4. 计算期望频数 $E_i = n \times p_i$
5. 检查 $E_i$，合并 $E_i &lt; 5$ 的类别
6. 计算 $\chi^2 = \sum \dfrac{(O_i - E_i)^2}{E_i}$
7. 自由度 $\mathrm{df} = k - 1 - m$（$k$ = 合并后类别数，$m$ = 估计参数数）
8. 查表比较，下结论

### Binomial 特殊情况

- 若 $n$ 未知，需从数据估计；若已知，直接用已知 $n$
- 估计 $p$：$\hat{p} = \dfrac{\sum x \times f_x}{n \times \text{total}}$（加权平均）
- 最后几项合并使 $E \geq 5$
- 例如 $P(X \geq r)$ 合并为一项

### Poisson 特殊情况

- 估计 $\hat{\lambda} = \bar{x} = \dfrac{\sum x \times f_x}{\text{total}}$
- 右侧尾部合并：$P(X \geq r) = 1 - \sum_{x=0}^{r-1} P(X = x)$

## 方法二：独立性检验（一般流程）

### 步骤

1. 构造列联表，标注行和、列和、总和
2. 对每格计算 $E_{ij} = \dfrac{R_i \times C_j}{T}$
3. 检查所有 $E_{ij} \geq 5$，否则合并行或列
4. 计算 $\chi^2 = \sum \dfrac{(O_{ij} - E_{ij})^2}{E_{ij}}$
5. 自由度 $\mathrm{df} = (r - 1)(c - 1)$
6. 查表比较，下结论

### 计算技巧

- 先算行和 $R_i$、列和 $C_j$、总和 $T$
- 逐格计算 $E_{ij}$，**不要四舍五入到整数**
- 使用分数或保留更多小数位

## 方法三：检验临界值与结论

:::note[标准结论模板]

$H_0$: The data follow the specified distribution / the variables are independent

$H_1$: The data do not follow the specified distribution / the variables are not independent

$\chi^2$ test statistic $ = \underline{\qquad}$

$\chi^2_{\text{critical}} (\nu = \underline{\qquad},\ \alpha = \underline{\qquad}) = \underline{\qquad}$

Since $\chi^2_{\text{calc}} \; [> / &lt;] \; \chi^2_{\text{crit}}$ at the $\underline{\qquad}\%$ significance level, we [reject / do not reject] $H_0$.

Conclusion: There is [sufficient / insufficient] evidence to suggest that...

:::
