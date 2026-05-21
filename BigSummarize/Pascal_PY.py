#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PASCAL风味的Python代码
特点：BEGIN/END、PROCEDURE/FUNCTION、强类型注释、单入口单出口
"""

# Pascal风格常量定义
CONST = {
    'MAX_CARDS': 13,
    'MAX_PLAYERS': 3,
    'FILE_NAME_CARD': 'Card.txt',
    'FILE_NAME_PLAYER': 'PlayerInfo.txt',
    'TRUE': True,
    'FALSE': False
}

# Pascal风格类型定义（用类模拟）
class TCardArray:
    """卡片数组类型"""
    def __init__(self):
        self.data = [0] * CONST['MAX_CARDS']
        self.count = 0

class TPlayerRecord:
    """玩家记录类型"""
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.age = 0
        self.height = 0
        self.grade = ""

class TPlayerArray:
    """玩家数组类型"""
    def __init__(self):
        self.data = [TPlayerRecord() for _ in range(CONST['MAX_PLAYERS'])]
        self.count = 0

# 全局变量（Pascal风格）
VAR = {
    'Cards': TCardArray(),
    'Players': TPlayerArray(),
    'i': 0,
    'j': 0,
    'temp': 0,
    'found': False,
    'key': 0,
    'input_file': None
}

# Pascal风格的PROCEDURE（无返回值）
def PROCEDURE_ReadCards():
    """读取卡片文件"""
    try:
        VAR['input_file'] = open(CONST['FILE_NAME_CARD'], 'r')
        VAR['Cards'].count = 0

        for i in range(CONST['MAX_CARDS']):
            line = VAR['input_file'].readline()
            if not line:
                break
            VAR['Cards'].data[i] = int(line.strip())
            VAR['Cards'].count += 1

        VAR['input_file'].close()
        print(f"成功读取 {VAR['Cards'].count} 张卡片")

    except FileNotFoundError:
        print("错误: 找不到卡片文件")
    except Exception as e:
        print(f"错误: {e}")

def PROCEDURE_ReadPlayers():
    """读取玩家信息"""
    try:
        VAR['input_file'] = open(CONST['FILE_NAME_PLAYER'], 'r')
        VAR['Players'].count = 0

        for i in range(CONST['MAX_PLAYERS']):
            line = VAR['input_file'].readline()
            if not line:
                break

            parts = line.strip().split(',')
            if len(parts) >= 5:
                player = VAR['Players'].data[i]
                player.name = parts[0]
                player.gender = parts[1]
                player.age = int(parts[2])
                player.height = int(parts[3])
                player.grade = parts[4]
                VAR['Players'].count += 1

        VAR['input_file'].close()
        print(f"成功读取 {VAR['Players'].count} 名玩家")

    except FileNotFoundError:
        print("错误: 找不到玩家文件")
    except Exception as e:
        print(f"错误: {e}")

def PROCEDURE_PrintCards():
    """打印所有卡片"""
    print("当前卡片列表:")
    for i in range(VAR['Cards'].count):
        print(f"  Card[{i+1}] = {VAR['Cards'].data[i]}")

def PROCEDURE_PrintPlayers():
    """打印所有玩家"""
    print("玩家信息:")
    for i in range(VAR['Players'].count):
        p = VAR['Players'].data[i]
        print(f"  玩家{i+1}: {p.name}, {p.gender}, {p.age}岁, {p.height}cm, 等级:{p.grade}")

def PROCEDURE_BubbleSort():
    """冒泡排序卡片"""
    n = VAR['Cards'].count
    for i in range(n-1):
        for j in range(n-i-1):
            if VAR['Cards'].data[j] > VAR['Cards'].data[j+1]:
                # 交换元素
                VAR['temp'] = VAR['Cards'].data[j]
                VAR['Cards'].data[j] = VAR['Cards'].data[j+1]
                VAR['Cards'].data[j+1] = VAR['temp']
    print("冒泡排序完成")

def PROCEDURE_ShuffleCards():
    """洗牌"""
    import random
    n = VAR['Cards'].count
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)
        VAR['temp'] = VAR['Cards'].data[i]
        VAR['Cards'].data[i] = VAR['Cards'].data[j]
        VAR['Cards'].data[j] = VAR['temp']
    print("洗牌完成")

# Pascal风格的FUNCTION（有返回值）
def FUNCTION_BinarySearch(key: int) -> int:
    """二分查找（返回位置，从1开始计数）"""
    low = 0
    high = VAR['Cards'].count - 1

    while low <= high:
        mid = (low + high) // 2
        if VAR['Cards'].data[mid] == key:
            return mid + 1  # Pascal索引从1开始
        elif VAR['Cards'].data[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return 0  # 返回0表示未找到

def FUNCTION_LinearSearch(key: int) -> int:
    """线性查找（返回位置，从1开始计数）"""
    for i in range(VAR['Cards'].count):
        if VAR['Cards'].data[i] == key:
            return i + 1  # Pascal索引从1开始
    return 0  # 返回0表示未找到

def FUNCTION_SumCards() -> int:
    """计算卡片总和"""
    total = 0
    for i in range(VAR['Cards'].count):
        total += VAR['Cards'].data[i]
    return total

def FUNCTION_AverageCards() -> float:
    """计算卡片平均值"""
    if VAR['Cards'].count == 0:
        return 0.0
    return FUNCTION_SumCards() / VAR['Cards'].count

def FUNCTION_FindMaxCard() -> int:
    """查找最大卡片"""
    if VAR['Cards'].count == 0:
        return 0

    max_val = VAR['Cards'].data[0]
    for i in range(1, VAR['Cards'].count):
        if VAR['Cards'].data[i] > max_val:
            max_val = VAR['Cards'].data[i]
    return max_val

def FUNCTION_FindMinCard() -> int:
    """查找最小卡片"""
    if VAR['Cards'].count == 0:
        return 0

    min_val = VAR['Cards'].data[0]
    for i in range(1, VAR['Cards'].count):
        if VAR['Cards'].data[i] < min_val:
            min_val = VAR['Cards'].data[i]
    return min_val

# Pascal风格的主程序
def main():
    """主程序（Pascal的BEGIN...END块）"""
    print("=" * 50)
    print("PASCAL风格卡片管理系统")
    print("=" * 50)

    # 读取数据
    PROCEDURE_ReadCards()
    PROCEDURE_ReadPlayers()
    print("-" * 30)

    # 显示原始数据
    PROCEDURE_PrintCards()
    PROCEDURE_PrintPlayers()
    print("-" * 30)

    # 排序
    print("执行冒泡排序...")
    PROCEDURE_BubbleSort()
    PROCEDURE_PrintCards()
    print("-" * 30)

    # 计算统计信息
    print("卡片统计信息:")
    print(f"  卡片总数: {VAR['Cards'].count}")
    print(f"  卡片总和: {FUNCTION_SumCards()}")
    print(f"  卡片平均值: {FUNCTION_AverageCards():.2f}")
    print(f"  最大卡片: {FUNCTION_FindMaxCard()}")
    print(f"  最小卡片: {FUNCTION_FindMinCard()}")
    print("-" * 30)

    # 查找演示
    print("查找演示:")

    # 二分查找（需要有序）
    search_key = 7
    pos = FUNCTION_BinarySearch(search_key)
    if pos > 0:
        print(f"  二分查找: 卡片{search_key}在第{pos}个位置")
    else:
        print(f"  二分查找: 卡片{search_key}未找到")

    # 洗牌后线性查找
    PROCEDURE_ShuffleCards()
    PROCEDURE_PrintCards()

    search_key = 12
    pos = FUNCTION_LinearSearch(search_key)
    if pos > 0:
        print(f"  线性查找: 卡片{search_key}在第{pos}个位置")
    else:
        print(f"  线性查找: 卡片{search_key}未找到")

    print("-" * 30)
    print("程序执行完毕")
    print("=" * 50)

# Pascal程序的典型结构
if __name__ == "__main__":
    """
    PROGRAM CardManagementSystem;
    { 主程序开始 }
    BEGIN
        main();
    END.
    """
    main()
