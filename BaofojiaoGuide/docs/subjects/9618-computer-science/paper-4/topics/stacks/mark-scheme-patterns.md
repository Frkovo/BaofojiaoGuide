---
title: 评分标准模式
sidebar_position: 4
---

# 评分标准模式

## Push Operation（4 marks）

| Mark | 条件 | 说明 |
|------|------|------|
| **M1** | `IF top = maxSize - 1` 或 `IF isFull()` | 正确判断栈满 |
| **M1** | Output ＂Stack Overflow＂ 或相应处理 | 溢出处理 |
| **A1** | `top ← top + 1` | 指针先自增 |
| **A1** | `stack[top] ← item` | 正确赋值 |

## Pop Operation（4 marks）

| Mark | 条件 | 说明 |
|------|------|------|
| **M1** | `IF top = -1` 或 `IF isEmpty()` | 正确判断栈空 |
| **M1** | Output ＂Stack Underflow＂ + Return 特殊值 | 下溢处理 |
| **A1** | `item ← stack[top]` | 正确取值 |
| **A1** | `top ← top - 1` + `RETURN item` | 指针更新且返回值 |

<details>
<summary>评分标准通用规律</summary>

- **M 分（Method）**：逻辑框架、条件判断、错误处理 — 写对结构就有分
- **A 分（Accuracy）**：具体变量名、指针顺序、返回值 — 必须完全准确
- 如果只写了条件判断但没有具体实现 → 拿 M 分但拿不到 A 分
- 如果条件判断错了但后续步骤正确 → **全部不得分**（依赖错误）
</details>

:::note[阅卷要点]
1. 方法分（M）可以重复给 — 条件判断用 `IF top = maxSize` 或 `IF top &gt;= maxSize` 都算 M1
2. 精度分（A）必须完全匹配标准答案 — 指针更新顺序错了全局扣 A 分
3. 如果 procedure 忘记声明 `BYREF` → 通常不扣分（除非题目明确要求声明参数传递方式）
:::
