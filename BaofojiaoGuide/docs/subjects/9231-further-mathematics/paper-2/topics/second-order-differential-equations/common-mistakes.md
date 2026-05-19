---
title: 常见错误
sidebar_position: 6
---

# 常见错误 — Second Order Differential Equations

## 错误 1：辅助方程漏 $= 0$

**错误**：写出 $am^2 + bm + c$ 但没有 $= 0$。

**正解**：辅助方程必须等于 $0$，即 $am^2 + bm + c = 0$。

## 错误 2：重根 CF 形式写错

**错误**：重根 $m$ 时写 $CF = Ae^{mx} + Be^{mx}$ 或 $Ae^{mx} + Be^{mx}$。

**正解**：重根时必须乘 $x$：$CF = (A + Bx)e^{mx}$。

## 错误 3：复数根的 CF 形式

**错误**：$m = \alpha \pm i\beta$ 写成 $Ae^{\alpha x}\cos\beta x + Be^{\alpha x}\sin\beta x$ 不含括号。

**正解**：$CF = e^{\alpha x}(A\cos\beta x + B\sin\beta x)$，或明确写出两项。

注意：有时写成 $Ae^{\alpha x}\cos\beta x + Be^{\alpha x}\sin\beta x$ 也算对，但要统一。

## 错误 4：PI 试设与 CF 冲突

**错误**：解 $y'' - 3y' + 2y = e^x$ 时设 $y_p = Ce^x$，但 CF 中已有 $Ae^x$。

**正解**：冲突时试设 $y_p = Cxe^x$。若仍冲突（重根），乘 $x^2$。

## 错误 5：PI 试设不完整

**错误**：对 $f(x) = 3\cos 2x$ 只设 $y_p = C\cos 2x$，漏 $\sin 2x$ 项。

**正解**：正/余弦 RHS 必须同时包含 $\cos$ 和 $\sin$ 项：$y_p = C\cos\omega x + D\sin\omega x$。

## 错误 6：初值代入时未先求导

**错误**：代入 $y'(x_0) = y_0'$ 时直接用通解，未对通解求导。

**正解**：先对通解 $y = y_c + y_p$ 求导得 $y'$，再代入 $x = x_0$。

## 错误 7：Euler-Cauchy 代换混淆

**错误**：使用 $t = e^u$ 变换后，忘记将 $y$ 也视为 $u$ 的函数，混合使用 $t$ 和 $u$。

**正解**：统一使用新变量 $u$，求出 $y(u)$ 后再将 $u = \ln t$ 代回。

## 错误 8：多项式 RHS 的 PI 次数偏低

**错误**：对 $f(x) = 3x^2 + 30x$，设 $y_p = \alpha x^2 + \beta x$，漏常数项。

**正解**：多项式 PI 应包括所有降幂项：$\alpha x^2 + \beta x + \gamma$。

## 错误 9：耦合系统中特征值/向量计算错误

**错误**：特征值求错或特征向量方向搞反。

**正解**：验算 $A\mathbf{v} = \lambda\mathbf{v}$ 是否成立。
