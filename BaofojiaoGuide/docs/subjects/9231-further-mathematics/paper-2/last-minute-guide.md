---
title: 考前速通
sidebar_position: 4
---

# 考前速通指南 — Paper 2

## 必须记住的公式（MF19 不一定全有）

### Hyperbolic Functions
$$\sinh x = \frac{e^x - e^{-x}}{2},\qquad \cosh x = \frac{e^x + e^{-x}}{2}$$
$$\cosh^2 x - \sinh^2 x \equiv 1,\qquad \sinh 2x \equiv 2\sinh x\cosh x$$

**Inverse hyperbolic（对数形式）：**
$$\sinh^{-1} x = \ln(x + \sqrt{x^2+1})$$
$$\cosh^{-1} x = \ln(x + \sqrt{x^2-1})\;(x\ge 1)$$
$$\tanh^{-1} x = \frac12\ln\frac{1+x}{1-x}\;(|x|<1)$$

### Derivatives
$$\frac{d}{dx}\sin^{-1}x = \frac{1}{\sqrt{1-x^2}},\quad \frac{d}{dx}\cos^{-1}x = -\frac{1}{\sqrt{1-x^2}}$$
$$\frac{d}{dx}\sinh^{-1}x = \frac{1}{\sqrt{1+x^2}},\quad \frac{d}{dx}\cosh^{-1}x = \frac{1}{\sqrt{x^2-1}}$$

### Standard Integrals
$$\int\frac{dx}{\sqrt{a^2-x^2}} = \sin^{-1}\frac{x}{a}+C,\qquad \int\frac{dx}{a^2+x^2} = \frac1a\tan^{-1}\frac{x}{a}+C$$
$$\int\frac{dx}{\sqrt{x^2+a^2}} = \sinh^{-1}\frac{x}{a}+C,\qquad \int\frac{dx}{\sqrt{x^2-a^2}} = \cosh^{-1}\frac{x}{a}+C$$

### de Moivre
$$(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$$

### Maclaurin
$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \cdots$$

## 见到什么就先做什么

| 看到这个… | 第一步 |
|-----------|--------|
| Hyperbolic equation | 写成指数形式 |
| $3\times3$ system | 算行列式 |
| Eigenvalues | $\det(A-\lambda I)=0$ |
| $1/\sqrt{x^2+a^2}$ | 用 $\sinh^{-1}$ 或 $x=a\sinh u$ |
| de Moivre | 写成 $r(\cos\theta+i\sin\theta)$ 形式 |
| 2nd order DE | 写辅助方程 |
| Maclaurin | 算 $f(0),f'(0),f''(0)$ |

## 时间分配（75 分 / 120 分钟）

| 分值 | 建议时间 |
|------|---------|
| 3 分 | ~5 分钟 |
| 5 分 | ~8 分钟 |
| 8 分 | ~13 分钟 |
| 10 分 | ~16 分钟 |
| 12+ 分 | ~18–20 分钟 |

## 卡住时

1. 跳过——别在 1 道题上浪费 15 分钟
2. "Show that" 卡住？从答案往回推
3. 写下你认为相关的公式（可能拿 M 分）
4. 检查答案是否满足原方程

## 交卷前

- [ ] 每题都写到 3 s.f.（或题目指定精度）
- [ ] 不定积分加了 $+C$？
- [ ] 所有符号检查过一遍
- [ ] 微分方程初值条件代入了？
