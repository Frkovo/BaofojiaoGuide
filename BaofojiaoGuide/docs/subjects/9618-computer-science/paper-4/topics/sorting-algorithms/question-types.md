---
title: "题型分析"
sidebar_position: 2
---

# 题型分析

---

## Q1: Bubble Sort Implementation (4–5 marks)

**How to recognise:** Question says "bubble sort", "bubble pass", "adjacent swap".

**Standard method:**
1. Outer loop `for i in range(n-1)` controls number of passes
2. Inner loop `for j in range(n-1-i)` compares adjacent elements
3. If `arr[j] > arr[j+1]`, swap them
4. Return the sorted array

**MS pattern:**
- **A1** Correct procedure header `Function bubbleSort(arr)` / `Procedure bubbleSort(arr)`
- **A1** Outer loop `n-1` times
- **A1** Inner loop `n-1-i` times
- **A1** Correct comparison `arr[j] > arr[j+1]`
- **A1** Swap and return

**Example:** 9618/s24/qp/42 Q3 — write a bubble sort procedure.

<details>
<summary>MS</summary>

**M1** Correct loop structure (outer + inner)  
**A1** Outer loop runs `n-1` times  
**A1** Inner loop runs `n-1-i` times  
**A1** Correct comparison `arr[j] > arr[j+1]`  
**A1** Correct swap with temp variable (or Python tuple swap) and returning array

</details>

**Common traps:**
- Using `range(n)` for outer loop — extra pass, not wrong but inefficient
- Inner loop bound `n-1` instead of `n-1-i` — still works but extra comparisons
- Swapping `arr[i]` instead of `arr[j]`

---

## Q2: Iterative Insertion Sort (4 marks)

**How to recognise:** "insertion sort", "insert into sorted portion", "shift elements".

**Standard method:**
1. Outer loop `for i in range(1, n)` — first element is already sorted
2. Store `key = arr[i]`
3. Inner loop shifts elements right: `while j >= 0 and arr[j] > key`
4. Place `key` at correct position

**MS pattern:**
- **A1** Loop from index 1 to `n-1`
- **A1** Store current element as `key`
- **A1** While loop to shift
- **A1** Place `key` back

**Example:** 9618/s24/qp/41 Q1d — complete the insertion sort function.

<details>
<summary>MS</summary>

**M1** Iterates from index 1 to last element  
**A1** Stores current element (`curr = arr[i]` or `key = arr[i]`)  
**A1** Shifting loop: `while j >= 0 AND arr[j] > curr`  
**A1** Inserts `curr` at `arr[j+1]` after shifting

</details>

**Common traps:**
- Starting outer loop at `i = 0` instead of `i = 1`
- Forgetting to decrement `j` inside while loop — infinite loop
- Writing `arr[j] = arr[j+1]` instead of `arr[j+1] = arr[j]`

---

## Q3: Recursive Insertion Sort (4 marks)

**How to recognise:** "recursive", "repeatedly call", "base case n &lt;= 1".

**Standard method:**
1. Base case: `if n <= 1: return`
2. Recursive call: `insertionSortRec(arr, n-1)`
3. Take last element as `key = arr[n-1]`
4. Shift sorted portion (indices 0 to n-2) and insert key

**MS pattern:**
- **A1** Base case `n <= 1`
- **A1** Recursive call on `n-1`
- **A1** Extract key and shift loop
- **A1** Insert key at correct position

**Example:** 9618/s24/qp/42 Q3 — also had a recursion variant in some sessions.

<details>
<summary>MS</summary>

**M1** Base case: IF `n <= 1` THEN `RETURN`  
**A1** Recursive call on `n-1`  
**A1** Key assignment + while loop shifting elements  
**A1** Insert key at `arr[j+1]` — no return needed (in-place)

</details>

**Common traps:**
- No base case — stack overflow
- Passing wrong array size to recursive call
- Using `return` in a procedure that should modify array in-place

---

## Q4: Converting Between Iterative and Recursive Insertion Sort (4–5 marks)

**How to recognise:** "rewrite the iterative version as a recursive version", or vice versa.

**Standard method (iterative to recursive):**
1. The outer `for` loop becomes the recursive parameter `n`
2. Base case replaces loop termination
3. Body of loop becomes post-recursive-call code

**Standard method (recursive to iterative):**
1. The recursive parameter `n` becomes the loop variable
2. Base case becomes loop start/end condition
3. Post-recursive code becomes loop body

**MS pattern:**
- **A1** Recognise loop → recursion transformation
- **A1** Correct base case
- **A1** Correct recursive call
- **A1** Correct insertion logic preserved

<details>
<summary>MS</summary>

**M1** Identifies the loop to replace  
**A1** Sets the base case correctly  
**A1** Wraps remaining logic in the recursive call / loop  
**A1** Preserves the shift-and-insert logic exactly

</details>
