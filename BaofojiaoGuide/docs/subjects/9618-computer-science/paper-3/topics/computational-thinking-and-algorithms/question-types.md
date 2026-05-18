---
title: 题型分析
---

# 题型分析

## 类型 1：Binary Search 伪代码

### 识别特征
- 题目描述在一个**已排序（sorted）**数组中查找某个值
- 要求完成或写出 binary search 的伪代码
- 关键词："sorted array", "divide and conquer", "midpoint"

### 标准解题方法

:::note[标准解题方法]
```pseudocode
FUNCTION BinarySearch(array: ARRAY, target: INTEGER) RETURNS INTEGER
    DECLARE low, high, mid : INTEGER
    low <- 0
    high <- LENGTH(array) - 1
    WHILE low <= high DO
        mid <- (low + high) DIV 2
        IF array[mid] = target THEN
            RETURN mid
        ELSE IF array[mid] < target THEN
            low <- mid + 1
        ELSE
            high <- mid - 1
        ENDIF
    ENDWHILE
    RETURN -1
ENDFUNCTION
```

**关键点**：必须检查 Low `&lt;=` High（不是 Low `&lt;` High），mid 使用整数除法 DIV；区间缩小：low = mid + 1 或 high = mid - 1

:::

:::info[评分标准（MS 模式）]
- **M1**：正确初始化 low 和 high
- **M2**：正确计算 mid = (low + high) DIV 2
- **A1**：正确的循环条件和区间更新
- **B1**：处理未找到的情况（return -1）

:::

### 真题示例

**示例 1：9618/s24/qp/31 Q10**

> Complete the pseudocode for a binary search algorithm that searches an array `Data[1:N]` for a given `Value`.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Low = 1 (or 0) and High = N (or N-1) correctly initialised
- **M2**: WHILE Low `&lt;=` High
- **A1**: Mid = (Low + High) DIV 2
- **A2**: IF Data[Mid] = Value THEN RETURN Mid
- **B1**: IF Data[Mid] `&lt;` Value THEN Low = Mid + 1 ELSE High = Mid - 1
- **B2**: RETURN -1 if not found

</details>

**示例 2：9618/w22/qp/33 Q12(a)**

> Write pseudocode for a binary search to find an item in a sorted array.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Correct initialisation of search boundaries
- **M2**: Correct loop with termination condition
- **A1**: Correct calculation of midpoint
- **A2**: Correct comparison and boundary adjustment
- **B1**: Return index if found, -1 if not found

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 数组未排序时错误使用 Binary Search：Binary Search 只适用于 sorted data
2. 循环条件写成 Low `&lt;` High 而非 Low `&lt;=` High，可能漏掉最后一个元素
3. mid 计算溢出：在伪代码中用 DIV 即可
4. 忘记处理找不到的情况
5. 区间更新写成 low = mid 或 high = mid，可能导致无限循环

:::

---

## 类型 2：Linear Search 伪代码

### 识别特征
- 在数组（可排序可不排序）中按顺序查找
- 通常要求从第一个元素开始逐个比较

### 标准解题方法

:::note[标准解题方法]
```pseudocode
FUNCTION LinearSearch(array: ARRAY, target: INTEGER) RETURNS INTEGER
    DECLARE i : INTEGER
    FOR i <- 0 TO LENGTH(array) - 1 DO
        IF array[i] = target THEN
            RETURN i
        ENDIF
    ENDFOR
    RETURN -1
ENDFUNCTION
```

**关键点**：简单顺序遍历；找到后立即返回索引；遍历完未找到则返回 -1

:::

:::info[评分标准（MS 模式）]
- **M1**：正确设置循环遍历数组
- **M2**：IF 语句比较当前元素与目标值
- **A1**：找到后返回正确的索引
- **B1**：未找到时返回 -1

:::

### 真题示例

**示例 1：9618/s24/qp/32 Q8**

