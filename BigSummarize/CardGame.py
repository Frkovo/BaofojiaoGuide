
# identify the card as the global array
global Card
Card=[]

# read the 13 row of cards from the Card.txt source file and saved in card.
def ReadCard():
    global Card
    try:
        TextFile = "Card.txt"
        File = open(TextFile, 'r')

        for i in range(12):
            line = File.readline()
            Card.append(int(line.rstrip('\n')))
        File.close()
    except IOError:
        print("Could not find file")

# Call read File and make screen to print the card list

ReadCard()
print(Card)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


# def the class player include the Player name String, Player Gender String, Age integer,Height integer
# 创建父类 People（包含姓名、性别、年龄、身高）
class People:
    # private Name as string
    # private Gender as String
    # private Age as Integer
    # private Height as Integer
    def __init__(self, Namep, Genderp, Agep, Heightp):
        self.__Name = Namep
        self.__Gender = Genderp
        self.__Age = Agep
        self.__Height = Heightp

    # People 类的 Setter 方法（与 Player 原有方法名保持一致）
    def SetName(self, Namep):
        self.__Name = Namep

    def set_gender(self, Genderp):
        self.__Gender = Genderp  # 修正原代码的拼写错误（__Nender→__Gender）

    def set_age(self, Agep):
        self.__Age = Agep  # 修正属性名大小写一致

    def set_height(self, Heightp):
        self.__Height = Heightp  # 修正属性名大小写一致

    # People 类的 Getter 方法
    def get_name(self):
        return self.__Name

    def get_gender(self):
        return self.__Gender

    def get_age(self):
        return self.__Age

    def get_height(self):
        return self.__Height

# Player 类继承自 People 父类
class Player(People):
    # Grade 属于 Player 独有的属性
    def __init__(self, Namep, Genderp, Agep, Heightp, Gradep):
        # 调用父类 People 的构造方法，初始化继承的属性（姓名、性别、年龄、身高）
        super().__init__(Namep, Genderp, Agep, Heightp)
        # 初始化 Player 自身的 Grade 属性
        self.__Grade = Gradep

    # Player 独有的 Grade Setter 方法（保留你原有代码）
    def set_grade(self, Gradep):
        self.__Grade = Gradep

    # Player 独有的 Grade Getter 方法（保留你原有代码）
    def get_grade(self):
        return self.__Grade

    # 重写 __str__ 方法（添加 Grade 信息，其他继承属性的打印逻辑不变）
    def __str__(self):
        return (f"Player info：\n"
                f"  Name：{self.get_name()}\n"  # 调用父类的 Getter 方法
                f"  Gender：{self.get_gender()}\n"
                f"  Age：{self.get_age()} 岁\n"
                f"  Height：{self.get_height()} cm\n"
                f"  PlayerGrade：{self.get_grade()}")  # Player 独有的 Grade 属性



# create the array of player
global ArrayPlayer
ArrayPlayer=[]

# Write the function called the ReadPlayerInfo to Read the PlayerInfo to read the line in the PlayerInfo
#  to generate three players and fill in the ArrayPlayer
def ReadPlayerInfo():
    global ArrayPlayer
    try:
        TextFile = "PlayerInfo.txt"
        File = open(TextFile, 'r')
        for i in range(3):
            line = File.readline()
            line = line.strip().split(",")
            # print("---",line)
            ArrayPlayer.append(Player(line[0],line[1],int(line[2]),int(line[3]),line[4]))
        File.close()
    except IOError:
        print("Could not find file")

# call the ReadPlayerInfo method and print the total PlayerInfo
ReadPlayerInfo()
for SinglePlayer in ArrayPlayer:
    print(SinglePlayer)



#Write the shuffle() to shuffle the card in the Card[] array
import random  # 导入随机数模块（仅用于洗牌）

def shuffle():
    global Card  # 操作全局的 Card 数组
    # Fisher-Yates 洗牌算法（简单高效，和 AP 课程逻辑一致）
    # 从最后一张牌反向遍历到第二张牌
    for i in range(len(Card) - 1, 0, -1):
        # 生成 0 到 i 的随机索引（确保每张牌概率均等）
        random_index = random.randint(0, i)
        # 交换当前位置 i 和随机索引的牌（Python 简洁交换写法）
        Card[i], Card[random_index] = Card[random_index], Card[i]

