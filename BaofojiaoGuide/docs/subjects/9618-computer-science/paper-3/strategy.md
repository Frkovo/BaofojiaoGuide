---
title: 答题策略
sidebar_position: 5
---

## 前 5 分钟策略：浏览全局

:::note[开局五步法]
1. **扫读全卷** — 快速翻看所有题目，了解题型分布
2. **标记 easy pickings** — 在题目旁边标注 ✓（确定会做）、?（需要思考）、✗（不确定）
3. **圈出指令词** — 用笔圈出每题的 command word（Calculate, Explain, State, Write 等）
4. **识别大题板块** — 记下需要较长时间的题目（如 Draw diagram、Write pseudocode）
5. **确认页面** — 检查是否有多页题目，避免漏题
:::

**检查清单**：
- [ ] 试卷总页数，确认没有缺页
- [ ] 每题的分值标注，用于分配时间
- [ ] 是否有选项题（Paper 3 无选项题，全部必答）

---

## 按主题的应对策略

### Section 13：Data Representation（浮点数、RPN、Bit manipulation）

这类题目以 Calculation & Conversion 为主。

:::note[计算题策略]
- 浮点数小题：**4 步标准法** — ① 确定 sign bit ② 计算 exponent（注意 bias） ③ 提取 mantissa ④ 组合计算真值
- RPN 求值：使用 **stack simulation**，每读一个 token 更新一次 stack 状态
- 转换题：写出中间进制（二进制作为桥梁），每一步单独写出
- 务必展示 working，分步写清楚
:::

### Section 14-15：Communication & Internet（协议、加密、网络）

以 Explain / Describe + State 为主。

:::note[概念题策略]
- 涉及协议（TCP/IP, HTTP, FTP）时，用 **层次结构** 回答
- 加密相关题：区分 symmetric 与 asymmetric，说出各自用途和场景
- 使用对比结构：'Symmetric encryption uses the same key for encryption and decryption, whereas asymmetric encryption uses a pair of public and private keys.'
- 列出 2-3 个 point 即可，每个 point 要展开
:::

### Section 16：Artificial Intelligence（AI 概念、搜索策略）

State + Explain 为主，偶尔出现 Small pseudocode。

:::note[AI 题策略]
- 定义 A*、BFS、DFS 等搜索算法时，需要：全称 + 原理 + 一张图示意
- 区分 heuristic search 和 uninformed search
- 如果考到 Natural Language Processing，用 **pipeline 结构** 回答（Tokenisation → Parsing → Semantic analysis → etc.）
- 涉及 Machine Learning 时区分 supervised vs unsupervised
:::

### Section 17：Computational Thinking & Problem Solving（ADT、算法）

Pseudocode Completion + Write Pseudocode 的重灾区。

:::note[算法题策略]
- **先写注释**：用中文或英文写出伪代码框架，再翻译为 pseudocode
- 排序/搜索题：三种套路任选一种 — Iterative | Recursive | 混合
- ADT 操作题：牢记每种 ADT 的特性 — Stack (LIFO)、Queue (FIFO)、Linked List (dynamic)
- 复杂度分析：Big-O 记号要准确，用 n 表示数据规模
:::

### Section 18：Algorithm Design Methods（声明式编程、OOP）

Write Pseudocode + Explain。

:::note[OOP & Declarative 策略]
- 定义 class 时：PRIVATE attributes → PUBLIC methods → Constructor
- Declarative programming 题：事实（facts）+ 规则（rules）→ 查询（query）
- 如果考 recursion：**base case 优先写**，再写 recursive case
- 画继承图时：箭头方向从 subclass 指向 superclass
:::

### Section 19-20：Further Programming & Low-level（File handling、Assembly、Virtual Machine）

混合题型 — 计算 + 写代码 + 解释。

:::note[编程 & 底层策略]
- File handling 三段式：OpenFile → 循环 ReadFile/WriteFile → CloseFile
- Assembly 题：注意 LDM 和 Immediate addressing 的区别
- Virtual machine 题：区分 translator (compiler/interpreter/assembler) 各自的优缺点
- Boolean algebra / K-map：化简后再画电路，不要跳步
:::

---

## 计算题：如何展示 Working

:::note[展示步骤的黄金法则]
**结果可能错，但步骤分不能丢**

1. 每步单独一行，标注步骤编号或箭头 (→)
2. 写清楚每一步的依据（如 "Exponent bias = 127 for single precision"）
3. 关键中间值用 **方框** 或 **下划线** 标出
4. 如果在草稿纸上先演算，誊写时整理成清晰的流水线
:::

**举例示范**（浮点数转十进制）：

```
Step 1: Sign bit = 0 (positive)
Step 2: Exponent bits = 10000011₂ = 131₁₀
Step 3: Actual exponent = 131 - 127 = 4 (bias = 127)
Step 4: Mantissa = 1.0101₂ (加上隐含的 leading 1)
Step 5: Value = 1.0101₂ × 2⁴ = 10101₂ = 21₁₀
```

---

## 伪代码题：语法与命名规范

:::note[剑桥 Pseudocode 规范要点]
- 控制结构：`IF ... THEN ... ELSE ... ENDIF`，`FOR ... TO ... NEXT`，`WHILE ... DO ... ENDWHILE`
- 赋值使用 `←`（题目中写 `=` 通常也可接受）
- 过程/函数定义：`PROCEDURE name(params)` / `FUNCTION name(params) RETURNS datatype`
- 变量命名：**见名知意** — `total`, `counter`, `studentName`，不要用 `x`, `y`, `z`
- 注释用 `//` 或 `{}`
- 数据类型大写：INTEGER, REAL, CHAR, STRING, BOOLEAN, ARRAY
:::

**常见扣分点**：
- 语法错误（如没有匹配的 ENDIF / NEXT）
- 变量名与题目不一致
- 没有处理边界条件（empty list, zero input）
- 递归函数缺少 base case

---

## 解释/描述题：用对 Command Words

:::note[指令词深度对照表]
| Command Word | 要求深度 | 答题结构 |
|-------------|---------|---------|
| **State** | 表层定义 | 一句话，直接回答 |
| **Identify** | 识别 | 一个名词/短语 |
| **List** | 列举 | 按编号逐条列出 |
| **Describe** | 描述 | 2-3 句，说明特征 |
| **Explain** | 解释 | 因果分析，Why + How |
| **Discuss** | 讨论 | 多角度，优缺点对比 |
| **Compare** | 比较 | A vs B 结构，相似点 + 不同点 |
:::

**Explain 题的高分模板**：

> "Topic X 的工作原理是 …（核心机制）…。这会导致 …（直接结果）…，因此 …（更广泛的影响）…。"

---

## 最后 10 分钟：检查清单

:::note[冲刺检查]
- [ ] **每道题都答了** — 没有空白题
- [ ] **计算题有 working** — 步骤完整，没有跳步
- [ ] **单位/进制标注正确** — 二进制有下标 ₂，十六进制有 ₁₆ 或 H
- [ ] **Pseudocode 语法** — 检查 IF/WHILE/FOR 是否闭合，变量名是否一致
- [ ] **画图题** — 标签完整，箭头方向正确，电路门符号正确
- [ ] **字迹清晰** — 如果时间允许，把潦草的地方重写
- [ ] **页码对应** — 答案写在正确的题号位置
- [ ] **圈出最终答案** — 确保阅卷老师一眼能看到你的答案
:::