> Complete the pseudocode for a linear search algorithm.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Initialises index (e.g. i = 0)
- **M2**: Loop through all elements of the array
- **A1**: Compares each element with the search value
- **B1**: Returns the position if found
- **B2**: Returns -1 if not found

</details>

**示例 2：9618/s22/qp/32 Q8**

> The array `Names[1:50]` contains unsorted names. Write pseudocode for a linear search to find a given name.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: FOR loop from 1 to 50
- **M2**: IF Names[i] = SearchName THEN OUTPUT i
- **A1**: OUTPUT "Not found" if search is unsuccessful
- **B1**: Correct use of array indexing

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 混淆 Linear Search 与 Binary Search：Linear 不需要 sorted array
2. 循环范围错误：从 0 到 n-1 或从 1 到 n，要与数组声明一致
3. 未找到时没有返回或输出

:::

---

## 类型 3：Insertion Sort 伪代码

### 识别特征
- 要求将给定的 Bubble Sort 改为 Insertion Sort
- 或者直接要求写 Insertion Sort 的伪代码
- 关键词："sorted part", "insert", "shift elements"

### 标准解题方法

:::note[标准解题方法]
```pseudocode
PROCEDURE InsertionSort(array: ARRAY)
    DECLARE i, j, key : INTEGER
    FOR i <- 1 TO LENGTH(array) - 1 DO
        key <- array[i]
        j <- i - 1
        WHILE j >= 0 AND array[j] > key DO
            array[j + 1] <- array[j]
            j <- j - 1
        ENDWHILE
        array[j + 1] <- key
    ENDFOR
ENDPROCEDURE
```

**关键点**：从第二个元素开始（index 1）；将当前元素 key 与前面已排序部分比较；比 key 大的元素后移一位；最后将 key 插入正确位置

:::

:::info[评分标准（MS 模式）]
- **M1**：外层 FOR 循环从 1 开始
- **M2**：保存当前值到 key/temp
- **A1**：WHILE 循环正确地移动元素
- **A2**：正确插入 key 到合适位置
- **B1**：避免数组越界（j `&gt;=` 0）

:::

### 真题示例

**示例 1：9618/s21/qp/31 Q8(b)**

> A bubble sort algorithm is given. Write the pseudocode for an insertion sort algorithm that sorts the same array into ascending order.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: FOR loop from second element
- **M2**: Stores current element in a temporary variable
- **A1**: WHILE loop to shift elements
- **A2**: Inserts stored element in correct position
- **B1**: Outer loop iterates n-1 times

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 忘记保存 key：移动元素时会覆盖原值
2. WHILE 条件中 j `&gt;=` 0 需要先判断，否则可能数组越界
3. 混淆 Bubble Sort 与 Insertion Sort：Bubble 是交换相邻元素，Insertion 是插入到已排序部分
4. 外层循环从 i = 1 开始但数组是 1-indexed 则应为 i = 2

:::

---

## 类型 4：Stack ADT（声明 + Push/Pop）

### 识别特征
- 要求声明栈的数据结构（数组 + 指针）
- 要求写出 Push 和 Pop 操作的伪代码
- 关键词："LIFO", "stack pointer", "top of stack"

### 标准解题方法

:::note[标准解题方法]
**Stack 声明**
```pseudocode
CONSTANT MaxSize <- 100
DECLARE Stack : ARRAY[1:MaxSize] OF INTEGER
DECLARE StackPointer : INTEGER
StackPointer <- 0
```

**Push 操作**
```pseudocode
PROCEDURE Push(value: INTEGER)
    IF StackPointer = MaxSize THEN
        OUTPUT "Stack is full"
    ELSE
        StackPointer <- StackPointer + 1
        Stack[StackPointer] <- value
    ENDIF
ENDPROCEDURE
```