# 调用洗牌函数并打印结果
shuffle()
print("洗牌后的牌组：", Card)



# Use the stack to reverse the cards in the Card list.

# 定义一个栈类
class Stack:
    # 初始化栈，设置栈的容量
    def __init__(self, capacity):
        # 创建一个固定大小的列表来存储栈元素，初始值为None
        self.list = [None] * capacity
        # top指针表示栈顶位置，初始为0（指向第一个可用位置）
        self.top = 0
        # 记录栈的总容量
        self.capacity = capacity

        # 入栈操作，将元素压入栈顶

    def inStack(self, element):
        # 打印当前要入栈的元素
        # 检查栈是否已满（top指针等于容量）
        if self.top == self.capacity:
            print("栈已满，无法入栈")
            return  # 栈满则直接返回

        # 将元素放入当前top指针位置
        self.list[self.top] = element
        # top指针向上移动（指向下一个可用位置）
        self.top += 1

        # # 打印当前栈顶指针位置
        # print(f"当前栈顶指针: {self.top}")
        # # 栈底指针始终为0
        # print(f"当前栈底指针: 0")

    # 出栈操作，从栈顶弹出元素
    def outstack(self):
        # 检查栈是否为空（top指针为0）
        if self.top == 0:
            print("栈已空，无法出栈")
            return  # 栈空则直接返回

        # 先将top指针下移（指向当前栈顶元素）
        self.top -= 1
        # 获取当前栈顶元素
        out_element = self.list[self.top]

        # # 打印出栈的元素
        # print(f"出栈元素: {out_element}")
        # # 打印当前栈顶指针位置
        # print(f"当前栈顶指针: {self.top}")
        # # 栈底指针始终为0
        # print(f"当前栈底指针: 0")

        # 返回出栈的元素
        return out_element

    # # 输出栈中所有元素（从栈顶到栈底）
    # def output(self):
    #     print("栈中元素(从栈顶到栈底):")
    #
    #     # 检查栈是否为空
    #     if self.top == 0:
    #         print("栈为空")
    #         return  # 栈空则直接返回
    #
    #     # 从栈顶到栈底倒序输出元素
    #     # 从top-1开始（当前栈顶元素），到0结束（栈底），步长为-1（倒序）
    #     for i in range(self.top - 1, -1, -1):
    #         # 打印元素并用"------"分隔
    #         print(self.list[i], "------")
    #
    # # 辅助方法：判断栈是否为空
    # def is_empty(self):
    #     """返回布尔值，表示栈是否为空"""
    #     return self.top == 0  # top为0表示栈空
    #
    # # 辅助方法：判断栈是否已满
    # def is_full(self):
    #     """返回布尔值，表示栈是否已满"""
    #     return self.top == self.capacity  # top等于容量表示栈满

CardStack=Stack(len(Card))
for SingleCard in Card:
    CardStack.inStack(SingleCard)

for index in range(len(Card)):
    Card[index]=CardStack.outstack()

print(Card)


# Save the Single Card into Queue by 13 space and output it in the Card again.

# 定义一个循环队列类
class MyQueue:
    # 初始化队列，设置队列容量
    def __init__(self, capacity):
        self.list = [None] * capacity  # 创建固定大小的列表存储队列元素
        self.front = 0  # 队头指针，初始指向0
        self.rear = 0  # 队尾指针，初始指向0

    # 入队操作，向队列尾部添加元素
    def enqueue(self, element):
        # print("enqueue", element)  # 打印入队元素
        # 检查队列是否已满（队尾指针+1取模等于队头指针）
        if (self.rear + 1) % len(self.list) == self.front:
            raise Exception("the queue is full")  # 队列已满抛出异常

        self.list[self.rear] = element  # 将元素放入队尾位置
        # 队尾指针后移，使用取模运算实现循环
        self.rear = (self.rear + 1) % len(self.list)

        # 打印当前队头和队尾指针位置
        # print("current front is", self.front)
        # print("current rear is", self.rear)

    # 出队操作，从队列头部移除元素
    def dequeue(self):
        # 检查队列是否为空（队头指针等于队尾指针）
        if self.rear == self.front:
            raise Exception("Queue is full! ")  # 队列为空抛出异常

        dequeue_element = self.list[self.front]  # 获取队头元素
        # 队头指针后移，使用取模运算实现循环
        self.front = (self.front + 1) % len(self.list)

        # 打印出队元素和当前指针位置
        # print("dequeue_element", dequeue_element)
        # print("current front is", self.front)
        # print("current rear is", self.rear)
        return dequeue_element  # 返回出队的元素

    # 输出队列中的所有元素
    def output(self):
        i = self.front  # 从队头开始
        # 循环直到到达队尾
        while i != self.rear:
            print(self.list[i])  # 打印当前元素
            i = (i + 1) % len(self.list)  # 指针后移，使用取模运算实现循环

