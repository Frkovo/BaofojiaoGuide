---
title: 常见错误
---

# 常见错误

## 错误 1：Prolog 语法错误

**错误表现**：
- 常量首字母大写：`Likes(John, Apple).`
- 变量首字母小写：`likes(john, x).`
- 忘记末尾句点：`likes(john, apple)`
- Rule 中用 `:` 而不是 `:-`

**正确做法**：
- 常量小写：`likes(john, apple).`
- 变量大写：`likes(john, X).`
- 句点结尾：`likes(john, apple).`
- 规则：`happy(X) :- likes(X, apple).`

---

## 错误 2：混淆 Class 和 Object

**错误表现**：在伪代码中将 class 当作 object 使用，如直接调用 `Car.drive()` 但未先创建实例。

**正确做法**：
- Class = 模板/蓝图（declaration）
- Object = 实例（`myCar ← NEW Car(...)`）
- 方法应该通过实例调用：`myCar.drive()`

---

## 错误 3：OOP 中忘记 Constructor（NEW）

**错误表现**：写了一个 class 但没有写 constructor（构造方法），导致属性无法初始化。

**正确做法**：每个 class 都应该有 `PUBLIC PROCEDURE NEW(...)`。

---

## 错误 4：Inheritance 中未调用父类构造

**错误表现**：子类的 constructor 中没有调用父类的 constructor。

**正确做法**：
```
PUBLIC PROCEDURE NEW(...)
    CALL SuperClass::NEW(...)
    // 子类的其他初始化
ENDPROCEDURE
```

---

## 错误 5：RPN 中减法和除法的操作数顺序错误

**错误表现**：计算 `a b -` 时计算为 `b - a`（而非 `a - b`）。

**正确做法**：
- `a b -` → a - b ← 先弹出的是 b（右操作数），后弹出的是 a（左操作数）
- `a b /` → a ÷ b

```
POP b    // second operand (right)
POP a    // first operand (left)
result ← a - b   // NOT b - a
PUSH result
```

---

## 错误 6：Infix → RPN 转换错误

**错误表现**：转换时操作数的顺序变了，或忽略了运算符优先级。

**正确做法**：操作数顺序不变（与 infix 一致），只移动运算符到操作数之后。

---

## 错误 7：File Processing 模态混淆

**错误表现**：
- 用 `"w"`（覆盖写入）当想追加内容
- 用 `"r"` 当想写入
- 忘记指定模式

**正确做法**：
- 读取 → `"r"`
- 写入（覆盖）→ `"w"`
- 追加 → `"a"`

---

## 错误 8：忘记 CLOSEFILE

**错误表现**：文件操作完成后没有关闭文件。

**正确做法**：每个 OPENFILE 都应该有对应的 CLOSEFILE。

---

## 错误 9：Exception Handling 中使用错误异常类型

**错误表现**：描述了一个异常（如 division by zero）但写成了 syntax error 之类的非 runtime error。

**正确做法**：Exception 只处理 runtime errors，不是 syntax errors。

---

## 错误 10：混淆 WITH 和 RPN

**错误表现**：不知道两者之间的关系，或者认为 RPN 是另一种编程语言。

**正确做法**：RPN 是表达式的表示法（postfix notation），不是编程语言。可以用栈实现求值。

---

## 错误 11：编程范式识别错误

**错误表现**：看到 loops 就认为是 OOP，或者看到 variables 就认为是 declarative。

**正确做法**：

| 代码特征 | 范式 |
|----------|------|
| CLASS, NEW, method | OOP |
| facts, rules, `?-` | Declarative |
| registers, MOV, ADD | Low-level |
| FOR, WHILE, IF, `←` | Imperative |

---

## 错误 12：OOP 概念定义混淆

**错误表现**：将 Polymorphism 解释为 Inheritance，或将 Encapsulation 解释为 Abstraction。

**正确做法**：
- **Encapsulation** = bundling data + methods, hiding data (PRIVATE)
- **Inheritance** = subclass 继承 superclass
- **Polymorphism** = 同一方法名，不同实现
- **Abstraction** = 隐藏实现细节，只暴露接口
