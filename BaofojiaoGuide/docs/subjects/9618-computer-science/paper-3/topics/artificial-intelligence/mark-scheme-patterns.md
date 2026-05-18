---
title: 评分标准模式
---

# 评分标准模式（MS Pattern）

## 通用评分模式

### A* / Dijkstra 计算题

| 分类 | 常见表述 | 分值 |
|------|----------|------|
| **M1** | "Correct initialisation" / "Selects correct node" | 1 |
| **M2** | "Correct calculation of distances" | 1-2 |
| **A1** | "Correct final path/distance" | 1 |
| **A2** | "All intermediate values correct" | 1 |
| **B1** | "Correct backtracking" / "Understanding of heuristic" | 1 |

### 机器学习描述题

| 分类 | 常见表述 | 分值 |
|------|----------|------|
| **A1** | "Correct identification of ML type" | 1 |
| **M1** | "Uses labelled/unlabelled data" | 1 |
| **M2** | "Description of learning process" | 1 |
| **B1** | "Appropriate real-world example" | 1 |

### ANN / Deep Learning 解释题

| 分类 | 常见表述 | 分值 |
|------|----------|------|
| **M1** | "Structure: input/hidden/output layers" | 1 |
| **M2** | "Role of weights and activation function" | 1 |
| **A1** | "Forward propagation: input → output" | 1-2 |
| **A2** | "Back propagation: error correction" | 1-2 |
| **B1** | "Need for large data / computational resources" | 1 |

## 关键词汇

| 题目中的指令词 | 要求 | 答题策略 |
|---------------|------|----------|
| **Calculate** | 计算结果 | 列出公式和中间步骤 |
| **Complete** | 填写表格 | 确保每一步的计算正确 |
| **Describe** | 描述特征 | 给出 2-3 个关键特征 |
| **Explain** | 解释原理/机制 | 需要说明 "how" 或 "why" |
| **Identify** | 识别类型 | 一句话给出类型 + "because..." |
| **State** | 陈述 | 简洁直接，不需要详细解释 |
| **Justify** | 证明/给出理由 | 给出具体证据或原因 |

## 常见的 Follow-through Mark

Paper 3 的 MS 经常有 **follow-through marks（跟进分）**：
- 如果上一步的 A* 表格计算错误，但后续回溯路径的方法正确，仍然可以得 B1
- 如果 Dijkstra 的中间值错误，但使用了正确的方法更新距离，仍然可以得 M2

## 错误扣分模式

1. **只写答案不写过程** → 即使答案对了也可能扣方法分
2. **单位/格式错误** → 如距离值没标单位可能扣 1 分
3. **混淆概念** → 如把 Supervised 写成 Unsupervised，整题 0 分
4. **未能区分 A* 和 Dijkstra** → 给 A* 表格加上 h(n) 是必须的，Dijkstra 不允许加
