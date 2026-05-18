---
title: 题型分析
sidebar_position: 2
---

# 题型分析

## Q1: Declare class with private attributes + constructor (4-5 marks)

**Identify**: 题目要求 "declare a class"、"constructor"、"private attributes"

**Standard method**:
1. `class ClassName:`
2. `def __init__(self, ...):`
3. `self.__attr = param`（每个 private attribute 一行）
4. 有时需要初始化默认值 `self.__count = 0`

:::note[MS Pattern]
- **M1**: Correct class declaration with `class` keyword and colon
- **A1**: Correct `__init__` method signature with `self` as first parameter
- **A1**: Each private attribute correctly assigned with `self.__attr = param`
- **B1**: Any additional default attribute correctly initialised
:::

<details>
<summary>Example: 9618/s24/qp/41 Q2</summary>

```python
class Employee:
    def __init__(self, empID, empName):
        self.__empID = empID
        self.__empName = empName
        self.__salary = 0.0
```
</details>

<details>
<summary>Example: 9618/w22/qp/41 Q2</summary>

```python
class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health
        self.__maxHealth = health
```
</details>

**Traps**:
- 忘记 `self` 参数 → 0 marks for constructor line
- Private attribute 必须用 `__`（双下划线）而不是单下划线
- 拼写错误：attribute 名称必须和题目完全一致

---

## Q2: Implement getter methods (3 marks)

**Identify**: "getter"、"accessor"、"return the value of"

**Standard method**:
1. `def GetAttrName(self):`
2. `return self.__attr`

:::note[MS Pattern]
- **M1**: Correct method signature with `self` parameter
- **A1**: Use of `return` keyword
- **A1**: Correctly references `self.__attr`
:::

<details>
<summary>Example: 9618/s24/qp/41 Q2</summary>

```python
def GetEmpID(self):
    return self.__empID
```
</details>

<details>
<summary>Example: 9618/w23/qp/42 Q2</summary>

```python
def GetTitle(self):
    return self.__title
```
</details>

**Traps**:
- 用了 `print` 而不是 `return` → 扣 1 mark
- 遗漏 `self.` → 写成 `return __attr`

---

## Q3: Implement setter methods (3 marks)

**Identify**: "setter"、"mutator"、"update/change the value of"

**Standard method**:
1. `def SetAttrName(self, value):`
2. `self.__attr = value`
3. 有时需要 validation（如 `if value >= 0`）

:::note[MS Pattern]
- **M1**: Correct method signature with `self` and parameter
- **A1**: Correct assignment `self.__attr = value`
- **B1**: Validation / range check where required
:::

<details>
<summary>Example: 9618/s24/qp/41 Q2</summary>

```python
def SetSalary(self, salary):
    if salary >= 0.0:
        self.__salary = salary
```
</details>

<details>
<summary>Example: 9618/w22/qp/41 Q2</summary>

```python
def SetHealth(self, health):
    if 0 <= health <= self.__maxHealth:
        self.__health = health
```
</details>

**Traps**:
- 题目要求 validation 但没写 → 扣 B1 mark
- setter parameter name 和 attribute name 混淆

---

## Q4: Create objects and call methods (2-4 marks)

**Identify**: "instantiate"、"create an object"、"call the method"

**Standard method**:
1. `obj = ClassName(args)`
2. `obj.MethodName()`

:::note[MS Pattern]
- **M1**: Correct object instantiation with class name and arguments
- **A1**: Correct method call on object using dot notation
:::

<details>
<summary>Example: 9618/s24/qp/41 Q2</summary>

```python
emp1 = Employee("E001", "Alice")
emp1.SetSalary(3500.0)
print(emp1.GetEmpName())
```
</details>

<details>
<summary>Example: 9618/s23/qp/41 Q2</summary>

```python
player1 = Character("Hero", 100)
player1.TakeDamage(20)
```
</details>

**Traps**:
- 对象名必须和题目要求一致（如 `myObject` 而不是随便起名）
- constructor 参数顺序错误

---

## Q5: Array of objects with file reading (7 marks)

**Identify**: "read from file"、"array/list of objects"、"store in array"

**Standard method**:
1. Open file: `file = open("data.txt", "r")`
2. Loop through lines: `for line in file.readlines():`
3. Split line: `data = line.strip().split(",")`
4. Create object: `obj = ClassName(data[0], data[1])`
5. Append to list: `arr.append(obj)`
6. Close file: `file.close()`

:::note[MS Pattern]
- **M1**: Correct file opening with mode `"r"`
- **M1**: Write a loop to read all lines from file
- **A1**: Correct use of `strip()` and `split()` to parse data
- **A1**: Create new object and add to list
- **B1**: File is closed after reading
:::

<details>
<summary>Example: 9618/s24/qp/42 Q2</summary>

```python
def ReadEmployees():
    empList = []
    file = open("employees.txt", "r")
    for line in file.readlines():
        data = line.strip().split(",")
        emp = Employee(data[0], data[1], data[2])
        empList.append(emp)
    file.close()
    return empList
```
</details>

<details>
<summary>Example: 9618/w22/qp/42 Q2</summary>

```python
def LoadStudents():
    students = []
    file = open("students.txt", "r")
    for line in file.readlines():
        parts = line.strip().split(",")
        s = Student(parts[0], parts[1], int(parts[2]))
        students.append(s)
    file.close()
    return students
```
</details>

**Traps**:
- 忘记 `strip()` — 换行符 `\n` 会残留 → 数据错误
- 忘记类型转换 — 文件读取的都是 string，数字需要 `int()` 或 `float()`
- 忘记 `file.close()` — 可能只扣 1 mark 但必须写

---

## Q6: Business logic using object methods (6 marks)

**Identify**: "calculate"、"display all"、"find the highest"、"process"

**Standard method**:
1. Loop through array of objects
2. Call getter methods to access data
3. Implement logic (sum, max, count, display)
4. Return or print result

:::note[MS Pattern]
- **M1**: Loop through all objects in array
- **A1**: Correct use of method calls to access data
- **A1**: Correct logic (accumulation / comparison / condition)
- **A1**: Return or output the result
:::

<details>
<summary>Example: 9618/s24/qp/41 Q2</summary>

```python
def CalculateTotalSalary(empList):
    total = 0.0
    for emp in empList:
        total += emp.GetSalary()
    return total
```
</details>

<details>
<summary>Example: 9618/w23/qp/41 Q2</summary>

```python
def DisplayHighScorers(playerList):
    for player in playerList:
        if player.GetScore() >= 80:
            print(player.GetName(), player.GetScore())
```
</details>

**Traps**:
- 直接用 `emp.__salary` 而不是通过 getter → 正确但违反 encapsulation 原则，考试允许但推荐用 getter
- 循环外要初始化累加器 `total = 0`
- 比较最大值时用 `>` 时注意初始值设为 `None` 或第一个元素
