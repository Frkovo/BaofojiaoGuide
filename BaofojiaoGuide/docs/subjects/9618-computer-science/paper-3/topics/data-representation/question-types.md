---
title: 题型分析
---

# 题型分析：Data Representation

---

## 题型 1：浮点数 Normalisation / Denary 转换

### 题目特征

- 给出一个浮点数格式（如 10-bit mantissa + 6-bit exponent，均为 two's complement）
- 要求将 denary 数转换为 floating-point 格式
- 将 floating-point 数转换为 denary
- 判断是否 normalised，如不是则 normalise
- 判断 underflow / overflow

:::note[标准解题方法]

1. Denary → Floating-point：
   - 将绝对值转换为 binary（整数部分 + 小数部分）
   - Normalise：移动二进制小数点，使 mantissa 在 0.1 到 1（或 -1 到 -0.5）之间
   - 记录指数为移动的位数
   - 补全 mantissa 到指定位数
   - 如原数为负数，对 mantissa 取 two's complement
   - 将指数转换为指定位数的 two's complement

2. Floating-point → Denary：
   - 检查 mantissa 首位：0 为正数，1 为负数
   - 如为负数，对 mantissa 取 two's complement 得到绝对值
   - 计算二进制小数数值
   - 指数转换：two's complement 转 denary
   - 最终值 = mantissa 值 × 2^exponent

:::

:::info[评分标准（MS 模式）]

- **M1**：正确将绝对值转换为 binary
- **M1**：正确 normalise（移动小数点并记录指数）
- **A1**：正确写出正数 mantissa
- **A1**：正确对负数 mantissa 取 two's complement
- **A1**：正确写出 exponent
- **B1**：正确计算浮点数转 denary 的 final value

:::

### 典型例题 1：9618/s21/qp/31 Q1

> Convert -7.25 to a floating-point number with 10-bit mantissa and 6-bit exponent. Both are in two's complement.

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：正确将 7.25 转换为 binary 111.01
- **M1**：正确 normalise 为 0.11101 × 2³
- **A1**：正确正数 mantissa (positive) 0111010000
- **A1**：正确 two's complement mantissa 1000110000
- **A1**：正确 exponent 000011

</details>

### 典型例题 2：浮点数转 Denary

> A floating-point number uses 8-bit mantissa and 8-bit exponent in two's complement. Mantissa = `01010000`, Exponent = `00000010`. Find the denary value.

<details>
<summary>📝 MS 展开查看</summary>

- **M1**：正确识别 mantissa 为正数
- **M1**：正确计算 mantissa 的二进制小数
- **M1**：正确将 exponent 转为 denary
- **A1**：最终答案 2.5

</details>

---

## 题型 2：用户自定义数据类型（User-defined Data Types）

### 题目特征

- 要求定义 enumerated type / pointer type / record type
- 要求用 pseudocode 实现数据操作

:::note[标准解题方法]

1. Enumerated TYPE：`TYPE TypeName = (Value1, Value2, Value3, ...) ENDTYPE`
2. Composite TYPE：用 `TYPE ... DECLARE ... ENDTYPE` 结构
3. Pointer type：用 `^TypeName` 声明指针
4. 注意语法格式：严格遵循 Pseudocode 风格

:::

:::info[评分标准（MS 模式）]

- **B1**：正确 `TYPE ... = (...)` 枚举语法
- **B1**：正确使用枚举值
- **B1**：正确 `TYPE ... DECLARE ... ENDTYPE` 复合类型语法
- **B1**：正确声明 pointer type `^TypeName`

:::

### 典型例题 1：9618/s21/qp/31 Q2

> A program needs to store days of the week and details of club meetings.
> - Define an enumerated type `SchoolDay` representing Monday to Friday.
> - Define a composite type `Weekend` representing Saturday and Sunday.
> - Define a composite type `ClubMeet` to store club name (STRING), day (SchoolDay), start time (INTEGER), and a pointer to next meeting.

```
TYPE SchoolDay = (Monday, Tuesday, Wednesday, Thursday, Friday)
ENDTYPE

TYPE Weekend
  DECLARE Saturday : BOOLEAN
  DECLARE Sunday : BOOLEAN
ENDTYPE

TYPE ClubMeet
  DECLARE clubName : STRING
  DECLARE day : SchoolDay
  DECLARE startTime : INTEGER
  DECLARE nextMeet : ^ClubMeet
ENDTYPE
```

<details>
<summary>📝 MS 展开查看</summary>

- **B1**：正确 `TYPE ... = (...)` 语法
- **B1**：正确使用枚举值（Monday-Friday）
- **B1**：正确 `TYPE ... DECLARE ... ENDTYPE` 语法
- **B1**：正确声明 pointer type `^ClubMeet`

</details>

### 典型例题 2：自定义数据类型综合

> A library system needs to store book information. Define:
> - An enumerated type `Genre` with values: Fiction, NonFiction, Reference, Periodical
> - A composite type `Book` with fields: title (STRING), author (STRING), genre (Genre), ISBN (STRING)

```
TYPE Genre = (Fiction, NonFiction, Reference, Periodical)
ENDTYPE

TYPE Book
  DECLARE title : STRING
  DECLARE author : STRING
  DECLARE genre : Genre
  DECLARE ISBN : STRING
ENDTYPE
```

<details>
<summary>📝 MS 展开查看</summary>

- **B1**：正确 `TYPE ... = (...)` 语法
- **B1**：正确使用枚举值
- **B1**：正确 `TYPE ... DECLARE ... ENDTYPE` 语法
- **B1**：正确声明所有字段及其数据类型

