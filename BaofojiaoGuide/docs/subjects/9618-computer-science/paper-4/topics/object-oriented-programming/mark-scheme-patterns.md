---
title: 评分标准模式
sidebar_position: 4
---

# 评分标准模式

## General Mark Scheme Structure

| 分值 | 含义 | 条件 |
|------|------|------|
| **M1**, **M2**... | Mark — 方法 / 结构分 | 需要正确使用特定方法 |
| **A1**, **A2**... | Application — 应用分 | 在 M mark 基础上正确实现 |
| **B1**, **B2**... | Bonus — 额外分 | 独立于流程的正确做法 |

## 各题型 MS 模式对照

### Q1: Class + Constructor (4-5 marks)

<details>
<summary>Typical MS Breakdown</summary>

- **M1**: `class` keyword followed by class name and colon
- **A1**: `__init__` method defined with `self` as first parameter
- **A1**: `self.__attr = param` for each private attribute (x3)
- **B1**: Default attributes correctly initialised (if required)

**Total: M1 + 3 x A1 = 4 marks**
</details>

### Q2: Getter Methods (3 marks)

<details>
<summary>Typical MS Breakdown</summary>

- **M1**: `def GetX(self):` correct signature
- **A1**: `return` statement
- **A1**: references `self.__x`

**Total: M1 + A1 + A1 = 3 marks**
</details>

### Q3: Setter Methods (3 marks)

<details>
<summary>Typical MS Breakdown</summary>

- **M1**: `def SetX(self, val):` correct signature
- **A1**: `self.__x = val` assignment
- **B1**: Validation / range check (e.g. `if val >= 0`)

**Total: M1 + A1 + B1 = 3 marks**
</details>

### Q4: Object + Method Call (2-4 marks)

<details>
<summary>Typical MS Breakdown</summary>

- **M1**: `obj = ClassName(args)` instantiation
- **A1**: `obj.Method()` dot notation call
- **A1**: Correct number and order of arguments passed

**Total: M1 + A1 + A1 = 3 marks**
</details>

### Q5: Array of Objects + File (7 marks)

<details>
<summary>Typical MS Breakdown</summary>

- **M1**: Open file `open("file.txt", "r")`
- **M1**: Loop through file `for line in file:`
- **M1**: Parse line `split(",")` or `strip()`
- **A1**: Create new object from parsed data
- **A1**: Append to list `arr.append(obj)`
- **A1**: Return list or process further
- **B1**: `file.close()`

**Total: 3 x M1 + 3 x A1 + B1 = 7 marks**
</details>

### Q6: Business Logic (6 marks)

<details>
<summary>Typical MS Breakdown</summary>

- **M1**: Loop through all objects in array
- **A1**: Use getter methods to access data
- **A1**: Correct logic (accumulation / comparison / condition)
- **M1**: Correct output format (e.g. `print` with formatting)
- **A1**: Handle edge cases (empty list, boundary values)
- **B1**: Return value where appropriate

**Total: 2 x M1 + 3 x A1 + B1 = 6 marks**
</details>

## Common MS Keywords

| MS Keyword | 含义 | 例子 |
|------------|------|------|
| "Correct use of `self`" | `self` 作为第一个参数且在 body 中使用 | `self.__x` |
| "Correct dot notation" | 对象名 + `.` + 方法名 | `emp.GetName()` |
| "Correct parameter passing" | 参数数量 + 类型匹配 | `Employee("E01", "Ali")` |
| "File handling" | 打开、读取、关闭 | `open`, `readlines`, `close` |
| "String manipulation" | `strip()`, `split()`, casting | `int(parts[0])` |

## 扣分常见原因

| 错误 | 扣分影响 |
|------|----------|
| 缺少 `self` 参数 | **M mark 丢失** |
| 缺少 `return` | **A mark 丢失** |
| private 没加 `__` | 扣 1 mark per attribute |
| 没有 `file.close()` | 扣 B1 mark |
| 没用 getter/setter（直接用 `obj.__attr`） | **通常不扣分**但推荐用 getter |
| 循环逻辑错误（off-by-one） | 扣 A1 mark |