**Pop 操作**
```pseudocode
FUNCTION Pop() RETURNS INTEGER
    IF StackPointer = 0 THEN
        OUTPUT "Stack is empty"
        RETURN -1
    ELSE
        DECLARE value : INTEGER
        value <- Stack[StackPointer]
        StackPointer <- StackPointer - 1
        RETURN value
    ENDIF
ENDFUNCTION
```

:::

:::info[评分标准（MS 模式）]
- **M1**：栈溢出检查（StackPointer = MaxSize）
- **M2**：栈空检查（StackPointer = 0）
- **A1**：Push 中指针先加再存值
- **A2**：Pop 中先取值再减指针
- **B1**：正确的返回值

:::

### 真题示例

**示例 1：9618/w23/qp/31 Q10**

> A stack is implemented using an array `Stack[1:10]`. Write pseudocode for the Push and Pop operations.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Push checks if stack is full
- **M2**: Push increments pointer and stores value
- **A1**: Pop checks if stack is empty
- **A2**: Pop retrieves value and decrements pointer
- **B1**: Pop returns the retrieved value

</details>

**示例 2：9618/w23/qp/32 Q9**

> Write pseudocode declarations for a stack of characters. Implement the Push operation.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Array declaration for stack storage
- **M2**: StackPointer initialised to 0
- **A1**: Push procedure with full check
- **A2**: Push correctly updates pointer and stores data
- **B1**: Appropriate data types used

</details>

### 常见陷阱

:::warning[常见陷阱]
1. Push 中先存值再加指针：必须先加指针再存值（与 Pop 反过来）
2. 忘记检查栈空或栈满
3. 混淆 StackPointer 的初始值：空栈时 pointer = 0
4. Pop 后未返回被移除的值

:::

---

## 类型 5：Queue ADT（声明 + Enqueue/Dequeue）

### 识别特征
- 要求声明线性队列或循环队列
- 要求写出 Enqueue 和 Dequeue 操作的伪代码
- 关键词："FIFO", "front", "rear", "circular queue"

### 标准解题方法

:::note[标准解题方法]
**Linear Queue 声明**
```pseudocode
CONSTANT MaxSize <- 100
DECLARE Queue : ARRAY[1:MaxSize] OF INTEGER
DECLARE Front, Rear : INTEGER
Front <- 0
Rear <- 0
```

**Enqueue 操作**
```pseudocode
PROCEDURE Enqueue(value: INTEGER)
    IF Rear = MaxSize THEN
        OUTPUT "Queue is full"
    ELSE
        Rear <- Rear + 1
        Queue[Rear] <- value
        IF Front = 0 THEN
            Front <- 1
        ENDIF
    ENDIF
ENDPROCEDURE
```

**Dequeue 操作**
```pseudocode
FUNCTION Dequeue() RETURNS INTEGER
    IF Front = 0 OR Front > Rear THEN
        OUTPUT "Queue is empty"
        RETURN -1
    ELSE
        DECLARE value : INTEGER
        value <- Queue[Front]
        Front <- Front + 1
        RETURN value
    ENDIF
ENDFUNCTION
```

:::

:::info[评分标准（MS 模式）]
- **M1**：队列满检查
- **M2**：队列空检查
- **A1**：Enqueue 正确更新 Rear
- **A2**：Dequeue 正确获取并更新 Front
- **B1**：处理队列初始状态（Front = 0, Rear = 0）

:::

### 真题示例

**示例 1：9618/s23/qp/31 Q11**

> Write pseudocode for Enqueue and Dequeue operations on a linear queue.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Enqueue checks if Rear = MaxSize
- **M2**: Enqueue increments Rear and adds item
- **A1**: Dequeue checks if Queue is empty
- **A2**: Dequeue retrieves item at Front and increments Front
- **B1**: Correct handling of empty queue

</details>

**示例 2：9618/s23/qp/32 Q11**

