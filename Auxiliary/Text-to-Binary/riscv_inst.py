class RISCV_Inst:
    def __init__(self):
        self.opcode = ''
        self.operand_type = ''
        self.dest = ''
        self.src = []
        self.imm = None