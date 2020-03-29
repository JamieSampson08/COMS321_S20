from register import Register
from constants import STACK_SIZE, MEMORY_SIZE


class Machine:
    def __init__(self):
        # subtract from stack
        self.stack = "{:0512b}".format(0)  # string binary representation of all data in stack
        self.stack_size = STACK_SIZE
        # self.stack_location held in register 28's data as int

        # add to memory
        self.memory = "{:04096b}".format(0)  # string binary representation of all data in memory
        self.memory_size = MEMORY_SIZE
        self.memory_location = 0

        self.filename = None
        self.PC = 0  # current instruction index
        self.binary_instructions = None
        self.instructions_executed = 0
        self.loads_issued = 0
        self.stores_issued = 0

        self.registers = []
        self.condition_registers = []

        self.init_registers()

    def init_registers(self):
        # 32 registers
        for i in range(32):
            self.registers.append(Register(i))

        # 14 conditional registers
        for i in range(15):
            self.condition_registers.append(Register(i, is_conditional=True))

    def print_all_registers(self, include_conditional=False):
        print("Registers:")
        for reg in self.registers:
            reg.print_register()

        if include_conditional:
            print("\nConditional Registers:")
            for reg in self.condition_registers:
                reg.print_register()

    def print_program(self):
        print("Program")
        for instruct in self.binary_instructions:
            print(" ", instruct.assembly)
