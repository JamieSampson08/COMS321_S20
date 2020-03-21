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
        self.init_registers()

        self.condition_registers = []
        self.init_condition_registers()

    def init_condition_registers(self):
        for i in range(14):
            self.condition_registers.append(Register(i))

    def init_registers(self):
        for i in range(31):
            self.registers.append(Register(i))

    def print_registers(self):
        for reg in self.registers:
            print("X{}: {}".format(reg.number, reg.data))

    def print_condition_registers(self):
        for reg in self.condition_registers:
            print("X{}: {}".format(reg.number, reg.data))


class Register:
    def __init__(self, number):

        # set usage
        if 0 <= number <= 7:
            self.use = "Arguments/Results"
        elif 9 <= number <= 15:
            self.use = "Temporaries"
        elif 19 <= number <= 27:
            self.use = "Saved"
        elif number == 28:
            self.use = "Stack Pointer"
        elif number == 29:
            self.use = "Frame Pointer"
        elif number == 30:
            self.use = "Return Address"
        elif number == 31:
            self.use = "Constant Value 0"
        else:
            self.use = "General Register"

        self.address = 0 if number == 31 else None
        self.reg_number = number

