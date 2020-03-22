from register import Register


class Machine:
    def __init__(self):
        # subtract from stack
        self.stack = bytes(512)
        self.stack_size = bytes(512)

        # add to memory
        self.memory = bytes(0)
        self.memory_size = bytes(4096)

        self.PC = 0

        self.registers = []
        self.condition_registers = []

        self.init_registers()

    def init_registers(self):
        # 32 registers
        for i in range(31):
            self.registers.append(Register(i))

        # 14 conditional registers
        for i in range(14):
            self.condition_registers.append(Register(i, is_conditional=True))

    def print_all_registers(self, include_conditional=False):
        for reg in self.registers:
            reg.print_register()

        if include_conditional:
            print("Conditional Registers")
            for reg in self.condition_registers:
                reg.print_register()

