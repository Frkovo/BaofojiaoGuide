---
title: "考前速记"
sidebar_position: 7
---

# 考前速记

## Quick Reference

| Task | Code |
|------|------|
| Declare 1D array (size 10) | `Arr = [0] * 10` |
| Declare 2D array (3 × 4) | `Arr = [[0] * 4 for i in range(3)]` |
| Traverse 1D | `for i in range(len(Arr)):` |
| Traverse 2D | `for r in range(R): for c in range(C):` |
| Read input to array | `Arr[i] = int(input(...))` |
| Sum all elements | `Total = Total + Arr[i]` |
| Find max | `if Arr[i] > Max: Max = Arr[i]` |
| Search | `if Arr[i] == SearchValue:` |
| Global declaration | `global Arr` **before** assignment |

## Common Patterns

:::note[Fill-and-process template]

```python
def main():
    global Arr
    Arr = [0] * 10
    for i in range(10):
        Arr[i] = int(input())
    # process Arr here
```

:::

:::note[Find average]

```python
Total = 0
for i in range(len(Arr)):
    Total = Total + Arr[i]
Average = Total / len(Arr)
```

:::

## Red Flags — Check These During Exam

| Red Flag | What to Check |
|----------|---------------|
| `global` used? | If declaring array inside a function, yes |
| `range(1, N+1)` | Off-by-one — should be `range(N)` |
| `Arr = []` then `Arr[i] = x` | Must use `append()` or pre-allocate |
| `[0] * N` for 2D | Shallow copy bug — use comprehension |
| `input()` without `int()` | String stored instead of number |
| Loop bounds wrong way round | Rows first, columns second in 2D |
| `if Arr[i] = x` | Should be `==` not `=` |
| Array name spelling | Must match exactly what question gives |

## Mark Scheme Keywords

:::note

**M1** = method / structure (loop, function, file open)

**A1** = accuracy (correct variable, correct indexing)

**B1** = bonus / alternative (type conversion, edge case)

:::

## If You Get Stuck

1. Write the loop first: `for i in range(N):`
2. Decide what happens inside: input, calculation, comparison
3. Check array bounds: `0` to `N-1`
4. Check `global` if inside a function
5. Test with a small example mentally
