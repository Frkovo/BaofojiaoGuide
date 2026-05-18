---
title: 知识点总结
---

## RISC vs CISC

- **RISC** (Reduced Instruction Set Computer): 指令少且简单，每条指令长度固定，通常一个时钟周期完成
- **CISC** (Complex Instruction Set Computer): 指令多且复杂，长度可变，一条指令可能需要多个时钟周期
- RISC 使用 Load/Store 架构，只有 load/store 指令访问内存；CISC 允许内存-内存操作
- RISC 有大量通用寄存器，CISC 寄存器较少
- RISC 编译器更复杂（需将复杂操作拆解），CISC 汇编编程更容易

:::tip[RISC 特点]
指令数量少、格式固定、单周期执行、寄存器丰富、硬连线控制
:::

:::warning[CISC 特点]
指令丰富、变长指令、多周期执行、微程序控制（Microprogrammed Control）
:::

### 中断处理（Interrupt Handling）

- **RISC**: 硬件自动处理较少，需要软件保存/恢复寄存器，中断响应快
- **CISC**: 微程序处理中断，自动保存更多上下文，但响应较慢

## Pipelining（流水线技术）

### 经典五级流水线

| 阶段 | 全称 | 操作 |
|------|------|------|
| IF | Instruction Fetch | 从内存取指令 |
| ID | Instruction Decode | 译码并读取寄存器 |
| OF | Operand Fetch | 获取操作数 |
| IE | Instruction Execute | 执行运算或计算地址 |
| WB | Write Back | 将结果写回寄存器 |

- **Benefits**: 提高吞吐量（throughput），同一时间多条指令在不同阶段并行
- 流水线不影响单个指令延迟，但整体效率大幅提升

### 流水线冒险（Hazards）

- **Data Hazards（数据冒险）**: 下一条指令依赖上一条结果
  - 解决：Forwarding（旁路转发）、插入 NOP（空操作）、编译器重排指令
- **Control Hazards（控制冒险）**: 分支指令导致流水线清空
  - 解决：Branch Prediction（分支预测）、延迟槽（Delay Slot）

## Flynn's Taxonomy（弗林分类法）

| 分类 | 含义 | 实例 |
|------|------|------|
| **SISD** | Single Instruction, Single Data | 传统单核 CPU |
| **SIMD** | Single Instruction, Multiple Data | GPU 向量处理 |
| **MISD** | Multiple Instruction, Single Data | 容错系统（少见） |
| **MIMD** | Multiple Instruction, Multiple Data | 多核处理器、集群 |

## Massively Parallel Computers（大规模并行计算机）

- 包含大量处理器（数百/数千个），协同完成计算任务
- **MPP** (Massively Parallel Processing): 分布式内存架构，每个节点有独立内存
- 用于科学计算、气象模拟、AI 训练等需要高计算能力的场景
- 编程模型常用 MPI (Message Passing Interface)

## Virtual Machines（虚拟机）

### 概念

- **Host OS**: 运行在物理硬件上的操作系统
- **Guest OS**: 运行在虚拟机内部的的操作系统
- **Hypervisor/VMM** (Virtual Machine Monitor): 负责管理和隔离多个虚拟机

### Benefits（优势）

- **Isolation**: 不同 VM 相互隔离，一个崩溃不影响其他
- **Flexibility**: 可在同一硬件上运行不同 OS（如 Windows + Linux）
- 便于测试、开发、部署；支持快照（snapshot）和迁移（migration）

### Limitations（限制）

- **Overhead**: 性能开销，VM 访问硬件需通过 Hypervisor 转换
- 资源竞争：多个 VM 共享 CPU、内存、I/O
- Type 2 Hypervisor（如 VirtualBox）开销更大；Type 1（如 VMware ESXi）性能更接近裸机
