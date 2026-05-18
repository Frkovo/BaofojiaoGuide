---
title: 知识点总结
---

# 数据表示 (Data Representation)

## 用户自定义数据类型 (User-defined Data Types)

### 非组合类型 (Non-composite)

- **枚举类型 (Enumerated type)**: 将变量的取值限制在一个预定义的集合中
  - 语法: `TYPE <typeName> = (value1, value2, ...);`
  - 示例: `TYPE Days = (Mon, Tue, Wed, Thu, Fri, Sat, Sun);`
  - 枚举值实际存储为整数，可进行比较操作

- **指针类型 (Pointer type)**: 存储内存地址，指向另一个变量的位置
  - 语法: `TYPE <ptrName> = ^<baseType>;`
  - 示例: `TYPE IntPtr = ^Integer;`
  - 使用 `NEW()` 分配动态内存，使用 `DISPOSE()` 释放
  - 通过 `ptr^` 解引用访问指向的值
  - 用于动态数据结构（链表、树、图）

### 组合类型 (Composite Types)

- **集合类型 (Set type)**: 存储同一基类型的无序元素的集合
  - 语法: `TYPE <typeName> = SET OF <baseType>;`
  - 支持操作: 并集 `+`、交集 `*`、差集 `-`、成员测试 `IN`
  - 示例: `TYPE CharSet = SET OF 'A'..'Z';`

- **记录类型 (Record type)**: 将不同类型的相关数据组合成一个单元
  - 语法:
    ```
    TYPE <typeName>
      DECLARE <field1> : <type1>
      DECLARE <field2> : <type2>
      ...
    ENDTYPE
    ```
  - 通过 `.` 访问字段（如 `student.name`）

- **类/对象 (Class/Object)**: 将数据和操作方法封装在一起
  - 支持继承、封装、多态
  - 构造函数 (`CONSTRUCTOR`) 和析构函数 (`DESTRUCTOR`)
  - 访问修饰符: `PRIVATE`, `PUBLIC`, `PROTECTED`

## 文件组织 (File Organisation)

### 文件组织方式

- **串行组织 (Serial organisation)**: 记录按时间顺序写入，无特定顺序
  - 新记录追加到文件末尾
  - 查找需要遍历整个文件，效率低
  - 适用于日志文件

- **顺序组织 (Sequential organisation)**: 记录按键字段(key field)的升序或降序排列
  - 必须通过键字段排序
  - 批量更新效率高，但单条插入/删除需要重写文件
  - 适用于磁带存储、批处理系统

- **随机组织 (Random organisation)**: 记录通过记录键(record key)直接定位
  - 使用哈希函数将记录键映射到存储位置
  - 支持快速直接访问
  - 可能产生哈希冲突

### 文件访问方式

- **顺序访问 (Sequential access)**: 从文件开头按顺序读取记录
  - 必须读取前一条记录才能访问后一条
  - 适用于串行和顺序组织文件

- **直接访问 (Direct access)**: 通过记录键直接访问任意记录
  - 不需要读取其他记录
  - 适用于随机组织文件
  - 速度快，适合实时系统

## 哈希算法 (Hashing Algorithms)

### 基本概念

- **哈希函数 (Hash function)**: 将记录键映射到存储地址的算法
  - 常见方法: 除法哈希 (`key MOD n`)、乘法哈希、折叠法
  - 理想哈希函数应分布均匀、计算快速

- **冲突 (Collision)**: 两个不同的键被哈希到同一个地址

- **装载因子 (Load factor)**: `已存储记录数 / 总桶数`
  - 装载因子越高，冲突概率越大

### 冲突处理 (Collision Handling)

- **开放地址法 (Open addressing / Linear probing)**: 冲突时顺序查找下一个空位
  - 优点: 实现简单
  - 缺点: 容易产生聚集(clustering)问题
  - 删除记录需要特殊标记（tombstone），不能直接删除

- **链地址法 (Separate chaining)**: 每个桶维护一个链表，冲突的记录链入同一桶
  - 优点: 删除简单，装载因子可以 >1
  - 缺点: 需要额外空间存储指针

## 浮点数 (Floating-point Numbers)

### 表示格式

- **浮点数 = 尾数 × 基数<sup>指数</sup>** 即 `M × 2<sup>E</sup>`
- **尾数 (Mantissa / Significand)**: 表示有效数字部分，通常使用二进制补码(two's complement)
- **指数 (Exponent)**: 表示小数点的位置，使用二进制补码或偏移码
- 存储时分为符号位、指数部分、尾数部分

### 规格化 (Normalisation)

- 规格化的浮点数保证尾数的最高有效位与符号位不同
  - 正数: 尾数以 `0.1...` 开头
  - 负数: 尾数以 `1.0...` 开头（补码表示）
- 目的: 最大化精度，每个数值有唯一表示
- 规格化过程: 左移/右移尾数，同时调整指数

### 溢出与下溢

- **上溢 (Overflow)**: 尾数超出可用位数，无法正确表示
  - 尾数左移后超出范围
  - 表现为结果为无穷大或最大值

- **下溢 (Underflow)**: 指数太小，小于可表示的最小值
  - 尾数右移后指数过小
  - 表现为结果为 0 或次正规数(subnormal)

### 精度与范围的权衡

- **更多尾数位 = 更高精度 (Precision)**: 更多有效数字位数
- **更多指数位 = 更大范围 (Range)**: 更大/更小的数值范围
- 固定总位数下，精度和范围不可兼得

### 舍入误差 (Rounding Errors)

- 许多十进制小数无法用二进制精确表示（如 0.1）
- **舍入误差**: 由于截断或舍入导致的精度损失
- 多次运算后误差可能累积放大
- 比较浮点数时应使用容差(`epsilon`)，而非直接相等