Queue1=MyQueue(len(Card)+1)
for SingleCard in Card:
    Queue1.enqueue(SingleCard)

for index in range(len(Card)):
    Card[index]=Queue1.dequeue()

print("After dequeue",Card)







# Use Linked List to save and take the single cards in the cardlist



class LinkedList:
    def __init__(self, size):
        # 初始化数据数组，用于存储链表中的实际元素值，初始值均为None
        self.data_array = [None] * size
        # 初始化指针数组，存储每个位置对应的下一个元素索引
        # 初始形成从1到size-1的连续序列（空闲链表），最后一个位置指向-1表示结束
        self.pointer_array = list(range(1, size)) + [-1]
        # 初始化链表的起始指针，-1表示链表为空
        self.startPointer = -1
        # 初始化堆指针，指向当前可用的第一个空闲位置（初始为0）
        self.heapPointer = 0
        # 存储数组的总大小，用于边界检查（虽然此处未直接使用，但保留便于扩展）
        self.size = size

    def insert(self, value):
        # 检查堆指针是否为-1，若是则表示链表已满，无法插入
        if self.heapPointer == -1:
            print("Linked list is full")
            return
        # 获取当前可用的空闲位置索引（从堆指针获取）
        insert_index = self.heapPointer
        # 将新元素的值存入数据数组的对应位置
        self.data_array[insert_index] = value
        # 更新堆指针为当前位置在指针数组中指向的下一个空闲位置
        self.heapPointer = self.pointer_array[insert_index]

        # 处理链表为空的情况（起始指针为-1）
        if self.startPointer == -1:
            # 将起始指针指向新插入的位置（新元素成为链表第一个节点）
            self.startPointer = insert_index
            # 新位置的指针设为-1，表示它是链表的最后一个元素
            self.pointer_array[insert_index] = -1
        else:
            # 保存原来的起始指针（原链表头部）
            prev_start = self.startPointer
            # 新位置的指针设为原来的起始指针（新元素指向原头部）
            self.pointer_array[insert_index] = prev_start
            # 更新起始指针为新插入的位置（新元素成为新的链表头部）
            self.startPointer = insert_index

    def insert_at_position(self, value, position):
        # 检查堆指针是否为-1，若是则表示链表已满，无法插入
        if self.heapPointer == -1:
            print("Linked list is full")
            return
        # 处理插入位置为0的特殊情况（等价于头插法，直接调用insert方法）
        if position == 0:
            self.insert(value)
            return
        # 从链表头部开始查找，找到要插入位置的前一个节点
        current = self.startPointer
        # 计数变量，用于定位到第position-1个节点
        count = 0
        # 循环移动指针，直到找到目标位置的前一个节点或到达链表末尾
        while current != -1 and count < position - 1:
            # 移动到下一个节点（通过当前节点的指针获取）
            current = self.pointer_array[current]
            # 计数加1，向目标位置靠近
            count += 1
        # 如果current为-1，说明position超出了链表长度范围
        if current == -1:
            print("Position out of range")
            return
        # 获取空闲位置用于插入新元素
        insert_index = self.heapPointer
        # 提前保存下一个空闲位置（避免后续修改指针后丢失）
        next_heap = self.pointer_array[insert_index]
        # 将新元素的值存入数据数组的对应位置
        self.data_array[insert_index] = value
        # 保存前一个节点原来指向的节点索引
        next_index = self.pointer_array[current]
        # 新节点的指针设为前一个节点原来指向的节点（新节点连接原后续节点）
        self.pointer_array[insert_index] = next_index
        # 前一个节点的指针设为新节点的位置（前节点连接新节点）
        self.pointer_array[current] = insert_index
        # 更新堆指针为提前保存的下一个空闲位置
        self.heapPointer = next_heap

    def delete(self, value):
        # 检查起始指针是否为-1，若是则表示链表为空，无法删除
        if self.startPointer == -1:
            print("Linked list is empty")
            return
        # 处理要删除的元素是头节点的特殊情况
        if self.data_array[self.startPointer] == value:
            # 保存当前头节点的索引
            temp = self.startPointer
            # 更新起始指针为原头节点指向的下一个节点（头节点后移）
            self.startPointer = self.pointer_array[self.startPointer]
            # 保存当前堆指针（空闲链表的头部）
            prev_heap = self.heapPointer
            # 将被删除节点的指针指向原堆指针（被删除节点加入空闲链表头部）
            self.pointer_array[temp] = prev_heap
            # 更新堆指针为被删除节点的索引（空闲链表头部更新为该节点）
            self.heapPointer = temp
            return

        # 查找要删除节点的前一个节点（从链表头开始遍历）
        current = self.startPointer
        # 循环条件：当前节点的下一个节点存在，且下一个节点的值不是目标值
        while self.pointer_array[current] != -1 and self.data_array[self.pointer_array[current]] != value:
            # 移动到下一个节点
            current = self.pointer_array[current]

        # 如果找到要删除的节点（当前节点的下一个节点存在）
        if self.pointer_array[current] != -1:
            # 保存要删除节点的索引
            temp = self.pointer_array[current]
            # 更新前一个节点的指针，跳过要删除的节点（直接指向被删除节点的下一个节点）
            self.pointer_array[current] = self.pointer_array[temp]
            # 保存当前堆指针
            prev_heap = self.heapPointer
            # 将被删除节点的指针指向原堆指针（加入空闲链表）
            self.pointer_array[temp] = prev_heap
            # 更新堆指针为被删除节点的索引
            self.heapPointer = temp
        else:
            # 遍历到链表末尾仍未找到目标值，输出提示
            print(f"Value {value} not found in the list")

    def traverse(self):
        # 从链表头开始遍历
        current = self.startPointer
        # 用于存储遍历到的元素值
        elements = []
        # 循环遍历：当前节点不为空（未到达链表末尾）
        while current != -1:
            # 将当前节点的值添加到元素列表
            elements.append(self.data_array[current])
            # 移动到下一个节点
            current = self.pointer_array[current]
        # 打印链表元素（用"->"连接），若为空则打印"Empty list"
        print(" -> ".join(map(str, elements)) if elements else "Empty list")

    def display_arrays(self):
        # 显示数据数组的当前状态
        print("Data array:", self.data_array)
        # 显示指针数组的当前状态
        print("Pointer array:", self.pointer_array)
        # 显示起始指针和堆指针的当前值
        print(f"Start pointer: {self.startPointer}, Heap pointer: {self.heapPointer}")




