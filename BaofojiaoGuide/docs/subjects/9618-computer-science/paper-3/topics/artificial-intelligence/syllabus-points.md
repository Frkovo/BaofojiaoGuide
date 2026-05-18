---
title: 教学大纲要点
---

# Section 18: Artificial Intelligence

## 18.1 Graphs in Artificial Intelligence

- 理解图（Graph）如何用于表示 AI 问题
- 节点（Nodes）表示状态，边（Edges）表示转换
- 图搜索算法（A*, Dijkstra）的应用

## 18.2 Search Algorithms

### A* Algorithm
- 使用 evaluation function: $$f(n) = g(n) + h(n)$$
- g(n): actual cost from start to node n
- h(n): heuristic estimated cost from n to goal
- Open list 和 Closed list 的管理
- 启发函数的可采纳性（admissibility）

### Dijkstra's Algorithm
- 寻找从起点到所有节点的最短路径
- 不使用启发函数（与 A* 的区别）
- 适用于非负权边

## 18.3 Artificial Neural Networks

- 生物神经元的类比（dendrites, axon, synapse → inputs, processing, outputs）
- ANN 结构：Input layer, Hidden layer(s), Output layer
- Weighted connections 和 Bias
- Activation function（如 Sigmoid, ReLU, Tanh）
- Forward propagation
- Back propagation（误差反向传播 + 梯度下降更新权重）
- 多层网络即 Deep Learning

## 18.4 Machine Learning

| 类型 | 数据 | 目标 | 典型应用 |
|------|------|------|----------|
| Supervised learning | Labelled data | 学习输入到输出的映射 | 分类、回归 |
| Unsupervised learning | Unlabelled data | 发现数据中的模式 | 聚类、降维 |
| Reinforcement learning | 环境交互（reward） | 最大化累积奖励 | 游戏、机器人控制 |

## 18.5 Deep Learning

- 使用多层（>2 层）的 ANN
- 自动特征提取（Automatic feature extraction）
- 需要大量数据（避免过拟合、训练大量参数）
- 需要高性能计算资源（GPU）

## 18.6 Back Propagation Algorithm

- 计算输出层误差：$$\delta_{output} = (y_{pred} - y_{true}) \times f'(z)$$
- 反向传播：$$\delta_{hidden} = W^T \times \delta_{output} \times f'(z)$$
- 权重更新：$$W_{new} = W_{old} - \alpha \times \delta \times input$$
- $\alpha$ = learning rate（学习率）
- 迭代进行直到误差收敛
