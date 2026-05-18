---
title: "解题方法"
sidebar_position: 3
---

# 解题方法

## 1. Declaration

Pseudocode syntax:

```
DECLARE <identifier> : ARRAY[<rowLower>:<rowUpper>, <colLower>:<colUpper>] OF <type>
```

**Examples:**

```
DECLARE Grid : ARRAY[1:8, 1:8] OF CHAR
DECLARE Scores : ARRAY[0:9, 0:2] OF REAL
DECLARE Tree : ARRAY[1:20, 1:3] OF INTEGER
```

## 2. Row Access vs Column Access

| Operation | Outer Loop | Inner Loop | Code Pattern |
|-----------|-----------|-----------|--------------|
| Row-major (row-by-row) | Row index | Column index | `FOR i ← 1 TO r ... FOR j ← 1 TO c ... arr[i][j]` |
| Column-major (col-by-col) | Column index | Row index | `FOR j ← 1 TO c ... FOR i ← 1 TO r ... arr[i][j]` |
| Single row | - | Column index | `FOR j ← 1 TO c ... arr[row][j]` |
| Single column | Row index | - | `FOR i ← 1 TO r ... arr[i][col]` |

## 3. Insertion Sort by One Column

适用: Sort entire rows based on values in a specific column.

**Template:**

```
DECLARE keyRow : ARRAY[1:numCols] OF <type>
FOR i ← 2 TO numRows
  keyRow ← arr[i]
  j ← i - 1
  WHILE j >= 1 AND arr[j][sortCol] > keyRow[sortCol]
    arr[j+1] ← arr[j]
    j ← j - 1
  ENDWHILE
  arr[j+1] ← keyRow
NEXT i
```

Key points:
- `keyRow` must match the number of columns
- Compare only `arr[j][sortCol]` against `keyRow[sortCol]`
- Shift entire rows, not just the sort column

## 4. Binary Tree Traversal (In-order)

Left → Root → Right:

```
PROCEDURE InOrder(ByRef Tree : ARRAY[1:, 1:3] OF INTEGER, ByVal index : INTEGER)
  IF index <> -1 THEN
    CALL InOrder(Tree, Tree[index][1])   ' LeftPointer
    OUTPUT Tree[index][2]                 ' Data
    CALL InOrder(Tree, Tree[index][3])   ' RightPointer
  ENDIF
ENDPROCEDURE
```

## 5. Binary Tree Insertion

```
PROCEDURE InsertNode(ByRef Tree : ARRAY[1:, 1:3] OF INTEGER,
                     ByRef nextFree : INTEGER,
                     ByRef root : INTEGER,
                     ByVal newData : INTEGER)
  Tree[nextFree][DataCol] ← newData
  Tree[nextFree][LeftCol] ← -1
  Tree[nextFree][RightCol] ← -1
  nextFree ← nextFree + 1

  IF root = -1 THEN
    root ← nextFree - 1
  ELSE
    current ← root
    inserted ← FALSE
    WHILE inserted = FALSE
      IF newData < Tree[current][DataCol] THEN
        IF Tree[current][LeftCol] = -1 THEN
          Tree[current][LeftCol] ← nextFree - 1
          inserted ← TRUE
        ELSE
          current ← Tree[current][LeftCol]
        ENDIF
      ELSE
        IF Tree[current][RightCol] = -1 THEN
          Tree[current][RightCol] ← nextFree - 1
          inserted ← TRUE
        ELSE
          current ← Tree[current][RightCol]
        ENDIF
      ENDIF
    ENDWHILE
  ENDIF
ENDPROCEDURE
```

## 6. Reading From File Into 2D Array

```
DECLARE Data : ARRAY[1:100, 1:5] OF INTEGER
OPENFILE "data.txt" FOR READ
FOR i ← 1 TO 100
  FOR j ← 1 TO 5
    READFILE "data.txt", Data[i][j]
  NEXT j
NEXT i
CLOSEFILE "data.txt"
```
