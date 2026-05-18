---
title: 方法总结
---

# 方法总结

## A* 算法计算步骤

```
1. 初始化：
   Open list = {start}
   g(start) = 0
   f(start) = g(start) + h(start)

2. 循环：
   a. 从 Open list 选取 f 值最小的节点 n
   b. 将 n 从 Open list 移到 Closed list
   c. 如果是目标节点，停止并回溯路径
   d. 对 n 的每个邻居 m：
      - tentative_g = g(n) + distance(n, m)
      - 若 m 在 Closed list 中，跳过
      - 若 m 不在 Open list 中或 tentative_g < g(m)：
        更新 g(m) = tentative_g
        更新 f(m) = g(m) + h(m)
        设置 parent(m) = n
        将 m 加入 Open list（若不在）
```

### 表格填写模板

| Node | g(n) | h(n) | f(n) | Parent |
|------|------|------|------|--------|
| S | 0 | 5 | 5 | - |
| A | 2 | 3 | 5 | S |
| B | 4 | 4 | 8 | A |

### 关键公式

$$f(n) = g(n) + h(n)$$

---

## Dijkstra 算法计算步骤

```
1. 初始化：
   dist[start] = 0
   dist[其他节点] = ∞
   visited = {}

2. 循环直到 visited 包含所有节点：
   a. 选取未访问节点中 dist 最小的节点 u
   b. 将 u 加入 visited
   c. 对 u 的每个邻居 v：
      如果 dist[u] + weight(u, v) < dist[v]：
        更新 dist[v] = dist[u] + weight(u, v)
        prev[v] = u
```

### 表格填写模板

| Iteration | Current | A | B | C | D | E |
|-----------|---------|---|---|---|---|---|
| 0 | - | 0 | ∞ | ∞ | ∞ | ∞ |
| 1 | A | - | 4 | 2 | ∞ | ∞ |
| 2 | C | - | 3 | - | 5 | ∞ |
| 3 | B | - | - | - | 5 | 8 |

---

## 机器学习四分类识别方法

| 特征/线索词 | 类型 |
|-------------|------|
| "labelled data", "known output", "classified", "training set with correct answers" | Supervised |
| "unlabelled data", "find patterns", "group", "cluster", "no target output" | Unsupervised |
| "agent", "environment", "reward", "punishment", "trial and error", "game" | Reinforcement |
| "multiple hidden layers", "deep neural network", "automatic feature extraction" | Deep Learning |

---

## ANN 结构速记

```
Input Layer (features)
    ↓
Hidden Layer(s) — weighted sum → activation function → output
    ↓
Output Layer (prediction)
    ↓
Error calculation → Back propagation → Weight update
```
