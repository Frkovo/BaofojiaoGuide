---
title: String Processing
sidebar_position: 1
---

# String Processing（字符串处理）

## 考纲要求

- 11.1 字符串操作：MID, LENGTH
- 字符串比较和排序

## 核心代码模板

### Python 字符串索引
```python
s = "hello"
first = s[0]       # "h"
last = s[len(s)-1]  # "o"
```

### MID 函数对应
```python
# MID(s, start, length) 在 Python 中是 s[start:start+length]
# 注意：Python 从 0 开始索引

def MID(s, start, length):
    return s[start:start + length]

# 示例
# MID("computer", 0, 3) -> "com"
# MID("tiger", 0, 2) -> "ti"
```

### LENGTH 函数
```python
# LENGTH(s) 在 Python 中是 len(s)
length = len("computer")  # 8
```

### 按首字母排序字符串数组
```python
def SortDescending(arr, n):
    for i in range(0, n):
        for j in range(0, n - i - 1):
            if arr[j][0] < arr[j + 1][0]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
```

### 字符类型判断
```python
def IsVowel(ch):
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        return True
    return False
```

### 字符大小写转换
```python
# 转小写
s = s.lower()
# 转大写
s = s.upper()
```

## 常见错误

- MID 函数的起始位置搞混（CIE 从 0 开始）
- LENGTH 比实际长度多 1 或少 1
- 字符串比较用 `==` 不是 `is`
- 忘记 Python 字符串索引从 0 开始
