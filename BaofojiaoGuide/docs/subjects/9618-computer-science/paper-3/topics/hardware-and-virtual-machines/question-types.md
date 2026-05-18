---
title: 题型分析
---

# 题型分析：Hardware and Virtual Machines

---

## 题型 1：RISC vs CISC 比较

### 题目特征

- 完成比较表格
- 勾选特征归属（RISC / CISC / Both）
- 描述差异并给出推荐

:::note[标准解题方法]

1. 根据指令集大小、CPI、寻址模式、流水线效率、代码密度等维度比较
2. RISC 关键词：simple, fixed-length, one cycle, load/store, many registers
3. CISC 关键词：complex, variable-length, many cycles, micro-programmed
4. 应用场景：RISC 适合低功耗设备，CISC 适合复杂计算

:::

:::info[评分标准（MS 模式）]

- **M1**：每组正确比较得 1 分
- **A1**：使用表格或成对陈述
- **B1**：给出具体的特征描述而非模糊回答

:::

### 典型例题 1：9618/s22/qp/31 Q4

> Tick the boxes to show whether each characteristic applies to RISC, CISC or both.

| Characteristic | RISC | CISC |
|---------------|------|------|
| Each instruction takes approximately one clock cycle | | |
| Variable instruction length | | |
| Large number of addressing modes | | |
| Micro-programmed control unit | | |
| Many general purpose registers | | |

<details>
<summary>📝 MS 展开查看</summary>

| Characteristic | RISC | CISC |
|---------------|------|------|
| Each instruction takes approximately one clock cycle | **M1** ✅ | |
| Variable instruction length | | **A1** ✅ |
| Large number of addressing modes | | **A1** ✅ |
| Micro-programmed control unit | | **B1** ✅ |
| Many general purpose registers | **B1** ✅ | |

</details>

### 典型例题 2：9618/w22/qp/31 Q10

> (a) Describe **two** differences between RISC and CISC processors.
> (b) A computer designer needs to choose between a RISC and a CISC processor for a new device. State which processor you would recommend for each application and justify your answer.
> (i) A battery-powered mobile phone
> (ii) A desktop computer used for video editing

<details>
<summary>📝 MS 展开查看</summary>

(a) Differences (any 2):
- **M1**：RISC has fewer / simpler instructions; CISC has more / complex instructions
- **A1**：RISC has fixed instruction length; CISC has variable instruction length
- **A1**：RISC typically executes one instruction per clock cycle; CISC may need multiple cycles
- **B1**：RISC uses load/store architecture; CISC allows memory-to-memory operations

(b)(i) Mobile phone:
- **M1**：RISC recommended — lower power consumption
- **A1**：RISC generates less heat / more energy efficient

(b)(ii) Video editing:
- **M1**：CISC recommended — complex instructions handle multimedia tasks efficiently
- **A1**：CISC offers higher code density / backward compatibility

</details>

---

## 题型 2：流水线（Pipelining）

### 题目特征

- 描述流水线各阶段
- 绘制 timing diagram
- 分析 hazard 及其解决方法

:::note[标准解题方法]

1. 五阶段顺序：IF → ID → OF → IE → WB
2. 每个阶段通常需要一个时钟周期
3. Timing diagram：横轴为时钟周期，纵轴为指令编号
4. Hazard 会使流水线停顿（stall / bubble）
5. 数据相关（data hazard）可用 forwarding 解决

:::

:::info[评分标准（MS 模式）]

- **M1**：正确列出流水线阶段名称
- **A1**：正确绘制 timing diagram
- **B1**：识别 hazard 类型并解释

:::

### 典型例题 1：9618/s23/qp/32 Q8

> A processor uses a five-stage pipeline: IF (Instruction Fetch), ID (Instruction Decode), OF (Operand Fetch), IE (Instruction Execute), WB (Write Back).
> (a) Explain what is meant by pipelining.
> (b) The following three instructions are to be executed:
> I1: LDR R1, 100
> I2: ADD R2, R1, #5
> I3: SUB R3, R4, #1
> Complete a timing diagram showing the execution of these three instructions through the pipeline. Assume no hazards.

<details>
<summary>📝 MS 展开查看</summary>

(a) Pipelining:
- **M1**：将指令执行分成多个阶段，各阶段重叠执行不同的指令（overlapping execution of multiple instructions）
- **A1**：提高 CPU 吞吐量（throughput），但不减少单条指令的执行时间

(b) Timing diagram:
- **M1**：Cycle 1 → I1: IF
- **A1**：Cycle 2 → I1: ID, I2: IF
- **A1**：Cycle 3 → I1: OF, I2: ID, I3: IF
- **B1**：Cycle 4 → I1: IE, I2: OF, I3: ID
- **B1**：Cycle 5 → I1: WB, I2: IE, I3: OF
- **B1**：Cycle 6 → I2: WB, I3: IE
- **B1**：Cycle 7 → I3: WB

</details>

### 典型例题 2：Data Hazard

> A processor has a five-stage pipeline. Explain what happens when a data hazard occurs. Suggest how this hazard can be resolved.

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：Data hazard occurs when an instruction depends on the result of a previous instruction that has not yet been written back
- **A1**：Pipeline stalls / inserts a bubble (NOP) until the data is available
- **B1**：Solution: forwarding / bypassing (forward the result directly from the execute stage to the next instruction without waiting for write back)

