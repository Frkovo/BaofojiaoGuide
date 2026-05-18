---
title: 评分标准模式
sidebar_position: 4
---

# 评分标准模式

## 队列声明与初始化（1-3 分）

- **M1**: Queue 声明为 1D 数组（string 类型），初始化为 20 个空值
- **M1**: Front/HeadPointer 初始化为 -1
- **M1**: Rear/TailPointer 初始化为 -1 或 0

## Enqueue（4 分）

- **M1**: 函数头，1 个参数，返回 Boolean
- **M1**: 检查队列满，返回 FALSE
- **M1**: 数据插入到 Rear 位置，Rear 递增
- **M1**: 第一个元素时设 Front=0，返回 TRUE

## Dequeue（3 分）

- **M1**: 函数头，返回 string
- **M1**: 检查空队列（Front `&lt;` 0 或 Front `&gt;`=Rear），返回 "false"
- **M1**: 取出 Front 处值，Front 递增，返回值

## 数据验证结合队列（6 分）

- **M1**: 过程/函数头
- **M1**: 输入读取
- **M1**: 数据分割和字符串处理
- **M1**: check digit 计算
- **M1**: 比较校验位
- **M1**: 调用 Enqueue + 输出结果信息
