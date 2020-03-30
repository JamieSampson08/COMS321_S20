from register import Register
from constants import STACK_SIZE, MEMORY_SIZE
from emulate import ex_dump
from conditionals import CONDITIONS, Conditional, TYPES


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
        self.condition_registers = {}

        self.init_registers()

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
            print(" ", instruct.assembly)

    def print_memory(self, start, end):
        print(self.memory[start:end])

    def convert_and_store_binary_string(self, decimal_value, address):
        binary_rep = "{:08b}".format(decimal_value)
        before = self.memory[:address]
        after = self.memory[address + 8:]
        self.memory = before + binary_rep + after

    def check_out_of_bounds(self):
        if self.registers[28].data < 8 or self.PC > 4088:
            print("Error: Attempting to access out of bounds address")
            ex_dump(self)

    def shift_memory(self, value):
        start_address = self.memory_location  # DEBUGGING
        self.convert_and_store_binary_string(value, self.memory_location)

        self.memory_location += 8
        # self.print_memory(start_address, self.memory_location) # DEBUGGING

    def set_conditional_flags(self, result):
        if result == 0:
            type_list = "EQUALS"
        elif result > 0:
            type_list = "GREATER"
        elif result < 0:
            type_list = "LESSER"

        for reg in self.condition_registers:
            conditional = reg.data
            if conditional.name in TYPES[type_list]:
                conditional.set_flag()

    def get_value_at_address(self, address):
        binary_string = self.memory[address:address+8]
        value = int(binary_string, 2)
        return value

    def set_value_at_address(self, address, new_value):
        self.convert_and_store_binary_string(new_value, address)

    def print_stats(self):
        print("\nInstructions Executed: {}\nLoads Executed: {}\nStores Executed: {}\n".format(
            self.instructions_executed, self.loads_issued, self.stores_issued))
