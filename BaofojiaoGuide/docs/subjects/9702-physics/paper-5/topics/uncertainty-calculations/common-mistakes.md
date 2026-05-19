---
title: 常见错误
sidebar_position: 6
---

# 常见错误

## 1. 表格中未列出 uncertainty

**错误**：只计算了 derived quantity 的值，没有在同一行列出对应的 absolute uncertainty。

**正确**：每个 derived quantity 值后面紧跟其 uncertainty，如 $\ln V = 1.825 \pm 0.032$。

---

## 2. uncertainty 有效数字位数错误

**错误**：uncertainty 给出 3 位或更多有效数字（如 $\pm 0.0324$）。

**正确**：uncertainty 一般保留 1 位有效数字（如 $\pm 0.03$），最多 2 位。

---

## 3. Derived quantity 有效数字位数与 uncertainty 不匹配

**错误**：$\ln V = 1.8 \pm 0.032$（value 与 uncertainty 小数位数不一致）。

**正确**：$\ln V = 1.825 \pm 0.032$（小数位数对齐）。

---

## 4. 误用 uncertainty propagation 公式

**错误**：计算 $\Delta(\ln V)$ 时用了 $\Delta(\ln V) = \ln(\Delta V)$。

**正确**：$\Delta(\ln V) = \frac{\Delta V}{V}$。

**错误**：计算 $\Delta(1/d)$ 时用了 $\Delta(1/d) = \frac{1}{\Delta d}$。

**正确**：$\Delta(1/d) = \frac{\Delta d}{d^2}$。

---

## 5. Worst line 没有通过所有 error bars

**错误**：worst acceptable line 忽略了一些 error bars。

**正确**：worst line 必须穿过所有数据点的 error bars（上、下、左、右均需触及）。

---

## 6. 忘记 $\lg$ 公式中的 0.434 因子

**错误**：$\Delta(\lg x) = \frac{\Delta x}{x}$。

**正确**：$\Delta(\lg x) = 0.434 \times \frac{\Delta x}{x}$（因为 $\ln 10 \approx 2.303$，$1/\ln 10 \approx 0.434$）。

---

## 7. 组合误差时遗漏项

**错误**：$C = -\frac{1}{R \times k}$ 时只算了 $\frac{\Delta k}{k}$ 忘记加 $\frac{\Delta R}{R}$。

**正确**：$\frac{\Delta C}{C} = \frac{\Delta R}{R} + \frac{\Delta k}{k}$，所有项都需要包含。

---

## 8. 梯度计算没有用大三角形

**错误**：用两个相邻数据点计算 gradient，结果受局部误差影响大。

**正确**：在 best fit line 上选两个远端点，$\Delta x$ 覆盖图幅 &gt; 一半。

---

## 9. 最终结果缺少单位

**错误**：只写数字 $3.24 \pm 0.05$。

**正确**：$3.24 \pm 0.05$ s$^{-1}$（带单位）。

---

## 10. 混淆 $\ln$ 和 $\lg$

**错误**：题目给的是 $\ln$ 却用 0.434 因子，或 $\lg$ 却用 $1/x$ 因子。

**正确**：
- $\ln x$: $\Delta(\ln x) = \Delta x / x$
- $\lg x$: $\Delta(\lg x) = 0.434 \times \Delta x / x$

---

## 11. y-intercept 不确定度直接从图上估读误差

**错误**：随意估计 y-intercept 的误差而没有画 worst line。

**正确**：必须通过 best line 和 worst line 的 y-intercept 差值计算。

---

## 12. 忘记对 uncertainty 进行四舍五入

**错误**：$\Delta k = 0.0463$ 未处理保留 1 位有效数字。

**正确**：$\Delta k = 0.05$（1 s.f.），value 的小数位数对齐为 $k = 1.23 \pm 0.05$。
