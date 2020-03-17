import sys
from formatting import FormatType
from instruction import Instruction
from directory import instruct_dir, format_values


def main(argv):
    binary_instructions = []

    filename = argv[0]
    print("Filename: {}".format(filename))

    with open(filename, "rb") as file:
        while True:
            opcode6 = file.read(6)

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


def remove_spaces(file, read_length):
    final_line = ""
    while True:
        temp_line = file.read(read_length)
        print(type(temp_line))
        print(temp_line)
        # TODO - convert line to string to remove spaces or something
        num_spaces = temp_line.count(" ")
        if num_spaces == 0:
            break
        temp_line.replace(" ", "")
        read_length = num_spaces
        final_line += temp_line

    return final_line


def find_instruction_name(instruction):
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
    format_type = instruct_dir[instruction.name]["format_type"]
    data_dic = FormatType(format_type).value
    fill_values = data_dic["order"]
    print("{}".format(fill_values))
    get_set_format_values(file, instruction, fill_values)  # set values
    binary_instruct = get_set_format_values(file, instruction, fill_values, get=True)
    print(binary_instruct)


def get_set_format_values(file, instruction, values, get=False):
    """
    Sets all format values in the given array of values
    If get=True, return a list of values corresponding to the given format names
    :param file: that is being read
    :param instruction: to retrieve info from
    :param values: list of format values to get or set
    :param get: defaults to setting values (False)
    :return: list if get=True, else None
    """
    binary_data = []

    for val in values:
        if "opcode" in val:
            if get:
                binary_data.append(val)
            continue
        byte_len = format_values[val]
        binary_val = remove_spaces(file, byte_len)
        print(binary_val)

        if val == "shamt":
            if get:
                binary_data.append(instruction.shamt)
            else:
                instruction.shamt = binary_val
        elif val == "Rn":
            if get:
                binary_data.append(instruction.Rn)
            else:
                instruction.Rn = binary_val
        elif val == "Rd":
            if get:
                binary_data.append(instruction.Rd)
            else:
                instruction.Rd = binary_val
        elif val == "Rt":
            if get:
                binary_data.append(instruction.Rt)
            else:
                instruction.Rt = binary_val
        elif val == "Rm":
            if get:
                binary_data.append(instruction.Rm)
            else:
                instruction.Rm = binary_val
        elif val == "aluimm":
            if get:
                binary_data.append(instruction.aluimm)
            else:
                instruction.aluimm = binary_val
        elif val == "braddr":
            if get:
                binary_data.append(instruction.braddr)
            else:
                instruction.braddr = binary_val
        elif val == "dtaddr":
            if get:
                binary_data.append(instruction.dtaddr)
            else:
                instruction.dtaddr = binary_val
        elif val == "condaddr":
            if get:
                binary_data.append(instruction.condaddr)
            else:
                instruction.condaddr = binary_val
        elif val == "op":
            if get:
                binary_data.append(instruction.op)
            else:
                instruction.op = binary_val
        else:
            print("{} is not a valid format value".format(val))

    if get:
        return binary_data
    return None


if __name__ == "__main__":
   main(sys.argv[1:])