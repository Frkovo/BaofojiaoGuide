---
title: 题型分析
---

# 题型分析

## 类型 1：Declarative Programming（Prolog）

### 识别特征
- 要求写出 Prolog facts（事实）和 rules（规则）
- 要求解释 Prolog queries（查询）的结果
- 关键词："Prolog", "facts", "rules", "queries", "declarative"

### 标准解题方法

:::note[标准解题方法]
**Facts（事实）**
- 格式：`relation(arg1, arg2, ...).`
- 首字母小写
- 以句点 `.` 结尾

```prolog
likes(john, apple).
likes(mary, orange).
```

**Rules（规则）**
- 格式：`head :- body1, body2, ...`
- `:-` 表示 "if"（左边成立如果右边都成立）
- `,` 表示 AND

```prolog
likes(john, X) :- fruit(X), sweet(X).
```

**Queries（查询）**
- 格式：`?- relation(arg1, arg2, ...).`
- `?-` 表示 "Is it true that..."
- 大写字母开头是变量，Prolog 会尝试绑定

```prolog
?- likes(john, apple).    % true
?- likes(john, X).        % X = apple; X = orange
```

**关键规则**
- `:-` = IF
- `,` = AND
- `;` = OR
- `not` = NOT
- 变量以大写字母开头，常量以小写字母开头

:::

:::info[评分标准（MS 模式）]
- **M1**：正确写出 facts 的语法（小写、句点结尾）
- **M2**：正确写出 rules（使用 `:-`）
- **A1**：正确使用变量（大写字母开头）
- **A2**：查询结果正确
- **B1**：理解 Prolog 的 backward chaining（反向链）推理

:::

### 真题示例

**示例 1：9618/w23/qp/31 Q11（Subject Choice）**

> A school uses Prolog to represent subject choices. Write facts and a rule to determine if a student can take a subject.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Correct fact format: `studies(alice, maths).`
- **M2**: Correct rule format: `can_take(X, Y) :- studies(X, Z), requires(Y, Z).`
- **A1**: Facts end with `.`
- **A2**: Variables start with uppercase letter
- **B1**: Rule uses `:-` to define condition

**Example facts:**
```prolog
studies(bob, maths).
studies(bob, physics).
requires(computing, maths).
```

**Example rule:**
```prolog
can_take(Student, Subject) :-
    studies(Student, Requirement),
    requires(Subject, Requirement).
```

</details>

**示例 2：9618/w23/qp/32 Q11（Hobbies）**

> Write Prolog facts and a rule to represent people and their hobbies. Write a query to find all people who enjoy swimming.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Correct fact: `hobby(anna, swimming).`
- **M2**: Correct rule: `enjoys(Person, Hobby) :- hobby(Person, Hobby).`
- **A1**: Query: `?- hobby(Person, swimming).`
- **A2**: Variables correctly capitalised
- **B1**: Understanding that Prolog searches for all matching bindings

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 忘记在 facts 末尾加句点 `.`
2. 常量首字母大写了：常量小写，变量大写
3. 混淆 `:-` 方向：`head :- body.` 意思是 head 为真如果 body 为真
4. Query 中忘记 `?-`
5. 理解 Prolog 的搜索策略：Prolog 使用 backward chaining（深度优先）

:::

---

## 类型 2：OOP Class 设计

### 识别特征
- 要求用伪代码设计一个 class
- 包括 attributes（属性）、methods（方法）、constructor（构造方法）
- 可能涉及 inheritance（继承）

### 标准解题方法

:::note[标准解题方法]
**Class 声明模板**
```pseudocode
CLASS ClassName
    // Private attributes
    DECLARE attribute1 : DATATYPE
    DECLARE attribute2 : DATATYPE

    // Constructor
    PUBLIC PROCEDURE NEW(param1: DATATYPE, param2: DATATYPE)
        attribute1 <- param1
        attribute2 <- param2
    ENDPROCEDURE

    // Getter
    PUBLIC FUNCTION GetAttribute1() RETURNS DATATYPE
        RETURN attribute1
    ENDFUNCTION

    // Setter
    PUBLIC PROCEDURE SetAttribute1(value: DATATYPE)
        attribute1 <- value
    ENDPROCEDURE

    // Other methods
    PUBLIC PROCEDURE SomeMethod()
        // implementation
    ENDPROCEDURE
ENDCLASS
```