> A queue is implemented using an array. Write the pseudocode for the Enqueue operation including any necessary declarations.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Array declaration with size
- **M2**: Front/Rear initialised to 0
- **A1**: Check for queue full
- **A2**: Increment Rear, store value
- **B1**: Handle first item (Front = 1 if Front = 0)

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 混淆 Front 与 Rear：Front 指向第一个元素，Rear 指向最后一个元素
2. 忘记更新 Front（Dequeue 后）
3. 线性队列存在假溢出问题：即使前面有空位也无法再添加
4. 队列空的判断条件混淆：Front = 0 或 Front > Rear

:::

---

## 类型 6：Linked List 操作

### 识别特征
- 要求对链表进行插入、删除或搜索
- 涉及 Node 结构（Data + Pointer）
- 关键词："node", "pointer", "next", "linked list traversal"

### 标准解题方法

:::note[标准解题方法]
**Node 声明**
```pseudocode
TYPE Node
    DECLARE Data : INTEGER
    DECLARE Pointer : INTEGER
ENDTYPE
DECLARE List : ARRAY[1:MaxSize] OF Node
DECLARE HeadPointer : INTEGER
DECLARE FreePointer : INTEGER
```

**链表遍历**
```pseudocode
PROCEDURE TraverseList()
    DECLARE Current : INTEGER
    Current <- HeadPointer
    WHILE Current <> -1 DO
        OUTPUT List[Current].Data
        Current <- List[Current].Pointer
    ENDWHILE
ENDPROCEDURE
```

**有序链表插入**
```pseudocode
PROCEDURE InsertItem(value: INTEGER)
    IF FreePointer = 0 THEN
        OUTPUT "No free node"
    ELSE
        DECLARE NewNode : INTEGER
        DECLARE Current, Previous : INTEGER
        NewNode <- FreePointer
        FreePointer <- List[FreePointer].Pointer
        List[NewNode].Data <- value
        Previous <- -1
        Current <- HeadPointer
        WHILE Current <> -1 AND List[Current].Data < value DO
            Previous <- Current
            Current <- List[Current].Pointer
        ENDWHILE
        IF Previous = -1 THEN
            List[NewNode].Pointer <- HeadPointer
            HeadPointer <- NewNode
        ELSE
            List[NewNode].Pointer <- List[Previous].Pointer
            List[Previous].Pointer <- NewNode
        ENDIF
    ENDIF
ENDPROCEDURE
```

:::

:::info[评分标准（MS 模式）]
- **M1**：正确声明 Node 结构和链表数组
- **M2**：正确初始化 HeadPointer 和 FreePointer
- **A1**：插入时正确从 Free list 获取新节点
- **A2**：正确更新前后节点的 pointer
- **B1**：处理空链表或链表头插入的特殊情况

:::

### 真题示例

**示例 1：9618/w22/qp/32 Q11**

> A linked list is used to store integer values in ascending order. Write pseudocode to insert a new value into the linked list.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Declares Node type with Data and Pointer
- **M2**: Allocates new node from free list
- **A1**: Traverses list to find correct insertion point
- **A2**: Updates pointers to insert new node
- **B1**: Handles insertion at head of list

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 忘记检查 Free list 是否为空
2. 插入时忘记更新前驱节点的 pointer
3. 处理链表头插入时逻辑错误：Previous = -1 时需要特殊处理
4. 遍历链表时作为终止条件使用 Current.Pointer 而非 Current

:::

---

## 类型 7：递归（Trace Table 与特征描述）

### 识别特征
- 给出一个递归函数，要求填写 trace table
- 或要求描述递归的特征（base case, recursive case）
- 关键词："recursive", "base case", "call stack"

### 标准解题方法

:::note[标准解题方法]
**递归三要素**
1. **Base case**：递归终止条件，不再调用自身
2. **Recursive case**：函数调用自身，且向 base case 逼近
3. **Progress**：每次调用都使问题规模减小

**Trace Table 填法**
- 每一行记录一次函数调用
- 记录参数值、返回值
- 注意调用栈的顺序：后进先出

