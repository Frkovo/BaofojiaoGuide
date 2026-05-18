---
title: "题型分析"
sidebar_position: 2
---

# 题型分析

## Q1: Declare and Initialize 2D Array (3 marks)

**Identify**: Question asks to declare a 2D array and initialize all elements, e.g. a 6×4 board, all zeros.

**Method**:
1. Use `DECLARE` with correct bounds: `DECLARE arr : ARRAY[1:r, 1:c] OF <type>`
2. Nested `FOR` loops: outer loop rows, inner loop columns
3. Assign value inside inner loop: `arr[i][j] ← 0`

**Mark Scheme**:

<details>
<summary>Typical MS (3 marks)</summary>

**M1** Correct declaration with dimensions

**A1** Outer loop for rows

**A1** Inner loop for columns with assignment

</details>

**Example**:

```
DECLARE Board : ARRAY[1:6, 1:4] OF INTEGER
FOR Row ← 1 TO 6
  FOR Col ← 1 TO 4
    Board[Row][Col] ← 0
  NEXT Col
NEXT Row
```

---

## Q2: Insert Data Into 2D Array (5 marks)

**Identify**: Read data from a file or user input and store into a 2D array.

**Method**:
1. Open file / get input
2. Outer loop for each row
3. Inner loop for each column
4. Read value and assign to `arr[i][j]`

**Mark Scheme**:

<details>
<summary>Typical MS (5 marks)</summary>

**M1** Open file correctly / loop structure set up

**A1** Read data inside row loop

**A1** Store into correct row index

**A1** Correct column loop

**A1** Close file (if applicable)

</details>

---

## Q3: Sort 2D Array by One Column — Insertion Sort (5 marks)

**Identify**: Sort rows of a 2D array based on values in a specified column.

**Method**:
1. Outer loop from second row to last: `FOR i ← 2 TO r`
2. Store current row as `key`
3. Inner loop (`j ← i - 1`) compares `arr[j][sortCol]` with `key[sortCol]`
4. Shift rows: `arr[j+1] ← arr[j]`, decrement `j`
5. Place key: `arr[j+1] ← key`

**Mark Scheme**:

<details>
<summary>Typical MS (5 marks)</summary>

**M1** Outer loop from 2nd row

**A1** Store current row / key row

**A1** Compare target column values

**A1** Shift rows right

**A1** Insert key at correct position

</details>

**Example** — sort by column 2 ascending:

```
DECLARE keyRow : ARRAY[1:3] OF INTEGER
FOR i ← 2 TO 6
  keyRow ← arr[i]
  j ← i - 1
  WHILE j >= 1 AND arr[j][2] > keyRow[2]
    arr[j+1] ← arr[j]
    j ← j - 1
  ENDWHILE
  arr[j+1] ← keyRow
NEXT i
```

---

## Q4: Binary Tree in 2D Array (4+ marks)

**Identify**: Tree stored as rows where each row has columns `LeftPointer`, `Data`, `RightPointer`. Root pointer indicates the root row.

**Structure**:

| LeftPointer | Data | RightPointer |
|-------------|------|--------------|
| 0           | 10   | 2            |
| -1          | 5    | -1           |
| 3           | 20   | -1           |
| -1          | 15   | -1           |

A pointer of `-1` means no child.

**Mark Scheme**:

<details>
<summary>Typical MS (4 marks)</summary>

**M1** Understand structure: 3-column layout

**A1** Follow `LeftPointer` to traverse left

**A1** Follow `RightPointer` to traverse right

**A1** Stop when pointer = -1

</details>

---

## Q5: Insert Node Into 2D Array Binary Tree (8 marks)

**Identify**: Insert a new value into a binary tree stored as a 2D array. Must find next free row, then traverse from root to locate correct position.

**Method**:
1. Find next free row (e.g. `nextFree` pointer or scan for `-1` in `Data`)
2. Insert value into `Data` column at free row
3. Set `LeftPointer` and `RightPointer` to `-1`
4. If tree empty (`root = -1`), set root to free row
5. Else traverse: start at `current ← root`
6. While not inserted:
   - If `newData < arr[current][DataCol]`:
     - If `LeftPointer[current] = -1`, set it to free row → done
     - Else `current ← LeftPointer[current]`
   - Else:
     - If `RightPointer[current] = -1`, set it to free row → done
     - Else `current ← RightPointer[current]`

**Mark Scheme**:

<details>
<summary>Typical MS (8 marks)</summary>

**M1** Find next free position in array

**A1** Insert data into free row

**A1** Set left & right pointers to -1

**A1** Check for empty tree

**A1** Traverse from root based on comparison

**A1** Correct comparison: new < current → go left

**A1** Update correct pointer (LeftPointer / RightPointer)

**A1** Loop until insertion complete

</details>
