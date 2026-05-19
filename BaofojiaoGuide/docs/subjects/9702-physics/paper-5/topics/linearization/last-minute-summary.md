---
title: 考前速记
sidebar_position: 7
---

# 考前速记

## Must-Know Linearization Formulas

| 原始关系 | 线性化形式 | Gradient | Y-intercept | 反解常数 |
|---------|-----------|----------|-------------|---------|
| $y = mx + c$ | $y$ vs $x$ | $m$ | $c$ | — |
| $y = ax^n$ | $\lg y$ vs $\lg x$ | $n$ | $\lg a$ | $a = 10^{\text{int}}$ |
| $y = ae^{kx}$ | $\ln y$ vs $x$ | $k$ | $\ln a$ | $a = e^{\text{int}}$ |
| $y = a + \frac{b}{x}$ | $y$ vs $\frac{1}{x}$ | $b$ | $a$ | — |
| $y = \frac{a}{x}$ | $y$ vs $\frac{1}{x}$ | $a$ | $0$ | — |
| $y^2 = ax$ | $y^2$ vs $x$ | $a$ | $0$ | — |

## Problem Patterns to Recognise

| 看到... | 立即想到... |
|---------|-------------|
| $y = a x^n$ | $\lg y = \lg a + n \lg x$ |
| $y = a e^{kx}$ | $\ln y = \ln a + kx$ |
| $e^{-t/RC}$ | gradient $= -1/RC$ |
| $(R_1 + R_2)$ in denominator | plot $1/I$ against $(R_1 + R_2)$ |
| $\frac{h_i}{h_o}$ vs $d$ | gradient $= 1/f$ |
| $\eta = H e^{E/kT}$ | x-axis is $1/T$, NOT $T$ |

## Red Flags

| 信号 | 可能的问题 |
|------|-----------|
| 公式中有 $\lg$ 或 $\ln$ | 确保对数参数无量纲 |
| 两个都是变量且关系为 power | 用 $\lg$，不是 $\ln$ |
| 指数中有负号 | gradient 有负号 |
| 题目给 $n$ 或 $k$ 要求计算 | 注意反解时是 $10^{\text{int}}$ 还是 $e^{\text{int}}$ |
| 常数有多个字母（如 $SZ$） | intercept 是 $\lg(SZ)$，不是分开的 |
| 参数有分数指数 | 试试 $\lg$ 或 reciprocal |

## Quick Checklist — Q2(a) Linearization

- [ ] Rearranged to $y = mx + c$ form
- [ ] $y$-axis quantity identified
- [ ] $x$-axis quantity identified
- [ ] Gradient expression correct (including sign)
- [ ] Y-intercept expression correct
- [ ] If $\lg$ or $\ln$: argument is dimensionless ($V/\text{V}$, not $V$)
- [ ] If $\lg$: $a = 10^{\text{intercept}}$
- [ ] If $\ln$: $a = e^{\text{intercept}}$

## Quick Checklist — Q2(b) Graph & Calculation

- [ ] Table calculated with correct derived quantities
- [ ] Axes labelled with quantity and unit
- [ ] Sensible scales (at least half the grid used)
- [ ] Data points plotted correctly (small crosses)
- [ ] Line of best fit drawn (thin, straight, even distribution)
- [ ] Gradient calculated using two points far apart on the line
- [ ] Y-intercept read from graph where line crosses $y$-axis
- [ ] Constant calculated from gradient/intercept

:::tip

Paper 5 Q2 中，推导 gradient 和 intercept 表达式只占 2 分，但与后续的表格计算、画图、求常数紧密相关。公式推导错误会导致后面全线失分。仔细检查符号和对数底数。

:::
