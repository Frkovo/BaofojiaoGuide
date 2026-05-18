---
title: 9618 Paper 3 Advanced Theory
sidebar_position: 1
---

# Paper 3: Advanced Theory（高级理论）

## 快速信息表

| 项目 | 内容 |
|------|------|
| 考试时长 | 1 小时 30 分钟 |
| 总分 | 75 分 |
| 题目数量 | 约 10–12 道，全部必答 |
| 覆盖章节 | 13–20（A Level 专属内容） |
| 计算器 | 不允许使用 |
| 题型 | 计算、解释、伪代码、算法分析、电路设计等 |

## 八大 Topic 总览

| 章节 | Topic | 中文 | 一句话总结 |
|------|-------|------|-----------|
| 13 | Data Representation | 数据表示 | 用户定义类型、文件组织、浮点数表示与运算 |
| 14 | Communication and Internet Technologies | 通信与互联网技术 | 协议、交换技术、网络拓扑、加密、DNS |
| 15 | Hardware and Virtual Machines | 硬件与虚拟机 | 处理器架构、并行处理、虚拟机、布尔代数与逻辑电路 |
| 16 | System Software | 系统软件 | 操作系统、编译/解释/汇编、链接与加载 |
| 17 | Security | 安全 | 各类威胁与防护措施（加密、防火墙、认证） |
| 18 | Artificial Intelligence | 人工智能 | 图灵测试、机器学习、专家系统 |
| 19 | Computational Thinking and Problem Solving | 计算思维与问题解决 | 算法设计、递归、ADT、搜索/排序 |
| 20 | Further Programming | 进阶编程 | OOP、异常处理、低级语言与汇编 |

## 核心公式速查

:::warning[Not a formula sheet]
以下公式仅为复习速查。Paper 3 **不提供公式表**，所有公式必须牢记。
:::

### Floating-point Representation

| 概念 | 公式 / 表示 |
|------|------------|
| 规格化浮点数 | $(-1)^s \times 1.\text{mantissa} \times 2^{\text{exponent} - \text{bias}}$ |
| 浮点数范围 | 最大正数 $= (1 - 2^{-n}) \times 2^{+m}$，最小正规格化数 $= 1 \times 2^{-m}$ |
| Excess-N (bias) | N = $2^{k-1} - 1$（k = 指数位数） |
| 精度 | 尾数位数决定精度，指数位数决定范围 |
| 舍入误差 | Rounding error = 浮点近似与真实值的差 |

### Boolean Algebra

| 定律 | 公式 |
|------|------|
| 恒等律 | $A + 0 = A$, $A \cdot 1 = A$ |
| 零律 | $A + 1 = 1$, $A \cdot 0 = 0$ |
| 互补律 | $A + \overline{A} = 1$, $A \cdot \overline{A} = 0$ |
| 幂等律 | $A + A = A$, $A \cdot A = A$ |
| 双重否定 | $\overline{\overline{A}} = A$ |
| 交换律 | $A + B = B + A$, $A \cdot B = B \cdot A$ |
| 结合律 | $(A + B) + C = A + (B + C)$, $(A \cdot B) \cdot C = A \cdot (B \cdot C)$ |
| 分配律 | $A \cdot (B + C) = A \cdot B + A \cdot C$, $A + (B \cdot C) = (A + B) \cdot (A + C)$ |
| 吸收律 | $A + AB = A$, $A \cdot (A + B) = A$ |
| De Morgan's Laws | $\overline{A + B} = \overline{A} \cdot \overline{B}$, $\overline{A \cdot B} = \overline{A} + \overline{B}$ |

### Karnaugh Map (K-map) Simplification

- 2-variable K-map: $2 \times 2$ grid
- 3-variable K-map: $2 \times 4$ grid
- 4-variable K-map: $4 \times 4$ grid
- 相邻项可合并为乘积项；最大乘组为 $2^n$ 个相邻 1
- Gray code 排列：相邻格子仅 1 bit 变化

### Processor Performance

