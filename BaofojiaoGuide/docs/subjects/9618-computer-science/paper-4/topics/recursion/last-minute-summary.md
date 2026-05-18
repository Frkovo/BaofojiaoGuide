---
title: 考前速记
---

# 考前速记

## Recursion Template

```python
def func(parameters):
    if base_condition:
        return base_value
    else:
        return combine(parameters, func(smaller_parameters))
```

## Key Rules

| Rule | Why |
|------|-----|
| Must have base case | Stops infinite recursion |
| Must shrink input | Ensures base case is reached |
| Must `return` in every branch | Avoids `None` result |
| Pass `n - 1` not `n--` | Don't mutate parameters |

## Common Base Cases

| Function | Base Case | Return |
|----------|-----------|--------|
| Factorial | `n &lt;= 1` | `1` |
| Fibonacci | `n &lt;= 1` | `n` |
| Power | `n == 0` | `1` |
| GCD | `b == 0` | `a` |
| Sum of array | `i == len(arr)` | `0` |

## Converting Iterative → Recursive

| Iterative | Recursive |
|-----------|-----------|
| Loop variable (`i`) | Function parameter (`i`) |
| Loop condition (`i < n`) | Base case (`if i >= n`) |
| Loop body | Recursive case |
| Accumulator (`total`) | Pass as parameter or return |

## Exam Day Reminders

- Read the problem: identify **base case** first
- Write the function signature **before** the body
- If the problem says "array of `n` elements", you likely need an **index parameter**
- **Trace** your own code mentally to verify it works
- If tracing: show **every call** and **every return**
- For convert questions: preserve the **same logic**, just change the structure

:::note[Last Minute]

If you forget everything, write:

```
if simplest case: return answer
else: return operation + recursive_call(smaller_input)
```

:::
