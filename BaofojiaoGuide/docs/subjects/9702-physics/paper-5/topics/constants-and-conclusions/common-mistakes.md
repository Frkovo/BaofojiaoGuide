---
title: 常见错误
sidebar_position: 6
---

# 常见错误

## 1. 忘记单位

**错误**：$C = 4.7 \times 10^{-6}$（没有单位）。

**正确**：$C = 4.7 \times 10^{-6}$ F（带单位）。

---

## 2. 从 y-intercept 求常数时忘记取指数

**错误**：y-intercept $= 2.30$，直接写 $V_0 = 2.30$ V。

**正确**：y-intercept $= \ln V_0 = 2.30$，所以 $V_0 = e^{2.30} = 9.97$ V。

**错误**：y-intercept $= 0.398$，直接写 $a = 0.398$。

**正确**：y-intercept $= \lg a = 0.398$，所以 $a = 10^{0.398} = 2.50$。

---

## 3. 符号错误

**错误**：gradient $k = -0.25$ s$^{-1}$，代入 $C = -\frac{1}{Rk}$ 时写成 $C = -\frac{1}{R \times (-0.25)} = \frac{1}{0.25R}$，但忘了负号在公式中已处理。

**正确**：$C = -\frac{1}{R \times (-0.25)} = \frac{1}{0.25R}$。仔细核对原始公式中的正负号。

---

## 4. 结论没有考虑 uncertainty

**错误**：理论值 $4.7$，实验值 $4.5$，直接说 "does not support"（忽略 $\pm 0.3$ 的 uncertainty）。

**正确**：实验值 $(4.5 \pm 0.3)\ \Omega$，范围 $4.2$ 到 $4.8\ \Omega$，$4.7$ 在此范围内，所以 "supports within experimental uncertainty"。

---

## 5. 比较时用的不是同一个量

**错误**：题目问实验值是否支持 $n = 2.0$，却比较了 gradient 值。

**正确**：正确使用 $n = \text{gradient}$，比较 $n_{\text{exp}} \pm \Delta n$ 和 $2.0$。

---

## 6. 扩展计算中使用错误常数

**错误**：Part (e) 使用 Part (d)(i) 求出的常数时，抄错了数值。

**正确**：仔细将 (d)(i) 的计算结果带入 (e) 的计算，最好使用精确值而非四舍五入后的值。

---

## 7. 从 gradient 反解常数时代入错误

**错误**：$g = \frac{4\pi^2}{\text{gradient}}$ 写成了 $g = \frac{\text{gradient}}{4\pi^2}$。

**正确**：仔细推导代数关系，确保常数在正确的位置。

---

## 8. 有效数字位数不恰当

**错误**：$C = 4.723958 \times 10^{-6}$ F（过多有效数字）。

**正确**：$C = 4.72 \times 10^{-6}$ F 或 $C = (4.72 \pm 0.12) \times 10^{-6}$ F（与输入精度匹配）。

---

## 9. 忘记在 y-intercept 中处理常数因子

**错误**：$1/f = \frac{4}{v}L + \frac{4c}{v}$，y-intercept $= 4c/v$，直接写 $c = \text{intercept}$。

**正确**：$c = \frac{\text{intercept} \times v}{4}$，需要先求出 $v$（从 gradient）再解 $c$。

---

## 10. 结论书写不完整

**错误**：仅写 "Yes, it supports."

**正确**：写完整句子，包括比较值、范围、判断依据。

---

## 11. 单位推导错误

**错误**：$C$ 的单位写成 $\Omega \cdot \text{s}$。

**正确**：$C = -\frac{1}{Rk}$，$[\Omega] \times [\text{s}^{-1}]$ 在分母，所以 $C$ 的单位是 $\text{F}$（法拉）。

---

## 12. 忽略题目提供的已知常数

**错误**：题目给了 $k = 1.38 \times 10^{-23}\ \text{J K}^{-1}$ 但没有使用。

**正确**：$E = \text{gradient} \times k$，必须代入 $k$ 的值。
