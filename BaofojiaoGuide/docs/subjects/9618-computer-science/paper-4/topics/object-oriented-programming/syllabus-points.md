---
title: 考纲要点
sidebar_position: 6
---

# 考纲要点

## 20.1.2 Object-Oriented Programming (OOP)

### Class 与 Object

| 概念 | 定义 | 考试要求 |
|------|------|----------|
| **Class** | 对象的模板/蓝图 | 能根据题目描述定义 class |
| **Object** | class 的实例 | 能创建对象并调用方法 |
| **Attribute** | 对象的数据/属性 | 通常全部为 private |
| **Method** | 对象的行为/操作 | getter、setter、自定义逻辑 |

### Encapsulation（封装）

- **Private attributes**: 用 `self.__attr` 定义，外部不能直接访问
- **Public methods**: getter / setter 作为接口
- **考试重点**: 所有 attribute 必须是 private，通过 public methods 访问

### Constructor（构造方法）

```python
def __init__(self, params):
    self.__attr = param
```

- 在对象创建时自动调用
- 用于初始化所有 attribute
- `self` 指向当前实例

### Getter / Setter

| 类型 | 命名规则 | 关键字 |
|------|----------|--------|
| Getter | `GetAttrName()` | `return self.__attr` |
| Setter | `SetAttrName(val)` | `self.__attr = val` |
| Boolean Getter | `IsAttrName()` | `return True/False` |

### Inheritance（继承）

考试较少考查，但需要了解：

```python
class Parent:
    def __init__(self, x):
        self.__x = x

class Child(Parent):       # 继承
    def __init__(self, x, y):
        super().__init__(x)   # 调用父类 constructor
        self.__y = y
```

| 知识点 | 说明 |
|--------|------|
| `class Child(Parent):` | 子类继承父类 |
| `super().__init__(args)` | 调用父类 constructor |
| Private attributes 不继承 | 需要用父类的 getter/setter |

### Composition（组合）

- "has-a" 关系：一个 class 包含另一个 class 作为 attribute
- 在 constructor 中创建内部对象

```python
class Room:
    def __init__(self, number):
        self.__number = number

class Building:
    def __init__(self, address):
        self.__address = address
        self.__rooms = []    # composition
```

### Polymorphism（多态）

- 同一方法名在不同 class 中有不同实现
- Paper 4 很少单独考查，理解即可

## Paper 4 高频考点地图

```
考纲条目              考查频率     Paper 4 实际题型
────────────────────────────────────────────────────
Class definition       ★★★★★     Q1 (4-5 marks)
Getter methods         ★★★★★     Q2 (3 marks)
Setter methods         ★★★★★     Q3 (3 marks)
Object instantiation   ★★★★★     Q4 (2-4 marks)
Array of objects       ★★★★★     Q5 (7 marks)
File I/O               ★★★★★     Q5 (integrated)
Business logic         ★★★★☆     Q6 (6 marks)
Inheritance            ★★☆☆☆     Rare (2-3 marks)
Composition            ★★☆☆☆     Rare (2-3 marks)
Polymorphism           ★☆☆☆☆     Almost never
```

## 建议复习顺序

1. Class + constructor → 2. Getter/Setter → 3. Object + method call
4. Array of objects → 5. File I/O → 6. Business logic → 7. Inheritance/Composition
