---
title: "常见错误"
sidebar_position: 5
---

# 常见错误

## Mistake 1: Confusing Row and Column Bounds

```
' Wrong — dimensions reversed
DECLARE arr : ARRAY[1:5, 1:10] OF INTEGER  ' Intended: 10 rows, 5 cols
```

**Fix**: First dimension = rows, second = columns. Always match the problem description.

## Mistake 2: Off-by-One in Nested Loops

```
' Wrong — loop starts at 0 but array is 1-indexed
FOR i ← 0 TO 9
```

**Fix**: Use `1 TO n`, where `n` is the upper bound declared in the array.

## Mistake 3: Sorting Only the Column Instead of Full Rows

```
' Wrong — only swaps values in one column
IF arr[j][col] > arr[j+1][col] THEN
  temp ← arr[j][col]
  arr[j][col] ← arr[j+1][col]
  arr[j+1][col] ← temp
```

**Fix**: Store and swap entire rows (or store row as key and shift), not just one column's value.

## Mistake 4: Binary Tree — Forgetting to Set Child Pointers to -1

```
' Wrong — new node's LeftPointer and RightPointer left uninitialised
Tree[nextFree][DataCol] ← newData
' No pointer initialisation!
```

**Fix**: Always set both pointers to -1 for any new node.

## Mistake 5: Binary Tree — Comparing Wrong Column

```
' Wrong — comparing against LeftPointer column instead of Data
IF newData < Tree[current][LeftCol] THEN
```

**Fix**: Compare `newData` against `Tree[current][DataCol]`, not against a pointer.

## Mistake 6: Binary Tree — Updating Wrong Parent's Pointer

```
' Wrong — modifies current node's pointer instead of parent's
current ← Tree[current][LeftCol]
IF Tree[current][LeftCol] = -1 THEN
  Tree[current][LeftCol] ← freeRow  ' This is the child, not parent!
```

**Fix**: Before moving `current`, check if the next node to visit would be `-1`. If so, update the current node's pointer before moving.

## Mistake 7: Using 1D Array Instead of 2D

```
DECLARE arr : ARRAY[1:50] OF INTEGER  ' Wrong for question needing 2D
```

**Fix**: If the question says "store rows and columns", you must use `ARRAY[1:r, 1:c]`.

## Mistake 8: Incorrect Binary Tree Traversal Order

```
' Wrong order for in-order traversal
OUTPUT Tree[index][DataCol]
CALL InOrder(Tree, Tree[index][LeftCol])
CALL InOrder(Tree, Tree[index][RightCol])
```

**Fix**:
- In-order: Left → Data → Right
- Pre-order: Data → Left → Right
- Post-order: Left → Right → Data

## Mistake 9: Array Declaration Inside Loop

```
FOR i ← 1 TO 10
  DECLARE arr : ARRAY[1:5, 1:3] OF INTEGER  ' Wrong — redeclares each iteration
```

**Fix**: Declare once before any loop.

## Mistake 10: Pointer vs Index Confusion in Binary Tree

Root pointer indicates which row is the tree root, not the index of a column. The array indices are the "nodes". A pointer value of `-1` means "no node", not row 0.

```
' Correct: root variable stores a row index
IF root = -1 THEN
  root ← freeRow
```
