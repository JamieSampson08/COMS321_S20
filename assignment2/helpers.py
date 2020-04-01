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

    :param c:
    :return: c if printable, else "."
    """
    return c if c.isprintable() else '.'


# TODO - broken
def hexdump(file, start, size, machine_state):
    """
    Formats the contents of storage/stack
    :param file: to write to
    :param start: address location
    :param size: either size of storage or size of stack
    :param machine_state: need access to memory
    :return:
    """
    i = 0
    storage = machine_state.storage

    while i < (size - size % 16):
        file.write("{:#010x} "
                   " {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} "  # 02hhx
                   " {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} "  # 02hhx
                   " |{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}|"  # char
                   "\n".format(i,
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

    file.write("{:#010x}\n".format(size))
