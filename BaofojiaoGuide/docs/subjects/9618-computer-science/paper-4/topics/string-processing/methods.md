---
title: "解题方法"
---

# 解题方法

## Python 字符串索引

Python 字符串是 0-indexed 的，每个字符可以通过索引访问。

```python
s = "COMPUTER"
# 正向索引:  0  1  2  3  4  5  6  7
# 字符:     C  O  M  P  U  T  E  R
# 反向索引: -8 -7 -6 -5 -4 -3 -2 -1
```

| 操作 | Python 代码 | 结果 |
|------|------------|------|
| 第一个字符 | `s[0]` | `'C'` |
| 第 3 个字符 | `s[2]` | `'M'` |
| 最后一个字符 | `s[-1]` | `'R'` |
| 前 3 个字符 | `s[:3]` | `'COM'` |
| 第 2-4 个字符 | `s[1:4]` | `'OMP'` |

## MID 等效写法

| 伪代码 `MID(X, start, length)` | Python 等效 |
|-------------------------------|------------|
| `MID(X, 1, 1)` | `X[0]` |
| `MID(X, i, 1)` | `X[i-1]` |
| `MID(X, 1, n)` | `X[:n]` |
| `MID(X, i, n)` | `X[i-1:i-1+n]` |
| `MID(X, i, LEN(X)-i+1)` | `X[i-1:]` |

## 字符比较

字符比较基于 ASCII/Unicode 码点：

```python
# 常用 ASCII 码值
# '0'-'9': 48-57
# 'A'-'Z': 65-90
# 'a'-'z': 97-122

# 比较操作
print('A' < 'B')    # True
print('a' < 'B')    # False (97 > 65)
print('5' < 'A')    # True  (53 < 65)

# 获取 ASCII 码
print(ord('A'))     # 65
print(chr(65))      # 'A'
```

## 常见考法

### 冒泡排序字符串

```python
def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j][0] > arr[j + 1][0]:  # 按首字符排序
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### 统计元音

```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count
```

### 大小写转换

```python
def to_uppercase(text):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result
```

### 递归统计元音

```python
def count_vowels_recursive(text):
    if len(text) == 0:
        return 0
    first = text[0].lower()
    count = 1 if first in "aeiou" else 0
    return count + count_vowels_recursive(text[1:])
```

## 关键技巧

:::note[Tips]

1. 始终明确字符串是 0-indexed 还是 1-indexed
2. 处理 `MID(X, i, 1)` 时，`i` 是 1-indexed，Python 中用 `X[i-1]`
3. 大小写比较使用 `str.upper()` 或 `str.lower()` 统一
4. 注意空字符串的边界情况 (`len(text) == 0`)
5. 在伪代码中，字符串连接用 `← X[i-1] & Y[j-1]`

:::
