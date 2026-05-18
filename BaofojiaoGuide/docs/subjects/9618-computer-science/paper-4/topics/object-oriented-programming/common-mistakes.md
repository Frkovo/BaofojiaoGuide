---
title: 常见错误
sidebar_position: 5
---

# 常见错误

## 错误 1: 忘记 `self`

```python
# ❌ 错误
class Employee:
    def __init__(name, id):    # 缺少 self
        self.__name = name    # 运行时 TypeError

# ✅ 正确
class Employee:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
```

**后果**: Python 会把第一个参数当作 `self`，导致参数错位 → **所有依赖该 constructor 的代码都出错**。

---

## 错误 2: 私有属性没用 `__`

```python
# ❌ 错误 (public attribute)
self.name = name

# ✅ 正确 (private attribute)
self.__name = name
```

:::note
考试中 paper 4 要求所有 attribute 都是 private，除非题目明确指明 public. 单下划线 `_name` 是 protected 不是 private，不够严格。
:::

---

## 错误 3: 在方法中忘记 `self.`

```python
class Student:
    def __init__(self, name):
        self.__name = name

    def GetName(self):
        return __name    # ❌ NameError: '__name' not defined
        return self.__name  # ✅ 正确
```

**记忆技巧**: 访问任何 attribute 或调用同类方法时，都需要 `self.`

---

## 错误 4: 文件读取后忘记 `strip()`

```python
file = open("data.txt", "r")
for line in file.readlines():
    data = line.split(",")        # ❌ data[-1] contains '\n'
    data = line.strip().split(",")  # ✅ 正确
file.close()
```

**假设文件内容**: `Alice,20\n`
- 没有 `strip()`: `["Alice", "20\n"]` → `int("20\n")` 报错
- 有 `strip()`: `["Alice", "20"]` → `int("20")` 正常

---

## 错误 5: 忘记类型转换

```python
# ❌ 错误
parts = line.strip().split(",")
obj = Student(parts[0], parts[1])   # parts[1] 是 string
# 如果 constructor 期望 int 或 float

# ✅ 正确
parts = line.strip().split(",")
obj = Student(parts[0], int(parts[1]))
```

---

## 错误 6: Getter 用了 `print` 而不是 `return`

```python
# ❌ 错误 (return None)
def GetName(self):
    print(self.__name)

# ✅ 正确
def GetName(self):
    return self.__name
```

**后果**: 调用 `x = obj.GetName()` 后 `x` 是 `None`，后续逻辑全部异常。

---

## 错误 7: Setter 缺少 validation

```python
# ❌ 错误 — 如果题目要求 validation
def SetAge(self, age):
    self.__age = age

# ✅ 正确
def SetAge(self, age):
    if age >= 0:
        self.__age = age
```

**提示**: 题目说 "must be positive"、"must be between 0 and 100" → **必须写 validation**.

---

## 错误 8: Constructor 参数顺序错误

```python
# 题目要求: (studentName, studentID, yearGroup)
# ❌ 错误
s = Student("S01", "Alice", 12)

# ✅ 正确 — 与题目定义一致
s = Student("Alice", "S01", 12)
```

---

## 错误 9: 忘记初始化累加器

```python
# ❌ 错误
def TotalScore(players):
    for p in players:
        total += p.GetScore()    # NameError: total not defined
    return total

# ✅ 正确
def TotalScore(players):
    total = 0   # 先初始化
    for p in players:
        total += p.GetScore()
    return total
```

---

## 错误 10: 文件模式错误

```python
# ❌ 错误 — 'w' 会清空文件
file = open("data.txt", "w")
for line in file.readlines():   # ⚠️ 无法读取

# ✅ 正确
file = open("data.txt", "r")    # 读取用 'r'
```

| 模式 | 含义 | 文件不存在时 |
|------|------|-------------|
| `"r"` | 读取 | 报错 |
| `"w"` | 写入（覆盖） | 新建 |
| `"a"` | 追加 | 新建 |
| `"r+"` | 读写 | 报错 |

---

## 错误 11: Off-by-one 索引错误

```python
# 文件有 5 行，数组长度为 5，索引 0-4
# ❌ 错误
for i in range(1, len(arr) + 1):   # 索引从 1 开始，越界
    print(arr[i])

# ✅ 正确
for i in range(len(arr)):
    print(arr[i])
```

---

## Error Checklist

- [ ] `self` 是第一个参数
- [ ] 所有 attribute 前有 `self.__`
- [ ] 访问 attribute 时加了 `self.`
- [ ] file 读取用了 `strip()`
- [ ] string 转成了 `int()` / `float()` 如果需要
- [ ] getter 用 `return` 不是 `print`
- [ ] setter 有 validation（如需要）
- [ ] 循环有正确边界
- [ ] 累加器已初始化
- [ ] `file.close()` 已写
