# Riemann Sums — Last Minute Summary

## Rectangle Bounds

### Increasing Function ($f' &gt; 0$)

Upper bound = right endpoints: $\displaystyle \sum_{i=1}^n f(x_i)\Delta x$

Lower bound = left endpoints: $\displaystyle \sum_{i=0}^{n-1} f(x_i)\Delta x$

### Decreasing Function ($f' &lt; 0$)

Upper bound = left endpoints

Lower bound = right endpoints

## Summation Formulae

$$\sum_{r=1}^n r = \frac{n(n+1)}{2}$$

$$\sum_{r=1}^n r^2 = \frac{n(n+1)(2n+1)}{6}$$

$$\sum_{r=1}^n r^3 = \left[\frac{n(n+1)}{2}\right]^2$$

## Stirling Approximation

$$\ln N! = \sum_{r=1}^N \ln r$$

Since $\ln x$ is increasing:
$$\int_1^N \ln x\,dx \le \ln N! \le \int_1^N \ln x\,dx + \ln N$$

$$N\ln N - N + 1 \le \ln N! \le N\ln N - N + 1 + \ln N$$

Exponential form: $N^N e^{1-N} \le N! \le N^{N+1} e^{1-N}$

## Riemann Sum to Definite Integral

$$\lim_{n\to\infty} \frac{1}{n} \sum_{r=1}^n f\left(\frac{r}{n}\right) = \int_0^1 f(x)\,dx$$

## Trap Checklist

❌ Forgetting to check increasing/decreasing before picking endpoints

❌ Right endpoints: $i = 1$ to $n$, Left endpoints: $i = 0$ to $n-1$

❌ $\sum r^2$ formula: $\frac{n(n+1)(2n+1)}{6}$, not $\frac{n(n+1)}{2}$

❌ $\ln N!$ summation: $\sum_{r=1}^N \ln r$, lower bound uses $N-1$ terms

❌ Inequality direction: upper $\ge$ integral $\ge$ lower

❌ $e^{N\ln N - N + 1} = N^N \cdot e^{1-N}$, don't forget $e^{a+b}=e^a e^b$
