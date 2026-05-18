---
title: 知识点总结
---

## OS 的目的（Purposes of an Operating System）

- **Memory Management**: 分配和回收内存，虚拟内存映射
- **File Management**: 文件系统组织、权限控制、目录管理
- **Security**: 用户认证、访问控制、防止非法访问
- **Hardware Management**: 驱动 I/O 设备、中断处理、DMA
- **Process Management**: 进程调度、同步、死锁处理

## Process Management（进程管理）

### 进程状态（Process States）

- **Running**: CPU 正在执行该进程
- **Ready**: 进程就绪，等待 CPU 分配
- **Blocked**: 进程因等待 I/O 或资源而暂停

进程状态转换：Running ↔ Ready；Running → Blocked；Blocked → Ready

### 调度算法（Scheduling Algorithms）

| 算法 | 全称 | 策略 |
|------|------|------|
| **FCFS** | First Come First Served | 先到先服务，非抢占式 |
| **SJF** | Shortest Job First | 最短作业优先，非抢占式 |
| **SRT** | Shortest Remaining Time | 最短剩余时间优先，抢占式 |
| **Round Robin** | 时间片轮转 | 每个进程分配固定时间片，抢占式 |

:::tip[Round Robin]
时间片大小至关重要：太短 → 频繁切换（上下文切换开销大）；太长 → 响应变慢
:::

## Virtual Memory（虚拟内存）

- 将物理内存扩展到磁盘（swap file/page file）
- 使程序可使用超过物理内存的地址空间
- 通过 **MMU** (Memory Management Unit) 实现虚拟地址 → 物理地址的映射

### Paging（分页）vs Segmentation（分段）

| 特性 | Paging | Segmentation |
|------|--------|--------------|
| 划分方式 | 固定大小页（4KB） | 可变大小段（逻辑划分） |
| 外部碎片 | 无 | 有 |
| 内部碎片 | 有（最后一页不完整） | 无 |
| 逻辑视角 | 线性地址空间 | 代码段/数据段/堆栈段 |
| 地址组成 | 页号 + 页内偏移 | 段号 + 段内偏移 |

### Page Replacement 页面置换算法

- **FIFO**: 替换最早调入的页（可能有 Belady 异常）
- **LRU** (Least Recently Used): 替换最久未使用的页
- **Optimal**: 替换未来最晚使用的页（理论最优，不可实现）

### Disk Thrashing（磁盘抖动）

- 系统频繁在内存和磁盘之间换页，CPU 大部时间花在换页而非执行
- **原因**: 物理内存不足、多道程序度过高
- **解决**: 增加内存、减少运行进程数、优化页面置换算法

## Translation Software（翻译软件）

| 类型 | 输入 | 输出 | 说明 |
|------|------|------|------|
| **Assembler** | 汇编语言 | 机器码 | 1:1 翻译，逐条转换 |
| **Compiler** | 高级语言 | 目标代码/机器码 | 整体翻译，产生独立可执行文件 |
| **Interpreter** | 高级语言 | 直接执行 | 逐行翻译执行，不产生独立文件 |

- Compiler 优点：执行速度快、可分发可执行文件
- Interpreter 优点：跨平台、调试方便、无需编译步骤

## Compilation Stages（编译阶段）

### 1. Lexical Analysis（词法分析）

- 扫描源代码，去除注释和空白
- 识别 **Token**（关键字、标识符、运算符、字面量）
- 生成 Token 流供语法分析使用

### 2. Syntax Analysis（语法分析）

- 根据文法规则检查 Token 序列结构
- 生成 **Parse Tree**（语法树）或 **AST** (Abstract Syntax Tree)
- 检测语法错误（如缺少分号、括号不匹配）

### 3. Code Generation（代码生成）

- 将 AST 转换为目标机器代码或中间代码
- 分配寄存器、生成指令序列

### 4. Optimisation（优化）

- **Local Optimisation**: 常量折叠（Constant Folding）、死代码消除
- **Global Optimisation**: 循环展开（Loop Unrolling）、内联（Inlining）

## BNF Notation（巴科斯范式）

- 用于描述编程语言的语法规则
- 基本形式：

$$\text{<name>} ::= \text{expression}$$

- `::=` 表示"定义为"
- `|` 表示"或"（alternative）
- `<>` 包围非终结符（non-terminal）

### 递归规则（Recursion）

```
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
<number> ::= <digit> | <digit><number>
```

:::warning[]
递归规则必须包含一个终止条件（base case），否则会导致无限递归
:::

## Syntax Diagrams（语法图）

- BNF 的图形化表示
- **Alternative paths**: 分叉表示 `|` 选择
- **Repetition loops**: 循环箭头表示重复（如 `{...}` 或 `*`）
- 矩形框 = 非终结符，圆角/椭圆框 = 终结符

## IDE Features（集成开发环境功能）

- **Context-sensitive prompts**: 根据上下文自动提示可用函数、变量、参数
- **Syntax checking**: 实时语法检查，标记错误和警告
- **Debugging tools**: 断点（breakpoints）、单步执行（step over/into）、变量监视（watch）
- 其他：自动补全、重构工具、版本控制集成
