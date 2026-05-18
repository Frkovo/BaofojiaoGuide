---
title: 题型总览
sidebar_position: 4
---

Paper 3 共有 **6 种核心题型**，每题 75 分，考试时间 1 小时 30 分钟。以下表格总结了每种题型及其常见分数分配。

| 题型 | 常见分值 | 典型标志词 | 核心考点 |
|------|---------|-----------|---------|
| 1. Calculation & Conversion | 3-8分 | Calculate, Convert, Show working | 浮点数运算、RPN、K-map化简、二进制/十六进制转换 |
| 2. Pseudocode Completion | 4-8分 | Complete the pseudocode, Fill in the blanks | ADT操作、文件处理、搜索/排序算法 |
| 3. Write Pseudocode | 5-12分 | Write pseudocode, Define a procedure/function | OOP类定义、声明式编程、用户定义数据类型 |
| 4. Explain/Describe | 3-6分 | Explain, Describe, Discuss | 概念原理、体系结构、算法复杂度 |
| 5. State/Identify/List | 1-3分 | State, Identify, List, Give | 定义术语、列出差异、指出输出 |
| 6. Draw/Complete Diagram | 3-5分 | Draw, Complete the diagram | 语法图、K-map、逻辑电路 |

---

## 题型 1：Calculation & Conversion

:::note[标准解题方法]
1. 辨认题目要求的格式（如 IEEE 754、Two's complement、RPN）
2. 写出中间步骤（**必须展示 working**，否则会扣分）
3. 最终答案用框框标出（box your answer）
4. 检查单位与精度
:::

**识别方式**：题目包含 *Calculate*, *Convert*, *Evaluate*, *Show your working* 等指令词。

**常见考点**：
- 浮点数表示：Fixed-point → 二进制转换，Normalisation
- RPN (Reverse Polish Notation)：中缀转后缀、表达式树求值
- K-map：化简 SOP 表达式，圈选质蕴涵项
- Bit manipulation：移位、掩码、Two's complement 加减法

**评分模式**：
- 结果正确 + 有 working → 满分
- 结果错误但 working 部分正确 → 得步骤分
- 只写结果不写过程 → 结果错则全扣

---

## 题型 2：Pseudocode Completion

:::note[标准解题方法]
1. 阅读已有的代码框架，理解变量的用途
2. 关注注释中提示的算法逻辑
3. 填空时使用 **正确的 pseudocode 语法**（剑桥官方语法）
4. 注意缩进和语句结束符
:::

**识别方式**：题目提供一个不完整的 pseudocode，要求在空缺处填入正确代码。

**常见考点**：
- ADT (Abstract Data Type) 操作：Stack push/pop、Queue enqueue/dequeue、Linked list 遍历
- File handling：`OpenFile`, `ReadFile`, `WriteFile`, `CloseFile`
- Search & Sort：Linear search、Binary search、Bubble sort、Insertion sort
- Record / Dictionary 的 CRUD 操作

**评分模式**：
- 每个空 1-2 分
- 答案要求语法和语义都正确
- 变量名必须与题目中的一致

---

## 题型 3：Write Pseudocode

:::note[标准解题方法]
1. 分析题目需求，确定输入、处理、输出
2. 写出完整的 procedure/function 定义（包括参数和返回值类型）
3. 使用标准 pseudocode 控制结构（IF, FOR, WHILE, CASE）
4. 数据类型声明清晰
:::

**识别方式**：题目要求 *Write pseudocode for a procedure/function* 或 *Define a class*。

**常见考点**：
- OOP：Class 定义、constructor、getter/setter、inheritance、polymorphism
- Declarative programming：Prolog 式事实与规则的编写
- User-defined data types：ENUM、SET、RECORD 的定义与使用
- Recursive functions：base case + recursive case

**评分模式**：
- 逻辑正确（4-6 分）
- 语法正确（2-3 分）
- 边界条件处理（1-2 分）
- 适当注释（1 分）

---

## 题型 4：Explain / Describe

:::note[标准解题方法]
1. 定位题目关键词（command word + topic keyword）
2. 写出 **至少两个要点**，每个要点包含核心概念 + 简要展开
3. 如果牵涉比较，使用对比结构（A 是 …，而 B 是 …）
4. 必要时举例说明
:::

**识别方式**：题目包含 *Explain*, *Describe*, *Discuss*, *Compare* 等指令词。

**常见考点**：
- 虚拟机与编译器/解释器的区别
- RISC vs CISC 体系结构
- 不同 Sort/Search 算法的时间复杂度与适用场景
- OOP 四大特性的含义与用途
- Declarative vs Imperative 编程范式

**评分模式**：
- 每个有效点 1 分
- 需要 **深度** 而非广度 — 泛泛而谈只能得 1 分
- 使用专业术语加分（如 "polymorphism allows objects of different classes to be treated as objects of a common superclass"）

---

## 题型 5：State / Identify / List

:::note[标准解题方法]
1. 直接从题干中找出重复出现的关键概念
2. 答案尽量简短（一个词或一句话）
3. 按题目要求的数量作答（不要多写，多写不扣分但浪费时间）
4. 如果要求 "State the purpose"，一句话概括功能
:::

**识别方式**：题目包含 *State*, *Identify*, *List*, *Give*, *Name* 等指令词。

**常见考点**：
- 定义术语（如 "Define the term abstraction"）
- 列出 ADT 的操作
- 指出代码的输出结果
- 给出影响算法效率的因素

**评分模式**：
- 每题 1-3 分
- 一个正确的术语或短句即可得分
- 如果写错不扣分（但不建议乱写）

---

## 题型 6：Draw / Complete Diagram

:::note[标准解题方法]
1. 确认题目要求的图形类型
2. 使用铅笔（实际考试）或清晰标记
3. 遵循题目给出的示例格式
4. 标注所有必要的标签和箭头
:::

**识别方式**：题目包含 *Draw*, *Complete the diagram*, *Construct* 等指令词，或者题目区域预留了空白图形。

**常见考点**：
- Syntax diagrams / Railroad diagrams：画 BNF 语法图
- K-map：在图上圈选质蕴涵项
- Logic circuits：用 AND, OR, NOT 门画逻辑电路
- Tree diagrams：画 Binary search tree 或 Expression tree
- State transition diagrams：FSM 的有限状态机图

**评分模式**：
- 图形结构正确（2-3 分）
- 标签正确（1-2 分）
- 完整度（1 分）
