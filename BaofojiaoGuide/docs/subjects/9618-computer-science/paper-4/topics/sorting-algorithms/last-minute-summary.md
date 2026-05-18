---
title: "考前速记"
sidebar_position: 7
---

# 考前速记

---

## Bubble Sort vs Insertion Sort — Side by Side

| Bubble Sort | Insertion Sort |
|-------------|----------------|
| Nested loops (both `for`) | Outer `for`, inner `while` |
| Compare adjacent, swap | Shift right, insert key |
| Largest element bubbles to end | Sorted portion grows from left |
| Inner loop bound shrinks: `n-1-i` | Inner loop bound grows: `j ≥ 0` |

## Quick Templates

### Bubble Sort

```python
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### Insertion Sort (Iterative)

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

### Insertion Sort (Recursive)

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

## Big O

| Algorithm | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Bubble Sort | \(O(n)\) | \(O(n^2)\) | \(O(n^2)\) | \(O(1)\) |
| Insertion Sort | \(O(n)\) | \(O(n^2)\) | \(O(n^2)\) | \(O(1)\) |

## When to Use Which

| Situation | Recommendation |
|-----------|---------------|
| Exam asks for bubble sort by name | Use bubble sort |
| Exam asks for insertion sort by name | Use insertion sort |
| Nearly-sorted data | Insertion sort (fast best case) |
| Need simple code for small array | Either — bubble sort is simpler |
| Question asks for recursion | Insertion sort recursive |
| Question asks iterative → recursive conversion | Convert insertion sort (commonest) |
| Linked list sorting | Insertion sort preferred |

## 考前 Checklist

- [ ] Can I write bubble sort from memory? (nested loops, adjacent comparison, swap)
- [ ] Can I write iterative insertion sort from memory? (i from 1, key, shift while loop, insert)
- [ ] Can I write recursive insertion sort from memory? (base case, recursive call, insert last)
- [ ] Do I know Big O for both? (\(O(n^2)\) worst, \(O(n)\) best)
- [ ] Can I convert between iterative and recursive?
- [ ] Do I know the difference between procedure (no return) and function (must return)?
