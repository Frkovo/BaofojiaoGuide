
sidebar_position: 6
title: "考纲要点"
---

# 考纲要点

## 20.2 File Processing and Exception Handling

### 1. File Handling Operations

| 知识点 | 要求 | 考试层级 |
|--------|------|----------|
| Open file — `open(filename, mode)` | 理解不同模式的区别 | 应用 |
| Read — `read()` / `readline()` / `readlines()` | 区分三种读取方式 | 分析 |
| Write — `write()` / `writelines()` | 构造输出字符串 | 应用 |
| Close — `close()` / `with` 语句 | 确保资源释放 | 应用 |
| File modes — `"r"` `"w"` `"a"` `"r+"` | 选择正确模式 | 理解 |

### 2. Text File Processing

- 逐行读取 `for line in f:`
- 去除换行符 `line.strip()`
- 按分隔符分割 `line.split(",")`
- 类型转换 `int()` / `float()`
- 累加 / 计数 / 求平均
- 条件筛选

### 3. Exception Handling

- `try` / `except` / `finally` 结构
- `FileNotFoundError` — 文件不存在
- `IOError` — 输入/输出错误
- `ValueError` — 数据类型转换错误
- 异常类型继承关系

### 4. CSV File Processing

- 读取 CSV 文件
- 用 `split(",")` 分割字段
- 跳过标题行
- 处理每一列数据
- 汇总计算

:::note[重点提示]
- `with` 语句是隐含加分点（自动关闭文件）
- 异常处理在 20.2 中约占 40%
- CSV 处理是近年高频考点（连续 3 次考试出现）
- 评分标准中"处理异常"几乎必占 1-2 分
:::

## 常见考试动词

| 动词 | 含义 |
|------|------|
| **Write** | 编写完整程序代码 |
| **Describe** | 描述算法或方法 |
| **Explain** | 解释代码功能或结果 |
| **State** | 直接陈述答案 |
| **Identify** | 识别代码中的错误或特征 |
