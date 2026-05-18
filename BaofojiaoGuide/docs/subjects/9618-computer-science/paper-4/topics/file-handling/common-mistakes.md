
sidebar_position: 5
title: "常见错误"
---

# 常见错误

## 1. 忘记异常处理

```python
# ❌ 错误：文件不存在时崩溃
f = open(`data.txt`, `r`)
data = f.read()
f.close()

# ✅ 正确
try:
    with open(`data.txt`, `r`) as f:
        data = f.read()
except FileNotFoundError:
    print(`File not found`)
```

## 2. 路径错误

```python
# ❌ 错误：相对路径依赖工作目录
with open(`data.txt`, `r`) as f:

# ✅ 正确：使用完整路径或确认工作目录
with open(`./data/data.txt`, `r`) as f:
```

:::note
考试中通常文件在当前目录，直接写文件名即可。但要注意题目中给出的文件路径。
:::

## 3. 忘记 `strip()` 或 `rstrip()`

```python
# ❌ 错误：line 包含 `\n`
for line in f:
    print(line + `extra`)   # 输出: "hello\nextra"

# ✅ 正确
for line in f:
    line = line.strip()
    print(line + `extra`)   # 输出: "helloextra"
```

## 4. `write()` 参数非字符串

```python
# ❌ 错误：write 接受字符串而非数字
with open(`out.txt`, `w`) as f:
    f.write(42)              # TypeError

# ✅ 正确
with open(`out.txt`, `w`) as f:
    f.write(str(42) + `\n`)
```

## 5. `"w"` 和 `"a"` 混淆

```python
# ❌ 错误：w 模式覆盖已有内容
with open(`log.txt`, `w`) as f:
    f.write(`new data`)      # 原内容丢失

# ✅ 追加
with open(`log.txt`, `a`) as f:
    f.write(`new data` + `\n`)
```

## 6. CSV 分割错误

```python
# ❌ 错误：split() 按空白分割
parts = line.split()       # "a,b,c" → ["a,b,c"]

# ✅ 正确：指定逗号
parts = line.strip().split(`,`)
```

## 7. 未跳过标题行

```python
# ❌ 错误：标题行 "Name,Score" 被当作数据处理
with open(`scores.csv`, `r`) as f:
    for line in f:
        name, score = line.strip().split(`,`)

# ✅ 正确
with open(`scores.csv`, `r`) as f:
    f.readline()             # 跳过标题
    for line in f:
        name, score = line.strip().split(`,`)
```

## 8. 类型转换遗漏

```python
# ❌ 错误：字符串拼接而非数值相加
total = total + parts[1]     # "5" + "3" = "53"

# ✅ 正确
total = total + int(parts[1])
```

## 9. 未关闭文件

```python
# ❌ 错误：手动 open 未 close
f = open(`data.txt`, `r`)
data = f.read()

# ✅ 正确：with 自动关闭
with open(`data.txt`, `r`) as f:
    data = f.read()
```

## 10. Exception 顺序错误

```python
# ❌ 错误：父类在前，子类永远不会被触发
try:
    with open(`file.txt`, `r`) as f:
        data = f.read()
except IOError:              # 父类
    ...
except FileNotFoundError:    # 子类 — 永远不会到这里
    ...

# ✅ 正确
try:
    with open(`file.txt`, `r`) as f:
        data = f.read()
except FileNotFoundError:
    ...
except IOError:
    ...
```
