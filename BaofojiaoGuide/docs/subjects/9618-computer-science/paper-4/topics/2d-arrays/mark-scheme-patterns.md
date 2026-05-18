---
title: "评分标准模式"
sidebar_position: 4
---

# 评分标准模式

## General Mark Allocation Rules

| Mark | Type | Meaning |
|------|------|---------|
| **M1** | Method mark | 设对结构/算法即得，即使有小错 |
| **A1** | Accuracy mark | 依赖前面的 **M1**，实现完全正确 |
| **B1** | Independent mark | 独立给分，不依赖其他步骤 |
| **E1** | Explanation mark | 解释正确，通常出现在论述题 |

## Pattern 1: Declare + Initialize (3 marks)

<details>
<summary>分配逻辑</summary>

**M1** — Correct `DECLARE` with 2D array syntax and correct bounds

**A1** — Outer `FOR` loop for rows with correct range

**A1** — Inner `FOR` loop for columns with assignment `arr[i][j] ← value`

</details>

Common MS note: "If bounds are reversed (row/column swapped), penalise once only."

## Pattern 2: Read Data From File Into 2D Array (5 marks)

<details>
<summary>分配逻辑</summary>

**M1** — Open file / file reading structure

**A1** — Nested loop for rows

**A1** — Nested loop for columns

**A1** — Correct file read and store into `arr[i][j]`

**A1** — Close file after reading

</details>

## Pattern 3: Insertion Sort by Column (5 marks)

<details>
<summary>分配逻辑</summary>

**M1** — Outer loop `i` starting at 2

**A1** — Store entire current row as key

**A1** — Compare `arr[j][col]` with `key[col]`

**A1** — Shift rows: `arr[j+1] ← arr[j]`

**A1** — Insert key row at correct position

</details>

Common MS note: "Comparing the wrong column loses **A1**."
"Partial sort (only sorting one column values instead of full rows) loses **A1**."

## Pattern 4: Binary Tree Insert Into 2D Array (8 marks)

<details>
<summary>分配逻辑</summary>

**M1** — Find / track next free row

**A1** — Insert data into free row

**A1** — Set `LeftPointer` ← -1, `RightPointer` ← -1

**M1** — Check if tree empty (`root = -1`)

**A1** — Correct root assignment for empty case

**A1** — Traverse left/right based on comparison

**A1** — Update parent's pointer when inserting

**A1** — Loop / recursion terminates correctly

</details>

## Pattern 5: Binary Tree Traversal (4 marks)

<details>
<summary>分配逻辑</summary>

**M1** — Recursive procedure with index parameter

**A1** — Base case check (`index = -1`)

**A1** — Recursive call left, output, recursive call right (in correct order for in-order)

**A1** — Correct array column access for left/data/right

</details>

## Key MS Observations From Past Papers

- A simple syntax error (e.g. `NEXT` missing variable) usually does **not** lose the mark — intent matters
- Reversed loop bounds (e.g. `1 TO 0`) loses the mark
- Array indices out of bounds at runtime loses the accuracy mark
- Using a 1D array instead of 2D loses all method marks
- For binary tree questions: forgetting to set `-1` for new node's pointers typically loses **A1**
- For sort questions: using bubble sort instead of insertion sort is **not** penalised unless the question specifies insertion sort
