---
title: Object-Oriented Programming
sidebar_position: 1
---

# Object-Oriented Programming（面向对象编程）

## 考纲要求

- 20.1.2 OOP：类、对象、属性、方法、封装、getter/setter

## 核心代码模板

### 基本类定义
```python
class Tree:
    def __init__(self, name, growth, maxH, maxW, evergreen):
        self.__TreeName = name
        self.__HeightGrowth = growth
        self.__MaxHeight = maxH
        self.__MaxWidth = maxW
        self.__Evergreen = evergreen

    def GetTreeName(self):
        return self.__TreeName

    def GetGrowth(self):
        return self.__HeightGrowth

    def GetMaxHeight(self):
        return self.__MaxHeight

    def GetMaxWidth(self):
        return self.__MaxWidth

    def GetEvergreen(self):
        return self.__Evergreen
```

### 创建对象并调用方法
```python
myTree = Tree("Beech", 30, 400, 200, "No")
print(myTree.GetTreeName())
```

### 对象数组
```python
TreeObjects = []
# 从文件读取数据
f = open("Trees.txt", 'r')
lines = f.read().splitlines()
f.close()
for i in range(len(lines)):
    parts = lines[i].split(",")
    name = parts[0]
    growth = int(parts[1])
    maxH = int(parts[2])
    maxW = int(parts[3])
    evergreen = parts[4]
    t = Tree(name, growth, maxH, maxW, evergreen)
    TreeObjects.append(t)
```

### 业务方法
```python
def PrintTrees(item):
    msg = "does not lose its leaves"
    if item.GetEvergreen() == "No":
        msg = "loses its leaves each year"
    print(item.GetTreeName(), "has a maximum height", item.GetMaxHeight(),
          "a maximum width", item.GetMaxWidth(), "and grows",
          item.GetGrowth(), "cm a year. It", msg)
```

## 常见错误

- 方法定义忘记 `self` 参数
- Python 私有属性用 `self.__`（双下划线）
- 调用方法时必须写 `self.Method()` 或 `object.Method()`
- getter 方法必须 return，不是 print
