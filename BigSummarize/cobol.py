# COBOL-PYTHON 模拟器
import random

class COBOLRuntime:
    def __init__(self):
        self.data = {}
        self.labels = {}
        
    def MOVE(self, value, target):
        """COBOL MOVE语句"""
        if isinstance(target, dict):
            target['value'] = value
        else:
            self.data[target] = value
            
    def ADD(self, value, target):
        """COBOL ADD语句"""
        self.data[target] = self.data.get(target, 0) + value
        
    def SUBTRACT(self, value, target):
        """COBOL SUBTRACT语句"""
        self.data[target] = self.data.get(target, 0) - value
        
    def DISPLAY(self, *args):
        """COBOL DISPLAY语句"""
        print(' '.join(str(arg) for arg in args))
        
    def PERFORM(self, start, end=None):
        """COBOL PERFORM循环"""
        if end:
            for i in range(start, end + 1):
                self.data['I'] = i
                # 这里实际应该执行循环体内的代码
        return self
        
    def COMPUTE(self, expression, target):
        """COBOL COMPUTE语句"""
        # 简单表达式求值
        result = eval(expression, {}, self.data)
        self.data[target] = result

# 实际可执行的COBOL风味Python
def COBOL_STYLE_PROGRAM():
    # DATA DIVISION
    CARD_TABLE = [0] * 13
    PLAYER_TABLE = [{'NAME': '', 'GENDER': '', 'AGE': 0, 'HEIGHT': 0, 'GRADE': ''} for _ in range(3)]
    
    # PROCEDURE DIVISION
    print("** COBOL-STYLE CARD PROGRAM **")
    print("INITIALIZATION COMPLETE")
    
    # 200-READ-CARDS
    print("READING CARD DATA")
    try:
        with open('Card.txt', 'r') as file:
            for i in range(13):
                CARD_TABLE[i] = int(file.readline().strip())
    except:
        print("FILE ERROR OCCURRED")
        # 默认数据
        CARD_TABLE = list(range(1, 14))
    
    # 300-READ-PLAYERS
    print("READING PLAYER DATA")
    try:
        with open('PlayerInfo.txt', 'r') as file:
            for i in range(3):
                parts = file.readline().strip().split(',')
                PLAYER_TABLE[i]['NAME'] = parts[0]
                PLAYER_TABLE[i]['GENDER'] = parts[1]
                PLAYER_TABLE[i]['AGE'] = int(parts[2])
                PLAYER_TABLE[i]['HEIGHT'] = int(parts[3])
                PLAYER_TABLE[i]['GRADE'] = parts[4]
    except:
        print("PLAYER FILE ERROR")
        # 默认数据
        for i in range(3):
            PLAYER_TABLE[i] = {
                'NAME': f'Player{i+1}',
                'GENDER': 'M',
                'AGE': 20 + i,
                'HEIGHT': 170 + i * 5,
                'GRADE': 'B'
            }
    
    # 400-SHUFFLE-CARDS
    print("SHUFFLING CARDS")
    for i in range(12, 0, -1):
        j = random.randint(0, i)
        CARD_TABLE[i], CARD_TABLE[j] = CARD_TABLE[j], CARD_TABLE[i]
    
    # 500-DISPLAY-CARDS
    print("CURRENT CARD VALUES:")
    for i in range(13):
        print(f"CARD({i+1}) = {CARD_TABLE[i]}")
    
    # 创建三个玩家手牌
    PLAYER1_CARDS = CARD_TABLE[0:4]
    PLAYER2_CARDS = CARD_TABLE[4:8]
    PLAYER3_CARDS = CARD_TABLE[8:12]
    
    # 600-SORT-PLAYER1 (冒泡排序)
    print("BUBBLE SORT FOR PLAYER 1")
    for i in range(len(PLAYER1_CARDS)-1):
        for j in range(len(PLAYER1_CARDS)-1-i):
            if PLAYER1_CARDS[j] > PLAYER1_CARDS[j+1]:
                PLAYER1_CARDS[j], PLAYER1_CARDS[j+1] = PLAYER1_CARDS[j+1], PLAYER1_CARDS[j]
    
    # 700-SORT-PLAYER2 (插入排序)
    print("INSERTION SORT FOR PLAYER 2")
    for i in range(1, len(PLAYER2_CARDS)):
        key = PLAYER2_CARDS[i]
        j = i-1
        while j >= 0 and PLAYER2_CARDS[j] > key:
            PLAYER2_CARDS[j+1] = PLAYER2_CARDS[j]
            j -= 1
        PLAYER2_CARDS[j+1] = key
    
    # 800-SORT-PLAYER3 (选择排序)
    print("SELECTION SORT FOR PLAYER 3")
    for i in range(len(PLAYER3_CARDS)):
        min_idx = i
        for j in range(i+1, len(PLAYER3_CARDS)):
            if PLAYER3_CARDS[j] < PLAYER3_CARDS[min_idx]:
                min_idx = j
        PLAYER3_CARDS[i], PLAYER3_CARDS[min_idx] = PLAYER3_CARDS[min_idx], PLAYER3_CARDS[i]
    
    # 显示结果
    print("="*50)
    print("PLAYER 1 CARDS (BUBBLE SORTED):", PLAYER1_CARDS)
    print("PLAYER 2 CARDS (INSERTION SORTED):", PLAYER2_CARDS)
    print("PLAYER 3 CARDS (SELECTION SORTED):", PLAYER3_CARDS)
    
    # 搜索示例
    print("="*50)
    print("SEARCHING FOR VALUE 12:")
    for i, cards in enumerate([PLAYER1_CARDS, PLAYER2_CARDS, PLAYER3_CARDS], 1):
        if 12 in cards:
            print(f"VALUE 12 FOUND IN PLAYER {i}")
    
    print("="*50)
    print("PROGRAM EXECUTION COMPLETE")
    print("TOTAL CARDS PROCESSED: 13")
    print("TOTAL PLAYERS: 3")

# 运行程序
if __name__ == "__main__":
    # 创建测试文件
    with open('Card.txt', 'w') as f:
        for i in range(1, 14):
            f.write(f"{i}\n")
    
    with open('PlayerInfo.txt', 'w') as f:
        players = [
            "Alice,F,25,165,A",
            "Bob,M,30,180,B",
            "Charlie,M,22,175,C"
        ]
        for player in players:
            f.write(f"{player}\n")
    
    # 执行COBOL风味程序
    COBOL_STYLE_PROGRAM()