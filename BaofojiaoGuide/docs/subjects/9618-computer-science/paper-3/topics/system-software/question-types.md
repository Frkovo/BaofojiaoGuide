---
title: 题型分析
---

## 1. 编译阶段（Compilation Stages）

题型：匹配编译阶段与描述、识别编译阶段、描述各阶段任务

:::note[标准解题方法]

1. 牢记四个阶段顺序：Lexical Analysis → Syntax Analysis → Code Generation → Optimisation
2. Lexical Analysis：将源代码转换为 token，移除注释和空白，创建 symbol table
3. Syntax Analysis：构建 syntax tree / parse tree，检查语法正确性
4. Code Generation：利用 syntax tree 和 symbol table 生成 object code / machine code
5. Optimisation：优化代码，移除 unreachable code，提高效率

:::

:::info[评分标准（MS 模式）]

- **M1**: 正确识别 lexical analysis 进行 tokenisation
- **A1**: 正确描述 syntax analysis 构建 parse tree
- **B1**: 正确描述 code generation 生成 object code
- 每个匹配 1 分

:::

### 示例 1：9618/w22/qp/31 Q4

> Four stages of compilation are listed.
>
> LEXICAL ANALYSIS
> SYNTAX ANALYSIS
> CODE GENERATION
> OPTIMISATION
>
> (a) State which stage of compilation:
> (i) removes items such as unreachable code from the object code
> (ii) assigns each token a label so that it can be stored in a symbol table
> (iii) checks that the grammar of the programming language is being used correctly
>
> (b) Describe what happens during the code generation stage of compilation.

<details>
<summary>📝 MS 展开查看</summary>

(a)(i) Optimisation (**M1**)
(a)(ii) Lexical analysis (**A1**)
(a)(iii) Syntax analysis (**A1**)

(b) Code generation:
- **M1**: 生成 object code / machine code
- **A1**: 使用 syntax tree / parse tree 和 symbol table
- **A2**: 将 syntax tree 转换为 machine code instructions

</details>

### 示例 2：9618/w22/qp/32 Q2

> The diagram below shows the stages involved in compiling high-level language code.
>
> Source code → Stage A → Stage B → Stage C → Object code
>
> (a) Identify the three stages A, B and C.
>
> (b) State **two** tasks that are performed during Stage A.
>
> (c) Explain **two** tasks that the linker performs before the compiled code can be executed.

<details>
<summary>📝 MS 展开查看</summary>

(a) A: Lexical analysis (**A1**)
    B: Syntax analysis (**A1**)
    C: Code generation (**A1**)

(b) Any 2:
- **M1**: 将代码转换为 token 序列（converts source code into tokens）
- **M1**: 移除注释和空白（removes comments and whitespace）
- **M1**: 创建 symbol table（creates symbol table）

(c) Linker 任务（any 2）:
- **A1**: 将多个 object code 文件合并
- **A1**: 将 library code 链接到程序中
- **B1**: 解析外部引用（resolve external references）

</details>

---

## 2. BNF 与语法图（BNF and Syntax Diagrams）

题型：判断字符串是否有效、补全 BNF 规则、根据规则绘制语法图

:::note[标准解题方法]

1. 从起始非终结符开始推导
2. 逐步替换每个非终结符，直到全部变为终结符
3. 检查每一步是否符合 BNF 规则中的定义
4. 语法图：矩形代表非终结符，圆形代表终结符

:::

:::info[评分标准（MS 模式）]

- **M1**: 正确识别起始非终结符
- **A1**: 每一步推导过程正确
- **B1**: 语法图的形状使用正确（矩形、圆形）

:::

### 示例 1：9618/s23/qp/31 Q6

> A system uses the following BNF rules to validate passwords:
>
> `<password> ::= <letter><digit><letter><digit>`
> `<letter> ::= A | B | C`
> `<digit> ::= 1 | 2 | 3`
>
> (a) Determine whether the following are valid passwords. Explain your answer.
> (i) A1B2
> (ii) AB12
> (iii) 1A2B
>
> (b) Rewrite the BNF rule for `<password>` so that `<letter>` and `<digit>` can appear in any order.

<details>
<summary>📝 MS 展开查看</summary>

(a)(i) Valid. A1B2 matches `<letter><digit><letter><digit>` pattern exactly. (**M1**)
(a)(ii) Invalid. AB are two letters followed by 12 which are two digits; does not match `<letter><digit><letter><digit>`. (**A1**)
(a)(iii) Invalid. Starts with digit, but BNF requires first character to be `<letter>`. (**A1**)

