---
title: 考前速记
---

## RISC vs CISC 速查

| 特征 | RISC | CISC |
|------|------|------|
| 指令数量 | 少 | 多 |
| 指令长度 | 固定 | 可变 |
| CPI | ~1 | >1 |
| 寄存器 | 多 | 少 |
| 寻址模式 | 少 | 多 |
| 流水线 | 高效 | 受限 |

## 流水线阶段

```
IF → ID → OF → IE → WB
```

- IF (Instruction Fetch): 取指令
- ID (Instruction Decode): 译码
- OF (Operand Fetch): 取操作数
- IE (Instruction Execute): 执行
- WB (Write Back): 写回

Three hazards: Structural, Data, Control

## Flynn's 分类

- **SISD**: 单指令单数据 — 传统单核 CPU
- **SIMD**: 单指令多数据 — GPU, vector processing
- **MISD**: 多指令单数据 — 容错系统
- **MIMD**: 多指令多数据 — 多核 CPU, clusters

## 虚拟机器

- **VM**: 模拟完整的计算机环境
- **Hypervisor / VMM**: 管理物理资源分配
- **Host OS**: 物理机上的 OS
- **Guest OS**: 虚拟机内的 OS
- 优点：隔离、资源利用、测试方便、迁移
- 缺点：性能开销
