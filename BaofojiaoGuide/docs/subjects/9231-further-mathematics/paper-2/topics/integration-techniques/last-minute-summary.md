# Integration Techniques — Last Minute Summary

## Reduction Formulae — Target Pattern

$$I_n = \int f(x,n)\,dx$$

Integration by parts → $I_n = A(n)I_{n-k} + B(x)$

### Common Recurrences

| $I_n$ | Recurrence |
|-------|-----------|
| $\int_0^{\pi/2} \sin^n x\,dx$ | $n I_n = (n-1)I_{n-2}$ |
| $\int_0^{\pi/2} \cos^n x\,dx$ | $n I_n = (n-1)I_{n-2}$ |
| $\int_0^1 x^n e^x\,dx$ | $I_n = e - nI_{n-1}$ |
| $\int_0^1 (1-x^2)^{n/2}\,dx$ | $(n+2)I_n = (n+1)I_{n-2}$ |

### Boundary Values

$$I_0 = \int_a^b 1\,dx = b-a$$

$$I_1: \text{ compute directly}$$

$$\int_0^{\pi/2} \sin^n x\,dx: I_0 = \frac{\pi}{2},\; I_1 = 1$$

## Integration by Parts (LIATE)

$$u = \text{Log} \to \text{Inverse trig} \to \text{Algebraic} \to \text{Trig} \to \text{Exponential}$$

## Partial Fractions Quick Reference

| Denominator Factor | Term Form |
|-------------------|-----------|
| $x-a$ | $\frac{A}{x-a}$ |
| $(x-a)^2$ | $\frac{A}{x-a} + \frac{B}{(x-a)^2}$ |
| $x^2 + a^2$ | $\frac{Ax+B}{x^2+a^2}$ |

## Standard Integrals

$$\int \frac{1}{x}\,dx = \ln|x|$$

$$\int \tan x\,dx = -\ln|\cos x|$$

$$\int \frac{1}{x^2 + a^2}\,dx = \frac{1}{a}\tan^{-1}\frac{x}{a}$$

$$\int \frac{x}{x^2 + a^2}\,dx = \frac{1}{2}\ln(x^2 + a^2)$$

## Trap Checklist

❌ Forgetting $+C$ for indefinite integrals

❌ Substitution: forgetting to change limits

❌ Partial fractions: need $\frac{Bx+C}{x^2+a^2}$, not just $\frac{B}{x^2+a^2}$

❌ Degree of numerator $\ge$ denominator → divide first

❌ Reduction: always state $I_0$ or $I_1$ before iterating
