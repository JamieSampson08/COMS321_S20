from directory import instruct_dir


def print_directory():
    """
    Prints all the key value pairs from the dictionary
    :return:
    """
    for name, data in instruct_dir.items():
        print("{} {}".format(name, data["assembly"]))


def how_to_read_mem_stack_table():
    message = "\n         *** HOW TO READ THIS TABLE ***\n" \
              "Left-most Column: offset(hex) of beginning of line\n" \
              "Next 16 columns: values of 16 bytes(hex) following the line offset\n" \
              "Data Between Vertical Bars: gives text value of same 16 bytes\n" \
              "   - if not printable or is an actual period, '.' will print\n" \
              "Single hex num on left column: gives the size of the data\n"
    print(message)


def printable_char(c):
    """
    Convert hex to an int and then int to ascii character
    :param c:
    :return: c if printable, else "."
    """
    val = chr(int(c, 16))
    return val if val.isprintable() else '.'


def format_storage_to_dump(storage):
    """
    Takes contents of memory or stack and formats into hex pairs
    :param storage: memory or stack list
    :return: list of hex pairs
    """
    storage_array = []

    for i in range(0, len(storage), 8):
        binary_string = ""
        for k in range(8):
            binary_string += str(storage[i + k])

        # convert stored binary string to int
        val = int(binary_string, 2)

        # handle if values are negative
        if val < 0:
            val = "{:X}".format(val & (2 ** 64 - 1))
            val = int(val, 16)

        # change int to hex rep
        hex_string = "{:016x}".format(val)
        hex_list = list(hex_string)
        for i in range(0, 16, 2):
            hex_pair = hex_list[i] + hex_list[i+1]
            storage_array.append(hex_pair)
    return storage_array


def hexdump(file, size, machine_state):
    """
    Formats the contents of memory/stack
    :param file: to write to
    :param size: either size of storage or size of stack
    :param machine_state: need access to memory
    :return:
    """
    i = 0

    storage = format_storage_to_dump(machine_state.memory)

    if size == machine_state.stack_size:
        storage = format_storage_to_dump(machine_state.stack)

    while i < (size - size % 16):
        offset = "{:0x}".format(i)

        if len(offset) != 10:
            len_diff = 10 - len(offset)
            zero_padding = "0" * len_diff
            offset = zero_padding + offset
        # offset = 0 -> next 16 bytes (ie. 4 sets of 8 bits)

        file.write("{} "
                   " {} {} {} {} {} {} {} {} " 
                   " {} {} {} {} {} {} {} {}" 
                   " |{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}|"
                   "\n".format(offset,
                               storage[i + 0], storage[i + 1], storage[i + 2], storage[i + 3],
                               storage[i + 4], storage[i + 5], storage[i + 6], storage[i + 7],
                               storage[i + 8], storage[i + 9], storage[i + 10], storage[i + 11],
                               storage[i + 12], storage[i + 13], storage[i + 14], storage[i + 15],
                               printable_char(storage[i + 0]), printable_char(storage[i + 1]),
                               printable_char(storage[i + 2]), printable_char(storage[i + 3]),
                               printable_char(storage[i + 4]), printable_char(storage[i + 5]),
                               printable_char(storage[i + 6]), printable_char(storage[i + 7]),
                               printable_char(storage[i + 8]), printable_char(storage[i + 9]),
                               printable_char(storage[i + 10]),
                               printable_char(storage[i + 11]),
                               printable_char(storage[i + 12]),
                               printable_char(storage[i + 13]),
                               printable_char(storage[i + 14]),
                               printable_char(storage[i + 15])))
        i += 16

    file.write("{:010x}\n".format(size))
