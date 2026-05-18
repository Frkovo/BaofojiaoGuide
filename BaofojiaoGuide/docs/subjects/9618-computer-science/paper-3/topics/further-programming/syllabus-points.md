---
title: 教学大纲要点
---

# Section 20: Further Programming

## 20.1 Programming Paradigms

### Low-level Programming
- 直接操作硬件和内存
- 使用 machine code 或 assembly language
- 寄存器（registers）直接操作
- 缺乏抽象，容易出错

### Imperative Programming
- 程序由一系列语句组成
- 使用变量、循环、条件分支控制执行流程
- 程序员指定每一步 HOW to do
- 代表语言：Pascal, C, BASIC

### Object-Oriented Programming（OOP）
- 基于类和对象
- 三大特征：Encapsulation（封装），Inheritance（继承），Polymorphism（多态）
- class = template / blueprint
- object = instance of a class
- 通过 methods 操作 attributes

### Declarative Programming
- 程序员描述 WHAT to achieve（而非 HOW）
- 使用 facts（事实）和 rules（规则）
- Prolog 是最典型的例子
- 使用 logic inference 进行查询

## 20.2 File Processing

### 文件操作

| 操作 | 伪代码 | 说明 |
|------|--------|------|
| 打开文件 | `handle ← OPENFILE("name")` | 默认读模式 |
| 打开文件（指定模式） | `handle ← OPENFILE("name", "r/w/a")` | r=读，w=写，a=追加 |
| 读取一行 | `line ← READFILE(handle)` | 读取当前行 |
| 写入一行 | `WRITEFILE(handle, text)` | 写入文本 |
| 检测文件结尾 | `EOF(handle)` | 到达结尾返回 TRUE |
| 关闭文件 | `CLOSEFILE(handle)` | 必须关闭 |

### 文件处理范例
```
handle ← OPENFILE("data.txt", "r")
WHILE NOT EOF(handle) DO
    line ← READFILE(handle)
    PROCESS(line)
ENDWHILE
CLOSEFILE(handle)
```

## 20.3 Exception Handling

- 处理 runtime errors
- 使用 TRY...EXCEPT...ENDTRY 结构
- 防止程序崩溃
- 常见异常类型：
  - Division by zero
  - Index out of range
  - File not found
  - Type mismatch
  - Null pointer dereference

## 20.4 RPN（Reverse Polish Notation）

- 一种无歧义的表达式表示法（不需括号）
- 运算符在操作数之后（postfix notation）
- 使用栈进行求值
- 中缀示例：`(3 + 4) × 5` → RPN：`3 4 + 5 ×`

### Infix ↔ RPN 转换规则
- 操作数顺序不变
- 运算符根据优先级决定输出时机
- 括号改变优先级
