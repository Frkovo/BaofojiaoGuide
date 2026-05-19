# Parametric Equations — Last Minute Summary

## Differentiation

$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{\dot{y}}{\dot{x}}$$

$$\frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}} \neq \frac{\ddot{y}}{\ddot{x}}$$

## Arc Length

$$L = \int_{t_1}^{t_2} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt$$

## Common Simplifications

| Expression | Simplified |
|------------|-----------|
| $(1-\cos\theta)^2 + \sin^2\theta$ | $2(1-\cos\theta) = 4\sin^2(\theta/2)$ |
| $(\cos t - \cos 2t)^2 + (\sin t - \sin 2t)^2$ | $2(1-\cos t)$ |
| $(a\sin\theta)^2 + (a\cos\theta)^2$ | $a^2$ |

## Half-Angle Identities (Essential for Arc Length)

$$1-\cos\theta = 2\sin^2\frac{\theta}{2}$$

$$1+\cos\theta = 2\cos^2\frac{\theta}{2}$$

## Trap Checklist

❌ $\frac{d^2y}{dx^2} \neq \frac{\ddot{y}}{\ddot{x}}$ — must differentiate $\frac{dy}{dx}$ then divide by $\dot{x}$

❌ Arc length: $\sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}$, not $\sqrt{\frac{dx}{dt} + \frac{dy}{dt}}$

❌ Integrate w.r.t. $t$, not $x$ or $y$

❌ Check sign when removing $\sqrt{\sin^2} = |\sin|$

❌ Simplify $\frac{dy}{dx}$ fully (e.g. $\frac{t}{2}$ not $\frac{t^2}{2t}$)
