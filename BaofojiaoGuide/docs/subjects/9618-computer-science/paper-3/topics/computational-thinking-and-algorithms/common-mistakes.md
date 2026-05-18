---
title: 常见错误
---

# 常见错误

## 错误 1：Binary Search 用于未排序数据

**错误表现**：对 unsorted array 使用 binary search，结果不正确

**正确做法**：Binary search 要求数组已排序（sorted），否则必须先排序或使用 linear search

```pseudocode
// 错误：binary search 用于未排序数组
// 数据 [5, 2, 8, 1, 9]，查找 1
// binary search 返回 -1（找不到），但实际存在

// 正确：先排序，或直接使用 linear search
FUNCTION LinearSearch(Data, 1)  // 返回索引 3
```

---

## 错误 2：Binary Search 循环条件写成 Low `<` High

**错误表现**：使用 `WHILE low < high` 而非 `WHILE low <= high`，导致当 low = high 时循环退出，漏掉最后一个元素

**正确做法**：使用 `WHILE low <= high`

```pseudocode
// 错误
WHILE low < high DO      // 当 low = high 时退出，可能漏掉
    // ...
ENDWHILE

// 正确
WHILE low <= high DO     // 包含 low = high 的情况
    // ...
ENDWHILE
```

---

## 错误 3：Insertion Sort 中忘记保存 key

**错误表现**：在移动元素时直接覆盖了当前要插入的值

```pseudocode
// 错误写法
FOR i <- 1 TO n - 1
    j <- i - 1
    WHILE j >= 0 AND arr[j] > arr[i]  // 直接引用 arr[i]
        arr[j + 1] <- arr[j]
        j <- j - 1
    ENDWHILE
ENDFOR
```

**正确做法**：先用 key 变量保存 arr[i]，再移动元素

```pseudocode
// 正确写法
FOR i <- 1 TO n - 1
    key <- arr[i]
    j <- i - 1
    WHILE j >= 0 AND arr[j] > key
        arr[j + 1] <- arr[j]
        j <- j - 1
    ENDWHILE
    arr[j + 1] <- key
ENDFOR
```

---

## 错误 4：Stack Push 中顺序错误

**错误表现**：Push 时先存值再增加指针，导致覆盖已有数据

```pseudocode
// 错误
Stack[StackPointer] <- value
StackPointer <- StackPointer + 1
```

**正确做法**：先加指针再存值

```pseudocode
StackPointer <- StackPointer + 1
Stack[StackPointer] <- value
```

---

## 错误 5：Stack Pop 中顺序错误

**错误表现**：Pop 时先减指针再取值，导致丢失数据

```pseudocode
// 错误
StackPointer <- StackPointer - 1
value <- Stack[StackPointer + 1]  // 复杂且易错
```

**正确做法**：先取值再减指针

```pseudocode
value <- Stack[StackPointer]
StackPointer <- StackPointer - 1
```

---

## 错误 6：Queue 中混淆 Front 与 Rear

**错误表现**
- Dequeue 时操作了 Rear 而非 Front
- Enqueue 时操作了 Front 而非 Rear

**正确做法**
- Enqueue 操作 Rear（尾部添加）
- Dequeue 操作 Front（头部移除）

---

## 错误 7：Linked List 插入时忘记更新前驱指针

**错误表现**：只设置了新节点的 Pointer，但没有修改前驱节点的 Pointer 指向新节点

**正确做法**

```pseudocode
// 必须同时完成两个操作
List[NewNode].Pointer <- List[Previous].Pointer
List[Previous].Pointer <- NewNode
// 两者缺一不可
```

---

## 错误 8：递归缺少 Base Case

**错误表现**：递归函数没有终止条件，导致无限递归（stack overflow）

**正确做法**：每个递归函数必须有至少一个 base case（不需要再次调用自身的条件分支）

```pseudocode
// 错误：缺少 base case
FUNCTION BadFactorial(n)
    RETURN n * BadFactorial(n - 1)  // 永不停止
ENDFUNCTION

// 正确：包含 base case
FUNCTION GoodFactorial(n)
    IF n = 0 THEN RETURN 1          // base case
    ELSE RETURN n * GoodFactorial(n - 1)
    ENDIF
ENDFUNCTION
```

---

## 错误 9：Big O 混淆

