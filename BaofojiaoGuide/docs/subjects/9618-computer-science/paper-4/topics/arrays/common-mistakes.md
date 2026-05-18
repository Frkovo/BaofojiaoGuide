---
title: "常见错误"
sidebar_position: 5
---

# 常见错误

## Mistake 1: Forgetting `global` Inside a Function

**Wrong:**

```python
def main():
    MyArray = [0] * 10   # local variable, not accessible elsewhere
```

**Fix:**

```python
def main():
    global MyArray
    MyArray = [0] * 10
```

**Why:** Without `global`, Python creates a new local variable. Other functions cannot see it, causing `NameError`.

---

## Mistake 2: Off-by-One Index Error

**Wrong:**

```python
Arr = [0] * 10
for i in range(1, 11):   # index 10 is out of bounds
    Arr[i] = i
```

**Fix:**

```python
Arr = [0] * 10
for i in range(10):      # indices 0–9
    Arr[i] = i
```

**Why:** Python uses 0-based indexing. `range(10)` produces `0, 1, ..., 9`.

---

## Mistake 3: Not Pre-Allocating Before Index Assignment

**Wrong:**

```python
Arr = []
Arr[0] = 5     # IndexError: list assignment index out of range
```

**Fix:**

```python
Arr = [0] * 10
Arr[0] = 5     # OK

# OR use append:
Arr = []
Arr.append(5)  # OK
```

**Why:** You cannot assign to an index that does not exist. Pre-allocate with `[0] * N` or use `append()`.

---

## Mistake 4: Shallow Copy in 2D Arrays

**Wrong:**

```python
Arr = [[0] * 4] * 3    # 3 references to the same row
Arr[0][1] = 5           # changes ALL rows at column 1
```

**Fix:**

```python
Arr = [[0 for j in range(4)] for i in range(3)]
# OR
Arr = [[0] * 4 for i in range(3)]
```

**Why:** `[row] * 3` creates shallow copies — all rows point to the same list object. Modifying one row "modifies" all rows.

---

## Mistake 5: Wrong Loop Bounds for 2D Arrays

**Wrong:**

```python
Arr = [[0 for j in range(4)] for i in range(3)]
for i in range(4):    # should be range(3) for rows
    for j in range(3):  # should be range(4) for columns
        print(Arr[i][j])
```

**Fix:**

```python
for i in range(len(Arr)):        # rows = 3
    for j in range(len(Arr[i])): # columns = 4
        print(Arr[i][j])
```

**Why:** Use `len(Arr)` for row count and `len(Arr[0])` for column count to avoid hardcoding wrong bounds.

---

## Mistake 6: Not Converting Input Type

**Wrong:**

```python
Scores[i] = input("Enter score: ")   # stores string, not integer
```

**Fix:**

```python
Scores[i] = int(input("Enter score: "))
```

**Why:** `input()` returns a string. Numeric operations (`+`, `>`, etc.) will fail or behave unexpectedly.

---

## Mistake 7: Using `=` Instead of `==` in Comparison

**Wrong:**

```python
if Arr[i] = SearchValue:   # assignment, not comparison
```

**Fix:**

```python
if Arr[i] == SearchValue:
```

**Why:** Single `=` is assignment, which always evaluates as True (truthy). Double `==` is equality comparison.
