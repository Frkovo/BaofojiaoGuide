---
title: 考前速查
sidebar_position: 7
---

# Last-Minute Summary — Integration

## Which inverse formula to use
| Integral | Result | Common wrong answer |
|----------|--------|---------------------|
| ∫ dx/√(a²−x²) | sin⁻¹(x/a) + C | sinh⁻¹(x/a) ✗ |
| ∫ dx/(x²+a²) | (1/a)tan⁻¹(x/a) + C | — |
| ∫ dx/√(x²+a²) | sinh⁻¹(x/a) + C | cosh⁻¹(x/a) ✗ |
| ∫ dx/√(x²−a²) | cosh⁻¹(x/a) + C | sinh⁻¹(x/a) ✗ |

## Arc length vs surface area
- Arc length: s = ∫√(1+(dy/dx)²) dx
- Surface area: S = 2π∫ y√(1+(dy/dx)²) dx (extra factor 2πy!)

## Reduction formulae
- Always start with integration by parts
- Express Iₙ in terms of Iₙ₋₂ (usually)
- For specific n, apply recursively until base case

## Rectangle bounds
- Upper bound: use outer rectangles (right endpoint heights)
- Lower bound: use inner rectangles (left endpoint heights)
- Sum rectangles → compare to integral → inequality
