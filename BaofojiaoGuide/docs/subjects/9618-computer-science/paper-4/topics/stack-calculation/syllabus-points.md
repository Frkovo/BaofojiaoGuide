---
title: "考纲要点"
---

# 考纲要点

---

## 9618 考纲相关条目

Paper 4 Practical 中涉及 stack calculation 的考纲内容包括：

### 4.2.1 — Abstract Data Types

- 理解栈（stack）的 **LIFO**（Last In, First Out）特性
- 栈的基本操作：`PUSH`、`POP`、`PEEK`（或 `TOP`）、`isEmpty`
- 使用栈实现表达式的求值（expression evaluation）

### 4.2.2 — Recursion

- 栈在递归调用中的隐式使用（系统栈）
- stack overflow 的原因

### 4.3.1 — Algorithm Design

- 使用栈作为中间数据结构来暂存运算数和运算符
- trace table 的填写

---

## 核心知识清单

### 栈操作

| 操作      | 说明               |
|-----------|--------------------|
| `PUSH(s, v)` | 将 `v` 压入栈 `s` |
| `POP(s)`   | 从栈 `s` 弹出顶部元素 |
| `isEmpty(s)` | 判断栈是否为空 |

### 栈计算规则

1. **初始化**：弹出第一个值作为 `total`
2. **循环**：弹出运算符 → 弹出操作数 → 运算
3. **终止**：栈为空时停止

### 伪代码模板

```
total ← POP(stack)
WHILE stack NOT EMPTY
    op ← POP(stack)
    val ← POP(stack)
    IF op = "+" THEN
        total ← total + val
    ELSE IF op = "-" THEN
        total ← total - val
    ELSE IF op = "*" THEN
        total ← total * val
    ELSE IF op = "/" THEN
        total ← total / val
    ENDIF
ENDWHILE
OUTPUT total
```

---

## 常见考试组合

- Paper 4 Q1 通常考查栈的**手动模拟**
- 也可能结合**面向对象编程**，要求实现 `Stack` 类（`PUSH`, `POP`, `display`）
- 还可能结合**文件操作**：从文本文件读取表达式，用栈求值

---

## 相关页面

- [题型分析](question-types.md)
- [解题方法](methods.md)
- [考前速记](last-minute-summary.md)
