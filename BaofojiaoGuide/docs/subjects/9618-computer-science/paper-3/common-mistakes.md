---
title: 常见错误
sidebar_position: 9
---

# 常见错误分析

## 浮点数（Floating Point）

### 1. ❌ 没有标准化尾数

:::danger[致命错误]
Floating point 题目中忘记 normalize mantissa，直接丢失 2-3 步骤分。
:::

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| `mantissa = 0.00101, exponent = 3` 直接写 value | 左移 2 位：`mantissa = 0.101, exponent = 1` |
| 负 mantissa `1.1101` 不 shift | `1.1101` → 右移 1 位：`1.11101`（补码右移填 1），exponent +1 |

**规则：** 正数 mantissa 以 `0.1` 开头，负数（two's complement）mantissa 以 `1.0` 开头

### 2. ❌ Two's complement 负 mantissa 值计算错误

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| `1.0110` 当普通二进制：`-(0.375)` | 先取反加一：`0.1001 + 0.0001 = 0.1010 = +0.625`，原值 `-0.625` |
| `1.0000` 看成 `-0` | `1.0000` 是 two's complement 最小值 = `-1.0`（8-bit 为例 `1.0000000 = -1`） |

**记忆：** MSB=1 → 负数 → 取反加一得绝对值

### 3. ❌ 指数 bias 计算错误

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| exponent `101` = 5，直接当指数 5 | excess-4 时 actual = 5 - 4 = 1 |
| 不知道 bias 值 | bias = 2^(k-1) - 1（k 为 exponent 位数），3-bit → bias = 3 |
| exponent 全 1 当正常值 | 全 1 表示 infinity/NaN（特殊值） |

### 4. ❌ 忽略浮点数精度限制

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| 说 0.1 可以用 binary 精确表示 | decimal 0.1 在 binary 中无限循环，mantissa 有限位→近似值 |
| 计算时不考虑 rounding error | 明确写 "limited mantissa bits cause approximation" |

## 布尔代数（Boolean Algebra）

### 5. ❌ 忘记 De Morgan's 定律

:::danger[致命错误]
De Morgan's 应用错误导致整个表达式化简全错。
:::

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| `¬(A ∧ B) = ¬A ∧ ¬B` | `¬(A ∧ B) = ¬A ∨ ¬B` |
| `¬(A ∨ B) = ¬A ∨ ¬B` | `¬(A ∨ B) = ¬A ∧ ¬B` |
| 只加横线不翻转运算符 | 运算符也要 AND ↔ OR 互换 |

**口诀：** "break the line, change the sign" — 长横变短横，AND/OR 互换，变量各自取反

### 6. ❌ K-map 分组不规则（Improper Grouping）

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| 圈了 3 个 / 5 个 1 | 只能圈 1, 2, 4, 8, 16 个（powers of 2） |
| 只圈单个 1 不合并 | 尽可能圈最大的矩形 |
| 忽略 K-map wrapping | 最上和最下行相邻，最左和最右列相邻 |
| group 中包含不同取值变量 | group 内每个变量必须取值相同（全 0 或全 1） |

### 7. ❌ 布尔代数恒等式混淆

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| `A + A = 2A`（代入普通代数） | `A + A = A` |
| `A · A = A²` | `A · A = A` |
| `A + 1 = A` | `A + 1 = 1` |
| `A · 0 = A` | `A · 0 = 0` |
| NAND = `¬A ∧ ¬B` | NAND = `¬(A ∧ B)` |
| NOR = `¬A ∨ ¬B` | NOR = `¬(A ∨ B)` |

## 逆波兰表达式（RPN）

### 8. ❌ 中缀转后缀优先级处理错误

:::danger[致命错误]
忽略 operator precedence 导致 conversion 错误。
:::

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| `3 + 4 × 2` → `3 4 + 2 ×`（先处理 +）| `3 + 4 × 2` → `3 4 2 × +` |
| 计算：`(3+4)×2 = 14` ❌ | 计算：`3 + (4×2) = 11` ✅ |
| 不等当前 stack top priority 直接 push | 当前 op ≤ stack top → pop top 到 output，再 push 当前 op |

### 9. ❌ RPN 求值操作数顺序颠倒

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| `5 3 -`: pop a=3, pop b=5, compute `a - b = 3 - 5 = -2` |  compute `b - a = 5 - 3 = 2` ✅ |
| `6 2 /`: pop a=2, pop b=6, compute `a / b = 2 / 6 = 0.33` | compute `b / a = 6 / 2 = 3` ✅ |

**关键：** pop a（先出栈=right operand），pop b（后出栈=left operand），result = `b op a`

### 10. ❌ RPN 转换中括号处理错误

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| 遇到 `(` 直接 push 不管 | `(` → push to stack，作为左括号标记 |
| 遇到 `)` 不管 | `)` → pop stack 到 output 直到遇到 `(`，然后丢弃 `(` |
| 忘记左括号出栈后要丢弃 | 弹出 `(` 后直接丢弃，不写入 output |

## 伪代码（Pseudocode）

### 11. ❌ 缺少 ENDxxx 闭合语句

:::danger[致命错误]
CIE 伪代码每个控制结构必须显式闭合，漏写直接扣分。
:::

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| `IF…THEN…ELSE…` 没有 ENDIF | `IF … THEN … ELSE … ENDIF` |
| `WHILE…DO…` 没有 ENDWHILE | `WHILE … DO … ENDWHILE` |
| `REPEAT…UNTIL` 缺失 | （REPEAT-UNTIL 自带闭合，不需要额外关键字） |
| `FOR…TO…` 没有 NEXT | `FOR … TO … NEXT` |
| `TYPE…` 没有 ENDTYPE | `TYPE … ENDTYPE` |
| `CASE…OF…` 没有 ENDCASE | `CASE … OF … ENDCASE` |

