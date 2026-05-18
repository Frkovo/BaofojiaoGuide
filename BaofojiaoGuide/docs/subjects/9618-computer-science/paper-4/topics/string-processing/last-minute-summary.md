---
title: "考前速记"
---

# 考前速记

## 核心公式

```
MID(X, i, n)  =>  X[i-1 : i-1+n]    # Python 切片
MID(X, i, 1)  =>  X[i-1]            # 单字符
LEN(X)        =>  len(X)            # 长度
```

## 字符比较速查

| 表达式 | ASCII 值 | 结果 |
|--------|---------|------|
| `'0'` | 48 | |
| `'A'` | 65 | |
| `'a'` | 97 | |
| `'A' < 'a'` | 65 < 97 | `True` |
| `'9' < 'A'` | 57 < 65 | `True` |
| `'Z' < 'a'` | 90 < 97 | `True` |

## 大小写转换

```
大写 → 小写: ORD(ch) + 32    # chr(ord('A') + 32) = 'a'
小写 → 大写: ORD(ch) - 32    # chr(ord('a') - 32) = 'A'
```

## 冒泡排序字符串模板

```python
for i in range(len(arr) - 1):
    for j in range(len(arr) - 1 - i):
        if arr[j][0] > arr[j + 1][0]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

## 递归模板

```python
def recursive_count(text):
    if len(text) == 0:       # 基本情况
        return 0
    count = 1 if text[0] in "aeiou" else 0
    return count + recursive_count(text[1:])  # 递归
```

## 检查清单

- [ ] 字符串索引是 1-indexed（伪代码）还是 0-indexed（Python）
- [ ] `MID(X, i, 1)` 中 `i` 从 1 开始
- [ ] 字符比较前统一大小写
- [ ] 冒泡排序内层循环 `n-1-i`
- [ ] 交换使用临时变量
- [ ] 空字符串作为递归基本情况
- [ ] ASCII 码 `ord()` 和 `chr()` 函数
- [ ] `LEN` = `len()`

<details>
<summary>考场应急</summary>

如果忘记 `ord()` 和 `chr()`，可以使用字符串方法：

```python
# 代替大小写转换
ch.upper()    # -> 大写
ch.lower()    # -> 小写
ch.isupper()  # -> 是否大写
ch.islower()  # -> 是否小写
ch.isalpha()  # -> 是否字母
ch.isdigit()  # -> 是否数字
```

</details>