**错误表现**
- Binary search 写成 O(n)
- Bubble sort 写成 O(n)
- Linear search 写成 O(log n)

**正确做法**

| 算法 | 正确 Big O |
|------|-----------|
| Linear search | O(n) |
| Binary search | O(log n) |
| Bubble sort | O(n²) |
| Insertion sort | O(n²) |
| Merge sort | O(n log n) |

---

## 错误 10：数组索引从 0 还是 1 开始混淆

**错误表现**：题目指定数组从 1 开始，但伪代码中使用了从 0 开始的写法，或反之

**正确做法**：仔细读题，注意题目中数组声明的写法
- `DECLARE arr : ARRAY[0:9] OF INTEGER` 表示从 0 开始
- `DECLARE arr : ARRAY[1:10] OF INTEGER` 表示从 1 开始

---

## 错误 11：伪代码中遗漏循环变量更新

**错误表现**：WHILE 循环中没有更新循环变量，导致无限循环

**正确做法**：确保循环体内有使循环条件最终变为 FALSE 的语句

```pseudocode
// 错误：无限循环
WHILE i < 10 DO
    OUTPUT i
    // 缺少 i <- i + 1
ENDWHILE

// 正确
WHILE i < 10 DO
    OUTPUT i
    i <- i + 1
ENDWHILE
```

---

## 错误 12：Trace Table 填写顺序错误

**错误表现**：递归 trace table 按照调用顺序而不是执行顺序填写，导致返回值错误

**正确做法**：递归是 depth-first 执行：先一直深入到底层 base case，然后逐层返回

---

## 错误 13：Queue 空满判断条件错误

**错误表现**
- 线性队列空条件写错
- 循环队列空满无法区分

**正确做法**
- 线性队列空：`Front = 0` 或 `Front > Rear`
- 线性队列满：`Rear = MaxSize`
- 循环队列空：`Front = Rear`
- 循环队列满：`(Rear + 1) MOD MaxSize = Front`

---

## 错误 14：Linked List 遍历终止条件错误

**错误表现**：使用 `Current.Pointer <> -1` 而非 `Current <> -1`，导致最后一个节点被跳过

**正确做法**

```pseudocode
// 错误：跳过最后一个节点
WHILE List[Current].Pointer <> -1 DO
    OUTPUT List[Current].Data
    Current <- List[Current].Pointer
ENDWHILE

// 正确：包含所有节点
WHILE Current <> -1 DO
    OUTPUT List[Current].Data
    Current <- List[Current].Pointer
ENDWHILE
```

---

## 错误 15：RPN 求值时操作数顺序搞反

**错误表现**：减法或除法时操作数顺序错误，例如计算 `5 3 -` 时用了 `3 - 5` 而非 `5 - 3`

**正确做法**：RPN 中操作数顺序与中缀一致

```pseudocode
// Token: 5 3 -
// 正确：先弹出 3，再弹出 5，计算 5 - 3 = 2
second <- Pop()   // 3
first <- Pop()    // 5
result <- first - second   // 5 - 3 = 2
```

---

## 错误 16：Sorting 无限循环

**错误表现**：排序算法的内层或外层循环条件错误，导致无限循环

**正确做法**：确保外层和内层循环的边界条件正确

```pseudocode
// Bubble Sort 错误：内层循环边界不对
FOR i <- 0 TO n - 1
    FOR j <- 0 TO n - 1  // 每次从头开始，效率低但还能工作
        // ...
    ENDFOR
ENDFOR

// 正确
FOR i <- 0 TO n - 2
    FOR j <- 0 TO n - 2 - i
        // ...
    ENDFOR
ENDFOR
```

---

## 错误 17：不处理空数据结构

**错误表现**：对空栈执行 Pop、对空队列执行 Dequeue、对空链表执行遍历时没有检查，导致程序崩溃

**正确做法**：始终先检查数据结构是否为空

```pseudocode
// 错误
FUNCTION Pop()
    value <- Stack[StackPointer]  // 如果 StackPointer = 0，访问无效
    StackPointer <- StackPointer - 1
    RETURN value
ENDFUNCTION

// 正确
FUNCTION Pop()
    IF StackPointer = 0 THEN
        OUTPUT "Stack is empty"
        RETURN -1
    ELSE
        value <- Stack[StackPointer]
        StackPointer <- StackPointer - 1
        RETURN value
    ENDIF
ENDFUNCTION
```
