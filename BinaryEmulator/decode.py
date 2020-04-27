from formatting import FormatType
from instruction import Instruction
from directory import instruct_dir
from conditionals import CONDITIONS


def decode(filename):
    binary_instructions = []
    with open(filename, "rb") as file:
        while True:
            raw_bytes = file.read(4)

            # raw bytes to int
            int_val = int.from_bytes(raw_bytes, byteorder='big')

            if int_val == 0:
                break

            # int to binary string
            master_opcode = format(int_val, "b")  # returns a string of format 10010001 (8 bits)

            # converting int to binary drops the leading zeros, so this adds them back
            if len(master_opcode) != 32:
                len_diff = 32 - len(master_opcode)
                zero_padding = "0" * len_diff
                master_opcode = zero_padding + master_opcode

            # creates all opcode versions with given 32 bit instruction
            opcode6 = master_opcode[:6].encode()
            opcode8 = master_opcode[:8].encode()
            opcode9 = master_opcode[:9].encode()
            opcode10 = master_opcode[:10].encode()
            opcode11 = master_opcode[:11].encode()

            # create a new instruction and set the values of it's opcode attributes
            new_instruction = Instruction()
            new_instruction.add_properties(
                opcode6=opcode6,
                opcode8=opcode8,
                opcode9=opcode9,
                opcode10=opcode10,
                opcode11=opcode11,
            )

            find_instruction_name(new_instruction)

            if new_instruction.name is None:
                print("Error: Opcode Does Not Exist")
                exit(1)

            fill_format_values(master_opcode, new_instruction)
            binary_instructions.append(new_instruction)
            construct_assembly(new_instruction)

    file.close()
    return binary_instructions


def find_instruction_name(instruction):
    """
    Using all variations of opcodes, compare them to valid opcodes
    :param instruction: to identify
    :return: length of the correct opcode for given instruction
    """
    name = None
    opcode_len = 0

    for key, value in instruct_dir.items():
        current_opcode = value["opcode"]

        if instruction.opcode6 == current_opcode:
            name = key
            opcode_len = 6
            break
        if instruction.opcode8 == current_opcode:
            name = key
            opcode_len = 8
        if instruction.opcode9 == current_opcode:
            name = key
            opcode_len = 9
            break
        if instruction.opcode10 == current_opcode:
            name = key
            opcode_len = 10
        if instruction.opcode11 == current_opcode:
            name = key
            opcode_len = 11
            break

    instruction.add_properties(name=name, opcode_len=opcode_len)
    return opcode_len


def fill_format_values(master_opcode, instruction):
    """
    Sets the values of the instruction using it's format type
    :param master_opcode: all 32 bits read in from file
    :param instruction: to get and set data to
    :return:
    """
    format_type = instruct_dir[instruction.name]["format_type"]
    format_obj = FormatType(format_type)
    instruction.add_properties(format_type=format_obj)

    fill_values = format_obj.value["order"]
    # set all the necessary format values for instruction
    instruction.set_format_values(master_opcode, fill_values)


def construct_assembly(instruction):
    """
    Based on the instruction name, read the necessary values and replace them in string
    :param instruction: to construct assembly
    :return:
    """

    # format values that start with # instead of X
    integer_offsets = ["dtaddr", "shamt", "aluimm"]
    signed_values = ["braddr", "dtaddr", "condaddr"]

    dir_instruct = instruct_dir[instruction.name]
    # build the skeleton assembly
    assembly = instruction.name + " " + dir_instruct["assembly"]
    needed_values = dir_instruct["operation"]
    for op in needed_values:
        # convert binary to int
        binary_value = instruction.get_value(op)
        decimal_value = int(binary_value, 2)

        # if binary is supposed to be signed, take the two's compliment
        if op in signed_values:
            if int(binary_value[0]) == 1:
                decimal_value -= 2 ** len(binary_value)

        # handle .cond of B.cond instructions
        if instruction.name == "B.cond" and op == "Rt":
            # dictionary takes in hex string
            condition = CONDITIONS[hex(decimal_value)]
            new_instruct_name = "B.{}".format(condition)
            assembly = assembly.replace(instruction.name, new_instruct_name)

        # formatting for assembly
        if op in integer_offsets:
            # int values
            assembly = assembly.replace(op, "#" + str(decimal_value))
        elif op in signed_values:
            # branch addresses
            assembly = assembly.replace(op, str(decimal_value))
        else:
            # registers
            assembly = assembly.replace(op, "X" + str(decimal_value))

        # replace binary value of attribute with decimal value
        instruction.update_value(op, decimal_value)
    instruction.add_properties(assembly=assembly)
    # instruction.print_values()

