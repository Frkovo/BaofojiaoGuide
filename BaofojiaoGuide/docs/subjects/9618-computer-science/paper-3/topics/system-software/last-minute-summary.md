---
title: 考前速记
---

## 操作系统核心功能

- **Process Management**: 创建/调度/终止进程
- **Memory Management**: 分配内存、虚拟内存
- **File Management**: 文件组织
- **Device Management**: I/O 设备控制
- **Security Management**: 访问控制

## 调度算法速查

| 算法 | 规则 | 抢占？ |
|------|------|--------|
| FCFS | 先到先服务 | 否 |
| SJF | 最短作业优先 | 否 |
| SRT | 最短剩余时间 | 是 |
| RR | 时间片轮转 | 是 |

## 虚拟内存

- Virtual memory = disk space used as extension of RAM
- Paging = fixed-size blocks, no external fragmentation
- Segmentation = variable-size blocks, external fragmentation
- Thrashing = excessive page swapping → low throughput

## 编译阶段顺序

```
Lexical Analysis → Syntax Analysis → Code Generation → Optimisation
```

- **Lexical**: tokenise, remove comments, symbol table
- **Syntax**: parse tree, grammar check
- **Code Gen**: machine code
- **Optimise**: improve efficiency

## BNF 速记

- `::=` — is defined as
- `|` — or
- `<...>` — non-terminal
- Terminal — literal character

## RPN 转换

- Infix: `3 + 4 * 2`
- RPN: `3 4 2 * +`
- 用 stack 辅助计算：遇到数字 push，遇到 operator pop 两个