| 概念 | 公式 |
|------|------|
| Clock cycle time | $T = \frac{1}{f}$ |
| CPI (Cycles Per Instruction) | $CPI = \frac{\text{总时钟周期数}}{\text{指令数}}$ |
| Execution time | $T_{\text{exec}} = \text{指令数} \times CPI \times \text{时钟周期}$ |
| Speedup (Amdahl's Law) | $S = \frac{1}{(1 - f) + f / n}$ |

### Number Systems

- Decimal → Binary: 除 2 取余
- Decimal → Hexadecimal: 除 16 取余
- Binary → Hexadecimal: 每 4 bit 一组
- Two's complement: 正数不变，负数取反加 1
- Two's complement range: $-2^{n-1}$ to $2^{n-1} - 1$

## 考试策略

1. **先浏览全卷**（2 分钟）——快速识别各题所属章节
2. **优先完成计算题**（浮点数、布尔代数、K-map）——这些有确定答案
3. **解释题（Explain/Describe）**——用中文草稿再翻译关键词；注意使用专业术语
4. **伪代码题**——严格遵循 CIE Pseudocode 规范（`OUTPUT` 而非 `print`，`←` 赋值，`RETURN` 等）
5. **算法分析题**——逐行跟踪（trace table）确保理解
6. **留最后 10 分钟**——检查单位、符号、位宽、符号扩展等细节

## 考前检查清单

### 13 Data Representation
- [ ] 理解 pointer、record、set、class 等用户定义类型的语法
- [ ] 掌握 serial、sequential、random file organisation 区别
- [ ] 能写出规格化浮点数的二进制表示（mantissa + exponent）
- [ ] 会进行浮点数加减运算并对齐指数
- [ ] 能解释 overflow、underflow、rounding error

### 14 Communication and Internet Technologies
- [ ] 熟记 TCP/IP 四层模型及各层协议
- [ ] 能区分 circuit switching vs packet switching
- [ ] 能解释 CSMA/CD 与 CSMA/CA 工作原理
- [ ] 理解 symmetric vs asymmetric encryption
- [ ] 了解 DNS 解析过程

### 15 Hardware and Virtual Machines
- [ ] 能比较 RISC vs CISC
- [ ] 理解 instruction pipeline 与 hazards
- [ ] 解释 virtual machine 概念与 JVM
- [ ] 熟练化简 Boolean expressions（De Morgan's laws）
- [ ] 会用 K-map 化简最多 4 变量表达式
- [ ] 能根据逻辑表达式画出 logic circuit

### 16 System Software
- [ ] 理解操作系统功能（process management, memory management, file management）
- [ ] 能区分 paging、segmentation、virtual memory
- [ ] 掌握编译各阶段：lexical analysis → syntax analysis → code generation → optimisation
- [ ] 能区分 compiler vs interpreter vs assembler
- [ ] 了解 linker、loader、dynamic link library 的作用

### 17 Security
- [ ] 能列举常见安全威胁（malware, phishing, DoS, brute force, SQL injection）
- [ ] 掌握防护措施：firewall、encryption、authentication、access rights
- [ ] 理解 digital signature 与 digital certificate 的区别与用途

### 18 Artificial Intelligence
- [ ] 能解释 Turing test 与 Chinese room argument
- [ ] 区分 supervised、unsupervised、reinforcement learning
- [ ] 理解 expert system 的 components（knowledge base, inference engine, rule base）
- [ ] 了解 forward chaining 与 backward chaining

### 19 Computational Thinking and Problem Solving
- [ ] 能设计算法解决给定问题（流程图 / 伪代码）
- [ ] 掌握 recursion：base case、recursive case、stack overflow
- [ ] 能实现 ADT：stack（push/pop）、queue（enqueue/dequeue）、linked list（insert/delete）、binary tree（traversal）
- [ ] 掌握 binary search、bubble sort、insertion sort、quicksort、merge sort

### 20 Further Programming
- [ ] 理解 OOP 四大特征：encapsulation、inheritance、polymorphism、abstraction
- [ ] 能编写 class definition、constructor、method override
- [ ] 理解 exception handling（try-catch-throw）
- [ ] 理解低级语言与汇编指令（LDR, STR, ADD, SUB, CMP, B, BEQ 等）
- [ ] 能进行 LMC（Little Man Computer）编程

:::tip[复习建议]
Section 13（浮点数）、15（布尔代数）、19（算法与 ADT）在历年试卷中占比最重，建议优先巩固。
:::
