from register import Register


class Machine:
    def __init__(self):
        # subtract from stack
        self.stack = bytes(512)
        self.stack_size = 512

        # add to memory
        self.memory = bytes(0)
        self.memory_size = 4096

        self.PC = 0
        self.filename = None
        self.binary_instructions = None

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
