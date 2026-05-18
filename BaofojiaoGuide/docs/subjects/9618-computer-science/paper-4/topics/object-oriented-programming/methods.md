---
title: 解题方法
sidebar_position: 3
---

# 解题方法

## 1. Class Structure 通用模板

```python
class ClassName:
    def __init__(self, param1, param2, ...):
        # private attributes
        self.__attr1 = param1
        self.__attr2 = param2
        # public / protected attributes
        self._counter = 0

    # --- Getter Methods ---
    def GetAttr1(self):
        return self.__attr1

    # --- Setter Methods ---
    def SetAttr1(self, value):
        # validation (if required)
        if condition:
            self.__attr1 = value

    # --- Other Methods ---
    def MethodName(self, args):
        # business logic
        return result
```

## 2. Constructor `__init__`

- **必须**有 `self` 作为第一个参数
- 每个 attribute 都用 `self.__name = ...` 初始化
- 题目要求 "initialise to 0" → `self.__count = 0`
- 题目要求 "initialise to empty string" → `self.__name = ""`

:::note
考试中 **所有** attribute 都是 private，除非题目明确要求 public（极少）。
:::

### 变量命名对照表

| 题目用语 | Python 写法 |
|----------|-------------|
| private attribute `name` | `self.__name` |
| public attribute `count` | `self.count` |
| protected attribute `id` | `self._id` |
| constructor with 2 params | `def __init__(self, a, b)` |
| default value | `self.__x = 0` |

## 3. Getter / Accessor Method

```python
def GetAttributeName(self):
    return self.__attributeName
```

- Method name 通常 Python 风格：`Get...`（PascalCase）
- 如果返回的是 boolean，有时用 `Is...`（如 `IsAvailable()`）
- **必须**用 `return`，不能只用 `print`

## 4. Setter / Mutator Method

```python
def SetAttributeName(self, value):
    if condition:  # optional validation
        self.__attributeName = value
```

- Setter 参数名可以和 attribute 不同以区分
- 常见 validation：`>= 0`、`0 <= x <= 100`、`.isnumeric()`
- 有时没有 validation，直接赋值即可

## 5. Object 创建与方法调用

```python
# Create object
obj = ClassName(arg1, arg2)

# Call getter
result = obj.GetAttr()

# Call setter
obj.SetAttr(newValue)

# Call other methods
obj.DoSomething()
```

## 6. Array / List of Objects

```python
# Empty list
arr = []

# Add objects
arr.append(obj1)
arr.append(obj2)

# Access via index
first = arr[0]
print(first.GetName())

# Loop through all
for item in arr:
    print(item.GetName())
```

## 7. Composition (一个 class 包含另一个 class)

```python
class Engine:
    def __init__(self, power):
        self.__power = power

class Car:
    def __init__(self, model, enginePower):
        self.__model = model
        self.__engine = Engine(enginePower)  # composition

    def GetModel(self):
        return self.__model
```

- 在 constructor 中创建 "has-a" 对象
- 外部通过 getter 访问内部对象

## 8. File I/O with Objects

```python
# --- Read from file to array of objects ---
def LoadData(filename):
    arr = []
    file = open(filename, "r")
    for line in file.readlines():
        parts = line.strip().split(",")
        # 类型转换：string → int/float
        obj = ClassName(parts[0], int(parts[1]))
        arr.append(obj)
    file.close()
    return arr

# --- Write array of objects to file ---
def SaveData(filename, arr):
    file = open(filename, "w")
    for obj in arr:
        file.write(obj.GetName() + "," + str(obj.GetValue()) + "\n")
    file.close()
```

:::note[数据解析要点]
- CSV 格式：`line.strip().split(",")`
- 空格分隔：`line.strip().split()`
- 固定宽度：string slicing `line[0:5]`
:::
