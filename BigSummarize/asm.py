#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
汇编风味的Python代码
特点：寄存器、内存、指令、标志位、跳转标签
"""

# 寄存器定义
REG = {
    'AX': 0,    # 累加器
    'BX': 0,    # 基址寄存器
    'CX': 0,    # 计数寄存器
    'DX': 0,    # 数据寄存器
    'SI': 0,    # 源索引
    'DI': 0,    # 目的索引
    'BP': 0,    # 基址指针
    'SP': 0,    # 栈指针
    'IP': 0,    # 指令指针
    'FLAGS': 0  # 标志寄存器
}

# 内存定义 (64K内存空间)
MEMORY = [0] * 65536

# 栈定义 (从0xFFFF向下生长)
STACK_BASE = 0xFFFF

# 标志位掩码
FLAG_ZF = 0x01  # 零标志
FLAG_SF = 0x02  # 符号标志
FLAG_CF = 0x04  # 进位标志
FLAG_OF = 0x08  # 溢出标志

# 指令集
class ASM_INSTRUCTIONS:
    @staticmethod
    def MOV(dest, src):
        """移动数据"""
        if isinstance(dest, str) and dest in REG:
            if isinstance(src, str) and src in REG:
                REG[dest] = REG[src]
            else:
                REG[dest] = src
        elif isinstance(dest, str) and dest.startswith('['):
            # 内存操作
            addr = eval(dest[1:-1])
            MEMORY[addr] = src
        REG['IP'] += 1

    @staticmethod
    def ADD(dest, src):
        """加法"""
        if isinstance(src, str) and src in REG:
            src_val = REG[src]
        else:
            src_val = src

        old_dest = REG[dest] if isinstance(dest, str) else dest
        result = old_dest + src_val

        # 更新标志位
        REG['FLAGS'] = 0
        if result == 0:
            REG['FLAGS'] |= FLAG_ZF
        if result < 0:
            REG['FLAGS'] |= FLAG_SF
        if result > 0xFFFFFFFF:  # 假设32位溢出
            REG['FLAGS'] |= FLAG_CF
        if (old_dest ^ src_val) >= 0 and (old_dest ^ result) < 0:
            REG['FLAGS'] |= FLAG_OF

        if isinstance(dest, str) and dest in REG:
            REG[dest] = result & 0xFFFFFFFF  # 32位截断
        REG['IP'] += 1

    @staticmethod
    def SUB(dest, src):
        """减法"""
        if isinstance(src, str) and src in REG:
            src_val = REG[src]
        else:
            src_val = src

        old_dest = REG[dest] if isinstance(dest, str) else dest
        result = old_dest - src_val

        # 更新标志位
        REG['FLAGS'] = 0
        if result == 0:
            REG['FLAGS'] |= FLAG_ZF
        if result < 0:
            REG['FLAGS'] |= FLAG_SF
        if result < -0xFFFFFFFF:  # 假设32位下溢
            REG['FLAGS'] |= FLAG_CF
        if (old_dest ^ src_val) < 0 and (old_dest ^ result) < 0:
            REG['FLAGS'] |= FLAG_OF

        if isinstance(dest, str) and dest in REG:
            REG[dest] = result & 0xFFFFFFFF  # 32位截断
        REG['IP'] += 1

    @staticmethod
    def MUL(src):
        """乘法 (AX = AX * src)"""
        if isinstance(src, str) and src in REG:
            src_val = REG[src]
        else:
            src_val = src

        result = REG['AX'] * src_val
        REG['AX'] = result & 0xFFFFFFFF
        REG['DX'] = (result >> 32) & 0xFFFFFFFF  # 高32位放DX

        # 更新标志位
        REG['FLAGS'] = 0
        if REG['AX'] == 0:
            REG['FLAGS'] |= FLAG_ZF
        if REG['AX'] & 0x80000000:  # 检查符号位
            REG['FLAGS'] |= FLAG_SF
        REG['IP'] += 1

    @staticmethod
    def DIV(src):
        """除法 (AX = DX:AX / src, DX = 余数)"""
        if isinstance(src, str) and src in REG:
            src_val = REG[src]
        else:
            src_val = src

        dividend = (REG['DX'] << 32) | REG['AX']
        if src_val != 0:
            REG['AX'] = dividend // src_val
            REG['DX'] = dividend % src_val
        else:
            print("错误: 除以零!")

        REG['IP'] += 1

    @staticmethod
    def AND(dest, src):
        """逻辑与"""
        if isinstance(src, str) and src in REG:
            src_val = REG[src]
        else:
            src_val = src

        result = REG[dest] & src_val

        # 更新标志位
        REG['FLAGS'] = 0
        if result == 0:
            REG['FLAGS'] |= FLAG_ZF
        if result & 0x80000000:  # 检查符号位
            REG['FLAGS'] |= FLAG_SF

        REG[dest] = result
        REG['IP'] += 1

    @staticmethod
    def OR(dest, src):
        """逻辑或"""
        if isinstance(src, str) and src in REG:
            src_val = REG[src]
        else:
            src_val = src

        result = REG[dest] | src_val

        # 更新标志位
        REG['FLAGS'] = 0
        if result == 0:
            REG['FLAGS'] |= FLAG_ZF
        if result & 0x80000000:  # 检查符号位
            REG['FLAGS'] |= FLAG_SF

        REG[dest] = result
        REG['IP'] += 1

    @staticmethod
    def XOR(dest, src):
        """逻辑异或"""
        if isinstance(src, str) and src in REG:
            src_val = REG[src]
        else:
            src_val = src

        result = REG[dest] ^ src_val

        # 更新标志位
        REG['FLAGS'] = 0
        if result == 0:
            REG['FLAGS'] |= FLAG_ZF
        if result & 0x80000000:  # 检查符号位
            REG['FLAGS'] |= FLAG_SF

        REG[dest] = result
        REG['IP'] += 1

    @staticmethod
    def CMP(op1, op2):
        """比较 (设置标志位但不存储结果)"""
        if isinstance(op1, str) and op1 in REG:
            val1 = REG[op1]
        else:
            val1 = op1

        if isinstance(op2, str) and op2 in REG:
            val2 = REG[op2]
        else:
            val2 = op2

        result = val1 - val2

        # 更新标志位
        REG['FLAGS'] = 0
        if result == 0:
            REG['FLAGS'] |= FLAG_ZF
        if result < 0:
            REG['FLAGS'] |= FLAG_SF
        if result > 0xFFFFFFFF:  # 假设32位溢出
            REG['FLAGS'] |= FLAG_CF

        REG['IP'] += 1

    @staticmethod
    def JMP(label):
        """无条件跳转"""
        REG['IP'] = label

    @staticmethod
    def JE(label):
        """等于时跳转"""
        if REG['FLAGS'] & FLAG_ZF:
            REG['IP'] = label
        else:
            REG['IP'] += 1

    @staticmethod
    def JNE(label):
        """不等于时跳转"""
        if not (REG['FLAGS'] & FLAG_ZF):
            REG['IP'] = label
        else:
            REG['IP'] += 1

    @staticmethod
    def JG(label):
        """大于时跳转"""
        if not (REG['FLAGS'] & FLAG_ZF) and not (REG['FLAGS'] & FLAG_SF):
            REG['IP'] = label
        else:
            REG['IP'] += 1

    @staticmethod
    def JL(label):
        """小于时跳转"""
        if REG['FLAGS'] & FLAG_SF:
            REG['IP'] = label
        else:
            REG['IP'] += 1

    @staticmethod
    def PUSH(src):
        """压栈"""
        if isinstance(src, str) and src in REG:
            val = REG[src]
        else:
            val = src

        MEMORY[REG['SP']] = val
        REG['SP'] -= 1
        REG['IP'] += 1

    @staticmethod
    def POP(dest):
        """出栈"""
        REG['SP'] += 1
        val = MEMORY[REG['SP']]

        if isinstance(dest, str) and dest in REG:
            REG[dest] = val

        REG['IP'] += 1

    @staticmethod
    def CALL(label):
        """调用子程序"""
        ASM_INSTRUCTIONS.PUSH(REG['IP'] + 1)  # 保存返回地址
        ASM_INSTRUCTIONS.JMP(label)

    @staticmethod
    def RET():
        """从子程序返回"""
        ASM_INSTRUCTIONS.POP('IP')

    @staticmethod
    def INT(interrupt_num):
        """中断调用"""
        if interrupt_num == 0x10:
            # 视频服务
            if REG['AH'] == 0x0E:
                # 显示字符
                char = chr(REG['AL'])
                print(f"[BIOS] 显示: {char}", end='')
        elif interrupt_num == 0x21:
            # DOS服务
            if REG['AH'] == 0x09:
                # 显示字符串
                addr = REG['DX']
                s = []
                while MEMORY[addr] != ord('$'):
                    s.append(chr(MEMORY[addr]))
                    addr += 1
                print(f"[DOS] 字符串: {''.join(s)}")
            elif REG['AH'] == 0x4C:
                # 程序结束
                print(f"[DOS] 程序结束，返回码: {REG['AL']}")
                return False  # 停止执行
        REG['IP'] += 1
        return True

# 汇编程序执行器
class AssemblerVM:
    def __init__(self):
        self.labels = {}
        self.program = []
        self.running = False

    def assemble(self, code_lines):
        """汇编代码到指令列表"""
        # 第一遍：收集标签
        line_num = 0
        for line in code_lines:
            line = line.strip()
            if not line or line.startswith(';'):
                continue

            if line.endswith(':'):
                # 标签定义
                label = line[:-1]
                self.labels[label] = line_num
            else:
                line_num += 1

        # 第二遍：生成指令
        for line in code_lines:
            line = line.strip()
            if not line or line.startswith(';') or line.endswith(':'):
                continue

            # 解析指令
            parts = line.split(';')[0].strip().split()
            instr = parts[0].upper()
            operands = parts[1:] if len(parts) > 1 else []

            # 处理操作数
            processed_operands = []
            for op in operands:
                if op in self.labels:
                    processed_operands.append(self.labels[op])
                elif op.upper() in REG:
                    processed_operands.append(op.upper())
                elif op.startswith('[') and op.endswith(']'):
                    # 内存地址
                    processed_operands.append(op)
                else:
                    # 尝试转换为数字
                    try:
                        if op.startswith('0x'):
                            num = int(op[2:], 16)
                        else:
                            num = int(op)
                        processed_operands.append(num)
                    except:
                        processed_operands.append(op)

            self.program.append((instr, processed_operands))

    def execute(self):
        """执行汇编程序"""
        # 初始化寄存器
        for reg in REG:
            REG[reg] = 0
        REG['SP'] = STACK_BASE

        self.running = True
        REG['IP'] = 0

        print("=" * 60)
        print("汇编虚拟机启动")
        print("=" * 60)

        step = 0
        while self.running and REG['IP'] < len(self.program):
            instr_name, operands = self.program[REG['IP']]

            # 获取指令方法
            instr_method = getattr(ASM_INSTRUCTIONS, instr_name, None)
            if instr_method:
                # 执行指令
                try:
                    if instr_name == 'INT':
                        self.running = instr_method(*operands)
                    else:
                        instr_method(*operands)
                except Exception as e:
                    print(f"指令执行错误: {instr_name} {operands}")
                    print(f"错误信息: {e}")
                    break
            else:
                print(f"未知指令: {instr_name}")
                break

            # 显示状态
            step += 1
            if step <= 20:  # 只显示前20步
                print(f"IP={REG['IP']:04X} | AX={REG['AX']:08X} BX={REG['BX']:08X} CX={REG['CX']:08X} DX={REG['DX']:08X} | FLAGS={REG['FLAGS']:04b}")

            # 安全检查
            if REG['IP'] < 0 or REG['IP'] >= len(self.program):
                print("指令指针越界!")
                break

        print("=" * 60)
        print("程序执行完成")
        print("寄存器最终状态:")
        for reg in ['AX', 'BX', 'CX', 'DX', 'SI', 'DI', 'BP', 'SP']:
            print(f"  {reg}: 0x{REG[reg]:08X} ({REG[reg]})")
        print(f"  FLAGS: {REG['FLAGS']:04b}")
        print("=" * 60)

# 示例汇编程序：计算1+2+3+...+10
asm_code = """
; 汇编风味的Python示例程序
; 计算1+2+3+...+10