CardLinkList=LinkedList(len(Card))
for item in Card:
    CardLinkList.insert(item)

print("CardLinkedList traverse")
CardLinkList.traverse()






# Create a class named tree to insert the card in that created by the After dequeue


class Node:
    def __init__(self):
        self.item = None  # 节点存储的整数值
        self.leftPointer = None  # 指向左子节点的指针
        self.rightPointer = None  # 指向右子节点的指针


class BinarySearchCardTree:
    def __init__(self, capacity=12):
        # 初始化树的容量（默认12个节点，与原代码一致）
        self.capacity = capacity
        self.myTree = [Node() for _ in range(capacity)]
        self.nullPointer = -1
        self.rootPointer = self.nullPointer  # 根节点指针初始化为-1
        self.nextFreePointer = 0  # 初始空闲节点为0

        # 初始化空闲链表（与原代码逻辑一致）
        for i in range(capacity - 1):
            self.myTree[i].leftPointer = i + 1
        self.myTree[capacity - 1].leftPointer = self.nullPointer

    def nodeAdd(self, itemAdd):
        # 检查是否还有空闲节点
        if self.nextFreePointer == self.nullPointer:
            print("No nodes free")
            return

        # 获取当前空闲节点并更新nextFreePointer
        itemAddPointer = self.nextFreePointer
        self.nextFreePointer = self.myTree[self.nextFreePointer].leftPointer

        # 初始化新节点
        self.myTree[itemAddPointer].item = itemAdd
        self.myTree[itemAddPointer].leftPointer = self.nullPointer
        self.myTree[itemAddPointer].rightPointer = self.nullPointer

        # 处理空树情况
        if self.rootPointer == self.nullPointer:
            self.rootPointer = itemAddPointer
            return

        # 查找插入位置（与原逻辑一致）
        current = self.rootPointer
        while True:
            if itemAdd < self.myTree[current].item:
                if self.myTree[current].leftPointer == self.nullPointer:
                    self.myTree[current].leftPointer = itemAddPointer
                    break
                else:
                    current = self.myTree[current].leftPointer
            else:
                if self.myTree[current].rightPointer == self.nullPointer:
                    self.myTree[current].rightPointer = itemAddPointer
                    break
                else:
                    current = self.myTree[current].rightPointer

    def preorderTraversal(self, nodeIndex=None):
        # 默认从根节点开始遍历
        if nodeIndex is None:
            nodeIndex = self.rootPointer
        if nodeIndex != self.nullPointer:
            print(self.myTree[nodeIndex].item, end=" ")
            self.preorderTraversal(self.myTree[nodeIndex].leftPointer)
            self.preorderTraversal(self.myTree[nodeIndex].rightPointer)

    def inorderTraversal(self, nodeIndex=None):
        if nodeIndex is None:
            nodeIndex = self.rootPointer
        if nodeIndex != self.nullPointer:
            self.inorderTraversal(self.myTree[nodeIndex].leftPointer)
            print(self.myTree[nodeIndex].item, end=" ")
            self.inorderTraversal(self.myTree[nodeIndex].rightPointer)

    def postorderTraversal(self, nodeIndex=None):
        if nodeIndex is None:
            nodeIndex = self.rootPointer
        if nodeIndex != self.nullPointer:
            self.postorderTraversal(self.myTree[nodeIndex].leftPointer)
            self.postorderTraversal(self.myTree[nodeIndex].rightPointer)
            print(self.myTree[nodeIndex].item, end=" ")

    def levelOrderTraversal(self):
        if self.rootPointer == self.nullPointer:
            return []
        queue = [self.rootPointer]
        result = []
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node_index = queue.pop(0)
                current_level.append(self.myTree[node_index].item)
                if self.myTree[node_index].leftPointer != self.nullPointer:
                    queue.append(self.myTree[node_index].leftPointer)
                if self.myTree[node_index].rightPointer != self.nullPointer:
                    queue.append(self.myTree[node_index].rightPointer)
            result.append(current_level)
        return result



