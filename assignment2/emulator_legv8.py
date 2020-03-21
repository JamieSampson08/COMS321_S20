import sys

from formatting import FormatType
from instruction import Instruction
from directory import instruct_dir


def main(argv):
    binary_instructions = []

    filename = argv[0]
    print("Filename: {}".format(filename))

    with open(filename, "rb") as file:
        while True:
            opcode6 = file.read(6)
            # print(opcode6)
            if opcode6 == b"":
                print("Reached End of File")
                break

            new_instruction = Instruction(opcode6)

            opcode8 = opcode6 + file.read(2)
            opcode9 = opcode8 + file.read(1)
            opcode10 = opcode9 + file.read(1)
            opcode11 = opcode10 + file.read(1)

            new_instruction.add_properties(
                opcode8=opcode8,
                opcode9=opcode9,
                opcode10=opcode10,
                opcode11=opcode11,
            )

            opcode_len = find_instruction_name(new_instruction)
            # print("Opcode Len: {}".format(opcode_len))
            if new_instruction.name is None:
                print("Opcode Does Not Exist")
                exit(1)

            # print("Original Position: {}".format(file.tell()))

            # go back 11 bytes (ie. max bytes looked at to find possible opcode)
            file.seek(-11, 1)  # 1 = referance to current location

            # add new opcode length
            file.seek(opcode_len, 1)
            # print("New Position: {}".format(file.tell()))

            fill_format_values(file, new_instruction)

            binary_instructions.append(new_instruction)
            construct_assembly(new_instruction)
            print("\n")


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

    print("Instruction Name: {}".format(name))
    instruction.add_properties(name=name)
    return opcode_len


def fill_format_values(file, instruction):
    """
    Sets the values of the instruction using it's format type
    :param file: to read from
    :param instruction: to get and set data to
    :return:
    """
    format_type = instruct_dir[instruction.name]["format_type"]

    format_obj = FormatType(format_type)
    instruction.add_properties(format_type=format_obj, execute=format_obj.value["execute"])

    fill_values = format_obj.value["order"]

    print("{}".format(fill_values))
    instruction.set_format_values(file, fill_values)


def construct_assembly(instruction):
    """
    Based on the instruction name, read the necessary values and replace them in string
    :param instruction: to construct assembly
    :return:
    """

    dir_instruct = instruct_dir[instruction.name]

    assembly = instruction.name + " " + dir_instruct["assembly"]
    print(assembly)
    needed_values = dir_instruct["operation"]
    for op in needed_values:
        binary_value = instruction.get_format_value(op)
        # print ("{} : {}".format(type(binary_value), binary_value))
        decimal_value = int(binary_value, 2)
        assembly = assembly.replace(op, "X" + str(decimal_value))

    print(assembly)
    instruction.add_properties(assembly=assembly)


if __name__ == "__main__":
   main(sys.argv[1:])