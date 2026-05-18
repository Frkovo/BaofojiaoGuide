---
title: 考试结构
sidebar_position: 3
---

# 考试结构 — Paper 3 (Advanced Theory)

## 试卷概况

| 项目 | 详情 |
|------|------|
| 试卷代码 | 9618/32（部分考季以 9618/31 编号） |
| 名称 | Advanced Theory |
| 时长 | 1 小时 30 分钟 |
| 满分 | 75 |
| 题目数量 | 约 10–12 题，全部必答 |
| 题型 | 简答、计算、解释、伪代码编写、算法跟踪、电路设计、布尔化简 |
| 计算器 | **不允许使用** |
| 参考材料 | 不提供公式表 |
| 答题方式 | **试卷上作答**，所有答案手写 |

## 各章节历年分值分布（2021–2025 年分析）

以下分值为综合分析 2021–2025 年历年试卷得出的典型范围，单次考试可能有小幅波动。

| 章节 | Topic | 典型分值 | 常见题号位置 | 出现频率 |
|------|-------|---------|-------------|---------|
| 13 | Data Representation | 8–12 | Q1–Q2 | 必考 |
| 14 | Communication and Internet Technologies | 6–10 | Q3–Q4 | 必考 |
| 15 | Hardware and Virtual Machines | 10–14 | Q4–Q6 | 必考 |
| 16 | System Software | 6–9 | Q5–Q7 | 必考 |
| 17 | Security | 4–6 | Q7–Q8 | 常考 |
| 18 | Artificial Intelligence | 4–6 | Q8–Q9 | 常考 |
| 19 | Computational Thinking and Problem Solving | 12–18 | Q9–Q11 | 必考（分值最高） |
| 20 | Further Programming | 8–12 | Q10–Q12 | 必考 |

:::note[分值规律]
Section 19（算法与 ADT）通常是试卷中分值最高的部分（12–18 分），常出现在试卷后半部分，需要较多书面解释和伪代码编写。
:::

## 题型分布

| 题型分类 | 典型分值 | 说明 |
|---------|---------|------|
| 计算题（Calculation） | 15–20 | 浮点数运算、布尔化简、K-map、数值转换、地址计算 |
| 解释题（Explain/Describe） | 20–25 | 解释概念、描述过程、比较差异 |
| 简答题（State/Define/Identify） | 10–15 | 陈述定义、列举特征、识别内容 |
| 伪代码题（Pseudocode/Write） | 10–15 | 编写算法、实现 ADT 操作、OOP 类定义 |
| 算法跟踪题（Trace/Complete） | 5–8 | Trace table 填充、补全算法步骤 |
| 画图题（Draw） | 5–7 | 逻辑电路图、K-map 圈组、数据结构示意图、流程图 |

## Mark Scheme 评分符号含义

CIE Paper 3 的 Mark Scheme 使用统一的评分符号，理解符号有助于判断答题得分点：

| 符号 | 含义 | 说明 |
|------|------|------|
| M1 | Method mark | 选择了正确的方法/公式，即使最终答案错误也获得 |
| A1 | Accuracy mark | 答案或结果完全正确（常依赖于前序 M1 成立） |
| B1 | Independent mark | 独立得分点，不依赖其他步骤正确即可得分 |
| E1 | Explanation mark | 解释正确，使用了恰当的专业术语 |
| C1 | Communication mark | 表达清晰、结构合理、使用了正确的符号与格式 |
| (M1) | Dependent method | 括号无 mark：仅作为前序步骤的辅助解释，不单独给分 |
| A1 ft | Follow through | 使用前序错误的计算结果继续推理，逻辑正确即可得分 |

:::warning[关键提醒]
- 仅写出最终答案而不展示过程：即使答案正确也可能只得到 B1 而非 M1 + A1
- Show your working 的题目——过程和答案缺一不可
- "ft"（follow through）在近年 Mark Scheme 中大量出现，说明**分步给分**是评分核心逻辑
:::

## 常见 Mark Scheme 模板示例

### 浮点数计算（典型 4 分）
```
M1: Align exponents correctly
A1: Correct aligned mantissa
M1: Perform addition/subtraction
A1: Correct normalised result
```

### 布尔代数化简（典型 3 分）
```
B1: Apply De Morgan's law correctly
B1: Apply distributive/absorption law
A1: Final simplified expression
```

### ADT 操作伪代码（典型 5 分）
```
M1: Correct method signature and parameters
A1: Correct base case handling
M1: Correct recursive/iterative logic
A1: Correct return value
B1: Appropriate use of data structure operations
```

## 答题格式要求

| 要求 | 说明 | 反例 |
|------|------|------|
| CIE Pseudocode 规范 | 使用 `←` 赋值、`OUTPUT` 输出、`RETURN` 返回 | 不要用 `=` 赋值、`print` 输出 |
| 展示计算过程 | 写出每一步推导 | 直接写最终答案 |
| 标注单位（如适用） | 浮点数结果无需单位，但地址计算等需指明进制 | 忘写 `(base 2)` 或 `(hex)` |
| K-map 圈组标记 | 用圆圈或方框标明 prime implicant 组合 | 只写结果不标圈组 |
| 逻辑电路画图 | 使用标准 gate 符号（AND, OR, NOT, NAND, NOR, XOR） | 自创符号 |
| 算法跟踪表格 | 绘制 trace table，每列对应一个变量 | 只用文字描述变化 |
| 定义题 | 给出完整定义，包含关键术语 | 零散关键词堆砌 |

## 时间分配建议

| 阶段 | 用时 | 任务 |
|------|------|------|
| 浏览全卷 | 2–3 min | 快速阅读所有题目，标记知识点归属 |
| 第 1 轮：易题 | 30–35 min | 完成计算题、简答题、定义题等分值明确且耗时短的题目 |
| 第 2 轮：中难题 | 35–40 min | 伪代码编写、算法分析、多步解释题 |
| 第 3 轮：检查 | 10–15 min | 复查符号、伪代码语法、进位/借位/精度、逻辑化简正确性 |

:::tip[Exam Day 提醒]
- 不带计算器
- 携带直尺（用于画逻辑电路、K-map、流程图）
- 携带黑色/蓝色笔 + 铅笔（画图用）
- 所有公式、定律必须靠记忆
:::