bst = BinarySearchCardTree()

for singlecard in Card:
    bst.nodeAdd(singlecard)
print("preorder")
bst.preorderTraversal()
print()
print("Inorder")
bst.inorderTraversal()
print()
print("Postorder")
bst.postorderTraversal()






# Create 3 Card array named Payer1 card Player2 card and Player3 Card
global Player1Card
global Player2Card
global Player3Card
def split_card_into_three():
    global Card
    total_cards = len(Card)
    print(f"\n===== 开始分牌：总牌数 = {total_cards} 张 =====")

    # 计算每份的基础数量和剩余牌数（处理无法均分的情况）
    base_count = total_cards // 3  # 每份基础张数（13//3=4）
    remainder = total_cards % 3  # 剩余牌数（13%3=1）→ 剩余的牌加到最后一份

    # 初始化三个分牌数组
    array1 = []
    array2 = []
    array3 = []

    # 分牌逻辑：按顺序分配，剩余牌补到最后一份
    # 第一份：前 base_count 张（0 ~ base_count-1）
    array1 = Card[:base_count]
    # 第二份：中间 base_count 张（base_count ~ 2*base_count-1）
    array2 = Card[base_count: 2 * base_count]
    # 第三份：剩余所有牌（2*base_count ~ 末尾）→ 包含剩余的 remainder 张
    array3 = Card[2 * base_count:]

    # 打印分牌结果
    print(f"分牌结果：")
    print(f"第一份（{len(array1)} 张）：{array1}")
    print(f"第二份（{len(array2)} 张）：{array2}")
    print(f"第三份（{len(array3)} 张）：{array3}")

    return array1, array2, array3  # 返回三个分牌数组，方便后续使用


# 调用分牌算法，获取三个数组
Player1Card, Player2Card, Player3Card = split_card_into_three()

# 可选：验证总牌数是否正确（避免分牌遗漏）
total_check = len(Player1Card) + len(Player1Card) + len(Player1Card)
print(f"\n分牌验证：三份总牌数 = {total_check} 张（与原牌数 {len(Card)} 一致）")



