# Maclaurin Series — Last Minute Summary

## Formula

$$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!}x^n$$

## Standard Expansions (must memorise)

| Function | Expansion (first terms) |
|----------|------------------------|
| $e^x$ | $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots$ |
| $\sin x$ | $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$ |
| $\cos x$ | $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$ |
| $\ln(1+x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots$ |
| $\tan^{-1}x$ | $x - \frac{x^3}{3} + \frac{x^5}{5} - \cdots$ |
| $\sinh x$ | $x + \frac{x^3}{3!} + \frac{x^5}{5!} + \cdots$ |
| $\cosh x$ | $1 + \frac{x^2}{2!} + \frac{x^4}{4!} + \cdots$ |

## Key Tricks

- $a^x = e^{x\ln a}$
- For composite $f(g(x))$, expand $f(u)$ then substitute $u=g(x)$
- For $\ln(\cosh x)$, expand $\cosh x$ then use $\ln(1+u)$ series
- For $\sin^{-1}x$, differentiate first then integrate series

## Derivatives to Remember

$$\frac{d}{dx}a^x = a^x \ln a$$

$$\frac{d}{dx}\sin^{-1}x = \frac{1}{\sqrt{1-x^2}}$$

$$\frac{d}{dx}\tan^{-1}x = \frac{1}{1+x^2}$$

$$\frac{d}{dx}\ln(\cosh x) = \tanh x$$

## Warning Signs

| Expression | Trap |
|------------|------|
| $a^x$ | $\neq xa^{x-1}$, correct: $a^x\ln a$ |
| $\sin^{-1}x$ | derivative has $1/\sqrt{1-x^2}$ |
| $\ln(\cosh x)$ | need $\cosh x$ expansion first |
| $e^{1+x^2}$ | factor $e$ first: $e \cdot e^{x^2}$ |