</details>

---

## 题型 3：计算机体系结构（Computer Architectures / Flynn's Taxonomy）

### 题目特征

- 解释 SISD / SIMD / MISD / MIMD
- 给出例子
- 匹配应用场景

:::note[标准解题方法]

1. 明确"指令流"和"数据流"的概念
2. SISD：单核顺序执行（一条指令处理一组数据）
3. SIMD：一条指令对多组数据并行操作
4. MISD：多条指令处理同一组数据（容错系统）
5. MIMD：多条指令处理多组数据（多核处理器）

:::

:::info[评分标准（MS 模式）]

- **M1**：正确解释每种分类的指令流和数据流
- **A1**：为每种分类给出合适例子
- **B1**：在比较中明确区分相似类别（如 SIMD vs MIMD）

:::

### 典型例题 1：9618/w23/qp/31 Q5

> (a) Complete the table using SISD, SIMD, MISD or MIMD.

| Description | Classification |
|-------------|---------------|
| A single processor executes one instruction on one item of data | |
| Each processor executes different instructions on different data | |
| One instruction is executed on multiple items of data simultaneously | |

> (b) Describe one advantage of a massively parallel computer.

<details>
<summary>📝 MS 展开查看</summary>

(a) Table:
- **M1**：A single processor executes one instruction on one item of data → SISD
- **A1**：Each processor executes different instructions on different data → MIMD
- **A1**：One instruction is executed on multiple items of data simultaneously → SIMD

(b) Massively parallel computer advantage:
- **B1**：可以同时处理大量数据 / 解决复杂计算问题
- **B1**：高性能计算（HPC）适用 scientific simulations / weather forecasting

</details>

### 典型例题 2：SIMD vs MIMD

> (a) State what is meant by SIMD.
> (b) State what is meant by MIMD.
> (c) Give one application of SIMD processors.

<details>
<summary>📝 MS 展开查看</summary>

(a) SIMD (Single Instruction, Multiple Data):
- **M1**：一条指令同时对多组数据执行相同的操作
- **A1**：用于 vector processing / parallel processing

(b) MIMD (Multiple Instruction, Multiple Data):
- **M1**：多条指令同时对多组数据执行不同的操作
- **A1**：每个处理器可以独立执行不同的任务

(c) Application of SIMD:
- **B1**：图形处理 / GPU / image processing / multimedia processing

</details>

---

## 题型 4：虚拟机（Virtual Machines）

### 题目特征

- 解释虚拟机的概念
- 列出优点和局限性
- 比较 host OS 和 guest OS

:::note[标准解题方法]

1. 虚拟机 = 软件模拟完整计算机，可以运行独立 OS
2. Hypervisor (VMM) 在物理硬件和 guest OS 之间
3. Host OS 运行在物理机上，Guest OS 运行在 VM 内
4. 优点：隔离、资源共享、测试、迁移
5. 缺点：性能开销、硬件访问限制

:::

:::info[评分标准（MS 模式）]

- **M1**：正确定义虚拟机
- **A1**：描述 hypervisor / VMM 的作用
- **A1**：列出优点（each valid point = 1）
- **B1**：列出局限性

:::

### 典型例题 1：9618/s24/qp/32 Q9

> (a) Describe the role of a hypervisor in a virtual machine environment.
> (b) Explain **one** limitation of using virtual machines compared to running the operating system directly on the hardware.

<details>
<summary>📝 MS 展开查看</summary>

(a) Hypervisor / VMM:
- **M1**：管理物理硬件资源（CPU, memory, I/O）
- **A1**：在多个 guest OS 之间分配资源
- **A1**：隔离不同 VM 之间的资源访问

(b) Limitation:
- **B1**：性能开销（performance overhead）— hypervisor 层增加了额外处理步骤
- **B1**：Guest OS 无法直接访问物理硬件，I/O 操作速度较慢

</details>

### 典型例题 2：虚拟机应用

> A company uses virtual machines on its server.
> (a) Explain what is meant by a virtual machine.
> (b) Describe **two** benefits of using virtual machines on the server.

<details>
<summary>📝 MS 展开查看</summary>

(a) Virtual machine:
- **M1**：软件模拟的计算机环境（software simulation of a computer system）
- **A1**：可以运行自己的 operating system (guest OS)，与物理机隔离

(b) Benefits (any 2):
- **A1**：隔离性 — 一个 VM 崩溃不影响其他 VM
- **A1**：资源利用 — 多个 VM 共享同一物理硬件
- **B1**：便于测试 — 可以快速创建销毁测试环境
- **B1**：便于迁移 — VM 可以移动到其他物理服务器

</details>

---

:::warning[常见陷阱]

- 混淆 RISC（精简指令）和 CISC（复杂指令）的核心特征
- 流水线阶段顺序错误，特别是 ID 和 OF 的顺序
- 认为 pipelining 减少单条指令延迟（实际提高 throughput）
- 混淆 SIMD 和 MIMD 的区别（指令流 vs 数据流）
- 认为虚拟机没有性能开销
- 混淆 host OS 和 guest OS 的关系
- 遗漏 hypervisor 在虚拟化中的核心作用

:::
