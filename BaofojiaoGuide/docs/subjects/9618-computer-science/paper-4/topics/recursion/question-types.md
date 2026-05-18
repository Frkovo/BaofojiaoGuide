---
title: 题型分析
---

# 题型分析

## Q1: Write a Recursive Function from Description (5–6 marks)

**Identify:** Question gives a problem (e.g. factorial, Fibonacci, power, sum of array, palindrome) and asks you to write a recursive function.

**Standard Method:**

1. Identify the **base case** — the simplest input that can be solved directly
2. Write the base case with `return`
3. Identify the **recursive case** — how to express the problem in terms of a smaller sub-problem
4. Call the function recursively with a **smaller argument**
5. Combine the result (if needed) and `return` it

**MS Pattern:**

<details>
<summary>Mark Scheme</summary>

- **M1** Correct base case condition and return value
- **A1** Correct recursive call with smaller argument
- **A1** Correct combination/operation on recursive result
- **A1** Correct `return` in all branches
- **A1** Correct function signature (parameters and return type)

</details>

**Example 1:** Factorial `n!`

```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
```

**Example 2:** Sum of first `n` natural numbers

```python
def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)
```

**Traps:**
- Using `n--` instead of `n - 1` (modifies `n`, wrong)
- No `return` before recursive call
- Base case condition wrong (e.g. `n == 0` when `n == 1` is correct)

---

## Q2: Convert Iterative to Recursive (4–6 marks)

**Identify:** Question gives an iterative loop (usually `while` or `for`) and asks you to rewrite it recursively. e.g. 9618/w23/qp/41 Q1.

**Standard Method:**

1. Identify what changes each iteration (the **loop variable** becomes the function **parameter**)
2. The **loop condition** becomes the **base case** (when to stop recursing)
3. The **loop body** becomes the **recursive case**
4. Accumulate result via **parameters** (passing state forward) or **return values**

**MS Pattern:**

<details>
<summary>Mark Scheme</summary>

- **M1** Correct function signature matching iterative parameters
- **A1** Base case corresponding to loop termination condition
- **A1** Recursive call updates the variable that changed in the loop
- **A1** Correct accumulation/passing of result
- **A1** Function returns the final result

</details>

**Example 1:** Iterative sum of array → recursive

```python
# Iterative
def sum_array(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

# Recursive
def sum_array_rec(arr, i):
    if i >= len(arr):
        return 0
    else:
        return arr[i] + sum_array_rec(arr, i + 1)
```

**Example 2:** Iterative power → recursive

```python
# Iterative
def power(x, n):
    result = 1
    while n > 0:
        result *= x
        n -= 1
    return result

# Recursive
def power_rec(x, n):
    if n == 0:
        return 1
    else:
        return x * power_rec(x, n - 1)
```

**Traps:**
- Forgetting to pass the data structure (e.g. array) as parameter
- Not returning the recursive result
- Base case does not match loop exit condition

---

## Q3: Trace Recursive Function Execution (2–3 marks)

**Identify:** Question provides a recursive function and asks you to trace its execution for a given input. May require a tree diagram or table.

**Standard Method:**

1. Start with the initial call
2. Work top-down: each recursive call goes on a new line / new branch
3. When base case is reached, return value and work back up
4. Show **each call** and **each return value**

**MS Pattern:**

<details>
<summary>Mark Scheme</summary>

- **M1** Shows all recursive calls in correct order
- **A1** Correct return values for each call
- **A1** Final answer matches the trace

</details>

**Example 1:** Trace `factorial(3)`

```
factorial(3) → 3 * factorial(2)
  factorial(2) → 2 * factorial(1)
    factorial(1) → 1 (base case)
    return 1
  return 2 * 1 = 2
return 3 * 2 = 6
```

**Example 2:** Trace `power_rec(2, 3)`

```
power_rec(2, 3) → 2 * power_rec(2, 2)
  power_rec(2, 2) → 2 * power_rec(2, 1)
    power_rec(2, 1) → 2 * power_rec(2, 0)
      power_rec(2, 0) → 1 (base case)
      return 1
    return 2 * 1 = 2
  return 2 * 2 = 4
return 2 * 4 = 8
```

**Traps:**
- Not showing intermediate steps
- Confusing order of calls (last in, first out)
- Forgetting the base case return value
