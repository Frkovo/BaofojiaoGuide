---
title: 题型分析
---

## 1. A* 路径搜索计算（A* Pathfinding）

题型：计算 g / h / f 值表格、找出最短路径、描述 A* 算法步骤

:::note[标准解题方法]

1. **初始化**：将起点放入 Open list，g(start) = 0，h(start) = 启发值，f(start) = g + h
2. **选择**：从 Open list 中选取 f 值最小的节点作为当前节点
3. **扩展**：对当前节点的每个邻居，计算 g(neighbor) = g(current) + distance(current, neighbor)
4. **评估**：
   - 如果邻居不在 Open list，加入并记录 f 值
   - 如果邻居已在 Open list，且新 g 值更小，则更新 g 和 f
5. **Closed list**：处理完当前节点后移入 Closed list
6. **终止**：到达目标节点时结束，回溯路径

:::

:::info[评分标准（MS 模式）]

- **M1**: 正确计算 g 值（初始为 0，后续为路径累加）
- **M2**: 正确使用 h(n) 启发值计算 f = g + h
- **A1**: 最终路径正确
- **B1**: 路径回溯步骤正确

:::

### 示例 1：9618/s23/qp/32 Q10(b)

> A* algorithm is to be used to find the shortest route from node S to node G.
> The heuristic values h(n) for each node are given.
> Complete the table to show the g, h and f values for the nodes explored.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Node S is selected first, g(S)=0, h(S)=5, f(S)=5
- **M2**: Correct g values for A, B, C after expansion
- **A1**: Node G reached with correct f value
- **A2**: Correct path S → A → D → G

**Example values:**
| Node | g | h | f |
|------|---|---|---|
| S | 0 | 5 | 5 |
| A | 2 | 3 | 5 |
| B | 3 | 4 | 7 |
| D | 5 | 1 | 6 |
| G | 7 | 0 | 7 |

</details>

### 示例 2：9618/w21/qp/31 Q9

> A* search is used on the graph below. The heuristic values are shown in brackets.
> Show the order in which nodes are explored and state the final path found.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Correct order of node exploration based on lowest f value
- **M2**: Correct calculation of all g values
- **A1**: Correct final path identified
- **B1**: Understanding that A* uses heuristic to guide search towards goal

**Key marking points:**
- A* considers both actual distance (g) and estimated distance (h)
- The algorithm is guaranteed to find the shortest path if heuristic is admissible
- Nodes in Closed list are not re-explored

</details>

---

## 2. Dijkstra 算法计算（Dijkstra's Algorithm）

题型：计算从起点到所有节点的最短距离、填写距离表格

:::note[标准解题方法]

1. **初始化**：起点距离为 0，其他节点距离为 ∞
2. **选择未访问节点中距离最小的节点**
3. **松弛操作**：对于当前节点的每个邻居，如果 `distance[current] + weight(current, neighbor) < distance[neighbor]`，则更新
4. **标记当前节点为已访问**
5. 重复步骤 2-4，直到所有节点都被访问

:::

:::info[评分标准（MS 模式）]

- **M1**: 正确初始化距离值（起点 0，其余 ∞）
- **M2**: 每次选择未访问节点中距离最小的节点
- **A1**: 所有节点的最终距离正确
- **B1**: 在距离更新时记录前驱节点

:::

### 示例 1：9618/s21/qp/31 Q5(a)

> Dijkstra's algorithm is used to find the shortest path from node A to all other nodes. Complete the table showing the distances after each iteration.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Initial distance to A = 0, all others = infinity
- **M2**: First iteration selects A, updates distances to B, C, D
- **A1**: Correct final distances to all nodes
- **B1**: Shows understanding that visited nodes are not revisited

**Example values:**
| Node | Dist | Prev |
|------|------|------|
| A | 0 | - |
| B | 4 | A |
| C | 2 | A |
| D | 5 | C |
| E | 7 | D |

</details>

### 示例 2：9618/w23/qp/32 Q8

> Apply Dijkstra's algorithm to the following graph to find the shortest distance from node P to node T. Show all working.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Correct initialisation table
- **M2**: Correct sequence of node selections
- **A1**: Final shortest distance value to T
- **A2**: All intermediate distances correctly updated

**Common marking points:**
- Dijkstra does NOT use heuristic values
- Each node is processed exactly once
- Algorithm fails with negative edge weights

</details>

---

## 3. 机器学习分类（Machine Learning Categories）

题型：判断机器学习类型、描述不同类型的特点和区别

:::note[标准解题方法]

**Supervised Learning（监督学习）**
- 使用 labeled training data（已标注数据）
- 输入和期望输出都已知
- 典型算法：Linear Regression, Decision Tree, Neural Network
- 例子：图片分类（给定已标注的猫狗图片）

**Unsupervised Learning（无监督学习）**
- 使用 unlabeled data（无标注数据）
- 让模型自己发现数据中的模式或结构
- 典型算法：K-means Clustering, PCA
- 例子：客户分群（根据购买行为自动分组）

**Reinforcement Learning（强化学习）**
- Agent 通过与环境交互学习
- 通过 reward / punishment 机制优化策略
- 典型算法：Q-learning, Deep Q Network
- 例子：AI 玩 Atari 游戏

**Deep Learning（深度学习）**
- 使用多层神经网络（multiple hidden layers）
- 自动提取特征（feature extraction）
- 需要大量数据和计算资源
- 例子：图像识别、自然语言处理

:::

:::info[评分标准（MS 模式）]

- **M1**: 正确识别 ML 类型
- **M2**: 给出关键特征（labeled/unlabeled data, reward 等）
- **A1**: 给出恰当的 real-world example
- **B1**: 对比说明与其他类型的区别

:::

