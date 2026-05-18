
sidebar_position: 4
title: "评分标准模式"
---

# 评分标准模式

## 通用文件操作 MS

<details>
<summary>General File Handling</summary>

- **M1** — 选择正确的文件模式（`"r"` / `"w"` / `"a"`）
- **A1** — 使用 `with open()` 语句（自动关闭）
- **M1** — 逐行读取 / 写入循环结构
- **A1** — 正确处理换行符（`strip()` / `\n`）
- **M1** — 类型转换（`int()` / `float()`）
- **A1** — 字符串拼接/格式化输出

</details>

## CSV Processing MS

<details>
<summary>CSV Processing</summary>

- **M1** — 打开 CSV 文件
- **A1** — 用 `split(",")` 分割每行
- **M1** — 跳过标题行（`readline()` 或用索引判断）
- **A1** — 将字符串转换为数值类型
- **M1** — 实现筛选条件（`if` 判断）
- **A1** — 累加/计数等计算结果
- **M1** — 输出/存储结果
- **A1** — 异常处理

</details>

## Exception Handling MS

<details>
<summary>Exception Handling</summary>

- **M1** — 用 `try:` 包围文件操作代码
- **A1** — 捕获 `FileNotFoundError`
- **M1** — 捕获 `IOError`（读取/写入失败）
- **A1** — 输出用户友好的错误信息
- **M1** — 程序异常后继续执行（不中断）
- **A1** — 适当使用 `finally` 清理资源

</details>

## Writing to File MS

<details>
<summary>Writing to File</summary>

- **M1** — 以 `"w"` 或 `"a"` 模式打开文件
- **A1** — 构造输出字符串（含 `\n`）
- **M1** — 调用 `write()` 或 `writelines()`
- **A1** — 格式化输出（如保留两位小数）
- **M1** — 关闭文件
- **A1** — 异常处理

</details>

:::note[评分规律]
- 文件打开/关闭通常是 **M1**（基础分）
- 数据处理逻辑通常是 **A1**（高阶分）
- 异常处理在 4+ 分题目中必占一个 **M1** + **A1**
- 忘记 `strip()` 或类型转换通常扣 **1 分**
:::

## 分数分配规律

| 分值 | 典型分配 |
|------|----------|
| 4 分 | open + read/write + process + close/exception |
| 5 分 | open + loop + process + write + exception |
| 6 分 | open + loop + strip + convert + process + exception |
| 7 分 | open + split + skip header + convert + filter + calc + exception |