start:
    MOV AX, 0      ; 累加器清零
    MOV CX, 1      ; 计数器从1开始
    MOV DX, 10     ; 上限为10

loop_start:
    ADD AX, CX     ; AX = AX + CX
    INC CX         ; CX = CX + 1
    CMP CX, DX     ; 比较CX和DX
    JLE loop_start ; 如果CX <= DX，继续循环

    ; 显示结果
    MOV BX, AX     ; 保存结果到BX
    MOV AH, 0x09   ; DOS显示字符串功能
    MOV DX, msg    ; 字符串地址
    INT 0x21       ; 调用DOS中断

    ; 程序结束
    MOV AH, 0x4C   ; DOS程序结束功能
    MOV AL, 0      ; 返回码0
    INT 0x21       ; 调用DOS中断

msg:
    DB 'Sum = $'
"""

# 创建虚拟机并运行
if __name__ == "__main__":
    vm = AssemblerVM()

    # 准备内存
    msg_addr = 0x1000
    msg = "Sum = "
    for i, c in enumerate(msg):
        MEMORY[msg_addr + i] = ord(c)
    MEMORY[msg_addr + len(msg)] = ord('$')

    # 修改汇编代码中的msg地址
    asm_code_lines = asm_code.split('\n')
    for i, line in enumerate(asm_code_lines):
        if 'msg:' in line:
            asm_code_lines[i] = f"    ; 字符串在内存地址0x{msg_addr:04X}"
            break

    # 添加INC指令（递增）
    ASM_INSTRUCTIONS.INC = lambda dest: ASM_INSTRUCTIONS.ADD(dest, 1)

    # 添加DEC指令（递减）
    ASM_INSTRUCTIONS.DEC = lambda dest: ASM_INSTRUCTIONS.SUB(dest, 1)

    # 添加JLE指令（小于等于时跳转）
    ASM_INSTRUCTIONS.JLE = lambda label: ASM_INSTRUCTIONS.JL(label) if REG['FLAGS'] & FLAG_SF else ASM_INSTRUCTIONS.JE(label)

    # 添加DB伪指令处理
    original_assemble = vm.assemble
    def custom_assemble(code_lines):
        processed_lines = []
        for line in code_lines:
            if line.strip().startswith('DB'):
                # 忽略DB指令，已在内存中设置
                continue
            processed_lines.append(line)
        original_assemble(processed_lines)
    vm.assemble = custom_assemble

    # 运行程序
    vm.assemble(asm_code_lines)

    # 修改程序中的标签地址
    if 'msg' in vm.labels:
        # 替换msg标签为实际地址
        for i, (instr, operands) in enumerate(vm.program):
            if instr == 'MOV' and len(operands) > 1 and operands[1] == vm.labels['msg']:
                vm.program[i] = ('MOV', [operands[0], msg_addr])

    vm.execute()

    # 显示计算结果
    print(f"计算结果: 1+2+...+10 = {REG['AX']}")
    print()

    # 演示直接汇编指令
    print("直接指令演示:")
    print("-" * 40)

    # 重置寄存器
    for reg in REG:
        REG[reg] = 0

    # 执行一些指令
    print("MOV AX, 5")
    ASM_INSTRUCTIONS.MOV('AX', 5)
    print(f"AX = {REG['AX']}")

    print("ADD AX, 3")
    ASM_INSTRUCTIONS.ADD('AX', 3)
    print(f"AX = {REG['AX']}")

    print("MOV BX, 4")
    ASM_INSTRUCTIONS.MOV('BX', 4)
    print(f"BX = {REG['BX']}")

    print("MUL BX")
    ASM_INSTRUCTIONS.MUL('BX')
    print(f"AX = {REG['AX']}, DX = {REG['DX']}")

    print("CMP AX, 0")
    ASM_INSTRUCTIONS.CMP('AX', 0)
    print(f"FLAGS = {REG['FLAGS']:04b}")

    print("-" * 40)