(b) `<password> ::= <letter><digit><letter><digit> | <letter><letter><digit><digit> | <digit><letter><digit><letter> | <digit><letter><letter><digit>` (**B1** for any correct combination covering all orders)

</details>

### 示例 2：9618/s23/qp/32 Q3

> A vehicle registration system uses BNF:
>
> `<registration> ::= <year><letter><digit><digit><digit>`
> `<year> ::= A | B | C`
> `<letter> ::= X | Y | Z`
> `<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9`
>
> (a) Determine validity:
> (i) AX123
> (ii) B2Y34
> (iii) CX000
>
> (b) Draw a syntax diagram for `<registration>`.

<details>
<summary>📝 MS 展开查看</summary>

(a)(i) Valid. A 为 `<year>`, X 为 `<letter>`, 1,2,3 为 `<digit>`. Pattern matches. (**M1**)
(a)(ii) Invalid. B 为 `<year>`, 2 is not in `<letter>` definition. (**A1**)
(a)(iii) Valid. C 为 `<year>`, X 为 `<letter>`, 000 为 `<digit><digit><digit>`. (**A1**)

(b) Syntax diagram:
- **B1**: 包含四个串联部分：`<year>` → `<letter>` → `<digit>` → `<digit>` → `<digit>`
- **B1**: 矩形框用于非终结符，圆形用于终结符
- **B1**: 箭头方向从左到右

</details>

---

## 3. 进程管理与调度（Process Management / Scheduling）

题型：描述调度算法、绘制甘特图、计算平均等待时间、比较调度策略

:::note[标准解题方法]

1. 确定调度算法类型
2. FCFS：按到达时间顺序执行
3. SJF：选择 CPU burst 时间最短的进程
4. SRT：选择剩余时间最短的进程（抢占式）
5. Round Robin：每个进程分配固定 time quantum，轮流执行
6. 绘制 Gantt chart 辅助计算等待时间
7. 等待时间 = 开始执行时间 - 到达时间

:::

:::info[评分标准（MS 模式）]

- **M1**: 正确描述调度算法工作原理
- **A1**: 给出正确的 Gantt chart 或执行顺序
- **B1**: 正确计算平均等待时间

:::

### 示例 1：9618/w22/qp/32 Q9

> A multiprogramming operating system uses Round Robin scheduling. Three processes P1, P2, P3:
>
> | Process | CPU burst / ms | Arrival time / ms |
> |---------|----------------|-------------------|
> | P1 | 5 | 0 |
> | P2 | 3 | 1 |
> | P3 | 8 | 2 |
>
> Time quantum = 2 ms.
>
> (a) Draw a Gantt chart showing the execution order.
>
> (b) Calculate the average waiting time.

<details>
<summary>📝 MS 展开查看</summary>

(a) Gantt chart:
- **M1**: P1 (0-2) → P2 (2-4) → P1 (4-5) → P3 (5-7) → P2 (7-8) → P3 (8-10) → P1 (10-11) → P3 (11-15)

(b) Waiting times:
- **A1**: P1 waiting = 2 + 1 + 5 = 8 ms
- **A1**: P2 waiting = 1 + 4 = 5 ms
- **A1**: P3 waiting = 3 + 1 + 1 = 5 ms
- **B1**: Average = (8 + 5 + 5) / 3 = 6 ms

</details>

### 示例 2：9618/s21/qp/32 Q8

> An OS uses preemptive priority scheduling (1 = highest priority):
>
> | Process | Burst / ms | Priority |
> |---------|------------|----------|
> | P1 | 4 | 2 |
> | P2 | 6 | 1 |
> | P3 | 3 | 3 |
>
> All arrive at time 0.
>
> (a) Explain the execution order.
>
> (b) Calculate the average waiting time.

<details>
<summary>📝 MS 展开查看</summary>

(a) Execution:
- **M1**: P2 runs first (highest priority), from 0-6
- **A1**: P1 runs next (priority 2), from 6-10
- **A1**: P3 runs last (priority 3), from 10-13

(b) Waiting times:
- **A1**: P1 = 6 ms, P2 = 0 ms, P3 = 10 ms
- **B1**: Average = (6 + 0 + 10) / 3 = 5.33 ms

</details>

---

## 4. 虚拟内存与分页（Virtual Memory and Paging）

题型：解释虚拟内存的工作原理、区分 paging 和 segmentation、解释 thrashing

:::note[标准解题方法]

1. 虚拟内存使用磁盘空间模拟 RAM，允许执行大于物理内存的程序
2. Paging：内存分为固定大小的 page 和 page frame
3. MMU 负责虚拟地址到物理地址的转换
4. Page table 维护映射关系
5. Thrashing：频繁的 page swap 导致系统性能骤降