**Inheritance**
```pseudocode
CLASS ChildClass EXTENDS ParentClass
    // Additional attributes
    DECLARE extraAttribute : DATATYPE

    PUBLIC PROCEDURE NEW(...)  // calls parent NEW
        CALL ParentClass::NEW(...)
        extraAttribute <- ...
    ENDPROCEDURE

    // Override method
    PUBLIC PROCEDURE SomeMethod()
        // new implementation
    ENDPROCEDURE
ENDCLASS
```

:::

:::info[评分标准（MS 模式）]
- **M1**：CLASS...ENDCLASS 结构完整
- **M2**：属性声明（PRIVATE）正确
- **A1**：Constructor（NEW）正确初始化属性
- **A2**：Getter/Setter 方法正确
- **B1**：继承关系正确实现（EXTENDS + 调用父类构造）

:::

### 真题示例

**示例 1：9618/w22/qp/33 Q11（Car Class）**

> Write a class definition for a Car with attributes make, model, year. Include a constructor and a method to display car details.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: CLASS Car ... ENDCLASS structure
- **M2**: PRIVATE attributes declared with correct types
- **A1**: Constructor NEW sets all attributes
- **A2**: DisplayDetails method outputs attributes
- **B1**: Appropriate encapsulation (PRIVATE)

</details>

**示例 2：9618/s22/qp/31 Q7（Yarn Shop）**

> A yarn shop requires a class to represent different types of yarn. Demonstrate inheritance by creating a base Yarn class and a subclass WoolYarn.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Base class Yarn with common attributes
- **M2**: Subclass WoolYarn EXTENDS Yarn
- **A1**: Subclass constructor calls parent constructor
- **A2**: Additional attributes in subclass
- **B1**: Polymorphism or method overriding demonstrated

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 混淆 class 与 object：class 是模板，object 是实例
2. 忘记 constructor（NEW）
3. inheritance 中忘记调用 parent constructor
4. 属性全部 PUBLIC：应该用 PRIVATE 实现 encapsulation

:::

---

## 类型 3：OOP 概念定义

### 识别特征
- 要求定义 Encapsulation / Inheritance / Polymorphism
- 要求举例说明

### 标准解题方法

:::note[标准解题方法]
**Encapsulation（封装）**
- 将 data (attributes) 和 methods 捆绑在 class 中
- 使用 PRIVATE 隐藏内部数据
- 通过 PUBLIC methods（getters/setters）控制访问
- 目的：保护数据不被外部直接修改

**Inheritance（继承）**
- subclass 继承 superclass 的属性和方法
- 实现代码复用（code reusability）
- 使用 EXTENDS 关键字
- 子类可以添加新属性和方法，或 override 父类方法

**Polymorphism（多态）**
- 同一方法名在不同 class 中有不同实现
- 通过 method overriding（子类重写父类方法）
- 同一接口、多种实现

:::

:::info[评分标准（MS 模式）]
- **M1**：准确定义概念
- **M2**：给出关键特征
- **A1**：给出具体例子
- **B1**：说明该概念的优点或目的

:::

### 真题示例

**示例 1：9618/w22/qp/32 Q10**

> Define the following OOP concepts: encapsulation, inheritance and polymorphism. Give an example of each.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Encapsulation = bundling data and methods, hiding data with PRIVATE
- **M2**: Inheritance = subclass inherits from superclass using EXTENDS
- **A1**: Polymorphism = same method name with different implementations
- **A2**: Appropriate example for each concept
- **B1**: Explanation of benefits (data security, code reuse, flexibility)

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 只写名字不写定义：考试要求定义 + 举例
2. 混淆 Polymorphism 与 Inheritance：Polymorphism 不是继承
3. 没有举例：定义 + 例子的组合才得满分

:::

---

## 类型 4：RPN（Reverse Polish Notation）

### 识别特征
- 要求将 infix expression 转换为 RPN（或反之）
- 要求使用栈计算 RPN 表达式的值
- 关键词："RPN", "postfix", "stack", "shunting-yard"

### 标准解题方法

:::note[标准解题方法]
**Infix 转 RPN 转换**
1. 操作数（operands）直接输出
2. 运算符（operators）根据优先级入栈或输出
3. 左括号 `(` 入栈，右括号 `)` 弹出直到左括号

