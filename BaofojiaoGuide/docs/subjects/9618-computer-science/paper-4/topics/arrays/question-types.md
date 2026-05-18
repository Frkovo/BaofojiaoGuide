---
title: "题型分析"
sidebar_position: 2
---

# 题型分析

## Question Type 1: Array Declaration and Initialization (1–2 marks)

**How to identify:** The question asks you to declare an array and fill it with initial values. Usually appears as the first part of a larger question.

**Standard Method:**
- Use list multiplication `[0] * N` for 1D
- Use nested list comprehension for 2D
- Match the data type required (integer, string, etc.)

**MS Pattern:**
- **M1** for correct declaration with correct size
- **A1** for correct initial values

**Example 1 — source:**
> A program needs to store the temperatures for 7 days. Write program code to declare and initialise an array `Temperatures` with 7 elements, each set to 0.

<details>
<summary>MS Expand</summary>

- **M1** declaration with size 7: `Temperatures = [0] * 7`
- **A1** all elements set to 0
</details>

**Example 2 — source:**
> Declare a 2D array `Grid` with 5 rows and 6 columns, initialised to 0.

<details>
<summary>MS Expand</summary>

- **M1** correct nested list comprehension syntax
- **A1** dimensions 5 rows × 6 columns, all 0
</details>

**Common traps:**
- Using `[0] * 5` for a 2D array (creates shallow copies)
- Wrong order of rows and columns
- Not using `global` when declaration is inside a function

---

## Question Type 2: Reading Data into an Array (4–6 marks)

**How to identify:** You are given a data source (user input, file, or generated values) and must store values into an array using a loop.

**Standard Method:**
1. Declare the array (if not already done)
2. Use a `for` loop with `range()`
3. Inside the loop, assign each element:
   - User input: `Array[i] = int(input(...))`
   - File: `Array[i] = int(File.readline())`
4. Handle validation if required

**MS Pattern:**
- **M1** correct loop structure with `range()`
- **M2** read/accept a value inside loop
- **A1** store value at correct index
- **B1** correct data type conversion

**Example 1 — source:**
> Write program code that asks the user to enter 10 scores and stores them in an array `Scores`.

<details>
<summary>MS Expand</summary>

```python
Scores = [0] * 10
for i in range(10):
    Scores[i] = int(input("Enter score: "))
```

- **M1** array declaration `Scores = [0] * 10`
- **M2** loop `for i in range(10)`
- **A1** assign input to `Scores[i]`
- **B1** use of `int()` for type conversion
</details>

**Example 2 — source:**
> Read 20 integers from a text file `data.txt` into an array `Numbers`. Each integer is on a separate line.

<details>
<summary>MS Expand</summary>

```python
Numbers = [0] * 20
File = open("data.txt", "r")
for i in range(20):
    Numbers[i] = int(File.readline())
File.close()
```

- **M1** open file and declare array
- **M2** loop `for i in range(20)`
- **A1** `File.readline()` and `int()` conversion
- **B1** close file
</details>

**Common traps:**
- Forgetting `int()` conversion for numeric data
- Off-by-one: using `range(1, 11)` with 0-based array
- Not pre-allocating array before assigning by index
- Forgetting `global` if inside a function

---

## Question Type 3: Array Traversal and Processing (2–4 marks)

**How to identify:** You must iterate over an existing array to perform a calculation (sum, average, count, find max/min, search).

**Standard Method:**
1. Declare accumulator variables (sum, count, max, etc.)
2. Loop through all elements using `for i in range(len(Array))`
3. Apply processing logic inside the loop
4. Output or return the result

**MS Pattern:**
- **M1** correct loop structure
- **M2** correct accumulation / comparison logic
- **A1** correct final result

**Example 1 — source:**
> The array `Marks` contains 30 integer values. Write program code to calculate and output the total of all values in `Marks`.

<details>
<summary>MS Expand</summary>

```python
Total = 0
for i in range(len(Marks)):
    Total = Total + Marks[i]
print(Total)
```

- **M1** loop `for i in range(len(Marks))`
- **M2** accumulation `Total = Total + Marks[i]`
- **A1** output `Total`
</details>

**Example 2 — source:**
> The array `Temperatures` contains 365 values. Write program code to find and output the highest value in the array.

<details>
<summary>MS Expand</summary>

```python
Max = Temperatures[0]
for i in range(1, len(Temperatures)):
    if Temperatures[i] > Max:
        Max = Temperatures[i]
print(Max)
```

- **M1** initialise `Max` to first element
- **M2** loop through remaining elements with comparison
- **A1** update `Max` when larger value found and output
</details>

**Common traps:**
- Initialising max to 0 instead of first element (fails if all values negative)
- Off-by-one in loop range
- Using `Total =+ Marks[i]` instead of `Total += Marks[i]`
- Not using `len()` when array size varies
