from register import Register
from constants import STACK_SIZE, MEMORY_SIZE
from emulate import ex_dump
from conditionals import CONDITIONS, Conditional, TYPES


class Machine:
    def __init__(self):
        # subtract from stack (ie. fill stack backwards)
        self.stack = []
        self.stack_size = STACK_SIZE

        # add to memory (ie. fill memory forwards)
        self.memory = []
        self.memory_size = MEMORY_SIZE
        self.memory_location = 0

        self.filename = None
        self.PC = 0  # current instruction index
        self.altered_pc = False
        self.binary_instructions = None
        self.instructions_executed = 0
        self.loads_issued = 0
        self.stores_issued = 0

        self.registers = []
        self.condition_registers = {}

        self.init_registers()
        self.init_storage()

    def init_storage(self):
        for i in range(self.memory_size):
            self.memory.append(0)

        for i in range(self.stack_size):
            self.stack.append(0)

    def init_registers(self):
        # 32 registers
        for i in range(32):
            self.registers.append(Register(i))

        # 14 conditional registers
        count = 0
        for val in CONDITIONS.values():
            self.condition_registers.update({val: Register(count, is_conditional=True)})
            reg = self.condition_registers[val]
            reg.data = Conditional(val)
            count += 1

    def print_all_registers(self, include_conditional=False):
        print("Registers:")
        for reg in self.registers:
            reg.print_register()

        if include_conditional:
            print("\nConditional Registers:")
            for reg in self.condition_registers.values():
                reg.print_register()

    def print_program(self):
        print("Program")
        for instruct in self.binary_instructions:
            to_print = instruct.assembly
            to_print = to_print.replace("X28", "SP")
            to_print = to_print.replace("X29", "FP")
            to_print = to_print.replace("X30", "LR")
            to_print = to_print.replace("X31", "XZR")
            print(" ", to_print)

    def check_out_of_bounds(self):
        if self.registers[28].data < 8 or self.PC > 4088:
            print("Error: Attempting to access out of bounds address")
            ex_dump(self)

    def get_value_at_address(self, address, in_stack):
        binary_string = ""

        for i in range(8):
            if in_stack:
                binary_string += str(self.stack[address+i])
            else:
                binary_string += str(self.memory[address+i])

        value = int(binary_string, 2)
        return value

    def set_value_at_address(self, address, new_value, in_stack):
        binary_rep = list("{:08b}".format(new_value))

        for i in range(8):
            if in_stack:
                self.stack[address+i] = binary_rep[i]
            else:
                self.memory[address+i] = binary_rep[i]

    def print_stats(self):
        print("\nInstructions Executed: {}\nLoads Executed: {}\nStores Executed: {}\n".format(
            self.instructions_executed, self.loads_issued, self.stores_issued))

    def set_conditional_flags(self, result):
        self.reset_conditional_registers()
        if result == 0:
            type_list = "EQUALS"
        elif result > 0:
            type_list = "GREATER"
        elif result < 0:
            type_list = "LESSER"

        for reg in self.condition_registers.values():
            conditional = reg.data
            if conditional.name in TYPES[type_list]:
                conditional.set_flag()

    def get_conditional_value(self, reg_number):
        for key, value in self.condition_registers.items():
            if value.reg_number == reg_number:
                return value.data.flag
        print("Error: Conditional Register {} does not exist".format(reg_number))

    def reset_conditional_registers(self):
        for reg in self.condition_registers.values():
            reg.data.reset_flag()