**RPN 栈求值**
1. 从左到右扫描 token
2. 操作数入栈
3. 运算符弹出两个操作数，计算结果，结果入栈
4. 最后栈顶即为结果

**RPN 求值示例：** `3 4 + 2 *`

```
Token | Stack
3     | [3]
4     | [3, 4]
+     | [7]          (3 + 4 = 7)
2     | [7, 2]
*     | [14]         (7 * 2 = 14)
```

:::

:::info[评分标准（MS 模式）]
- **M1**：正确使用栈结构
- **M2**：操作数入栈顺序正确
- **A1**：操作数弹出的顺序正确（注意减法和除法）
- **A2**：最终结果正确
- **B1**：RPN 不需要括号（无歧义）

:::

### 真题示例

**示例 1：9618/s24/qp/31 Q5**

> Convert the infix expression (3 + 4) x (5 - 2) into RPN. Then use a stack to evaluate it.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Correct RPN: 3 4 + 5 2 - x
- **M2**: Correct stack operations
- **A1**: 3 + 4 = 7, 5 - 2 = 3
- **A2**: 7 x 3 = 21
- **B1**: Understanding of LIFO stack behaviour

</details>

**示例 2：9618/w23/qp/31 Q9**

> Evaluate the RPN expression 8 2 / 3 1 - x using a stack.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Correct stack trace
- **M2**: 8 2 / = 4
- **A1**: 3 1 - = 2
- **A2**: 4 x 2 = 8
- **B1**: Correct order of operands for division and subtraction

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 减法和除法的操作数顺序：`a b -` = a - b，`a b /` = a / b（不是 b - a 或 b / a）
2. 混淆 Infix 与 RPN：中缀有括号，RPN 不需要
3. 忘记 RPN 的结果在栈顶
4. 转换 Infix 到 RPN 时忘记运算符优先级

:::

---

## 类型 5：编程范式识别

### 识别特征
- 给出一段代码，要求判断属于哪种编程范式
- 或要求说明不同范式的特征

### 标准解题方法

:::note[标准解题方法]
| 范式 | 特征 | 示例语言 |
|------|------|----------|
| **Low-level** | Direct memory access, registers, machine/binary code | Assembly, Machine code |
| **Imperative** | Sequence of statements, loops, IF, variables changed | Pascal, C, BASIC |
| **Object-Oriented** | Classes, objects, methods, inheritance, encapsulation | Java, C++, Python |
| **Declarative** | Facts, rules, queries, what NOT how | Prolog, SQL |

:::

:::info[评分标准（MS 模式）]
- **M1**：正确识别范式
- **M2**：给出 1-2 个代码特征作为证据
- **A1**：解释该范式的特点

:::

### 真题示例

**示例 1：9618/s21/qp/31 Q9(c)**

> Identify the programming paradigm used in the given code fragment. Justify your answer.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Correct identification
- **M2**: Reference to specific code features (e.g. "uses classes and objects")
- **A1**: Explanation of paradigm characteristics

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 混淆 OOP 与 Imperative：OOP 一定是 Imperative，但 Imperative 不一定是 OOP
2. Declarative 不等于 SQL：SQL 只是 declarative 的一种
3. Low-level 不等于 Assembly：Machine code 和 Assembly 都是 low-level

:::

---

## 类型 6：File Processing 伪代码

### 识别特征
- 要求使用 OPENFILE / READFILE / WRITEFILE 操作文件
- 通常涉及读取文件内容进行处理

### 标准解题方法

:::note[标准解题方法]
```pseudocode
DECLARE FileName : STRING
DECLARE FileHandle : INTEGER
DECLARE Line : STRING

// Open file for reading
FileHandle <- OPENFILE("data.txt")  // default for reading
// or explicitly:
FileHandle <- OPENFILE("data.txt", "r")

// Read all lines
WHILE NOT EOF(FileHandle) DO
    Line <- READFILE(FileHandle)
    OUTPUT Line
ENDWHILE

// Close file
CLOSEFILE(FileHandle)

// Open file for writing
FileHandle <- OPENFILE("output.txt", "w")
WRITEFILE(FileHandle, "Hello World")
CLOSEFILE(FileHandle)
```

