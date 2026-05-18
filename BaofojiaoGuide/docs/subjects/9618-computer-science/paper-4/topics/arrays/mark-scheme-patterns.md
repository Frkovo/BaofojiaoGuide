---
title: "评分标准模式"
sidebar_position: 4
---

# 评分标准模式

## Key Command Words

| Command Word | Meaning | Typical Mark |
|-------------|---------|-------------|
| Declare | Create the array variable with size | **M1** |
| Initialise | Set initial values (often 0) | **A1** |
| Read / Input | Accept values from user or file | **M1** |
| Store | Place value into array element | **A1** |
| Traverse / Loop | Use iterative statement to access each element | **M1** |
| Calculate | Perform arithmetic on array elements | **M2** |
| Output / Display | Print or return the result | **A1** |
| Search | Find a value in the array | **M1** |
| Find max/min | Identify largest/smallest element | **M2** |

## Common Mark Scheme Patterns

### Pattern 1: Declaration Only (1–2 marks)

- **M1** correct array name, correct size, correct data type (implied by initial value)
- **A1** all elements initialised correctly

### Pattern 2: Input and Store (4–6 marks)

- **M1** array declared with correct size
- **M2** loop construct (`for i in range(N)`)
- **A1** read/accept value inside loop
- **B1** store at correct index / correct data conversion

### Pattern 3: Processing (2–4 marks)

- **M1** correct loop to traverse array
- **M2** correct processing logic (sum, comparison, etc.)
- **A1** correct result stored and/or output

### Pattern 4: 2D Array (3–5 marks)

- **M1** correct 2D array declaration (nested list comprehension)
- **M2** nested loops with correct bounds
- **A1** correct row/column indexing
- **B1** correct processing

## Mark Allocation Logic

- **M marks** are for structure/method: loop, condition, function definition
- **A marks** are for accuracy: correct variable, correct operation, correct output
- **B marks** are for bonus/alternative: type conversion, file handling, edge cases

## Common MS Phrases

> "Allow equivalent mark if logic is correct but syntax has minor errors."

> "**M1** for loop – accept `for i in range(10)` or equivalent."

> "**A1** for correct use of array indexing – accept `Arr[i]`."

> "If array not declared, penalise **M1** but can still award **A1** for correct logic."
