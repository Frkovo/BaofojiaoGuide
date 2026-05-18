---
title: "常见错误"
sidebar_position: 5
---

# 常见错误

---

### 1. Outer loop uses `range(n)` instead of `range(n - 1)`

In bubble sort, `i` only needs to go up to `n-2` because `n-1` passes would be redundant. Using `range(n)` works but wastes one pass — in a 4-mark question, this loses accuracy.

```python
# Wrong
for i in range(n):       # ❌ extra pass
# Correct
for i in range(n - 1):   # ✅ n-1 passes
```

### 2. Inner loop bound wrong in bubble sort

Using `range(n - 1)` for the inner loop ignores that the last `i` elements are already sorted.

```python
# Wrong — compares already-sorted elements
for j in range(n - 1):
# Correct — skips sorted tail
for j in range(n - 1 - i):
```

### 3. Comparison direction reversed

Always check: do we want ascending (use `>`) or descending (use `<`)? Default exam assumption is **ascending**.

```python
# Wrong (sorts descending)
if arr[j] < arr[j + 1]:
# Correct (sorts ascending)
if arr[j] > arr[j + 1]:
```

### 4. Forgetting to decrement `j` in insertion sort shift loop

Without `j -= 1`, the while loop runs forever.

```python
# Wrong — infinite loop
while j >= 0 and arr[j] > key:
    arr[j + 1] = arr[j]
# Correct
while j >= 0 and arr[j] > key:
    arr[j + 1] = arr[j]
    j -= 1
```

### 5. Off-by-one in insertion sort outer loop

Starting `i` at `0` means `arr[0]` gets treated as unsorted, causing index errors.

```python
# Wrong — i should start at 1
for i in range(0, n):
# Correct
for i in range(1, n):
```

### 6. Recursive insertion sort missing base case or wrong parameter

Without a base case, recursion never terminates.

```python
# Wrong — no base case, will cause RecursionError
def insertionSortRec(arr, n):
    insertionSortRec(arr, n - 1)
    # ... insert logic ...

# Correct
def insertionSortRec(arr, n):
    if n <= 1:          # ✅ base case
        return
    insertionSortRec(arr, n - 1)
    # ... insert logic ...
```

### 7. Function returns `None` instead of the sorted array

If the question specifies a function (not a procedure), you must `return arr`.

```python
# Wrong — no return
def bubbleSort(arr):
    # ... sorting logic ...

# Correct
def bubbleSort(arr):
    # ... sorting logic ...
    return arr
```

### 8. Confusing `i` and `j` in bubble sort nested loops

Using `i` for the inner loop and `j` for the outer loop is not wrong per se, but examiners expect `i` for outer and `j` for inner. Mixing them may lead to confusion when tracing.
