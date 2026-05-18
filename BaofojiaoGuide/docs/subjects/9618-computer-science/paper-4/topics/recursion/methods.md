---
title: 解题方法
---

# 解题方法

## Step 1: Identify the Base Case

The base case is the **smallest possible input** that can be answered directly without recursion.

| Problem | Base Case |
|---------|-----------|
| Factorial `n!` | `n &lt;= 1` → return `1` |
| Fibonacci | `n &lt;= 1` → return `n` |
| Power `x^n` | `n == 0` → return `1` |
| Sum of array | `i >= len(arr)` → return `0` |
| Palindrome | `start >= end` → return `True` |

---

## Step 2: Design the Recursive Call

The recursive case must:
1. **Shrink** the problem toward the base case
2. Call the **same function** with a **smaller argument**
3. **Combine** the result appropriately

| Problem | Recursive Call | Combination |
|---------|---------------|-------------|
| Factorial | `factorial(n - 1)` | `n * ...` |
| Fibonacci | `fib(n - 1) + fib(n - 2)` | `... + ...` |
| Power | `power(x, n - 1)` | `x * ...` |
| Sum of array | `sum(arr, i + 1)` | `arr[i] + ...` |
| Palindrome | `is_pal(arr, s + 1, e - 1)` | `arr[s] == arr[e] and ...` |

---

## Step 3: Template Pattern

```python
def recursive_function(parameters):
    if base_condition:
        return base_value
    else:
        # recursive case: call with smaller input
        return combine(parameters[0], recursive_function(smaller_parameters))
```

:::note[Checklist]

- Base case returns a value (not recursive)
- Recursive call argument is **strictly smaller**
- All code paths have a `return`
- Function works for edge cases (e.g. `n = 0`, empty array)

:::
