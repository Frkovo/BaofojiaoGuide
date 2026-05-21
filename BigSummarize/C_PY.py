# 全局变量大写，C味拉满
GLOBAL_CARD = []
GLOBAL_PLAYERS = []

# 函数名大写+下划线，C标准库遗风
def READ_CARD():
    global GLOBAL_CARD
    fp = None  # C程序员不信任自动垃圾回收
    try:
        fp = open("Card.txt", "r")
        for i in range(13):  # 硬编码，C程序员最爱
            line = fp.readline()
            if not line:
                break
            GLOBAL_CARD.append(int(line.strip()))
    except:
        print("ERROR: FILE NOT FOUND")
    finally:
        if fp:
            fp.close()  # 手动管理资源，C的荣光

# 结构体用字典模拟
def CREATE_PLAYER(name, gender, age, height, grade):
    player = {
        'name': name,
        'gender': gender,
        'age': age,
        'height': height,
        'grade': grade,
        'next': None  # 链表指针，C魂燃烧
    }
    return player

# 手动内存管理模拟
PLAYER_POOL = [None] * 100
PLAYER_INDEX = 0

def ALLOCATE_PLAYER():
    global PLAYER_INDEX
    if PLAYER_INDEX >= 100:
        return -1  # 返回-1表示失败，NULL的Python版
    PLAYER_INDEX += 1
    return PLAYER_INDEX - 1

# 数组操作函数，下标从0开始，C标准
def ARRAY_REVERSE(arr):
    n = len(arr)
    for i in range(n // 2):
        # 经典三变量交换，C程序员的骄傲
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp

# 指针思维写循环
def PRINT_CARDS():
    i = 0
    while i < len(GLOBAL_CARD):
        print(f"Card[{i}] = {GLOBAL_CARD[i]}")
        i += 1  # 自增运算符的荣耀

# 匈牙利命名法遗毒
def bSearch(arr, nTarget, nSize):
    nLeft = 0
    nRight = nSize - 1
    while nLeft <= nRight:
        nMid = (nLeft + nRight) // 2
        if arr[nMid] == nTarget:
            return nMid
        elif arr[nMid] < nTarget:
            nLeft = nMid + 1
        else:
            nRight = nMid - 1
    return -1  # 经典错误码

# 手动实现一切，标准库是弱者的选择
def MY_STRCMP(s1, s2):
    i = 0
    while i < len(s1) and i < len(s2):
        if ord(s1[i]) != ord(s2[i]):
            return ord(s1[i]) - ord(s2[i])
        i += 1
    return len(s1) - len(s2)

# 函数指针的Python版
COMPARE_FUNC = lambda a, b: a - b

def QSORT_STYLE(arr, l, r, cmp):
    if l >= r:
        return
    pivot = arr[l]
    i, j = l, r
    while i < j:
        while i < j and cmp(arr[j], pivot) >= 0:
            j -= 1
        arr[i] = arr[j]
        while i < j and cmp(arr[i], pivot) <= 0:
            i += 1
        arr[j] = arr[i]
    arr[i] = pivot
    QSORT_STYLE(arr, l, i - 1, cmp)
    QSORT_STYLE(arr, i + 1, r, cmp)

# 用列表模拟结构体数组
class NODE:
    def __init__(self):
        self.data = 0
        self.left = -1
        self.right = -1

TREE = [NODE() for _ in range(100)]

# 永远不用的魔法方法
# 永远不用的装饰器
# 永远不用的生成器
# 永远不用的上下文管理器

# 注释风格都带着C味
# /*********************************************
# * 函数功能：洗牌算法
# * 参数说明：无
# * 返回值：无
# *********************************************/
def SHUFFLE_CARDS():
    import random
    n = len(GLOBAL_CARD)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        # 交换
        temp = GLOBAL_CARD[i]
        GLOBAL_CARD[i] = GLOBAL_CARD[j]
        GLOBAL_CARD[j] = temp

# main函数的Python版
if __name__ == "__main__":
    READ_CARD()
    SHUFFLE_CARDS()
    PRINT_CARDS()