**文件模式**
- `"r"` = read（读取）
- `"w"` = write（写入，覆盖）
- `"a"` = append（追加）

:::

:::info[评分标准（MS 模式）]
- **M1**：正确使用 OPENFILE
- **M2**：EOF 检查用于读取循环
- **A1**：正确使用 READFILE / WRITEFILE
- **B1**：文件操作结束后 CLOSEFILE

:::

### 真题示例

**示例 1：9618/s23/qp/31 Q10**

> Write pseudocode to read all lines from a text file named "scores.txt" and output the total number of lines.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: OPENFILE to open the file
- **M2**: WHILE NOT EOF loop
- **A1**: READFILE inside loop
- **A2**: Counter variable increments each line
- **B1**: CLOSEFILE after processing

</details>

**示例 2：9618/w23/qp/31 Q8(a)**

> A program needs to write data to a file "log.txt". Write the pseudocode to open the file for writing and append a timestamp to it.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: OPENFILE with "a" (append) mode
- **M2**: WRITEFILE to write data
- **A1**: CLOSEFILE after writing
- **B1**: Understanding that "a" mode adds to existing content

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 忘记 CLOSEFILE：可能导致数据丢失或文件损坏
2. 文件模式混淆："w" 覆盖，"a" 追加，"r" 读取
3. 检查 EOF 时忘记 NOT：`WHILE NOT EOF(handle)`
4. 没有处理文件不存在的情况

:::

---

## 类型 7：Exception Handling

### 识别特征
- 要求解释 exception handling 的概念
- 要求给出 TRY...EXCEPT 的例子
- 关键词："exception", "error handling", "try", "except", "runtime error"

### 标准解题方法

:::note[标准解题方法]
```pseudocode
TRY
    // Code that may cause an error
    DECLARE num : INTEGER
    num <- 10 / 0  // Division by zero
EXCEPT
    // Handle the error
    OUTPUT "An error occurred"
ENDTRY
```

**常见异常类型**
| 异常 | 说明 |
|------|------|
| Division by zero | 除以零 |
| Index out of range | 数组索引越界 |
| File not found | 文件不存在 |
| Type mismatch | 类型不匹配 |
| Null reference | 空引用 |

**Exception handling 的优点**
- 防止程序崩溃（program crash）
- 提供有意义的错误信息
- 将错误处理代码与正常逻辑分离
- 可以优雅地恢复或终止

:::

:::info[评分标准（MS 模式）]
- **M1**：正确使用 TRY...EXCEPT 结构
- **M2**：给出一个适当的异常例子
- **A1**：解释异常处理的好处
- **B1**：识别不同类型的异常

:::

### 真题示例

**示例 1：9618/w23/qp/32 Q12(a)**

> Describe what is meant by exception handling. Give a suitable example.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Exception handling deals with runtime errors
- **M2**: Prevents program from crashing
- **A1**: Uses TRY...EXCEPT structure
- **A2**: Example: division by zero, file not found
- **B1**: Allows graceful error recovery

</details>

**示例 2：9618/s22/qp/32 Q9**

> Write pseudocode that uses exception handling to safely read from a file that may not exist.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: TRY block containing file operations
- **M2**: EXCEPT block to catch error
- **A1**: Appropriate error message in EXCEPT
- **B1**: Program continues after handling

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 滥用 Exception Handling：不要用异常控制正常流程
2. 没有在 EXCEPT 中做有意义的处理（空 EXCEPT 是坏习惯）
3. 混淆 Syntax Error 与 Runtime Error：异常处理只解决 runtime error
4. 忘记 TRY...EXCEPT 的伪代码格式

:::

---

## 题型总结

| 题型 | 分值 | 难度 | 频率 |
|------|------|------|------|
| Prolog 事实/规则/查询 | 5-6 | ⭐⭐ | 中频 |
| OOP class 设计 | 6-8 | ⭐⭐⭐ | 必考 |
| OOP 概念定义 | 4-5 | ⭐⭐ | 高频 |
| RPN 转换/求值 | 5-6 | ⭐⭐ | 高频 |
| 范式识别 | 3-4 | ⭐ | 中频 |
| File processing | 4-5 | ⭐⭐ | 高频 |
| Exception handling | 3-4 | ⭐ | 中频 |
