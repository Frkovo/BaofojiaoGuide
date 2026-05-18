---
title: "考纲要点"
sidebar_position: 6
---

# 考纲要点

Based on Cambridge 9618 syllabus — Section 10.2: Arrays

## Syllabus Objectives

| # | Objective | Exam Frequency |
|---|-----------|----------------|
| 1 | Declare and initialise 1D arrays — fixed-size, any data type | High |
| 2 | Declare and initialise 2D arrays — fixed-size, any data type | Medium |
| 3 | Read data into an array from user input and from file | High |
| 4 | Traverse a 1D array using a loop | Very High |
| 5 | Traverse a 2D array using nested loops | Medium |
| 6 | Perform calculations on array elements (sum, average, max, min, count) | High |
| 7 | Search for a value in an array (linear search) | Medium |
| 8 | Use arrays with functions and procedures (passing arrays as parameters) | Medium |
| 9 | Understand 0-based indexing in Python arrays | High |
| 10 | Understand that arrays are mutable — elements can be updated | Medium |

## Key Syllabus Requirements

### 10.2.1 — 1D Arrays

> Candidates should be able to:
>
> - Declare a 1D array using list syntax: `ArrayName = [0] * N`
> - Initialise all elements to a given value
> - Access individual elements using index notation: `ArrayName[i]`
> - Traverse using `for i in range(len(ArrayName))`

### 10.2.2 — 2D Arrays

> Candidates should be able to:
>
> - Declare a 2D array: `ArrayName = [[0] * C for i in range(R)]`
> - Access elements: `ArrayName[row][col]`
> - Traverse using nested `for` loops
> - Distinguish between row-major and column-major traversal

### 10.2.3 — Arrays in Functions

> Candidates should be able to:
>
> - Pass arrays as parameters to functions
> - Understand that arrays are passed by reference in Python
> - Use `global` keyword when necessary

## What the Syllabus Does NOT Require

- Sorting algorithms (covered in Algorithm topic)
- Dynamic arrays beyond simple `append()`
- Advanced list methods (`insert`, `pop`, `remove` with index) — but they may appear in mark schemes
- Multi-dimensional arrays beyond 2D
- Array slicing (`Arr[1:3]`) — generally not examined
