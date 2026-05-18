---
title: Hardware and Virtual Machines
---

本主题涵盖处理器架构（RISC vs CISC）、流水线技术（pipelining）、并行处理（parallel processing）和虚拟机（virtual machines）。

## 处理器架构（Processor Architecture）

- **RISC (Reduced Instruction Set Computer)**：指令数量少且简单，每条指令在一个时钟周期内完成
- **CISC (Complex Instruction Set Computer)**：指令数量多且复杂，一条指令可能需要多个时钟周期

## 流水线（Pipelining）

将指令执行分为多个重叠的阶段，提高 CPU 吞吐量。典型阶段：IF（取指令）、ID（译码）、OF（取操作数）、IE（执行）、WB（写回）

## 并行处理（Parallel Processing）

- Flynn's Taxonomy：SISD、SIMD、MISD、MIMD
- 大规模并行计算机（Massively Parallel Computers）

## 虚拟机（Virtual Machines）

- 虚拟机监视器（Hypervisor / VMM）
- 宿主机（Host OS）和客户机（Guest OS）
