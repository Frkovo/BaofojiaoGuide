---
title: "评分标准模式"
sidebar_position: 4
---

# 评分标准模式

---

## Common MS Points for Sorting Algorithms

### Bubble Sort (4–5 marks)

| Point | Typical wording | Marks |
|-------|-----------------|-------|
| Procedure/function header | `FUNCTION bubbleSort(arr) RETURNS ARRAY` | **A1** |
| Outer loop | `FOR i ← 0 TO n-2` or `FOR i ← 1 TO n-1` | **A1** |
| Inner loop | `FOR j ← 0 TO n-2-i` | **A1** |
| Adjacent comparison | `IF arr[j] > arr[j+1]` — must be `>` for ascending | **A1** |
| Swap + return | Swap using temp variable; `RETURN arr` at end | **A1** |

### Insertion Sort — Iterative (4 marks)

| Point | Typical wording | Marks |
|-------|-----------------|-------|
| Loop from 1st element | `FOR i ← 1 TO n-1` (do not start at 0) | **A1** |
| Store current item | `curr ← arr[i]` or `key ← arr[i]` | **A1** |
| While loop (shift) | `WHILE j ≥ 0 AND arr[j] > curr` — both conditions needed | **A1** |
| Insert | `arr[j+1] ← curr` after shifting | **A1** |

### Insertion Sort — Recursive (4 marks)

| Point | Typical wording | Marks |
|-------|-----------------|-------|
| Base case | `IF n ≤ 1 THEN RETURN` | **A1** |
| Recursive call | `CALL insertionSortRec(arr, n-1)` | **A1** |
| Shift loop | `WHILE j ≥ 0 AND arr[j] > key` | **A1** |
| Insert key | `arr[j+1] ← key` | **A1** |

### Generic MS Notes

- **M marks** (method) are awarded for correct structure / approach even if there are minor errors
- **A marks** (accuracy) require correct implementation — syntax errors lose **A** marks
- If a question says "write a procedure", do not use `RETURN` — use parameters by reference
- If a question says "write a function", a `RETURN` is required

<details>
<summary>Example MS — 9618/s24/qp/42 Q3 (Bubble Sort)</summary>

**M1** Correct outer loop and inner loop structure (nested)  
**A1** Outer loop correct number of passes (`n-1`)  
**A1** Inner loop correct bound (`n-1-i`)  
**A1** Correct adjacent comparison (`arr[j] > arr[j+1]`)  
**A1** Correct swap and return

</details>

<details>
<summary>Example MS — 9618/s24/qp/41 Q1d (Insertion Sort)</summary>

**M1** Iterates from index 1 to last element  
**A1** Stores current element  
**A1** Shifting loop with correct conditions  
**A1** Inserts element at correct position

</details>
