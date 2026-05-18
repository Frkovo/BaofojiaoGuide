---
title: "题型分析"
---

# 题型分析

## Q1: Sort Strings by Character Comparison (6 marks)

**Identify**: 题目要求对字符串数组排序，比较依据是字符串中的特定字符（通常是第一个字符）。关键词如 "sort by the first character"。

**Method**: 使用冒泡排序，在比较时提取每个字符串的目标字符进行比较。

<details>
<summary>MS Pattern</summary>

**M1** 使用冒泡排序框架（外层循环 n-1 次，内层循环 n-i-1 次）
**M1** 提取当前元素的指定位置字符（`MID(Arr[j], 1, 1)`）
**A1** 比较两个字符的大小
**A1** 如果顺序错误则交换元素
**A1** 正确实现嵌套循环的边界条件

</details>

**Examples**: `23_qp_42 Q1c`、`24_qp_41 Q1`

---

## Q2: Count Vowels / Detect Characters (5 marks)

**Identify**: 要求统计字符串中元音、辅音、数字或特定字符的数量。关键词如 "count the number of vowels"。

**Method**: 遍历字符串的每个字符，判断是否属于目标集合。

<details>
<summary>MS Pattern</summary>

**M1** 循环遍历字符串的每一个字符（`FOR i ← 1 TO LENGTH(X)`）
**M1** 提取当前字符（`MID(X, i, 1)`）
**A1** 将字符转换为大写或小写统一比较
**A1** 判断字符是否属于目标集合（如 `"aeiou"`）
**A1** 累加计数并返回

</details>

**Examples**: `21_qp_41 Q1`（递归版）、`22_qp_42 Q2`

---

## Q3: Convert Case, Compare Strings (3-4 marks)

**Identify**: 要求将字符串中的字母转换大小写，或忽略大小写比较两个字符串。关键词如 "convert to uppercase" 或 "case-insensitive comparison"。

**Method**: 遍历字符串，对每个字符判断是否为字母，然后进行 ASCII 码偏移。

<details>
<summary>MS Pattern</summary>

**M1** 遍历字符串提取字符
**A1** 判断字符是否在 `'a'`-`'z'` 或 `'A'`-`'Z'` 范围内
**A1** 使用 ASCII 码加减 32 转换大小写
**A1** 构建新字符串并返回

</details>

**Examples**: `19_qp_42 Q1`、`20_qp_41 Q1`

---

## Q4: String Sorting with Custom Comparison (4-5 marks)

**Identify**: 不是按默认字典序排序，而是按自定义规则（如按字符串长度、按特定位置的字符、按某种优先级）。关键词如 "sort by length"。

**Method**: 在比较函数中实现自定义规则，然后使用标准排序算法。

<details>
<summary>MS Pattern</summary>

**M1** 定义比较函数或条件
**M1** 在比较中使用多个条件（如先比长度，长度相同比首字符）
**A1** 正确实现所有排序规则的优先级
**A1** 使用标准排序框架完成排序

</details>

**Examples**: `22_qp_41 Q2`（按长度排序）