**示例：Fibonacci**
```pseudocode
FUNCTION Fib(n: INTEGER) RETURNS INTEGER
    IF n = 0 THEN RETURN 0
    ELSE IF n = 1 THEN RETURN 1
    ELSE RETURN Fib(n - 1) + Fib(n - 2)
    ENDIF
ENDFUNCTION
```

:::

:::info[评分标准（MS 模式）]
- **M1**：正确识别 base case
- **M2**：正确跟踪递归调用的顺序
- **A1**：trace table 中参数值正确
- **A2**：返回值正确
- **B1**：理解递归使用 call stack 进行管理

:::

### 真题示例

**示例 1：9618/s23/qp/31 Q12**

> The recursive function `Fib(n)` is given. Complete the trace table for `Fib(5)`.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: Correct base case values (Fib(0) = 0, Fib(1) = 1)
- **M2**: Correct order of recursive calls
- **A1**: Fib(2) = Fib(1) + Fib(0) = 1
- **A2**: Fib(3) = Fib(2) + Fib(1) = 2
- **A3**: Fib(4) = Fib(3) + Fib(2) = 3
- **A4**: Fib(5) = Fib(4) + Fib(3) = 5

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 缺少 base case：会导致 infinite recursion（栈溢出）
2. 递归调用顺序搞错：Fib(n-1) 与 Fib(n-2) 的调用顺序可能是交替的
3. Trace table 填充顺序错误：递归是先深入后返回（depth-first）
4. 没有认识到递归使用 call stack：每次调用都压栈

:::

---

## 类型 8：Big O Notation

### 识别特征
- 要求给出某算法的 Big O 复杂度
- 或要求解释 Big O 的含义
- 关键词："time complexity", "order of", "Big O"

### 标准解题方法

:::note[标准解题方法]
**常见复杂度**

| Notation | Name | Example Algorithm |
|----------|------|-------------------|
| O(1) | Constant | Access array element |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search |
| O(n log n) | Linearithmic | Merge sort, Quick sort (avg) |
| O(n²) | Quadratic | Bubble sort, Insertion sort |

**Big O 的含义**
- 描述算法运行时间随输入规模增长的增长率（upper bound）
- 关注最坏情况（worst-case）
- 忽略常数因子和低阶项

:::

:::info[评分标准（MS 模式）]
- **M1**：正确识别算法复杂度
- **M2**：解释 Big O 表示最坏情况的增长率
- **A1**：理解忽略常数因子的意义
- **B1**：比较不同算法的效率

:::

### 真题示例

**示例 1：9618/w22/qp/33 Q12(b)**

> State the Big O notation for the binary search algorithm and explain what this means.

<details>
<summary>📝 MS 展开查看</summary>

**Mark Scheme:**
- **M1**: O(log n)
- **M2**: Explanation: the time taken increases logarithmically as n increases
- **A1**: Each step halves the search space
- **B1**: This is more efficient than linear search O(n) for large datasets

</details>

### 常见陷阱

:::warning[常见陷阱]
1. 混淆 Best-case 与 Worst-case：Big O 通常指 worst-case
2. 误认为 O(log n) 比 O(n) 慢：实际上 O(log n) 快得多
3. Binary Search 的复杂度是 O(log n) 不是 O(n)
4. 忘记在比较算法时使用 Big O

:::

---

## 题型总结

| 题型 | 分值 | 难度 | 频率 |
|------|------|------|------|
| Binary search | 4-5 | ⭐⭐ | 必考 |
| Linear search | 3-4 | ⭐ | 中频 |
| Insertion sort | 5-6 | ⭐⭐⭐ | 高频 |
| Stack (Push/Pop) | 5-6 | ⭐⭐ | 必考 |
| Queue (Enqueue/Dequeue) | 5-6 | ⭐⭐ | 高频 |
| Linked list | 6-8 | ⭐⭐⭐ | 中频 |
| Recursion trace | 4-5 | ⭐⭐ | 高频 |
| Big O | 2-3 | ⭐ | 中频 |
