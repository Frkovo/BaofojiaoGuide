---
title: "常见错误"
---

# 常见错误

## 1. 索引混淆

**错误**: 将伪代码的 1-indexed 直接映射到 Python 的 0-indexed 时忘记减 1。

```python
# 伪代码: MID(X, i, 1) -> Python
# 错误
ch = X[i]       # i 是 1-indexed，但 Python 从 0 开始
# 正确
ch = X[i - 1]
```

## 2. 循环边界错误

**错误**: 遍历字符串时使用 `<=` 而不是 `<`，导致索引越界。

```python
text = "HELLO"
# 错误：索引超出范围
for i in range(1, len(text) + 1):
    print(text[i])      # 最后一个循环 text[5] 越界

# 正确
for i in range(1, len(text) + 1):
    ch = text[i - 1]    # 注意减 1
```

## 3. 冒泡排序内层循环边界

**错误**: 内层循环没有减去已排序的元素数。

```python
n = len(arr)
# 错误
for i in range(n - 1):
    for j in range(n - 1):  # 每次都遍历全部
        ...

# 正确
for i in range(n - 1):
    for j in range(n - 1 - i):  # 减去已排序的 i 个
        ...
```

## 4. 字符比较时忽略大小写

**错误**: 直接比较字符但未考虑大小写，导致 `'a' > 'Z'` 等意外结果。

```python
# 错误
if ch == "A":   # 无法匹配 'a'

# 正确
if ch.upper() == "A":
```

## 5. 交换时未使用临时变量

<details>
<summary>错误示例</summary>

```python
# 错误：直接赋值导致数据丢失
arr[i] = arr[j]   # arr[i] 的原值丢失
arr[j] = arr[i]   # arr[j] 得到的是 arr[i] 的新值

# 正确
temp = arr[i]
arr[i] = arr[j]
arr[j] = temp
```

</details>

## 6. 递归缺少基本情况

```python
# 错误：没有基本情况，无限递归
def count_vowels(text):
    first = text[0]
    return (1 if first in "aeiou" else 0) + count_vowels(text[1:])

# 正确：有基本情况
def count_vowels(text):
    if len(text) == 0:
        return 0
    first = text[0]
    return (1 if first.lower() in "aeiou" else 0) + count_vowels(text[1:])
```

## 7. 混淆 LEN 与索引最大值

**错误**: `LEN(X) = 5` 表示有效索引为 1 到 5（伪代码 1-indexed），Python 索引为 `X[0]` 到 `X[4]`。

```python
text = "HELLO"      # LEN = 5
# 伪代码: FOR i ← 1 TO LEN(X)
# Python: for i in range(len(text)):  # i = 0, 1, 2, 3, 4
#         ch = text[i]
```

## 8. 伪代码中字符串连接使用错误符号

**正确的伪代码连接符**: 使用 `&` 或 `+`（不同试卷版本存在差异）。

```
Result ← Result & MID(X, i, 1)   ✓
Result ← Result + MID(X, i, 1)   ✓ (部分试卷允许)
```

## 9. Python 中字符串不可变

```python
text = "HELLO"
# 错误：不能直接修改字符串
text[0] = "h"   # TypeError!

# 正确：重新构建字符串
text = "h" + text[1:]
```

## 10. 忘记处理空字符串

```python
def first_char(text):
    # 错误：如果 text 为空会越界
    return text[0]

    # 正确：先检查长度
    if len(text) == 0:
        return ""
    return text[0]
```
