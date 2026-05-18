---
title: "题型分析"
sidebar_position: 2
---

# 题型分析

## Q1: Linear Search (4-6 marks)

### 识别方式

- 问题中提及 "unsorted array" 或 "linear search"
- 要求遍历数组找到某个元素
- 分值较低 (4-6 marks)

### 标准写法

```python
def find_item(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True    # or return i
    return False           # or return -1
```

### MS 评分模式

<details>
<summary>Linear Search MS 模板</summary>

**M1** — Correct loop structure (e.g., `for i in range(len(arr))`)

**A1** — Correct comparison (`if arr[i] == target`)

**M1** — Return True / index on match

**A1** — Return False / -1 after loop

</details>

### 真题示例

| 试卷 | 题号 | 分值 | 考点 |
|------|------|------|------|
| 9618/s21/qp/41 | Q2b | 5 | Linear search in a list of strings |
| 9618/s23/qp/42 | Q1c | 4 | Linear search returning index |
| 9618/s22/qp/41 | Q3a | 6 | Linear search with counting |

### Traps

- 循环结束后忘记 `return False`
- 在循环内提前 `return False` (只应在遍历全部元素后返回)
- 混淆下标和元素值

---

## Q2: Iterative Binary Search (5-6 marks)

### 识别方式

- 问题提及 "sorted array" 或 "binary search"
- 要求使用 `while` 循环实现
- 明确要求 iterative 而非 recursive

### 标准写法

```python
def binary_search(arr, target):
    first = 0
    last = len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return False
```

### MS 评分模式

<details>
<summary>Iterative Binary Search MS 模板</summary>

**M1** — Initialise `first` and `last`

**M1** — Correct `while` condition (`first &lt;= last`)

**M1** — Calculate `mid = (first + last) // 2`

**A1** — Correct comparison and branch

**A1** — Update `first = mid + 1` or `last = mid - 1`

**A1** — Return False after loop

</details>

### 真题示例

| 试卷 | 题号 | 分值 | 考点 |
|------|------|------|------|
| 9618/s21/qp/41 | Q2c | 6 | Iterative binary search on sorted array |
| 9618/s24/qp/41 | Q1e | 5 | Binary search with string comparison |
| 9618/s22/qp/42 | Q2d | 6 | Iterative binary search returning index |

### Traps

- 条件写成 `while first < last` (漏掉 `=` 导致边界元素丢失)
- `mid` 使用 `/` 而非 `//` (浮点数不能作为下标)
- 更新时写成 `first = mid` 或 `last = mid` (造成死循环)

---

## Q3: Recursive Binary Search (5-6 marks)

### 识别方式

- 问题明确要求 "recursive" 或 "using recursion"
- 函数签名包含 `first` 和 `last` 参数

### 标准写法

```python
def binary_search(arr, target, first, last):
    if first > last:
        return False
    mid = (first + last) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, last)
    else:
        return binary_search(arr, target, first, mid - 1)
```

### MS 评分模式

<details>
<summary>Recursive Binary Search MS 模板</summary>

**M1** — Base case: `if first > last: return False`

**M1** — Calculate `mid = (first + last) // 2`

**M1** — Compare `arr[mid]` with `target`

**A1** — Correct recursive call with updated parameters

**A1** — `return` before recursive call

</details>

### 真题示例

| 试卷 | 题号 | 分值 | 考点 |
|------|------|------|------|
| 9618/s24/qp/42 | Q3d | 6 | Recursive binary search on integer array |
| 9618/s23/qp/41 | Q2c | 5 | Recursive binary search wrapper function |
| 9618/s21/qp/42 | Q3b | 6 | Recursive search with custom object comparison |

### Traps

- **忘记 `return` 递归结果** — 这是最常见的错误! Python 中递归调用必须加 `return`
- Base case 条件写反 (`first < last`)
- 递归参数传错顺序或忘记传递 `first`/`last`
- 没有处理空数组的情况 (`first > last`)
