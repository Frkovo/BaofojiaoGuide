---
title: 解题方法
---

# 解题方法

---

## 方法 1：Denary → Floating-point Binary

**适用场景**：给定一个 denary 数（正或负），要求转换为指定 bit 数的 floating-point 格式。

**步骤**：
1. 将**绝对值**转换为 binary（整数部分 ÷2，小数部分 ×2）
2. Normalise：将二进制小数点移动到 mantissa 第一位之后，使前两位不同
   - 正数：0.1xxx...
   - 负数：1.0xxx...
3. 记录 exponent = 移动位数（左移为正，右移为负）
4. 将 mantissa 补齐到指定位数（右边补 0）
5. 如果原数为负，对 mantissa 做 **two's complement**
6. 将 exponent 转换为指定位数的 two's complement

**公式**：
$$\text{Value} = \text{Mantissa} \times 2^{\text{Exponent}}$$

**易错提醒**：
- 小数部分转换时不要忘记继续乘 2 直到精确或循环
- Normalise 后再做 two's complement
- Exponent 也要用 two's complement，不是直接写二进制

---

## 方法 2：Floating-point Binary → Denary

**适用场景**：给定 mantissa 和 exponent 的二进制，求 denary 值。

**步骤**：
1. 检查 mantissa 首位判断正负
2. 如为负数：先做 two's complement（取反加 1）得到绝对值
3. 将 mantissa 从二进制小数转为 denary（各位 × 2⁻¹, 2⁻², ...）
4. 将 exponent 从 two's complement 转为 denary
5. 计算：mantissa_value × 2^exponent

**易错提醒**：
- 负数 mantissa 必须先转回正数再计算，最后加负号

---

## 方法 3：Normalisation 判断与调整

**适用场景**：判断一个 floating-point 数是否 normalised，如不是则 normalise。

**判断条件**：
- **Mantissa 的前两位必须不同**
  - `01` → 正数，已 normalised
  - `10` → 负数，已 normalised
  - `00` 或 `11` → **未 normalised**

**调整步骤**：
1. 将 mantissa 左移直到前两位不同
2. 每左移 1 位，exponent 减 1
3. 检查 exponent 是否超出范围（underflow / overflow）

**公式**：
$$\text{Left shift mantissa by } n \text{ bits} \implies \text{exponent} - n$$

---

## 方法 4：编写 Enumerated Type

**适用场景**：题目要求定义一组固定值的类型。

**语法**：
```plaintext
TYPE TypeName = (Value1, Value2, Value3, ...)
ENDTYPE
```

**要点**：
- 枚举值用逗号分隔
- 值不能重复
- 用于限制变量只能取枚举列表中的值

---

## 方法 5：编写 Composite / Record Type

**适用场景**：题目要求定义一个包含多个字段的复合类型。

**语法**：
```plaintext
TYPE TypeName
  DECLARE field1 : DataType1
  DECLARE field2 : DataType2
  ...
ENDTYPE
```

**Pointer 类型**：
```plaintext
TYPE Node
  DECLARE data : INTEGER
  DECLARE next : ^Node
ENDTYPE
```

**访问字段**：使用 `.` 号：`variable.fieldName`
