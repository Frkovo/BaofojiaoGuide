---
title: 常见错误
sidebar_position: 6
---

# 常见错误

## 1. 没有先重排公式就直接认读

**错误**：直接从原始公式中读 gradient 和 intercept。

**正确**：必须先将公式重排成 $y = mx + c$ 形式，再识别系数。

**例子**：$\frac{h_i}{h_o} = \frac{d}{f} - \frac{t}{2f} - 1$，直接认为 gradient $= 1/f$ 但忘记检查 $\frac{h_i}{h_o}$ 是否已在 $y$ 侧。

---

## 2. 混淆 $\ln$ 和 $\lg$

**错误**：对 $y = ax^n$ 用 $\ln$ 而非 $\lg$。

**正确**：Power law $y = ax^n$ → $\lg$（base 10）；Exponential $y = ae^{kx}$ → $\ln$（base $e$）。

**原因**：MS 明确要求 $\lg$ 用于 power law，用 $\ln$ 虽然也能得到直线，但 gradient 是 $n\ln 10$ 而非 $n$。

---

## 3. 对数内忽略单位

**错误**：写 $\ln V$，$V$ 是带单位的物理量。

**正确**：$\ln(V/\text{V})$，将单位除去后再取对数。

**MS 要求**：对数函数的参数必须无量纲。

---

## 4. Gradient 符号错误

**错误**：$y = ae^{-kx}$ 写成 $\ln y = \ln a + kx$，gradient $= k$。

**正确**：$\ln y = \ln a - kx$，gradient $= -k$。

**检查方法**：如果 $y$ 随 $x$ 增大而减小，gradient 应为负。

---

## 5. 截距忘记反解

**错误**：$\lg y = \lg a + n\lg x$，写 intercept $= \lg a$ 后直接说 $a = \text{intercept}$。

**正确**：$a = 10^{\text{intercept}}$（$\lg$ 时）或 $a = e^{\text{intercept}}$（$\ln$ 时）。

---

## 6. 选错 $x$-axis 变量

**错误**：$\eta = He^{E/kT}$ 中 plot $\ln\eta$ against $T$。

**正确**：plot $\ln\eta$ against $1/T$，因为指数中是 $1/T$。

---

## 7. 将多个常数合并错误

**错误**：$L = SZM^n$，intercept $= \lg S + \lg Z + \lg M^n$（多出了变量）。

**正确**：$y$-intercept $= \lg(SZ)$，因为 $\lg L = n\lg M + \lg(SZ)$，其中 $SZ$ 是常数乘积。

---

## 8. 忘记检查量纲

**错误**：写出 gradient $= -\frac{1}{CR}$ 但没有确认量纲是否合理。

**检查**：$\ln V$ 无量纲，$t$ 单位是 s，所以 gradient 单位应为 $\text{s}^{-1}$，而 $-\frac{1}{CR}$ 的单位确实是 $\text{s}^{-1}$（因为 $CR$ 是时间常数）。

---

## 9. 对 $y$ 和 $x$ 的对应关系混淆

**错误**：题目说 "plot $A$ against $B$"，但把 $A$ 放 $x$-axis、$B$ 放 $y$-axis。

**正确**："plot $y$ against $x$" → $y$ 在 $y$-axis（vertical），$x$ 在 $x$-axis（horizontal）。

---

## 10. 在 linearization 题目中忽略表格计算

**错误**：Q2(a) 推导完公式后，Q2(b) 的表格中直接填入原始数据。

**正确**：必须根据 Q2(a) 推导出的 $y$ 和 $x$ 表达式，计算对应的 derived quantities 填入表格。

**例子**：如果 $y$-axis 是 $\ln V$，表格中应填 $\ln(V/\text{V})$，而非直接 $V$。
