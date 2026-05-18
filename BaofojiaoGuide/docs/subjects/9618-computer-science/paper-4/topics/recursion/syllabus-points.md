---
title: 考纲要点
---

# 考纲要点

## 19.2 Recursion

### 19.2.1 Show understanding of recursion

- Recursion is a technique where a function calls **itself**
- Each recursive call solves a **smaller** instance of the same problem
- Recursion uses a **call stack** — each call is pushed onto the stack and popped off when it returns
- **Base case:** the condition that stops recursion
- **Recursive case:** the call to the function with a smaller argument

### 19.2.2 Write recursive functions

- Must handle both **base case** and **recursive case**
- The problem must **shrink** toward the base case with each recursive call (e.g. `n - 1`, `i + 1`, smaller substring)
- Use `return` in **every** branch
- Suitable problems:
  - Factorial (`n!`)
  - Fibonacci sequence
  - Power (`x^n`)
  - Greatest Common Divisor (GCD)
  - Sum of array / list
  - Palindrome check
  - Binary search

### 19.2.3 Trace recursive functions

- Trace shows the **order** of calls (push onto call stack)
- Trace shows the **return values** (pop from call stack)
- Use a **tree diagram** or a **table** with columns: Call | Parameters | Result
- Work **top-down** then **bottom-up**

### 19.2.4 Convert iterative to recursive and vice versa

- **Iterative → Recursive:**
  - Loop variable → function parameter
  - Loop condition → base case
  - Loop body → recursive case
  - Accumulator → passed as parameter or returned

- **Recursive → Iterative:**
  - Replace recursion with a loop
  - Use a stack data structure if needed (for non-tail recursion)

### Common Functions to Know

| Function | Base Case | Recursive Call |
|----------|-----------|----------------|
| `factorial(n)` | `n &lt;= 1` → `1` | `n * factorial(n - 1)` |
| `fib(n)` | `n &lt;= 1` → `n` | `fib(n - 1) + fib(n - 2)` |
| `power(x, n)` | `n == 0` → `1` | `x * power(x, n - 1)` |
| `gcd(a, b)` | `b == 0` → `a` | `gcd(b, a % b)` |
| `sum(arr, i)` | `i == len(arr)` → `0` | `arr[i] + sum(arr, i + 1)` |
| `is_pal(s)` | `len(s) &lt;= 1` → `True` | `s[0] == s[-1] and is_pal(s[1:-1])` |
