---
title: "考纲要点"
sidebar_position: 6
---

# 考纲要点

---

## 19.1.3 Bubble sort

| Point | Detail |
|-------|--------|
| Understand bubble sort algorithm | Repeatedly step through array, compare adjacent elements, swap if out of order; largest element "bubbles" to end each pass |
| Implement bubble sort | Write a function/procedure that sorts an array using nested loops and adjacent swaps |
| Trace bubble sort | Manually execute the algorithm on a small array, showing array state after each pass |
| Compare performance | Bubble sort makes \(n-1\) passes, each pass does \(n-1-i\) comparisons; total comparisons \(n(n-1)/2\) |
| Big O notation | \(O(n^2)\) worst and average case; \(O(n)\) best case (already sorted, with early exit) |

## 19.1.4 Insertion sort

| Point | Detail |
|-------|--------|
| Understand insertion sort algorithm | Build sorted portion one element at a time; take next element, shift larger elements right, insert at correct position |
| Implement insertion sort (iterative) | Outer `for` loop starts at index 1; inner `while` loop shifts sorted portion; insert key at `j+1` |
| Implement insertion sort (recursive) | Base case `n <= 1`; recursive call on `n-1`; insert `arr[n-1]` into sorted portion |
| Trace insertion sort | Show the sorted left portion growing after each iteration |
| Compare performance | Insertion sort also \(O(n^2)\) worst case, but performs well on nearly-sorted data (\(O(n)\) best case) |
| Big O notation | \(O(n^2)\) worst/average; \(O(n)\) best (already sorted, no shifting needed) |

## Comparison of Bubble Sort vs Insertion Sort

| Aspect | Bubble Sort | Insertion Sort |
|--------|-------------|----------------|
| Algorithm type | Comparison-based swapping | Comparison-based insertion |
| Passes | \(n-1\) passes | \(n-1\) iterations |
| Comparisons | \(n(n-1)/2\) (worst) | \(n(n-1)/2\) (worst) |
| Swaps/shifts | \(n(n-1)/2\) swaps | \(n(n-1)/2\) shifts |
| Best case | \(O(n)\) with early exit flag | \(O(n)\) (already sorted) |
| Worst case | \(O(n^2)\) | \(O(n^2)\) |
| Stable? | Yes | Yes |
| In-place? | Yes | Yes |
| Typical exam focus | Write the procedure | Write iterative + recursive; convert between them |
