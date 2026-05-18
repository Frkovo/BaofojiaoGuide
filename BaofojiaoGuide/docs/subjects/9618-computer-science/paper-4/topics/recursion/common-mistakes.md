---
title: 常见错误
---

# 常见错误

## 1. No Base Case

```python
def factorial(n):          # ❌ Missing base case
    return n * factorial(n - 1)
```

Causes **infinite recursion** → stack overflow.

**Fix:** Always add a base case check (`if n &lt;= 1: return 1`).

---

## 2. No Return Statement

```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        factorial(n - 1)   # ❌ Missing return
```

The recursive result is computed but **not returned** → function returns `None`.

**Fix:** `return n * factorial(n - 1)`

---

## 3. Problem Doesn't Shrink

```python
def countdown(n):
    if n == 0:
        return
    else:
        return countdown(n)   # ❌ n never decreases
```

Same `n` passed every time → infinite recursion.

**Fix:** Pass `n - 1` (or a smaller value).

---

## 4. Wrong Base Case Condition

```python
def factorial(n):
    if n == 1:      # ❌ Fails when n = 0
        return 1
    else:
        return n * factorial(n - 1)
```

Calling `factorial(0)` causes infinite recursion because `n` skips past `1`.

**Fix:** Use `n &lt;= 1` instead of `n == 1`.

---

## 5. Modifying the Parameter

```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        n = n - 1              # ❌ Don't modify the parameter
        return n * factorial(n)
```

Modifying `n` before the recursive call changes the multiplication value.

**Fix:** Pass `n - 1` directly: `return n * factorial(n - 1)`

---

## 6. Confusing Iteration and Recursion

```python
def sum_array(arr):
    total = 0
    if len(arr) == 0:          # ❌ Mixed loop + recursion
        return 0
    for i in range(len(arr)):
        total += arr[i]
    return total + sum_array(arr)  # ❌ No shrinking argument
```

**Fix:** Write pure recursion with index parameter.

---

## 7. Stack Overflow for Deep Recursion

Very deep recursion (e.g. `n = 10000`) may overflow the call stack.

**Hint for exams:** If the question says "recursive function for a large `n`", consider the **depth limit**.

---

## Quick Checklist

| Check | OK? |
|-------|-----|
| Base case exists? | ☐ |
| Base case returns a value? | ☐ |
| Recursive call argument is smaller? | ☐ |
| Recursive result is returned? | ☐ |
| All branches have `return`? | ☐ |
| Function works for edge cases? | ☐ |