</details>

---

## 题型 3：文件组织方式（File Organisation）

### 题目特征

- 比较 serial / sequential / random 三种文件组织方式
- 给出每种方式的使用场景举例
- 讨论各自的优缺点

:::note[标准解题方法]

1. Serial：按到达顺序存储记录，无排序；读取需逐个搜索
2. Sequential：按 key 顺序存储记录，读取按 key 顺序进行；适合批处理
3. Random：通过 key 直接访问任意记录；使用 hash function 或 index
4. 理解各方式对应的存储介质特点（sequential → tape，random → disk）

:::

:::info[评分标准（MS 模式）]

- **B1**：正确描述 serial 的定义与使用场景
- **B1**：正确描述 sequential 的定义与使用场景
- **B1**：正确描述 random 的定义与使用场景

:::

### 典型例题 1：9618/w23/qp/31 Q4

> Describe the differences between serial, sequential, and random file access methods. Give an example of when each would be used.

<details>
<summary>📝 MS 展开查看</summary>

| Method | Description | Example |
|--------|-------------|---------|
| Serial | Records stored in order of arrival; no sorting; reading requires searching through all records | Log file, backup file |
| Sequential | Records stored in key order; reading is sequential by key; efficient for batch processing | Payroll processing, bank statements |
| Random | Direct access to any record by key; uses hash function or index | Database system, airline reservation |

- **B1**：正确描述 serial 的定义与使用场景
- **B1**：正确描述 sequential 的定义与使用场景
- **B1**：正确描述 random 的定义与使用场景

</details>

### 典型例题 2：文件组织方式应用

> A company maintains a customer database. Explain which file organisation method would be most suitable for the following scenarios and why:
> (a) Generating monthly bills for all customers
> (b) Looking up a single customer's details by account number

<details>
<summary>📝 MS 展开查看</summary>

- **B1**：(a) Sequential file organisation — 所有客户需要按顺序处理，高效批处理
- **B1**：Sequential files 存储在 tape 上，适合大规模批处理，成本低
- **B1**：(b) Random file organisation — 通过 key 直接访问，可即时检索特定记录
- **B1**：Random access 避免搜索所有记录，适合即时查询

</details>

---

## 题型 4：哈希算法（Hashing Algorithms）

### 题目特征

- 给定 hash function（如 key mod n）和一组 key
- 要求计算 hash value 并插入 hash table
- 处理 collision（冲突）—— linear probing / chaining
- 计算 average search length

:::note[标准解题方法]

1. 对每个 key 应用 hash function 计算位置
2. 检查是否已有冲突：
   - 无冲突：直接插入
   - 有冲突：使用 collision resolution method
3. Linear probing：依次检查下一个空位（index + 1，+2，...），注意 wrap around
4. Chaining：在每个位置维护链表
5. 列出最终 hash table 内容

:::

:::info[评分标准（MS 模式）]

- **M1**：正确计算所有 hash values
- **A1**：正确插入无冲突的 key
- **A1**：正确使用 linear probing 解决冲突
- **B1**：正确列出最终 hash table

:::

### 典型例题 1：9618/w23/qp/32 Q3

> A hash table has 11 locations (0-10). The hash function is key mod 11. Keys: 25, 37, 18, 42, 29, 14, 33. Show the hash table after inserting all keys. Use linear probing for collision handling.

<details>
<summary>📝 MS 展开查看</summary>

Hash values:
- 25 mod 11 = 3 → location 3
- 37 mod 11 = 4 → location 4
- 18 mod 11 = 7 → location 7
- 42 mod 11 = 9 → location 9
- 29 mod 11 = 7 → collision! linear probe → 8
- 14 mod 11 = 3 → collision! linear probe → 5
- 33 mod 11 = 0 → location 0

Final table:
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| 33 | | | 25 | 37 | 14 | | 18 | 29 | 42 | |

- **M1**：正确计算所有 hash values
- **A1**：正确插入无冲突的 key
- **A1**：正确使用 linear probing 解决冲突
- **B1**：正确列出最终 hash table

</details>

### 典型例题 2：Hash Table with Linear Probing

> A hash table has 7 locations (0-6). The hash function is key mod 7. Keys: 50, 51, 52, 53, 54, 55. Use linear probing for collision handling. Show the final hash table.

<details>
<summary>📝 MS 展开查看</summary>

Hash values:
- 50 mod 7 = 1 → location 1
- 51 mod 7 = 2 → location 2
- 52 mod 7 = 3 → location 3
- 53 mod 7 = 4 → location 4
- 54 mod 7 = 5 → location 5
- 55 mod 7 = 6 → location 6

Final table:
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| | 50 | 51 | 52 | 53 | 54 | 55 |

- **M1**：正确计算所有 hash values
- **A1**：正确将所有 key 插入对应位置
- **B1**：无冲突情况下的正确插入

</details>

---

:::warning[常见陷阱]

- 浮点数 normalisation 时忘记负数需要取 two's complement
- 混淆 mantissa 和 exponent 的符号位处理
- 混淆 enumerated type 和 composite type 的语法结构
- 忘记 pointer type 的声明方式 `^TypeName`
- 混淆 serial 和 sequential 文件组织方式的区别
- 在线性探测（linear probing）时忘记 wrap around（回绕到 table 开头）
- 哈希冲突处理时遗漏 key 或错误计算 hash value
- 将 two's complement 负数 mantissa 直接当作数值计算，忘记取补码

:::
