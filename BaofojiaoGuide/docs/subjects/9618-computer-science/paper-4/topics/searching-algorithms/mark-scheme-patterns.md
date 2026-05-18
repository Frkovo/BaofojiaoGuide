---
title: "评分标准模式"
sidebar_position: 4
---

# 评分标准模式

## 通用 MS 关键词对照

| English | 中文 |
|---------|------|
| "initialise first/last" | 初始化首尾指针 |
| "calculating mid value" | 计算中间值 |
| "updating first/last" | 更新首尾指针 |
| "returning -1" | 返回 -1 |
| "base case" | 基本情况 |
| "recursive call" | 递归调用 |

---

## Linear Search MS 模式

<details>
<summary>典型 5-mark 评分模板</summary>

**M1** — 正确初始化循环 (`for i in range(len(arr))`)
**A1** — 正确比较元素 (`if arr[i] == target`)
**M1** — 匹配时返回对应值 (`return True` / `return i`)
**A1** — 循环结束后返回未找到标志
**A1** — 语法正确，函数定义完整

</details>

### 关键词
- `for` loop / iteration
- comparison / equality check
- return within loop
- return after loop

---

## Iterative Binary Search MS 模式

<details>
<summary>典型 6-mark 评分模板</summary>

**M1** — 初始化 `first`, `last`
**M1** — `while first &lt;= last` 正确条件
**M1** — 正确计算 `mid = (first + last) // 2`
**A1** — 正确比较 `arr[mid]` 与 target
**A1** — 正确更新 `first = mid + 1` 或 `last = mid - 1`
**A1** — 循环后返回 -1 / False

</details>

### 关键词
- initialise `first`, `last`
- `while first &lt;= last`
- `mid = (first + last) // 2`
- `first = mid + 1` / `last = mid - 1`
- return `-1` after loop

---

## Recursive Binary Search MS 模式

<details>
<summary>典型 6-mark 评分模板</summary>

**M1** — 正确 base case (`if first > last`)
**A1** — Base case 返回正确值
**M1** — 计算 `mid`
**A1** — 正确比较分支
**A1** — 正确递归调用 (更新 first/last)
**A1** — `return` 递归结果

</details>

### 关键词
- base case / stopping condition
- `mid` calculation
- recursive call with `mid + 1` / `mid - 1`
- `return` recursive call result

---

## 常见扣分点 (Deducted marks)

| 错误 | 扣分 |
|------|------|
| 无 base case | -2 marks |
| 条件用 `while first < last` (缺 `=`) | -1 mark |
| `mid + 1` 写成 `mid` | -1 mark |
| 递归未 `return` | -1 mark |
| 用 `/` 而非 `//` | -1 mark |
