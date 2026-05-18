---
title: 解题方法
sidebar_position: 3
---

# 解题方法

## Linear Queue with Array — 完整实现方法

### Step 1: 声明全局常量与变量

```
CONSTANT QueueSize &lt;- 10
DECLARE Queue : ARRAY[0:QueueSize-1] OF INTEGER
DECLARE Front : INTEGER
DECLARE Rear : INTEGER
DECLARE NumberInQueue : INTEGER
```

**要点**:
- `$QueueSize$` 通常作为常量
- `$Front$` 初始化为 `$0$` (指向第一个有效元素)
- `$Rear$` 初始化为 `$0$` (指向下一个空位)
- `$NumberInQueue$` 初始化为 `$0$` (用 counter 避免指针比较歧义)

### Step 2: 初始化过程

```
PROCEDURE InitialiseQueue()
    Front &lt;- 0
    Rear &lt;- 0
    NumberInQueue &lt;- 0
ENDPROCEDURE
```

### Step 3: Enqueue 过程

```
PROCEDURE Enqueue(ByVal NewItem : INTEGER)
    IF NumberInQueue >= QueueSize THEN
        OUTPUT "Queue is full — cannot enqueue"
    ELSE
        Queue[Rear] &lt;- NewItem
        Rear &lt;- Rear + 1
        NumberInQueue &lt;- NumberInQueue + 1
    ENDIF
ENDPROCEDURE
```

**关键检查点**:
- Full condition: `$NumberInQueue >= QueueSize$`
- 赋值: `$Queue[Rear] \gets NewItem$` (在 rear 位置写入)
- 指针后移: `$Rear \gets Rear + 1$`
- Counter 递增

### Step 4: Dequeue 函数

```
FUNCTION Dequeue() RETURNS INTEGER
    DECLARE Item : INTEGER
    IF NumberInQueue = 0 THEN
        OUTPUT "Queue is empty"
        RETURN -1
    ELSE
        Item &lt;- Queue[Front]
        Front &lt;- Front + 1
        NumberInQueue &lt;- NumberInQueue - 1
        RETURN Item
    ENDIF
ENDFUNCTION
```

**关键检查点**:
- Empty condition: `$NumberInQueue = 0$`
- 暂存: `$Item \gets Queue[Front]$`
- 指针后移: `$Front \gets Front + 1$`
- Counter 递减
- 返回值: 正常返回 `$Item$`, 空返回 `$-1$`

### Step 5: Display 过程

```
PROCEDURE DisplayQueue()
    DECLARE Index : INTEGER
    IF NumberInQueue = 0 THEN
        OUTPUT "Queue is empty"
    ELSE
        FOR Index &lt;- Front TO Rear - 1
            OUTPUT Queue[Index]
        NEXT Index
    ENDIF
ENDPROCEDURE
```

**遍历范围**: `$Front$` 到 `$Rear-1$` (包含当前所有元素, 不含空位)

### Step 6: 主程序

```
DECLARE Choice : INTEGER
CALL InitialiseQueue()
REPEAT
    OUTPUT "1. Enqueue"
    OUTPUT "2. Dequeue"
    OUTPUT "3. Display"
    OUTPUT "4. Exit"
    INPUT Choice
    IF Choice = 1 THEN
        CALL Enqueue(UserInput)
    ELSE IF Choice = 2 THEN
        OUTPUT Dequeue()
    ELSE IF Choice = 3 THEN
        CALL DisplayQueue()
    ENDIF
UNTIL Choice = 4
```

---

## Circular Queue 要点 (较少考, 理解即可)

- `$Rear \gets (Rear + 1) \bmod QueueSize$`
- `$Front \gets (Front + 1) \bmod QueueSize$`
- Full condition: `$(Rear + 1) \bmod QueueSize = Front$`
- Empty condition: `$Front = Rear$`
- 留一个空位区分 full/empty

---

## 队列变量命名对照表

| 变量 | 常用名 | 说明 |
|------|--------|------|
| 队列数组 | Queue, QueueArray | 存储元素的静态数组 |
| 队首指针 | Front, Head, FrontPointer | 指向第一个有效元素 |
| 队尾指针 | Rear, Tail, RearPointer | 指向下一个空位 |
| 队列大小 | QueueSize, MaxQueue, Size | 数组容量 |
| 元素计数 | NumberInQueue, Count, QueueCount | 当前元素个数 |
