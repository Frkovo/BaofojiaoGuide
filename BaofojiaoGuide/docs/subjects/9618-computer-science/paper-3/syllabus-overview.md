---
title: 考纲总览
sidebar_position: 2
---

# 考纲总览 — Advanced Theory (Sections 13–20)

## Assessment Objectives

Paper 3 的所有题目均为**书面作答**，考察的重点从基础理解到综合应用：

| AO | 描述 | 占比 | 说明 |
|----|------|------|------|
| AO1 | Knowledge and understanding | 60% | 回忆知识点、标准算法、基本操作 |
| AO2 | Application and analysis | 40% | 将知识应用于新场景、多步推理、问题求解 |
| AO3 | Algorithm design and programming | 0% | Paper 3 不含程序设计题目（此部分由 Paper 4 考察） |

:::note[Paper 3 与 Paper 4 的分工]
Paper 3 侧重**书面理解与分析**，Paper 4（Practical）侧重**实际编程能力**。两者 AO3 的内容互补而非重叠。
:::

## 知识点列表 — Sections 13–20

| 章节 | Topic | 中文 | 核心内容 |
|------|-------|------|---------|
| 13 | Data Representation | 数据表示 | 用户定义数据类型、文件组织与访问模式、浮点数表示与规格化、浮点数运算 |
| 14 | Communication and Internet Technologies | 通信与互联网技术 | 协议栈（TCP/IP）、交换技术（电路/分组交换）、局域网与无线网络、加密方法、互联网基础 |
| 15 | Hardware and Virtual Machines | 硬件与虚拟机 | 处理器架构（RISC/CISC）、指令流水线、并行处理、虚拟机概念、布尔代数化简、K-map、逻辑电路 |
| 16 | System Software | 系统软件 | 操作系统功能与调度、内存管理（分页/分段/虚拟内存）、编译过程各阶段、解释与汇编 |
| 17 | Security | 安全 | 安全威胁类型、防护措施（加密/防火墙/认证/权限）、数字签名与证书 |
| 18 | Artificial Intelligence | 人工智能 | AI 定义与测试、机器学习类型、专家系统构建 |
| 19 | Computational Thinking and Problem Solving | 计算思维与问题解决 | 算法设计方法、递归、抽象数据类型、排序与搜索算法 |
| 20 | Further Programming | 进阶编程 | 面向对象编程、异常处理、文件操作、低级语言与汇编指令 |

## 完整考纲条目

### Section 13: Data Representation

| 编号 | 内容 | 要求 |
|------|------|------|
| 13.1.1 | Define and use user-defined data types: non-composite (enumeration, pointer) and composite (record, set, class) | AO1 |
| 13.1.2 | Choose appropriate data types for a given problem | AO2 |
| 13.2.1 | Describe file organisation: serial, sequential, random access | AO1 |
| 13.2.2 | Describe the use of indexes for file access | AO1 |
| 13.2.3 | Distinguish between static and dynamic data structures | AO1 |
| 13.3.1 | Represent positive and negative floating-point numbers in binary using mantissa and exponent | AO1 |
| 13.3.2 | Normalise floating-point numbers | AO1 |
| 13.3.3 | Describe the effect of changing the number of bits allocated to mantissa and exponent | AO1 |
| 13.3.4 | Describe floating-point errors: overflow, underflow, rounding error | AO1 |
| 13.4.1 | Perform binary floating-point addition and subtraction | AO2 |
| 13.4.2 | Explain the need for aligning exponents in floating-point arithmetic | AO1 |

### Section 14: Communication and Internet Technologies

| 编号 | 内容 | 要求 |
|------|------|------|
| 14.1.1 | Describe the TCP/IP protocol stack and the purpose of each layer | AO1 |
| 14.1.2 | Explain how protocols enable communication over the Internet | AO2 |
| 14.2.1 | Distinguish between circuit switching and packet switching | AO1 |
| 14.2.2 | Describe the structure of a data packet (header, payload, trailer) | AO1 |
| 14.3.1 | Describe characteristics of a LAN | AO1 |
| 14.3.2 | Describe CSMA/CD and CSMA/CA protocols | AO1 |
| 14.3.3 | Compare Ethernet and Wi-Fi standards | AO2 |
| 14.4.1 | Describe wireless networking technologies (Bluetooth, Wi-Fi, cellular) | AO1 |
| 14.5.1 | Describe symmetric and asymmetric encryption | AO1 |
| 14.5.2 | Explain the use of digital signatures and digital certificates | AO2 |
| 14.6.1 | Describe the role of DNS (Domain Name System) | AO1 |
| 14.6.2 | Explain IP addressing (IPv4, IPv6) and subnetting | AO1 |

### Section 15: Hardware and Virtual Machines

| 编号 | 内容 | 要求 |
|------|------|------|
| 15.1.1 | Describe the features of RISC and CISC processors | AO1 |
| 15.1.2 | Explain the concept of instruction pipelining and its hazards | AO2 |
| 15.1.3 | Describe parallel processing: SIMD, MIMD, multi-core | AO1 |
| 15.2.1 | Describe the concept of a virtual machine | AO1 |
| 15.2.2 | Explain the benefits of virtual machines (isolation, platform independence) | AO2 |
| 15.2.3 | Describe the role of the JVM (Java Virtual Machine) | AO1 |
| 15.3.1 | Simplify Boolean expressions using Boolean laws and De Morgan's laws | AO2 |
| 15.3.2 | Use Karnaugh maps (K-maps) to simplify expressions with up to 4 variables | AO2 |
| 15.3.3 | Design logic circuits from Boolean expressions and truth tables | AO2 |

### Section 16: System Software

