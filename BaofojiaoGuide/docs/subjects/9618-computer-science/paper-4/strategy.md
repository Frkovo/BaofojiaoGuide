---
title: 详细策略
sidebar_position: 5
---

# 详细策略

## 前 5 分钟策略

1. 浏览全部 3 道题，识别考点分布
2. 标记每题使用的数据文件
3. 规划答题顺序（从最熟悉的题目开始）

## 各知识点答题策略

### 数组与 2D 数组
- 分清全局/局部数组，全局赋值需加 `global`
- 2D 数组用 `arr[row][col]` 访问
- 2D 数组按列排序：交换整行

### 排序
- **冒泡**：双层循环，相邻比较，逆序则交换
- **插入**（迭代）：将当前元素插入已排序部分的正确位置
- **插入**（递归）：base case n `&lt;=` 1，递归排序前 n-1 个，再插入第 n 个

### 查找
- **线性**：遍历全部元素，找到返回
- **二分**：必须预先排序！`mid = (first + last) // 2`

### 线性队列
- 固定大小数组，Front 指向第一个，Rear 指向下一个空位
- 满：`Rear >= 数组大小`，空：`Front == -1 or Front >= Rear`

### 循环队列
- `TailPointer = (TailPointer + 1) % 数组大小`
- 用 `NumberItems` 区分满和空（不是靠指针位置）

### 栈
- `TopOfStack` 指向栈顶（最后一个元素）
- 满：`TopOfStack == 数组大小-1`，空：`TopOfStack == -1`

### 链表
- 每个 node 有 `data` + `nextNode`
- 遍历从 `startPointer` 开始，沿 `nextNode` 直到 -1
- 插入先找空位，更新前驱的 `nextNode`

### 二叉树（OOP 方式）
- `Node` 类：LeftPointer, Data, RightPointer
- `TreeClass`：Tree 数组, FirstNode, NumberNodes
- 小→左，大→右

### 二叉树（2D 数组方式）
- `ArrayNodes[row, 0]` = LeftPointer, `[row, 1]` = Data, `[row, 2]` = RightPointer
- `RootPointer` 指向根，`FreeNode` 指向下一个空位

### 中序遍历
- 递归：左 → 输出 → 右
- 2D 数组版：传入当前节点索引

### 哈希表
- `hash = key % 200`
- 碰撞时存到 Spare 数组的下一空位

### OOP
- 私有属性：`self.__Name`
- getter 返回属性值，setter 修改属性值
- 文件读取创建对象数组

### OOP 继承
- `class Child(Parent):`
- `super().__init__(parent_params)` 调用父类构造器
- 重写方法：同名方法，新实现

### 文件处理
- `with open(filename, 'r') as f:` 自动关闭
- `f.read().splitlines()` 读所有行
- `line.split(",")` 分割 CSV

### 递归模板
```python
def RecursiveFunc(n):
    if base_condition:  # 终止条件
        return base_value
    # 递归调用，缩小问题规模
    return operation(RecursiveFunc(smaller_n))
```

### 字符串处理
- 字符串按索引访问：`s[i]`
- `MID(s, start, len)` 相当于 `s[start:start+len]`
- 字符比较直接用 `<` `>` 比较 ASCII

## 最后 10 分钟检查

- [ ] 所有子问题代码完整
- [ ] evidence document 包含所有代码和截图
- [ ] 程序文件按要求命名
- [ ] 测试数据按要求输入
- [ ] 输出格式与题目一致
