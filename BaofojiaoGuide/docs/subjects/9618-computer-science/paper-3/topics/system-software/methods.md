---
title: 解题方法
---

## 1. 操作系统概念题

**方法步骤**：
1. 确定题目考查的具体 OS 功能（进程管理、内存管理、文件管理等）
2. 对于调度问题：先识别调度算法类型（FCFS / SJF / SRT / Round Robin）
3. 画出甘特图（Gantt chart）辅助计算等待时间
4. 注意区分抢占式（preemptive）和非抢占式（non-preemptive）调度
5. 涉及虚拟内存时：讲清楚 page / page frame / page table / MMU 的关系

## 2. 编译阶段说明题

**方法步骤**：
1. 牢记四个阶段的顺序：Lexical Analysis → Syntax Analysis → Code Generation → Optimisation
2. Lexical Analysis 阶段：将源代码转换为 token，移除注释和空白，创建 symbol table
3. Syntax Analysis 阶段：根据语法规则检查 token 序列，构建 parse tree / syntax tree
4. Code Generation 阶段：使用 syntax tree 和 symbol table 生成 machine code / object code
5. Optimisation 阶段：优化生成代码的效率，移除 unreachable code

## 3. BNF 规则书写

**方法步骤**：
1. 使用 `::=` 表示"定义为"
2. 使用 `|` 表示"或"
3. 非终结符用 `<...>` 括起（如 `<digit>`、`<letter>`）
4. 终结符（terminal）直接写具体字符或加引号
5. 递归定义处理重复模式
6. 写完后用有效/无效示例验证

**示例模板**：
```
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<letter> ::= A | B | C | ... | Z
<identifier> ::= <letter> | <identifier><letter> | <identifier><digit>
```

## 4. 语法图绘制

**方法步骤**：
1. 每个非终结符对应一个独立的语法图
2. 矩形框（或圆角矩形）代表非终结符，框内写非终结符名称
3. 圆形框代表终结符，框内写具体字符
4. 箭头表示可能的执行路径，从左向右
5. 分支用分叉路径表示（对应 `|`）
6. 循环回路表示重复（对应递归）

**绘图规则**：
```
非终结符: [  <name>  ]
终结符  : (  'c'  )
```
