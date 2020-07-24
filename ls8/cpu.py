"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010
ADD = 0b10100000
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
RET = 0b00010001
class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8 # Registers
        self.reg[7] = 0xF4
        self.ram = [0] * 256 # RAM
        self.pc = 0
        self.fl = 0
        self.running = True
        self.branch_table = {}
        self.branch_table[HLT] = self.handle_HLT

    def load(self, program):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        for instruction in program:
            # self.ram[address] = instruction
            self.ram_write(instruction, address)
            address += 1

    def handle_HLT(self):
        return False
    
    def ram_read(self, MAR):
        return self.ram[MAR]

    def ram_write(self, MDR, MAR):
        self.ram[MAR] = MDR


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        # self.trace()
        running = True
        while running:
            IR = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if IR == HLT:
                # self.trace()
                # running = False
                running = self.handle_HLT()

            if IR == LDI:
                # self.trace()
                # self.ram_write(operand_b, operand_a)
                self.reg[operand_a] = operand_b

            if IR == ADD:
                self.reg[operand_a] += self.reg[operand_b]

            if IR == MUL:
                # self.trace()
                self.reg[operand_a] *= self.reg[operand_b]
                # self.trace()

            if IR == PRN:
                # self.trace()
                print(self.reg[operand_a])

            if IR == PUSH:
                self.reg[7] -= 1
                value = self.reg[operand_a]

                self.ram_write(value, self.reg[7])

            if IR == POP:
                value = self.ram_read(self.reg[7])
                self.reg[operand_a] = value
                self.reg[7] += 1

            if IR == CALL:
                self.reg[7] -= 1
                self.ram_write(self.pc + 2, self.reg[7])
                self.pc = self.reg[operand_a]
                continue

            if IR == RET:
                self.pc = self.ram_read(self.reg[7])
                self.reg[7] += 1
                continue

            self.pc += (IR >> 6) + 1