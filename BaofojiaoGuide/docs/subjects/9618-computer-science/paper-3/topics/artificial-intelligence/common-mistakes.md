---
title: 常见错误
---

# 常见错误

## 错误 1：A* 算法中 g 值计算错误

**错误表现**：误将 g(n) 当作当前边的距离而不是从起点开始的累计距离。

**正确做法**：g(n) = 从起点到当前节点的实际距离总和，而非最后一个边的长度。

---

## 错误 2：混淆 Open list 和 Closed list

**错误表现**：将已经处理过的节点留在 Open list 中导致重复处理，或者错误地将未处理的邻居标记为 Closed。

**正确做法**：
- Open list = 已发现但未处理的节点
- Closed list = 已处理的节点
- 节点一旦进入 Closed list 就不再处理

---

## 错误 3：Dijkstra 算法中使用启发函数

**错误表现**：在 Dijkstra 表格中加入了 h(n) 列。

**正确做法**：Dijkstra 不使用启发函数，只使用实际距离。

---

## 错误 4：机器学习分类混淆

**错误表现**：
- 将 Supervised 和 Unsupervised 搞混
- 认为 Reinforcement Learning 需要 labelled data
- 认为 Deep Learning 是独立的 ML 类型而非 ANN 的子集

**正确做法**：
| 类型 | 关键特征 |
|------|----------|
| Supervised | labelled data, known target output |
| Unsupervised | unlabelled data, find patterns |
| Reinforcement | agent, environment, reward/punishment |
| Deep Learning | multi-layer ANN, feature extraction |

---

## 错误 5：神经网络中忽略激活函数

**错误表现**：描述 ANN 时只提 weighted sum，不提 activation function。

**正确做法**：必须说明 activation function 引入非线性，使网络能够学习复杂的模式。

---

## 错误 6：Back propagation 方向搞反

**错误表现**：认为 back propagation 是从 input 层向 output 层传播。

**正确做法**：Back propagation 是从 output 层向 input 层反向传播误差，用于更新权重。

---

## 错误 7：回答过于笼统

**错误表现**：当被问 "Explain how graphs are used in AI" 时，只写 "Graphs can represent data"。

**正确做法**：需要具体说明 nodes = states, edges = transitions, 用于 search algorithms。

---

## 错误 8：忽略 Follow-through Marks 的利用

**错误表现**：发现前面计算错了就放弃整个题目。

**正确做法**：即使前面错了也要继续，因为 MS 中通常有 follow-through marks（方法正确即可得分）。
