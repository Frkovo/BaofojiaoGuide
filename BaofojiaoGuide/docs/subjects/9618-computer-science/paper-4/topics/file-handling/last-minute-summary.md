
sidebar_position: 7
title: "考前速记"
---

# 考前速记

## 文件读取三板斧

| 方法 | 返回类型 | 适用场景 |
|------|----------|----------|
| `f.read()` | `str` | 小文件全文 |
| `f.readlines()` | `list[str]` | 需要行列表 |
| `for line in f:` | `str` each | 大文件逐行 ✅ 推荐 |

## 异常处理速记

```
try:         ← 保护代码
    ...
except ...:  ← 捕获异常（子类在前）
    ...
finally:     ← 总是执行（可选）
    ...
```

**异常类型顺序**：`FileNotFoundError` &rarr; `ValueError` &rarr; `IOError` &rarr; `Exception`

## CSV 处理模板

```python
with open(`data.csv`, `r`) as f:
    f.readline()                        # 跳过标题
    for line in f:
        parts = line.strip().split(`,`)
        val = int(parts[1])             # 类型转换
        if val &gt;= 50:                    # 条件筛选
            total += val
```

## 必记代码片段

```python
# 读取
with open(`f`, `r`) as file:
    for line in file:
        line = line.strip()

# 写入
with open(`f`, `w`) as file:
    file.write(str(x) + `\n`)

# 异常
try:
    with open(`f`, `r`) as file:
        data = file.read()
except FileNotFoundError:
    print(`Not found`)

# CSV 解析
parts = line.strip().split(`,`)
```

:::note
- 永远使用 `with open()`
- 永远在读取后加 `strip()`
- 永远在写入后加 `\n`
- 永远转换类型后再计算
- 永远用 `split(",")` 处理 CSV
- 考试 80% 的文件题可以用以上模板解决
:::

## 扣分点速查

| 错误 | 扣分 |
|------|------|
| 未使用 `with` / 未 `close()` | -1 |
| 忘记 `strip()` | -1 |
| 忘记类型转换 | -1 |
| 未处理异常 | -1 ~ -2 |
| CSV 忘记跳过标题 | -1 |
| 模式选错（`"w"` 应为 `"a"`） | -1 |
| `write()` 参数未转字符串 | -1 |
