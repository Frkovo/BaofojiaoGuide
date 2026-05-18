---
title: "考前速记"
sidebar_position: 7
---

# 考前速记

## Declaration Syntax

```
DECLARE arr : ARRAY[1:rows, 1:cols] OF INTEGER
```

- 第一维度 = 行 (row)，第二维度 = 列 (column)
- 下标从 1 开始 (Cambridge pseudocode convention)

## Row-Major Traversal

```
FOR r ← 1 TO rows
  FOR c ← 1 TO cols
    arr[r][c] ← ...
  NEXT c
NEXT r
```

## Column-Major Traversal

```
FOR c ← 1 TO cols
  FOR r ← 1 TO rows
    arr[r][c] ← ...
  NEXT r
NEXT c
```

## Insertion Sort by Column

```
keyRow ← arr[i]
j ← i - 1
WHILE j >= 1 AND arr[j][sortCol] > keyRow[sortCol]
  arr[j+1] ← arr[j]
  j ← j - 1
ENDWHILE
arr[j+1] ← keyRow
```

**Checklist:**
- `keyRow` 必须复制整行，不是单个值
- 比较用 `arr[j][sortCol]`，不是 `arr[j]`
- 移位移整行，不是单个元素

## Binary Tree in 2D Array (3 Columns)

| Index | Col 1 (LeftPtr) | Col 2 (Data) | Col 3 (RightPtr) |
|-------|-----------------|-------------|------------------|
| 1     | -1              | 10          | 2                |
| 2     | -1              | 5           | -1               |

- Root variable stores the index of root row
- `-1` means no child
- Insert: Data→`freeRow`, Left/Right→`-1`, traverse from root

## In-Order Traversal (Recursive)

```
IF index <> -1 THEN
  CALL InOrder(Tree, Tree[index][LeftCol])
  OUTPUT Tree[index][DataCol]
  CALL InOrder(Tree, Tree[index][RightCol])
ENDIF
```

## Binary Tree Insert Checklist

| Step | Done? |
|------|-------|
| Find next free row | `nextFree` pointer |
| Insert `newData` at free row | `arr[freeRow][DataCol]` |
| Set left & right pointers to `-1` | |
| If tree empty → root = free row | |
| Traverse: `current ← root` | |
| Compare new vs current data | `<` go left, `>=` go right |
| If child pointer `= -1` → set it to free row | |
| Else → move current to child | |

## Marks Breakdown Quick Reference

| Task | Max Marks | Critical Step |
|------|-----------|---------------|
| Declare + init 2D array | 3 | Correct bounds + nested loops |
| Read file into 2D array | 5 | File operations + nested loops |
| Sort by column (insertion) | 5 | Compare + shift entire rows |
| Binary tree traversal | 4 | Recursive calls in correct order |
| Binary tree insertion | 8 | Traverse + update correct pointer |
