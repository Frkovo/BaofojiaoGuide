---
title: 常见错误
---

## 错误 1：混淆编译器与解释器

**错误表现**：
- 认为解释器生成 object code / machine code
- 认为编译器可以交互式逐行执行

**纠正**：
- **Compiler**：一次性将整个源代码翻译为 machine code，生成独立的可执行文件
- **Interpreter**：逐行读取、翻译并立即执行，不生成独立的可执行文件

## 错误 2：BNF 语法错误

**错误表现**：
- 使用 `=` 而不是 `::=`
- 混淆终结符和非终结符的写法
- 忘记非终结符要用 `<...>` 括起

**纠正**：
```
正确：<digit> ::= 0 | 1 | 2
错误：<digit> = 0 | 1 | 2
错误：digit ::= 0 | 1 | 2
```

## 错误 3：混淆编译阶段的顺序

**错误表现**：
- 将 Optimisation 放在 Code Generation 之前
- 混淆 Lexical Analysis 和 Syntax Analysis 的任务

**纠正**：
1. Lexical Analysis — tokenisation, symbol table
2. Syntax Analysis — parse tree, grammar check
3. Code Generation — machine code
4. Optimisation — 优化代码

## 错误 4：混淆分页与分段的碎片问题

**错误表现**：
- 认为 Paging 有 external fragmentation
- 认为 Segmentation 没有 fragmentation

**纠正**：
- **Paging**（固定大小）：无 external fragmentation，可能有 internal fragmentation
- **Segmentation**（可变大小）：有 external fragmentation，无 internal fragmentation

## 错误 5：调度算法描述不准确

**错误表现**：
- 混淆 SJF 和 SRT（一个非抢占一个抢占）
- 认为 Round Robin 不需要 time quantum

**纠正**：
| 算法 | 选择依据 | 抢占？ |
|------|---------|--------|
| FCFS | 到达时间顺序 | 否 |
| SJF | 最短总执行时间 | 否 |
| SRT | 最短剩余时间 | 是 |
| Round Robin | 固定时间片轮转 | 是 |

## 错误 6：认为虚拟内存和物理内存速度相同

**错误表现**：
- 忽略 virtual memory 使用磁盘而非 RAM
- 未提及 thrashing 的成因

**纠正**：Virtual memory 使用磁盘作为扩展，磁盘 I/O 比 RAM 慢得多。频繁 page swap 导致 thrashing。

## 错误 7：认为 symbol table 在 syntax analysis 创建

**错误表现**：将 symbol table 的阶段搞错。

**纠正**：Symbol table 在 lexical analysis 阶段创建，在后续阶段（syntax analysis, code generation）中被查阅和更新。
