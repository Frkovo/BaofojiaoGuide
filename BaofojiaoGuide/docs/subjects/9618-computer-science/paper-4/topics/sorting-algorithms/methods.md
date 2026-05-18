---
title: "解题方法"
sidebar_position: 3
---

# 解题方法

---

## Method 1: Bubble Sort — Nested Loops, Adjacent Comparison, Swap

**适用条件:** Any question asking for bubble sort implementation.

**步骤:**

1. Get array length `n = len(arr)`
2. Outer loop: `for i in range(n - 1)` — controls number of passes
3. Inner loop: `for j in range(n - 1 - i)` — compares adjacent pairs, unsorted portion shrinks each pass
4. **Comparison:** `if arr[j] > arr[j + 1]` — swap if out of order
5. **Swap:** `arr[j], arr[j + 1] = arr[j + 1], arr[j]` (Python tuple swap) or use temp variable
6. **Return** the sorted array

```python
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

:::note[Key observation]

After each outer loop pass `i`, the largest `i+1` elements are in their correct positions at the end. So inner loop only needs to check up to `n-1-i`.

:::

---

## Method 2: Iterative Insertion Sort — Maintain Sorted Portion, Shift Elements

**适用条件:** Questions asking for standard insertion sort.

**步骤:**

1. Start with first element as the sorted portion: loop `for i in range(1, n)`
2. Pick the current element: `key = arr[i]`
3. Set comparison index: `j = i - 1`
4. **Shift loop:** `while j >= 0 and arr[j] > key:`
   - Move element right: `arr[j + 1] = arr[j]`
   - Decrement `j -= 1`
5. **Insert key** at correct position: `arr[j + 1] = key`
6. Return the sorted array

```python
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

:::note[Key observation]

The left portion `arr[0..i-1]` is always sorted. Each iteration inserts `arr[i]` into this sorted portion by shifting elements right.

:::

---

## Method 3: Recursive Insertion Sort — Base Case, Recurse, Insert Last

**适用条件:** Questions asking for recursion or converting iterative to recursive.

**步骤:**

1. **Base case:** `if n <= 1: return` — single element is already sorted
2. **Recursive call:** `insertionSortRec(arr, n - 1)` — sort first `n-1` elements
3. **Store last element:** `key = arr[n - 1]`
4. **Shift loop:** `j = n - 2`; while `j >= 0 and arr[j] > key`, shift right and decrement
5. **Insert:** `arr[j + 1] = key`

```python
def insertionSortRec(arr, n):
    if n <= 1:
        return
    insertionSortRec(arr, n - 1)
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
```

:::note[Key observation]

The recursive version replaces the outer `for i in range(1, n)` loop with a recursive parameter `n` that decreases to `1`. The base case `n <= 1` replaces the loop termination condition.

:::
