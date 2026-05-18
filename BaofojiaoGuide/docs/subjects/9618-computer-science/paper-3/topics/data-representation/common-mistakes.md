---
title: 常见错误
---

# 常见错误

## 错误 1：Two's Complement 转换错误
**问题**：对负数直接写 mantissa 而不是先做 two's complement。
**正确做法**：先写出对应正数的 mantissa，再取反加一。
**示例**：-7.25 → 先做正数 mantissa `0111010000`，再取反加一 → `1000110000`

## 错误 2：忘记 Normalise 或 Normalise 方向错误
**问题**：没有将二进制小数点移动到 mantissa 前两位不同。
**正确做法**：移动二进制小数点使 mantissa 在 `0.1xxx`（正）或 `1.0xxx`（负），相应调整 exponent。

## 错误 3：精度（Precision）与准确度（Accuracy）混淆
**问题**：将浮点数误差归因为 accuracy 而不是 precision。
**注意**：Floating-point 的误差是因为 **precision 有限**（finite number of bits for mantissa），不是 accuracy 问题。
- **Precision**：能表示的有效位数 → 位数不足时丢失精度
- **Accuracy**：与实际值的接近程度

## 错误 4：TYPE 语法错误
**问题**：
- 枚举类型漏写括号 `TYPE Day = Monday, Tuesday` ❌
- 复合类型漏写 `DECLARE` 关键字
- 忘记 `ENDTYPE`
**正确**：
```plaintext
TYPE Day = (Monday, Tuesday)  ✓
TYPE Student
  DECLARE name : STRING
ENDTYPE                        ✓
```

## 错误 5：文件存取方法混淆
**问题**：Serial 和 Sequential 混为一谈。
**区别**：
- **Serial**：按到达顺序存储，**没有排序**，查找需要遍历
- **Sequential**：按 key 排序存储，查找可用二分搜索
- **Random**：任意位置直接访问（通过 hash 或索引）

## 错误 6：Hash Collision 处理遗漏
**问题**：计算 hash 后遇到冲突没有继续 probing，或 probing 超出表长没有 wrap around。
**正确做法**：Linear probing → `(hash + i) mod table_size`，i = 0, 1, 2, ...
