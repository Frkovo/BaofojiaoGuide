---
title: "考纲要点"
---

# 考纲要点

---

## Section 19.1 — Programming Paradigms

### 相关考纲条目

> **19.1.1** 理解并使用 procedural programming 进行 input validation

### 具体要求

- 能够为不同类型的输入编写 validation 代码：
  - **Range check**: 验证数值是否在允许范围内
  - **Type check**: 验证输入是否为预期的数据类型（如 `ISNUMERIC`）
  - **Length check**: 验证字符串长度是否符合要求（如密码至少 8 位）
  - **Presence check**: 验证输入不为空
  - **Format check**: 验证输入格式（如正则表达式匹配）
- 理解 validation 需要结合 loop 结构重复提示直到输入合法
- 能够使用 boolean flag 控制 validation loop 的退出

---

## Section 20.2 — Error Handling & Testing

### 相关考纲条目

> **20.2.2** 区分 validation 与 verification  
> **20.2.3** 理解 validation 在 robust programming 中的作用

### 具体要求

- **Validation（验证）**：检查数据是否符合预定义的规则/约束
  - 例：年龄不能为负，邮编格式正确
  - **目的**：防止无效数据进入系统
- **Verification（核实）**：检查数据是否准确反映了原始来源
  - 例：double entry（两次输入对比），visual check（目视核对）
  - **目的**：确保数据转录的准确性
- Robust program 应该在输入端进行多重 validation，而非仅在数据处理阶段报错
- Validation 不能替代 verification，两者是互补的质量保证手段

---

## 常见考法对照

| 考纲条目 | 对应题型 | 典型分值 |
|----------|----------|----------|
| 19.1 range check | Q1: Input range validation | 2–5 |
| 19.1 type/length/presence check | Q3: Validation with loop | 3–5 |
| 19.1 check digit | Q2: Check digit | 4–6 |
| 20.2 validation vs. verification | 简答题 | 2 |
| 20.2 robust programming | 结合 error handling 大题 | 3–4 |

---

## 与 Paper 1 的区别

Paper 4 的数据验证侧重**代码实现**，而非理论定义：

- Paper 1 问：什么是 validation？列举三种 validation 类型。
- Paper 4 问：编写代码验证用户输入年龄在 0–120 之间，不合法则重新提示输入。

> 备考重点：**手写伪代码**能力，特别是 loop + flag + 多重条件的组合写法。
