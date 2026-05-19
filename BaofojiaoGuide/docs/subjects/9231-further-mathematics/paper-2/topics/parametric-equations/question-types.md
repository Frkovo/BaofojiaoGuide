# Parametric Equations — Question Types

## Type 1: Parametric Differentiation (3–5 marks)

> **Example: s20/23 Q5** — A curve is defined parametrically by $x = t^2 + 1$, $y = t^3 - 3t$.
> (a) Find $\frac{dy}{dx}$ in terms of $t$. [2]
> (b) Find $\frac{d^2y}{dx^2}$ in terms of $t$. [3]

<details>
<summary>📝 MS 展开查看</summary>

**(a)** $\frac{dx}{dt} = 2t$, $\frac{dy}{dt} = 3t^2 - 3$

$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{3t^2 - 3}{2t} = \frac{3(t^2 - 1)}{2t}$$

**M1** — Correct $\frac{dy}{dt}$ and $\frac{dx}{dt}$
**A1** — Correct $\frac{dy}{dx}$

**(b)** $\frac{d}{dt}\left(\frac{dy}{dx}\right) = \frac{d}{dt}\left(\frac{3t^2 - 3}{2t}\right)$

Using quotient rule: $\frac{(6t)(2t) - (3t^2 - 3)(2)}{4t^2} = \frac{12t^2 - 6t^2 + 6}{4t^2} = \frac{6t^2 + 6}{4t^2} = \frac{3(t^2 + 1)}{2t^2}$

$$\frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}} = \frac{3(t^2 + 1)}{2t^2} \div 2t = \frac{3(t^2 + 1)}{4t^3}$$

**M1** — Differentiate $\frac{dy}{dx}$ with respect to $t$
**A1** — Correct expression for $\frac{d}{dt}\left(\frac{dy}{dx}\right)$
**A1** — Correct $\frac{d^2y}{dx^2}$

</details>

> **Example: w21/22 Q5** — Given $x = \ln(1 + t^2)$, $y = t - \tan^{-1} t$.
> (a) Find $\frac{dy}{dx}$ in terms of $t$, simplifying your answer. [2]
> (b) Show that $\frac{d^2y}{dx^2} = \frac{f(t)}{(1+t^2)^2}$. [3]

<details>
<summary>📝 MS 展开查看</summary>

**(a)** $\frac{dx}{dt} = \frac{2t}{1+t^2}$, $\frac{dy}{dt} = 1 - \frac{1}{1+t^2} = \frac{t^2}{1+t^2}$

$$\frac{dy}{dx} = \frac{t^2/(1+t^2)}{2t/(1+t^2)} = \frac{t^2}{2t} = \frac{t}{2}$$

**M1** — Correct $\frac{dx}{dt}$ and $\frac{dy}{dt}$
**A1** — Correct simplified $\frac{t}{2}$

**(b)** $\frac{d}{dt}\left(\frac{dy}{dx}\right) = \frac{1}{2}$

$$\frac{d^2y}{dx^2} = \frac{1/2}{dx/dt} = \frac{1/2}{2t/(1+t^2)} = \frac{1+t^2}{4t}$$

**M1** — Differentiate $\frac{dy}{dx}$ w.r.t. $t$
**A1** — Divide by $\frac{dx}{dt}$ to find $\frac{d^2y}{dx^2}$
**A1** — Correct $\frac{1+t^2}{4t}$

</details>

## Type 2: Arc Length of Parametric Curves (5–6 marks)

> **Example: w20/21 Q5** — A curve is given by $x = 2\cos t - \cos 2t$, $y = 2\sin t - \sin 2t$ for $0 \le t \le \pi$. Find the length of the curve.

<details>
<summary>📝 MS 展开查看</summary>

$\frac{dx}{dt} = -2\sin t + 2\sin 2t$, $\frac{dy}{dt} = 2\cos t - 2\cos 2t$

$$\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 = 4(\sin^2 2t - 2\sin t\sin 2t + \sin^2 t) + 4(\cos^2 t - 2\cos t\cos 2t + \cos^2 2t)$$

$$= 4(2 - 2\sin t\sin 2t - 2\cos t\cos 2t) = 8(1 - \cos t)$$

Using $\cos 2t = 2\cos^2 t - 1$, $\sin 2t = 2\sin t\cos t$:

$\sin t\sin 2t + \cos t\cos 2t = 2\sin^2 t\cos t + \cos t(2\cos^2 t - 1) = 2\cos t(\sin^2 t + \cos^2 t) - \cos t = \cos t$

So $\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 = 8(1 - \cos t) = 16\sin^2\left(\frac{t}{2}\right)$

$$L = \int_0^\pi \sqrt{16\sin^2\left(\frac{t}{2}\right)}\,dt = \int_0^\pi 4\left|\sin\frac{t}{2}\right|dt = 4\int_0^\pi \sin\frac{t}{2}\,dt$$

$$= 4\left[-2\cos\frac{t}{2}\right]_0^\pi = 4(-2\cos\frac{\pi}{2} + 2\cos 0) = 4(0 + 2) = 8$$

**Marks scheme:**
- **M1** — Find $\frac{dx}{dt}$, $\frac{dy}{dt}$ correctly
- **M1** — Attempt $\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2$
- **A1** — Simplify to $8(1 - \cos t)$ or $16\sin^2(t/2)$
- **M1** — Set up correct integral $\int\sqrt{\cdots}\,dt$
- **A1** — Correct simplified integrand
- **A1** — Correct length $8$

</details>

> **Example: w23/21 Q5** — A curve is defined by $x = a(\theta - \sin\theta)$, $y = a(1 - \cos\theta)$ for $0 \le \theta \le 2\pi$. Find the arc length.

<details>
<summary>📝 MS 展开查看</summary>

$\frac{dx}{d\theta} = a(1 - \cos\theta)$, $\frac{dy}{d\theta} = a\sin\theta$

$$\left(\frac{dx}{d\theta}\right)^2 + \left(\frac{dy}{d\theta}\right)^2 = a^2[(1 - \cos\theta)^2 + \sin^2\theta]$$

$$= a^2[1 - 2\cos\theta + \cos^2\theta + \sin^2\theta] = a^2[2 - 2\cos\theta]$$

$$= 4a^2\sin^2\left(\frac{\theta}{2}\right)$$

$$L = \int_0^{2\pi} \sqrt{4a^2\sin^2\left(\frac{\theta}{2}\right)}\,d\theta = 2a\int_0^{2\pi} \sin\left(\frac{\theta}{2}\right)d\theta$$

$$= 2a\left[-2\cos\left(\frac{\theta}{2}\right)\right]_0^{2\pi} = 2a(-2\cos\pi + 2\cos 0) = 2a(2 + 2) = 8a$$

**Marks scheme:**
- **M1** — Find $\frac{dx}{d\theta}$, $\frac{dy}{d\theta}$
- **M1** — Form $\left(\frac{dx}{d\theta}\right)^2 + \left(\frac{dy}{d\theta}\right)^2$
- **A1** — Simplify to $4a^2\sin^2(\theta/2)$
- **M1** — Set up arc length integral
- **A1** — Correct integrand $\sqrt{4a^2\sin^2(\theta/2)}$
- **A1** — Correct answer $8a$

</details>