:::

:::info[评分标准（MS 模式）]

- **M1**: 解释虚拟内存和物理内存的区别
- **A1**: 描述 paging 机制（page, page frame, page table）
- **B1**: 区分 paging 和 segmentation
- **B2**: 解释 thrashing 的成因和后果

:::

### 示例 1：9618/w23/qp/32 Q5

> An OS uses virtual memory with paging. Page size = 4 KB. A program requires 12 KB, physical memory = 8 KB.
>
> (a) Explain what is meant by virtual memory.
>
> (b) Explain how the program can still execute despite requiring more memory than available.
>
> (c) State what is meant by disk thrashing.

<details>
<summary>📝 MS 展开查看</summary>

(a) Virtual memory:
- **M1**: 一种内存管理技术，使用硬盘空间扩展 RAM
- **A1**: 允许执行比物理内存更大的程序
- **A1**: 程序的部分内容存储在磁盘上，按需加载到 RAM

(b) Program execution:
- **M1**: 程序分为 3 个 page（12 KB / 4 KB）
- **A1**: 只有 2 个 page 同时在物理内存中
- **B1**: 需要 page 3 时，将 page 1 换出到磁盘，加载 page 3

(c) Disk thrashing:
- **B1**: 频繁在 RAM 和磁盘之间交换 page
- **B2**: CPU 大部分时间用于 paging，导致 throughput 急剧下降

</details>

### 示例 2：9618/w22/qp/31 Q8

> (a) Distinguish between paging and segmentation.
>
> (b) Physical memory = 16 MB, page size = 4 KB. A process requires 20 MB.
> (i) Calculate the number of pages required.
> (ii) Explain how the OS manages pages during execution.

<details>
<summary>📝 MS 展开查看</summary>

(a) Paging vs Segmentation:
- **M1**: Paging 固定大小 block；Segmentation 可变大小 block
- **A1**: Paging 无 external fragmentation；Segmentation 有 external fragmentation
- **A1**: Paging 对程序员透明；Segmentation 对程序员可见

(b)(i) Pages = 20 MB / 4 KB = 20 × 1024 / 4 = 5120 pages (**A1**)

(b)(ii) Page management:
- **M1**: 使用 page table 映射 virtual page 到 physical page frame
- **A1**: 仅部分 page 在物理内存，其余在磁盘
- **B1**: 需要不在内存的 page 时触发 page fault，OS 加载所需 page

</details>

---

## 5. 解释器执行（Interpreter Execution）

题型：解释解释器如何执行源代码、比较解释器和编译器的优缺点

:::note[标准解题方法]

1. 解释器逐行读取源代码
2. 对每行进行词法分析、语法分析
3. 立即翻译并执行该行代码
4. 每执行一次都需要重新解释
5. 不生成 object code

:::

:::info[评分标准（MS 模式）]

- **M1**: 指出逐行翻译和执行（line by line）
- **A1**: 不生成 object code
- **B1**: 每次运行需重新解释

:::

### 示例 1：9618/s21/qp/31 Q3(b)

> An interpreter translates and executes high-level code.
>
> (b) Explain how an interpreter translates and executes code without the need for a complete compilation stage.

<details>
<summary>📝 MS 展开查看</summary>

- **M1**: 逐行读取源代码（reads source code line by line）
- **A1**: 对每一行进行词法分析、语法分析、翻译并立即执行（analyse, translate and execute each line）
- **A2**: 不生成完整的 object code 文件
- **B1**: 遇到错误立即停止，后续代码不会被执行

</details>

### 示例 2：9618/s23/qp/32 Q1(c)

> A student uses an interpreter to execute a program. Describe **two** advantages of using an interpreter instead of a compiler when developing a program.

<details>
<summary>📝 MS 展开查看</summary>

Advantages (any 2):
- **M1**: 可以立即执行代码，无需等待完整编译完成
- **A1**: 错误更容易定位（stops at the line with the error）
- **B1**: 便于调试（easier to debug），可以检查变量状态
- **B1**: 适合快速原型开发（rapid prototyping）

</details>

---

:::warning[常见陷阱]

- 混淆 lexical analysis（tokenisation）和 syntax analysis（parse tree）的任务
- BNF 规则中错误使用 `=` 代替 `::=`
- 进程调度计算中忽略到达时间（arrival time）
- 认为 paging 产生 external fragmentation 而 segmentation 不产生
- 认为 interpreter 生成 object code 或 machine code
- 混淆 SJF（非抢占）和 SRT（抢占式）
- 认为 symbol table 在 syntax analysis 阶段创建

:::
