---
title: 评分标准模式
sidebar_position: 4
---

# 评分标准模式

## Node 类声明（4 分）

- **M1**: Class 声明（含结束）
- **M1**: 三个私有属性（LeftPointer, Data, RightPointer）声明为 Integer
- **M1**: 构造器含 1 个参数
- **M1**: 参数赋给 Data，LeftPointer 和 RightPointer 初始化为 -1

## getter 方法（每个 1 分，共 3 分）

- 1 个 getter 无参方法
- 返回正确的属性

## setter 方法（每个 1 分，共 3 分）

- 1 个 setter 含参数
- 参数赋给对应属性

## TreeClass 声明（4 分）

- **M1**: Class 声明
- **M1**: 私有数组 Tree（20 个 Node 元素）、FirstNode、NumberNodes
- **M1**: 构造器初始化 FirstNode=-1，NumberNodes=0
- **M1**: 初始化所有 Tree 元素为 Node(-1)

## InsertNode（6 分）

- **M1**: 方法头，参数为 Node
- **M1**: 检查空树，插入首节点，更新 FirstNode
- **M1**: 非空时在新位置插入节点
- **M1**: 访问根节点比较数据决定左/右
- **M1**: 重复直至找到正确位置
- **M1**: 更新父节点指针并递增 NumberNodes

## OutputTree（4 分）

- **M1**: 过程头，无参
- **M1**: 空树时输出 "No nodes"
- **M1**: 循环遍历已插入节点
- **M1**: 用 getter 输出 LeftPointer, Data, RightPointer
