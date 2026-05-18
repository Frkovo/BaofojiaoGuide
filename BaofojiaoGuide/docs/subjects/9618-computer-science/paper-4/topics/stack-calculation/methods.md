---
title: "解题方法"
---

# 解题方法

---

## 标准解法步骤

### Step 1 — 弹出第一个值作为 total

```
total ← POP(stack)
```

- 如果栈为空 → total 为 0（罕见，但需注意）

### Step 2 — 循环处理剩余元素

```
WHILE stack 非空
    op ← POP(stack)      // 弹出运算符
    val ← POP(stack)      // 弹出操作数
    IF op = '+' THEN total ← total + val
    IF op = '-' THEN total ← total - val
    IF op = '*' THEN total ← total * val
    IF op = '/' THEN total ← total / val
ENDWHILE
```

---

## Trace Table 写法

建议按以下格式记录：

| Step | Popped | Total | Working        |
|------|--------|-------|----------------|
| 1    | 5      | 5     | 5              |
| 2    | 12     | 5     | wait           |
| 3    | +      | 17    | 5 + 12 = 17    |
| 4    | 3      | 17    | wait           |
| 5    | *      | 51    | 17 * 3 = 51    |

关键：**不要省略 working 列**——这是判卷时 **M1–M5** 得分的直接依据。

---

## 技巧总结

1. **先弹先算**：第一个弹出值 = `total`，不是等待运算符。
2. **每次运算符 + 一个操作数**：弹出 `+` 后，**再弹一个数字**，做运算。
3. **最终结果**：栈被清空时的 `total` 即为答案。
4. **检查方向**：`-` 和 `/` 顺序敏感——`total - val` 而非 `val - total`。

---

## 示例

<details>
<summary>9618/s25/qp/42 Q1e — Stack: top `5` → `12` → `+` → `3` → `*`</summary>

| Step | Popped | Total | Working      |
|------|--------|-------|--------------|
| 1    | 5      | 5     | total = 5    |
| 2    | 12     | 5     | wait         |
| 3    | +      | 17    | 5 + 12 = 17  |
| 4    | 3      | 17    | wait         |
| 5    | *      | 51    | 17 * 3 = 51  |

Final answer: **51**
</details>

<details>
<summary>9618/w24/qp/42 Q1d — Stack: top `10` → `3` → `-` → `2` → `*`</summary>

| Step | Popped | Total | Working      |
|------|--------|-------|--------------|
| 1    | 10     | 10    | total = 10   |
| 2    | 3      | 10    | wait         |
| 3    | -      | 7     | 10 - 3 = 7   |
| 4    | 2      | 7     | wait         |
| 5    | *      | 14    | 7 * 2 = 14   |

Final answer: **14**
</details>

---

## 相关页面

- [题型分析](question-types.md)
- [评分标准模式](mark-scheme-patterns.md)
- [常见错误](common-mistakes.md)
