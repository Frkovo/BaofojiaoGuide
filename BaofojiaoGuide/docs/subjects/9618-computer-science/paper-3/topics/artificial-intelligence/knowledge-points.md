---
title: 知识点总结
---

## Graphs in AI — 人工智能中的图

- **Structure**: $G = (V, E)$ where $V$ = nodes/vertices, $E$ = edges/connections
- Each edge may have a **weight** (cost, distance, time)
- **Nodes**: represent states or locations
- **Edges**: represent relationships or transitions between nodes
- Used extensively in **pathfinding** problems (e.g. shortest route, game AI navigation)

:::tip[...]
Graphs are the foundation for both Dijkstra's and A* algorithms.
:::

## A* Algorithm — A* 搜索算法

- Combines **actual cost** and **heuristic estimate**
- Evaluation function: $$f(n) = g(n) + h(n)$$
  - $g(n)$: actual cost from the **start node** to node $n$
  - $h(n)$: **heuristic** estimated cost from node $n$ to the **goal node**
- Uses a priority queue (open set) sorted by $f(n)$
- Maintains a **closed set** of visited nodes to avoid revisiting
- **Optimal** when $h(n)$ is **admissible** (never overestimates true cost)
- More efficient than Dijkstra's when a good heuristic is available

:::warning[...]
A* degenerates to Dijkstra's algorithm if $h(n) = 0$ for all nodes.
:::

## Dijkstra's Algorithm — 迪杰斯特拉算法

- Finds the **shortest path** from a single source to all other nodes
- Uses only $g(n)$ — the actual accumulated cost — no heuristic
- **Guarantees optimal** solution for non-negative edge weights
- Explores nodes in order of increasing distance from the start
- Less efficient than A* in large search spaces (explores uniformly in all directions)

| Feature | A* | Dijkstra |
|---------|----|----------|
| Formula | $f(n) = g(n) + h(n)$ | $g(n)$ only |
| Heuristic | Yes | No |
| Optimal | Yes (if admissible) | Yes |
| Speed | Faster with good heuristic | Slower in large graphs |

## Machine Learning — 机器学习

- **Supervised learning — 监督学习**: trained on **labelled data** (input → expected output)
  - e.g. classification, regression
- **Unsupervised learning — 无监督学习**: trained on **unlabelled data**, finds hidden patterns
  - e.g. clustering, dimensionality reduction
- **Reinforcement learning — 强化学习**: agent learns via **rewards/penalties** from environment
  - e.g. game-playing AI, robotics control

## Deep Learning — 深度学习

- Subset of machine learning using **multi-layer neural networks**
- Automatically performs **feature extraction** from raw data
- Each layer learns progressively higher-level features
- Requires large amounts of data and computational power

## Artificial Neural Networks (ANN) — 人工神经网络

- **Input layer**: receives raw data features
- **Hidden layers**: one or more layers that process and transform data
- **Output layer**: produces the final prediction or classification
- **Weights**: each connection between neurons has an associated weight
- **Activation functions**: introduce non-linearity (e.g. ReLU, Sigmoid, Tanh)
- Forward propagation: data flows from input → hidden → output

## Back Propagation of Errors — 反向传播

- Algorithm for **training** neural networks by adjusting weights
- Steps:
  1. Forward pass: compute output
  2. Calculate error (difference between predicted and actual)
  3. Backward pass: propagate error **backwards** through the network
  4. Update each weight using gradient descent — 梯度下降
- Repeated over many epochs until error is minimised

## Regression Methods — 回归方法

- Used for predicting **continuous values** (not discrete classes)
- **Linear regression**: models relationship as a straight line — $$y = mx + c$$
- **Multiple regression**: uses multiple input features — $$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots$$
- **Polynomial regression**: fits a curved relationship to data
- Evaluation metrics: Mean Squared Error (MSE), R-squared
