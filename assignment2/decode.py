import binascii
import sys

from formatting import FormatType
from instruction import Instruction
from directory import instruct_dir, conditions


def decode(filename, machine_state):
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
            print(len(master_opcode))

            opcode6 = master_opcode[:6].encode()
            opcode8 = master_opcode[:8].encode()
            print(opcode8)
            opcode9 = master_opcode[:9].encode()
            opcode10 = master_opcode[:10].encode()
            opcode11 = master_opcode[:11].encode()

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
                print("Opcode Does Not Exist")
                return

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

    dir_instruct = instruct_dir[instruction.name]
    # build the skeleton assembly
    assembly = instruction.name + " " + dir_instruct["assembly"]
    needed_values = dir_instruct["operation"]
    for op in needed_values:
        # convert binary to int
        binary_value = instruction.get_format_value(op)
        decimal_value = int(binary_value, 2)
        # handle B.cond weirdness
        if instruction.name == "B.cond" and op == "Rt":
            # dictionary takes in hex string
            condition = conditions[hex(decimal_value)]
            new_instruct_name = "B.{}".format(condition)
            assembly = assembly.replace(instruction.name, new_instruct_name)
        elif op in integer_offsets:
            assembly = assembly.replace(op, "#" + str(decimal_value))
        else:
            assembly = assembly.replace(op, "X" + str(decimal_value))
    instruction.add_properties(assembly=assembly)
    print(assembly)