print("Player1Card",Player1Card)
print("Player2Card",Player2Card)
print("Player3Card",Player3Card)


# help Player1Card to sort by bubble Sort method
# help Player2Card to sort by insert Sort method
# help Player3Card to sort by selection Sort method

# 原始手牌数据
# Player1Card = [7, 1, 6, 10]  # 冒泡排序
# Player2Card = [8, 9, 5, 2]   # 插入排序
# Player3Card = [3, 4, 11, 12] # 选择排序

# -------------------------- 1. 冒泡排序（Bubble Sort）- 用于Player1 --------------------------
def bubble_sort(arr):
    # 复制原数组，避免修改原始数据
    arr_copy = arr.copy()
    n = len(arr_copy)
    # 外层循环：控制排序轮数（最多n-1轮）
    for i in range(n - 1):
        # 内层循环：每轮比较相邻元素，将大的元素"冒泡"到后面
        # 每轮结束后，最后i+1个元素已排序完成，无需再比较
        for j in range(n - 1 - i):
            if arr_copy[j] > arr_copy[j + 1]:
                # 交换相邻元素
                temp=arr_copy[j]
                arr_copy[j]=arr_copy[j + 1]
                arr_copy[j + 1]=temp

    return arr_copy

# -------------------------- 2. 插入排序（Insert Sort）- 用于Player2 --------------------------
def insert_sort(arr):
    # 复制原数组，避免修改原始数据
    arr_copy = arr.copy()
    n = len(arr_copy)
    # 从第二个元素开始（索引1），依次插入到前面已排序的序列中
    for i in range(1, n):
        # 保存当前要插入的元素
        current = arr_copy[i]
        # 找到当前元素在已排序序列中的插入位置
        j = i - 1
        # 向前遍历已排序序列，比current大的元素向后移动
        while j >= 0 and arr_copy[j] > current:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        # 将current插入到正确位置
        arr_copy[j + 1] = current
    return arr_copy

# -------------------------- 3. 选择排序（Selection Sort）- 用于Player3 --------------------------
def selection_sort(arr):
    # 复制原数组，避免修改原始数据
    arr_copy = arr.copy()
    n = len(arr_copy)
    # 外层循环：控制选择轮数，每轮选择一个最小值
    for i in range(n - 1):
        # 假设当前索引i的元素是最小值
        min_index = i
        # 内层循环：在未排序部分找到最小值的索引
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_index]:
                min_index = j
        # 将最小值交换到当前未排序部分的第一个位置
        arr_copy[i], arr_copy[min_index] = arr_copy[min_index], arr_copy[i]
    return arr_copy

# 执行排序
player1_sorted = bubble_sort(Player1Card)
player2_sorted = insert_sort(Player2Card)
player3_sorted = selection_sort(Player3Card)

# 输出结果
print("=== 排序结果 ===")
print(f"Player1 原始手牌: {Player1Card}")
print(f"Player1 冒泡排序后: {player1_sorted}")
print()
print(f"Player2 原始手牌: {Player2Card}")
print(f"Player2 插入排序后: {player2_sorted}")
print()
print(f"Player3 原始手牌: {Player3Card}")
print(f"Player3 选择排序后: {player3_sorted}")



# Use the binary Search to find the 12 is in which player's Card. .

def BinarySearch(Array,Key):
  First = 0
  Last= len(Array)-1
  while(First <= Last):
     MidIndex = int((First + Last) / 2)
     if Key == Array[MidIndex]:
        return MidIndex
     if Key < Array[MidIndex]:
        Last = MidIndex - 1
     else:
        First = MidIndex + 1
  return -1

if BinarySearch(player1_sorted,12)!=-1:
    print("Found 12 in player1_sorted Card")

if BinarySearch(player2_sorted,12)!=-1:
    print("Found 12 in player2_sorted Card")

if BinarySearch(player3_sorted, 12) != -1:
    print("Found 12 in player3_sorted Card")

#Use the Linear Search method to find which player_sorted card has value5



def LinearSearch(Array,Key):
    for i in range(len(Array)):
        if Key==Array[i]:
            return i
    return -1


if LinearSearch(player1_sorted,5)!=-1:
    print("Found 5 in player1_sorted Card")

if LinearSearch(player2_sorted,5)!=-1:
    print("Found 5 in player2_sorted Card")

if LinearSearch(player3_sorted, 5) != -1:
    print("Found 5 in player3_sorted Card")
