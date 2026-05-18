---
title: 评分标准模式
---

# 评分标准模式（MS Pattern）

## 通用评分模式

### Prolog 题

| 分类 | 常见 MS 表述 | 分值 |
|------|-------------|------|
| **M1** | Correct syntax for facts / rules | 1 |
| **M2** | Use of `:-` for rules | 1 |
| **A1** | Use of uppercase variables | 1 |
| **A2** | Query produces correct binding | 1 |
| **B1** | Understanding of backward chaining | 1 |

### OOP 设计题

| 分类 | 常见 MS 表述 | 分值 |
|------|-------------|------|
| **M1** | CLASS...ENDCLASS structure | 1 |
| **M2** | PRIVATE attribute declarations | 1 |
| **A1** | Constructor (NEW) initialises attributes | 1 |
| **A2** | Getter/Setter methods | 1 |
| **B1** | Inheritance with EXTENDS | 1 |

### RPN 题

| 分类 | 常见 MS 表述 | 分值 |
|------|-------------|------|
| **M1** | Correct stack operations | 1 |
| **M2** | Correct RPN expression | 1 |
| **A1** | Correct operand order for - and / | 1 |
| **A2** | Final result correct | 1 |
| **B1** | Understanding that RPN uses no brackets | 1 |

### File Processing 题

| 分类 | 常见 MS 表述 | 分值 |
|------|-------------|------|
| **M1** | OPENFILE with correct mode | 1 |
| **M2** | WHILE NOT EOF loop | 1 |
| **A1** | READFILE / WRITEFILE used correctly | 1 |
| **B1** | CLOSEFILE at end | 1 |

### Exception Handling 题

| 分类 | 常见 MS 表述 | 分值 |
|------|-------------|------|
| **M1** | TRY...EXCEPT structure | 1 |
| **M2** | Example of runtime error | 1 |
| **A1** | Explanation of preventing crash | 1 |
| **B1** | Graceful error recovery | 1 |

## 关键词与指令词

| 指令词 | 要求 |
|--------|------|
| **Write** | 写出完整代码/伪代码 |
| **Define** | 给出概念的定义 |
| **Explain** | 解释原理/机制 |
| **Convert** | 转换格式（Infix ↔ RPN） |
| **Evaluate** | 使用栈求值 |
| **Identify** | 识别范式/类型 |
| **Describe** | 描述特征（2-3 点） |
| **Justify** | 给出证据支撑 |

## 常见 Follow-through

- RPN 题：如果转换错了 RPN，但栈求值过程正确，可得分（方法分）
- OOP 题：如果某属性的类型错了，但 getter/setter 的逻辑正确，可得方法分
- Prolog 题：如果查询的变量名写错了（但仍是大写），正确的推理过程可得方法分

## 典型扣分点

| 错误 | 扣分 |
|------|------|
| Prolog fact 末尾无句点 | 1 |
| OOP class 中属性未声明 PRIVATE | 1 |
| RPN 中减/除操作数顺序颠倒 | 1-2 |
| File 操作忘记 CLOSEFILE | 1 |
| 伪代码中未声明变量 | 1 |
| Exception handling 无实际处理代码 | 1 |
