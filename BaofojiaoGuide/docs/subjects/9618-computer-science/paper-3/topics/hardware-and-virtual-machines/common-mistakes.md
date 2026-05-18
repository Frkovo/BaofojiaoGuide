---
title: 常见错误
---

## 错误 1：混淆 RISC 和 CISC 特征

**错误表现**：
- 认为 RISC 有复杂指令集而 CISC 有简单指令集
- 认为 RISC 有多周期执行而 CISC 是单周期

**纠正**：
| 特征 | RISC | CISC |
|------|------|------|
| 指令集 | 精简（少） | 复杂（多） |
| CPI | 通常 1 | 通常 > 1 |
| 寻址模式 | 少 | 多 |
| 寄存器 | 大量通用寄存器 | 少量专用寄存器 |

## 错误 2：流水线阶段顺序错误

**错误表现**：
- 将 ID 放在 OF 之后
- 遗漏 WB（Write Back）阶段
- 混淆 IF（Instruction Fetch）和 OF（Operand Fetch）

**纠正**：
正确顺序：IF → ID → OF → IE → WB
- IF: 从内存取指令
- ID: 指令译码
- OF: 取操作数
- IE: 执行指令
- WB: 结果写回寄存器

## 错误 3：流水线 hazard 概念混淆

**错误表现**：
- 无法区分三种 hazard
- 认为流水线一定提高单条指令速度

**纠正**：
- Structural hazard：硬件资源冲突（如 ALU 被两条指令同时需要）
- Data hazard：数据依赖性（下一条指令需要上一条指令的结果）
- Control hazard：分支跳转（pipeline 需要 flush）
- Pipelining 提高的是吞吐量（throughput），不是单条指令延迟

## 错误 4：混淆 Flynn's 分类

**错误表现**：
- 认为 SIMD 是多指令流
- 混淆 SIMD 和 MIMD 的例子

**纠正**：
| 分类 | 指令流 | 数据流 | 例子 |
|------|--------|--------|------|
| SISD | 1 | 1 | 传统单核 CPU |
| SIMD | 1 | 多 | GPU, vector processors |
| MISD | 多 | 1 | 容错系统 |
| MIMD | 多 | 多 | 多核 CPU, 集群 |

## 错误 5：混淆 host OS 和 guest OS 的角色

**错误表现**：
- 认为 guest OS 直接管理物理硬件
- 认为 host OS 运行在虚拟机内部

**纠正**：
- **Host OS**: 直接运行在物理硬件上的操作系统
- **Guest OS**: 运行在虚拟机内部的操作系统，通过 hypervisor 访问硬件
- **Hypervisor (VMM)**: 管理多个 guest OS 的资源分配

## 错误 6：认为虚拟机没有性能开销

**错误表现**：忽略 hypervisor 层带来的性能损失。

**纠正**：虚拟机增加了 hypervisor 层的开销，guest OS 无法直接访问物理硬件，性能通常低于物理机。涉及 I/O 密集型任务时开销更明显。
