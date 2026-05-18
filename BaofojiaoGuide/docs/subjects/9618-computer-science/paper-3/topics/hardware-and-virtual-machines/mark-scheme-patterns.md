---
title: MS 模式总结
---

## 通用模式

| 题型 | 分值 | 典型得分点 |
|------|------|------------|
| RISC vs CISC 比较 | 3-4 | **M1** 每个正确比较 1 分；**A1** 表格/陈述式回答 |
| 流水线阶段 | 4-5 | **M1** 阶段名称；**A1** timing diagram 正确；**B1** hazard 解释 |
| Flynn's 分类 | 3-4 | **M1** SISD/SIMD/MISD/MIMD 定义；**A1** 各给一个例子 |
| 虚拟机 | 3-4 | **M1** 定义；**A1** 优点；**A1** 缺点；**B1** hypervisor 角色 |

## 高频得分短语

- **RISC** — "small number of simple instructions" / "one instruction per clock cycle" / "load/store architecture" / "large number of registers" / "fixed instruction length"
- **CISC** — "large number of complex instructions" / "variable instruction length" / "multiple clock cycles per instruction" / "micro-programmed control" / "many addressing modes"
- **Pipelining** — "overlapping execution of instructions" / "increases throughput" / "IF, ID, OF, IE, WB stages"
- **Pipeline hazard** — "structural hazard: resource conflict" / "data hazard: instruction depends on previous result" / "control hazard: branch prediction"
- **Flynn's** — "SISD: single instruction single data" / "SIMD: vector processing / GPU" / "MIMD: multi-core"
- **Virtual machine** — "software simulation of a computer" / "hypervisor manages resources" / "host OS runs on physical hardware" / "guest OS runs in VM"
