---
title: MS 模式总结
---

## 通用模式

| 题型 | 分值 | 典型得分点 |
|------|------|------------|
| 编译阶段匹配 | 3-4 | **M1** lexical analysis tokenisation / symbol table; **A1** syntax analysis parse tree; **B1** code generation / optimisation |
| BNF 验证 | 3-4 | **M1** 正确推导; **A1** valid/invalid 判断; **A1** 解释 |
| BNF 规则书写 | 2-3 | **M1** 正确使用 `::=` 和 `|`; **A1** 递归定义 |
| 调度计算 | 5-6 | **M1** Gantt chart; **A1** 各进程等待时间; **B1** 平均值 |
| 虚拟内存 | 4-5 | **M1** 定义; **A1** paging 机制; **B1** thrashing |
| 解释器 | 2-3 | **M1** 逐行执行; **A1** 不生成 object code |
| RPN 转换 | 2-3 | **M1** 正确栈操作; **A1** 最终 RPN 表达式正确 |

## 高频得分短语

- **Lexical analysis** — "converts source code into tokens" / "removes comments and whitespace" / "creates symbol table"
- **Syntax analysis** — "checks syntax against grammar rules" / "builds parse tree / syntax tree"
- **Code generation** — "generates machine code / object code" / "uses symbol table and syntax tree"
- **Optimisation** — "improves efficiency" / "removes redundant code"
- **Virtual memory** — "uses disk space as extension of RAM" / "allows programs larger than physical memory to run"
- **Paging** — "divides memory into fixed-size blocks"
- **Segmentation** — "divides memory into variable-size blocks"
- **Thrashing** — "frequent swapping / paging" / "CPU spends most time paging"
- **Interpreter** — "translates and executes line by line" / "does not produce object code"

## 答题技巧

1. 描述题：每个独立 valid point 1 分，写 3-4 个点
2. 计算题：必须展示中间步骤（Gantt chart 或公式）
3. BNF 题：必须写出完整推导过程
4. 比较题：each correct comparison = 1 分