| 编号 | 内容 | 要求 |
|------|------|------|
| 16.1.1 | Describe the purpose and functions of an operating system | AO1 |
| 16.1.2 | Describe process scheduling algorithms (FCFS, SJF, Round Robin, priority) | AO1 |
| 16.1.3 | Describe memory management techniques: paging, segmentation, virtual memory | AO1 |
| 16.1.4 | Explain the difference between paging and segmentation | AO2 |
| 16.2.1 | Describe the stages of compilation: lexical analysis, syntax analysis, code generation, optimisation | AO1 |
| 16.2.2 | Describe the role of an assembler and the translation of assembly code to machine code | AO1 |
| 16.2.3 | Distinguish between compiler, interpreter, and assembler | AO1 |
| 16.3.1 | Describe the role of a linker and loader | AO1 |
| 16.3.2 | Describe the use of static and dynamic linking | AO1 |

### Section 17: Security

| 编号 | 内容 | 要求 |
|------|------|------|
| 17.1.1 | Describe security threats: malware, phishing, hacking, DoS/DDoS, brute force attack, SQL injection | AO1 |
| 17.1.2 | Describe data interception and social engineering | AO1 |
| 17.2.1 | Describe security measures: firewall, encryption, authentication, biometrics, CAPTCHA | AO1 |
| 17.2.2 | Explain how digital signatures and certificates provide authenticity and integrity | AO2 |
| 17.2.3 | Describe access rights and user permissions | AO1 |

### Section 18: Artificial Intelligence

| 编号 | 内容 | 要求 |
|------|------|------|
| 18.1.1 | Define AI and its goals | AO1 |
| 18.1.2 | Describe the Turing test | AO1 |
| 18.1.3 | Describe the Chinese room argument | AO1 |
| 18.2.1 | Describe machine learning: supervised, unsupervised, reinforcement learning | AO1 |
| 18.2.2 | Compare the three types of machine learning | AO2 |
| 18.3.1 | Describe the components of an expert system: knowledge base, inference engine, rule base, user interface | AO1 |
| 18.3.2 | Distinguish between forward chaining and backward chaining | AO1 |

### Section 19: Computational Thinking and Problem Solving

| 编号 | 内容 | 要求 |
|------|------|------|
| 19.1.1 | Design algorithms using pseudocode and flowcharts to solve problems | AO2 |
| 19.1.2 | Use trace tables to step through algorithms | AO2 |
| 19.2.1 | Describe the concept of recursion | AO1 |
| 19.2.2 | Write and trace recursive algorithms | AO2 |
| 19.2.3 | Describe the use of stack frames in recursion | AO1 |
| 19.3.1 | Describe and implement ADTs: stack, queue, linked list, binary tree, graph | AO1/AO2 |
| 19.3.2 | Describe operations on binary trees (insert, search, traversals: pre-order, in-order, post-order) | AO1 |
| 19.3.3 | Describe operations on hash tables | AO1 |
| 19.4.1 | Describe and implement searching algorithms: linear search, binary search | AO1/AO2 |
| 19.4.2 | Describe and implement sorting algorithms: bubble sort, insertion sort, quicksort, merge sort | AO1/AO2 |
| 19.4.3 | Compare time complexity of searching and sorting algorithms | AO2 |

### Section 20: Further Programming

| 编号 | 内容 | 要求 |
|------|------|------|
| 20.1.1 | Describe OOP concepts: class, object, encapsulation, inheritance, polymorphism, abstraction | AO1 |
| 20.1.2 | Write CIE Pseudocode to define classes, constructors, methods, and inheritance | AO2 |
| 20.2.1 | Describe exception handling: try, catch, throw | AO1 |
| 20.2.2 | Write programs that handle file operations and exceptions | AO2 |
| 20.3.1 | Describe low-level languages: machine code and assembly | AO1 |
| 20.3.2 | Write simple assembly programs using LMC (Little Man Computer) instruction set | AO2 |
| 20.3.3 | Describe addressing modes: immediate, direct, indirect, indexed | AO1 |

## 命令词对照表（Command Words）

| 英文 | 中文翻译 | 答题要求 |
|------|---------|---------|
| State | 陈述 | 简要陈述事实或定义，通常 1–2 句话 |
| Define | 定义 | 给出准确定义，通常包括公式或特征 |
| Describe | 描述 | 详细说明某概念、过程或功能 |
| Explain | 解释 | 不仅要描述，还要说明原因或原理 |
| Identify | 识别 | 从给定信息中找出特定内容 |
| Give | 给出 | 简单提供答案，不必详细解释 |
| List | 列举 | 逐项列出，不需展开 |
| Outline | 概述 | 简要概括主要特征 |
| Compare | 比较 | 指出两者或多者的异同 |
| Distinguish | 区分 | 说明不同之处 |
| Simplify | 化简 | 用布尔代数定律或 K-map 化简表达式 |
| Calculate | 计算 | 进行数值计算并给出结果 |
| Determine | 确定 | 通过计算或推理得到结果 |
| Draw | 画出 | 画出逻辑电路图、流程图或示意图 |
| Write | 编写 | 编写伪代码、算法或程序 |
| Trace | 跟踪 | 用 trace table 跟踪算法执行过程 |
| Complete | 补全 | 补充表格、示意图或代码片段 |
| Justify | 论证 | 为某个选择或结论提供理由 |
| Suggest | 建议 | 提出合理的方案或改进意见 |

:::tip[AO1 vs AO2]
Paper 3 中 AO1 题目（～45 分）通常为 "State" "Describe" "Define"，AO2 题目（～30 分）通常为 "Explain" "Compare" "Simplify" 或需要多步推理的 "Calculate" 与 "Write"。答题时间分配可据此调整。
:::
