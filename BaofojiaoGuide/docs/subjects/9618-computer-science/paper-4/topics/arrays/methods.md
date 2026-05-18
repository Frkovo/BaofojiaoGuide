---
title: "解题方法"
sidebar_position: 3
---

# 解题方法

## Method 1: Declaring Global Arrays in Python

When an array is declared inside a function (e.g. `main()`) and needs to be accessible from other functions, `global` is required.

:::note[Standard Method]

```python
def main():
    global MyArray
    MyArray = [0] * 10
    ...
```

**Key rule:** Declare `global` *before* assigning the array. Without `global`, Python creates a local variable.

:::

:::note[Alternative — Return value]

Instead of `global`, declare in `main()` and pass as a parameter:

```python
def main():
    MyArray = [0] * 10
    process(MyArray)

def process(Arr):
    # Arr receives reference to MyArray
    ...
```

:::

**When to use each:**
- Use `global` when the array must be accessed by many functions without parameter passing
- Use parameter passing when you want to control data flow and avoid side effects

---

## Method 2: Reading Data from User into Array

Standard pattern for filling an array with user input:

:::note[Standard Method]

```python
def main():
    global Scores
    Scores = [0] * 10
    for i in range(10):
        Scores[i] = int(input("Enter score: "))
```

:::

**Variations:**

| Scenario | Pattern |
|----------|---------|
| String data | `Array[i] = input(...)` (no `int()`) |
| Unknown size | Use `while` loop with sentinel, `append()` |
| File input | `Array[i] = int(File.readline())` |
| With validation | Loop until valid, then store |

**Example — Reading until sentinel ($-1$):**

```python
def main():
    global Values
    Values = []
    Value = int(input("Enter value (-1 to stop): "))
    while Value != -1:
        Values.append(Value)
        Value = int(input("Enter value (-1 to stop): "))
```

**Warning:** When using `append()`, do NOT pre-allocate with `[0] * N`.

---

## Method 3: Processing Array Elements with Loops

:::note[Standard Method — Sum and Average]

```python
Total = 0
for i in range(len(Array)):
    Total = Total + Array[i]
Average = Total / len(Array)
```

:::

:::note[Standard Method — Find Maximum]

```python
Max = Array[0]
for i in range(1, len(Array)):
    if Array[i] > Max:
        Max = Array[i]
```

:::

:::note[Standard Method — Linear Search]

```python
Found = False
Index = 0
while Index < len(Array) and not Found:
    if Array[Index] == SearchValue:
        Found = True
    else:
        Index = Index + 1
if Found:
    print("Found at position", Index)
else:
    print("Not found")
```

:::

:::note[Standard Method — 2D Array Traversal (row-major)]

```python
for r in range(ROWS):
    for c in range(COLS):
        # process Array[r][c]
```

:::
