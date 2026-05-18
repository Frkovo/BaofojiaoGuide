---
title: 考前速记
sidebar_position: 7
---

# 考前速记

## 10 秒模板

```python
class X:
    def __init__(self, a):
        self.__a = a
    def GetA(self):
        return self.__a
    def SetA(self, v):
        self.__a = v
```

## 5 个必须检查的点

| # | 检查项 | 为什么重要 |
|---|--------|-----------|
| 1 | `self` 在参数列表里 | 否则 constructor 报错 |
| 2 | `self.__attr` 双下划线 | private 封装 |
| 3 | `self.` 在方法 body 里 | 否则 NameError |
| 4 | `line.strip().split(",")` | 去掉 `\n` 再分割 |
| 5 | `file.close()` | 否则 resource leak |

## 2 个高频 logic 模式

**求和**:
```python
total = 0
for obj in arr:
    total += obj.GetValue()
```

**找最大值**:
```python
maxObj = arr[0]
for obj in arr:
    if obj.GetValue() > maxObj.GetValue():
        maxObj = obj
```

## 类型转换速查

```
file read  →  string         ← 不需要转换
file read  →  int            ←  int(parts[1])
file read  →  float          ←  float(parts[1])
file read  →  bool           ←  parts[1] == "True"
```

## 文件模式速查

| 操作 | 模式 |
|------|------|
| 读取文本文件 | `"r"` |
| 写入文本文件（覆盖） | `"w"` |
| 追加到文本文件 | `"a"` |

## 答题卡 Checklist

- [ ] `class` 关键字 + 类名 + 冒号
- [ ] `__init__` 有 `self`
- [ ] 每个 attribute 有 `self.__`
- [ ] Getter 有 `return`
- [ ] Setter 有 `self.__x = value`
- [ ] 对象用 `.` 调用方法
- [ ] 文件读完后 `.close()`
- [ ] 数字类型已 `int()` / `float()`

## 一句话口诀

> "Class colon init self, private double underscore, getter return setter assign, file strip split close."