### 示例 1：9618/s23/qp/31 Q2(a)

> A company uses an AI system to classify customer reviews as positive or negative. The system was trained using 10,000 reviews that had been manually classified.
> Identify the type of machine learning used and justify your answer.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **A1**: Supervised learning
- **M1**: The training data is labelled (positive/negative)
- **M2**: The system learns to map inputs to known outputs
- **B1**: Each review has a known correct classification

</details>

### 示例 2：9618/w22/qp/32 Q7

> Describe the differences between supervised learning and unsupervised learning. Give an appropriate application for each.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Supervised uses labelled data, unsupervised uses unlabelled data
- **M2**: Supervised has known output, unsupervised finds hidden patterns
- **A1**: Appropriate application of supervised (e.g. spam detection)
- **A2**: Appropriate application of unsupervised (e.g. customer segmentation)

</details>

---

## 4. 神经网络与深度学习（Neural Networks / Deep Learning）

题型：解释 ANN 结构、解释 back propagation 和权重更新、解释深度学习

:::note[标准解题方法]

**ANN 的核心结构**
- **Input layer**：接收原始数据
- **Hidden layer(s)**：通过 weighted connections 和 activation function 处理数据
- **Output layer**：输出结果

**Forward propagation（前馈）**
- 数据从 input 经 hidden 到 output 方向传播
- 每个 neuron 计算 `weighted sum = Σ(weight × input) + bias`
- 通过 activation function（如 Sigmoid, ReLU）引入非线性

**Back propagation（反向传播）**
- 计算 output 和 expected output 的误差
- 从 output 层向 input 层反向传播误差
- 使用 gradient descent 更新 weights
- 目的是最小化误差

**Deep Learning 的特点**
- 多个 hidden layers（≥ 2 layers）
- 自动特征提取，无需手工设计特征
- 需要大量训练数据和计算资源（GPU）

:::

:::info[评分标准（MS 模式）]

- **M1**: 正确描述 ANN 结构（input / hidden / output layers）
- **M2**: 解释 weighted connections 和 activation function 的作用
- **A1**: 理解 Back propagation 更新权重的过程
- **B1**: 解释 Deep Learning 需要大量数据的原因（multiple layers 需要大量参数，容易过拟合）

:::

### 示例 1：9618/w23/qp/31 Q12

> Explain how an artificial neural network (ANN) can be used to enable machine learning. Include in your answer the role of hidden layers, weights and the activation function.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: ANN consists of input, hidden, and output layers of neurons
- **M2**: Each connection between neurons has a weight that is adjusted during training
- **M3**: Hidden layers allow the network to learn complex/non-linear patterns
- **A1**: Activation function introduces non-linearity and determines neuron output
- **A2**: Forward propagation calculates output; back propagation adjusts weights based on error
- **B1**: Training involves minimising error function through iterative weight updates

</details>

### 示例 2：9618/s24/qp/31 Q9

> Describe what is meant by deep learning. Explain why deep learning typically requires a large amount of training data.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Deep learning uses ANNs with multiple hidden layers
- **M2**: Each layer extracts progressively higher-level features
- **A1**: Large amount of data needed because of the large number of parameters/weights to train
- **A2**: More data helps prevent overfitting
- **B1**: Deep learning models are more complex and require more examples to generalise well

</details>

---

## 5. 图在 AI 中的应用（Graphs in AI）

题型：解释图在 AI 中的用途、将图与状态空间搜索联系

:::note[标准解题方法]

**图在 AI 中的主要用途**
- **State space representation**：节点表示状态，边表示动作转换
- **Search problems**：A*、Dijkstra 等算法在图上搜索
- **Knowledge representation**：语义网络（semantic networks）中节点表示概念，边表示关系
- **Decision trees**：节点表示决策点，分支表示可能结果

:::

:::info[评分标准（MS 模式）]

- **M1**: 图可以表示状态和转换（nodes = states, edges = transitions）
- **A1**: AI 问题可以建模为在图中找路径
- **B1**: 搜索算法在图结构上运行
- **B2**: 图有效表示复杂关系

:::

### 示例 1：9618/s21/qp/31 Q5(b)

> Explain why graphs are used in artificial intelligence.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Graphs can represent states/nodes and transitions/edges
- **M2**: AI problems can be modelled as finding a path from start state to goal state
- **A1**: Search algorithms (A*, Dijkstra) operate on graph structures
- **B1**: Graphs allow efficient representation of complex relationships

</details>

---

:::warning[常见陷阱]

- 忘记计算 g 的累加值：g 是从起点到当前节点的实际距离，不是当前边的长度
- 忽略 f 值相同时的处理：f 值相同时通常按字母顺序或题目指定方式选择
- 路径回溯错误：必须从目标节点反向追踪 parent 节点
- 混淆 g 和 h：g 是实际距离（已知），h 是启发估计值（题目给定）
- Dijkstra 不使用启发函数：不要添加 h 值
- 仅更新未访问节点的距离
- 处理负权边时 Dijkstra 不适用
- 忘记标记已访问节点
- 混淆 Supervised 和 Unsupervised：关键区别在于是否使用 labeled data
- Reinforcement Learning 不等于 Supervised Learning：RL 没有 labeled data，而是通过 reward 学习
- Deep Learning 不是独立的 ML 类型：它是使用深层神经网络的子集
- 忘记提及 activation function 的非线性作用：没有激活函数，多层网络等同于单层
- 混淆 forward propagation 和 back propagation：前者计算输出，后者更新权重
- Deep Learning 与 ANN：所有 Deep Learning 都用 ANN，但不是所有 ANN 都是 Deep Learning
- 图在 AI 中的回答过于笼统：要具体到 state space 和 search
- 混淆图和树：图可以有环（cycles），树没有

:::
