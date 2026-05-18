---
title: "题型分析"
sidebar_position: 2
---

# 题型分析

## Q1: Declare Child Class with Constructor Calling Parent (4–5 marks)

**Identify:** 题目给出 parent class 代码，要求写 child class 声明和 constructor。

**Method:**
```
class Child(Parent):
    def __init__(self, params...):
        super().__init__(parent_params)
        self._new_attr = value
```

**MS Pattern:**
- **M1** Correct class header: `class Child(Parent):`
- **A1** Constructor method definition with correct parameters `def __init__(self, ...):`
- **A1** Call to `super().__init__(...)` passing correct parent attributes
- **A1** Initialise new child attributes with `self._attr = param`

**Example:** w23_qp_42 Q3 — `class MagicCharacter(Character):`

**Traps:**
- Forgetting `self` in `super().__init__()` — Python does it automatically, DO NOT pass `self`
- Parameter order must match parent constructor exactly
- Missing colon after class header

## Q2: Override Method in Child Class (3–4 marks)

**Identify:** 要求 override parent 的某个 method，通常需要调用 parent 版本再添加新功能。

**Method:**
```python
def method_name(self, params...):
    result = super().method_name(params)
    # add child-specific logic
    return result
```

**MS Pattern:**
- **M1** Method signature matches parent exactly (same name and parameters)
- **A1** Call `super().method_name(...)` to use parent version
- **A1** Additional child-specific logic (new attribute / calculation)
- **A1** Return value if parent method returned one

**Example:** s23_qp_41 Q2 — `Helicopter.get_info()` calls `super().get_info()` then appends blade info.

**Traps:**
- Wrong method signature (different number of parameters)
- Not calling `super()` when required by MS
- Returning wrong type

## Q3: Main Program with Both Parent and Child Objects (5 marks)

**Identify:** 要求写 main program 创建 parent 和 child 对象，调用方法并输出结果。

**Method:**
```python
def main():
    parent_obj = Parent(params)
    child_obj = Child(params_with_extra)
    print(parent_obj.method())
    print(child_obj.method())  # uses overridden version
```

**MS Pattern:**
- **A1** Instantiate parent object with correct arguments
- **A1** Instantiate child object with correct arguments (including extras)
- **M1** Call method on parent object
- **A1** Call method on child object (tests overriding)
- **A1** Output / print results

**Example:** s23_qp_42 Q3 — Create `Employee` and `Manager`, call `calculate_pay()` on both.

**Traps:**
- Mixing up parameter order between parent and child constructors
- Not capturing return value before printing
- Creating child object with wrong number of arguments

## Q4: Read File and Create Both Parent / Child Objects Based on Data (7 marks)

**Identify:** 题目提供数据文件，要求读取、解析、根据标识符创建 parent 或 child 对象。

**Method:**
```python
def read_data(filename):
    objects = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if parts[0] == "Parent":
                objects.append(Parent(parts[1], parts[2]))
            elif parts[0] == "Child":
                objects.append(Child(parts[1], parts[2], parts[3]))
    return objects
```

**MS Pattern:**
- **M1** Open file correctly (with statement or open/close pair)
- **A1** Loop to read each line / record
- **A1** Split / parse data (e.g. comma-separated)
- **A1** Conditional logic to distinguish parent vs child (e.g. `if type == "X"`)
- **M1** Create parent object with correct parsed arguments
- **A1** Create child object with correct parsed arguments (including extras)
- **A1** Store objects in a list and return / process

**Example:** w23_qp_42 Q3 variant — file contains `Character` and `MagicCharacter` records.

**Traps:**
- Not stripping newline before splitting
- Wrong index access after split
- Forgetting to convert numeric strings to `int` / `float`
- File path hardcoded when parameter expected
- Not handling empty lines
