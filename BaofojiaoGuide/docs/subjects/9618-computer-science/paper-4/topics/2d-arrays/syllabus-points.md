---
title: "考纲要点"
sidebar_position: 6
---

# 考纲要点

## Cambridge 9618 Syllabus (Paper 4)

### 2D Array Fundamentals

- Declare a 2D array with correct syntax: `ARRAY[rowLower:rowUpper, colLower:colUpper]`
- Initialise elements using nested iteration
- Access individual element: `arr[row][col]`
- Traverse in row-major (rows outer, columns inner) or column-major order
- Pass 2D arrays as parameters (by reference `ByRef`)

### Sorting

- Sort the rows of a 2D array based on values in a specified column
- Implement insertion sort across rows
- Understand that each row functions like a record; entire rows must be moved, not just column values

### Binary Tree Using 2D Array

- Represent a binary tree where each row stores `[LeftPointer, Data, RightPointer]`
- A `root` variable stores the index of the root row
- Pointer value `-1` means no child (null)
- Traverse in-order (Left → Data → Right), pre-order, post-order
- Insert a new node by finding next free row and traversing from root

### File I/O With 2D Arrays

- Read a file into a 2D array using nested loops
- Process data stored in a 2D array (search, count, aggregate)

### Common Commands/Procedures (may be asked to write)

| Task | Key Structures |
|------|---------------|
| Create 2D array | `DECLARE` + nested `FOR` |
| Display 2D array | Nested `FOR` + `OUTPUT` |
| Search 2D array | Nested `FOR` + `IF` comparison |
| Sort by column | Insertion sort pattern |
| Tree traversal | Recursive procedure |
| Tree insertion | Loop + pointer update |

### Typical Exam Vocabulary

- "row" — first index
- "column" — second index
- "populate" — fill with data
- "traverse" — visit each node/element
- "pointer" — index of child node in tree structure
- "free row" — next unused row in tree array