### 12. ❌ PROCEDURE 与 FUNCTION 混淆

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| FUNCTION 不写 RETURN | FUNCTION 必须有 `RETURN value` |
| PROCEDURE 写 RETURN | PROCEDURE 不应返回值（可用输出参数） |
| 调用 FUNCTION 用 CALL | FUNCTION 用于表达式：`result ← MyFunc(x)` |
| 调用 PROCEDURE 不用 CALL | PROCEDURE：`CALL MyProc(x)` |

### 13. ❌ 数组索引从 0 开始

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| `DECLARE arr : ARRAY[0:9] OF INTEGER` | `DECLARE arr : ARRAY[1:10] OF INTEGER` |
| `FOR i ← 0 TO 9` 循环数组 | `FOR i ← 1 TO 10` 循环数组 |

CIE 伪代码默认下标从 1 开始，除非题目明确指定。

### 14. ❌ 赋值用 = 而非 ←

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| `x = x + 1` | `x ← x + 1` |
| `total = total + i` | `total ← total + i` |
| `IF x = 5 THEN`（比较用 = 可以） | 赋值用 ←，比较用 = |

## 面向对象编程（OOP）

### 15. ❌ 混淆 Class 和 Object

:::danger[致命错误]
最常⻅的概念性错误 — class 和 object 的定义搞反。
:::

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| "Object is the template for class" | "Class is the template / blueprint for objects" |
| "Class is an instance of Object" | "Object is an instance of Class" |
| "Class occupies memory" | "Object occupies memory at runtime; Class is a definition" |

### 16. ❌ 封装（Encapsulation）理解不完整

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| "Encapsulation = grouping data together" | "Binding data and methods together, with data hiding via private access" |
| 只提到 grouping 没提到 information hiding | 关键词：private fields + public methods + hide implementation details |
| 认为 OOP 语言天然有封装 | 需手动声明 private/public 访问修饰符 |

### 17. ❌ 继承方向错误

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| "Parent class inherits from child" | "Child class (subclass) inherits from parent class (superclass)" |
| "Subclass has fewer features" | "Subclass extends — has all parent features + additional ones" |
| "Inheritance copies parent attributes to child" | "Child class inherits interface/behaviour, can override methods" |

## 声明式编程（Declarative Programming）

### 18. ❌ 事实与规则语法错误

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| `hasFur(Dog)`（无句点） | `hasFur(dog).`（句点结尾，常量小写） |
| `likes(john, X) :- likes(X, john)`（无句点） | `likes(john, X) :- likes(X, john).` |
| 规则用 AND / OR 关键字 | Prolog 中用 `,` 表示 AND，`;` 表示 OR |
| `LIKES(john, X)`（全大写） | `likes(john, X)`（谓词小写） |

### 19. ❌ 查询中变量大小写错误

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| `?- ancestor(john, mary).`（找特定关系，返回 yes/no） | `?- ancestor(john, X).`（找所有 descendant，X 被绑定到每个实例） |
| 变量用小写开头：`?- likes(john, X).`（X 是大写 ✅） | 变量必须大写或 `_` 开头，常量小写 |
| 匿名变量用 X 但不用 | 不需要名字的变量用 `_`：`?- likes(john, _).` |

## 二分查找（Binary Search）

### 20. ❌ 忘记数组必须有序

:::danger[致命错误]
Binary search 最基本的 precondition — 数组必须先排序。
:::

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| 对 `[5, 3, 8, 1, 9]` 直接 binary search | 先排序为 `[1, 3, 5, 8, 9]` 再 binary search |
| "Binary search works on any array" | "Array must be sorted in ascending order" |
| "Binary search is faster than linear search" | 需说明 "on sorted arrays binary search is O(log n) vs O(n)" |

### 21. ❌ 中间索引更新错误

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| `mid = (low + high) / 2`（可能产生小数） | `mid ← (low + high) DIV 2`（整数除法） |
| `low ← mid`（没有 +1）→ 死循环 | `low ← mid + 1` |
| `high ← mid`（没有 -1）→ 死循环 | `high ← mid - 1` |
| 不更新 low/high → 无限循环 | 每轮更新 low 或 high，直到 low > high |

## 文件操作（File Handling）

### 22. ❌ 文件打开模式错误

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| 读取时没写 READ | `OpenFile(myFile, "data.txt", READ)` |
| 覆盖写用了 APPEND | `OpenFile(myFile, "data.txt", WRITE)` 或 `APPEND` 取决于意图 |
| 追加上次内容用了 WRITE | `OpenFile(myFile, "data.txt", APPEND)` |

### 23. ❌ 文件未关闭

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| 操作后忘记 CloseFile | `CloseFile(myFile)` — 释放资源，确保缓冲区数据写入 |
| 只关了一部分打开的文件 | 每个 OpenFile 对应一个 CloseFile |
| 认为程序结束自动关闭就够 | 显式 CloseFile 是 good practice，mark scheme 会检查 |

## 其他常⻅错误

### 24. ❌ Trace Table 填写不完整

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| 只写变量最终值 | 每轮循环记录所有变量的变化，包括条件判断结果 |
| 跳过初始值行 | 第一行写变量声明后的初始状态 |
| 一行写多个变化不清晰 | 每个值变化就换行，一行一个状态 |

### 25. ❌ 逻辑门电路符号混淆

| Wrong ❌ | Correct ✅ |
|---------|-----------|
| NAND gate 画成 AND gate 再在输入加 bubble | NAND = AND + output bubble |
| NOR gate 画成 OR + input bubbles | NOR = OR + output bubble |
| XOR gate 当成 OR | XOR = A ⊕ B = (A ∧ ¬B) ∨ (¬A ∧ B) |
