---
title: 考前速通
sidebar_position: 8
---

# 考前速通

## 🧮 核心公式速查

### 浮点数标准化（Floating Point Normalisation）

$$ \text{Normalised mantissa: } \begin{cases} 0.1\ldots & \text{positive} \\ 1.0\ldots & \text{negative (two's complement)} \end{cases} $$

$$ \text{Value} = \text{mantissa} \times 2^{\text{actual exponent}} $$

$$ \text{Actual exponent} = \text{stored exponent} - \text{bias} $$

$$ \text{Bias} = 2^{(k-1)} - 1 \quad (k = \text{number of exponent bits}) $$

### 布尔代数（Boolean Algebra）

De Morgan's 定律：

$$ \overline{A + B} = \overline{A} \cdot \overline{B} $$

$$ \overline{A \cdot B} = \overline{A} + \overline{B} $$

常用恒等式：

$$ A + \overline{A} = 1 \quad A \cdot \overline{A} = 0 \quad A + A = A \quad A \cdot A = A $$

$$ A + 1 = 1 \quad A \cdot 0 = 0 \quad A + 0 = A \quad A \cdot 1 = A $$

$$ A + AB = A \quad A(A + B) = A \quad A + \overline{A}B = A + B $$

### 大 O 记号（Big O Notation）

$$ O(1) \prec O(\log n) \prec O(n) \prec O(n \log n) \prec O(n^2) \prec O(2^n) \prec O(n!) $$

| Algorithm | Best | Average | Worst |
|-----------|------|---------|-------|
| Linear Search | $O(1)$ | $O(n)$ | $O(n)$ |
| Binary Search | $O(1)$ | $O(\log n)$ | $O(\log n)$ |
| Bubble Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ |
| Quick Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ |

### 逆波兰表达式（RPN）求值

$$ \text{operand} \rightarrow \text{PUSH to stack} $$

$$ \text{operator} \rightarrow a \leftarrow \text{POP}, b \leftarrow \text{POP}, \text{PUSH}(b \text{ op } a) $$

$$ \text{Conversion (Shunting-yard): operand } \rightarrow \text{output}; \text{ operator } \rightarrow \text{stack} $$

$$ \text{Operator precedence: } () > \text{power} > \times / > + - $$

## 📋 "When you see X, do Y" 决策表

| 题目特征 | 立即行动 |
|---------|---------|
| 给 bit pattern 问 floating point 值 | 分离 sign / mantissa / exponent，注意 bias |
| "Normalise" | 左移 mantissa 直到首位有效，递减 exponent |
| "Denormalise" | 右移 mantissa 填充 0，递增 exponent |
| "Express as..." | 先算绝对值，转为 binary，再确定 mantissa & exponent |
| 化简 Boolean expression | 先尝试 De Morgan's，再用恒等式，最后 K-map |
| "最小化逻辑电路" | K-map 化简，每个 group 是 1/2/4/8/16 个相邻 1 |
| K-map with don't care | X 根据需要当作 0 或 1 来扩大 group |
| "Convert infix to RPN" | 用 Shunting-yard，operator stack 按优先级弹出 |
| "Evaluate RPN" | 遇 operand push，遇 operator pop 2 个，结果 push |
| "Compare algorithms" | 分析 time complexity（最好/平均/最坏） |
| "Binary search" | 检查数组是否 sorted ascending |
| "Trace binary search" | 三列：low / high / mid，更新 mid ← (low+high) DIV 2 |
| "Write recursive..." | 找 base case + recursive case（含参数减小的方向） |
| "Describe OOP concept" | 先写定义再说名 — Class=template, Object=instance, Encapsulation=hiding |
| OOP inheritance | 子类 extends 父类，调用 super.constructor，可 override 方法 |
| OOP polymorphism | Same method name, different behaviour by subclass |
| "Write pseudocode" | 用 CIE 规范：PROCEDURE/FUNCTION, ENDxxx, ← |
| "Describe purpose of..." | 功能 + 输入/输出 + 适用场景 + 优缺点 |
| "Execute assembly instruction" | 弄清 addressing mode（immediate/direct/indirect/indexed） |
| "Explain pipelining" | 取指→译码→执行 重叠，增加 throughput，但有 hazard |
| "Describe validation" | presence check / range check / type check / format check |
| "Describe verification" | 数据是否和源一致 — double entry / visual check / parity |

## ⏱ 时间分配

总分 **75 分**，时长 **1h30（90 分钟）**

$$ \text{约 } 1.2 \text{ 分钟/分} $$

| 阶段 | 内容 | 建议时间 |
|------|------|---------|
| Section A Q1-Q4 | 必修题（约 50 分） | **50 分钟** |
| Section B Q5-Q6 | 二选一（约 25 分） | **25 分钟** |
| 全卷检查 | review & fix | **15 分钟** |

### 时间管理技巧

- 每题 1.2 min/mark，不要在一小题上超过 2× 分值的用时
- Section B 先花 2 分钟读两题，选最有把握的
- 计算题写出 formula 和 intermediate steps — 步骤给分
- 还剩 5 分钟：检查选择题涂卡、答题纸名字、Section B 选项标识

## 🆘 卡壳时怎么办（Panic Checklist）

1. **深呼吸 10 秒**，重新读题 — 很可能漏了关键词
2. **划命令词** — State / Describe / Explain / Calculate / Write 决定答题深度
3. **跳过难题做下一题** — 会做的先做，积累信心
4. **写 partial answer** — 写得出 formula 就有分，写得出定义也有分
5. **画图辅助思考** — stack diagram / trace table / logic circuit 帮助理清思路
6. **检查单位** — bytes vs bits？kB vs KiB？exponent bias 位数？
7. **不要留白** — CIE mark scheme 踩点给分，沾边也可能有 B1
8. **Trace table 卡住** — 假设前几步正确，看规律，推到出错行
9. **Section B 选错了题** — 前 5 分钟内可以切换，不扣分
10. **最后 3 分钟** — 检查答题卡是否填涂、姓名是否写、选项是否标记

## ✅ 考前清单

### 📌 必带物品
- 黑色/蓝色笔 + 2B 铅笔 + 橡皮 + 直尺
- 计算器（CASIO fx-991CW 或同等科学计算器）
- 准考证 + 身份证/护照
- 手表（非智能）

### 📖 必复习主题

- [ ] **Section 13 Data Representation** — 浮点数标准化、range & precision、two's complement、binary/hex 转换
- [ ] **Section 14 Communication** — TCP/IP 协议栈、CSMA/CD、CSMA/CA、router/switch/gateway
- [ ] **Section 15 Boolean Algebra** — De Morgan's、K-map 化简、逻辑门电路、半加器/全加器、D-type flip flop
- [ ] **Section 16 Processor** — Von Neumann vs Harvard、RISC vs CISC、pipelining（hazard）、interrupt handling
- [ ] **Section 17 Assembly** — addressing modes、LMC 指令、tracing 程序
- [ ] **Section 18 Monitoring & Control** — sensor / actuator / ADC / DAC、feedback loop
- [ ] **Section 19 OOP** — class / object / inheritance / encapsulation / polymorphism、constructor、getter/setter
- [ ] **Section 20 Algorithms** — 排序（bubble / quick）、搜索（linear / binary）、递归、RPN、抽象数据类型（stack / queue / linked list）

### 💡 答题策略

- **命令词决定分数分配**：State(1) < Describe(3-4) < Explain(5-6) < Write/Construct(8-10)
- **Always show working** — 计算题步骤分给得很慷慨
- **Definition 题** — 写 keyword 就得分，不要写整段
- **Explain 题** — 用 because / therefore 引出因果关系
- **Describe 题** — 按顺序列步骤，一个动作一行
- **Compare 题** — 用 comparison table（Feature | A | B）+ 总结句
