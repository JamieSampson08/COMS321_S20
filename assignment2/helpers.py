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
def hexdump(file, start, size):
    """
    Formats the contents of memory/stack
    :param file: to write to
    :param start: address location
    :param size: either size of memory or size of stack
    :return:
    """
    i = 0

    while i < (size - size % 16):
        file.write("{:#010x} "
                   " {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} "  # 02hhx
                   " {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} {:#06x} "  # 02hhx
                   " |{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}|"  # char
                   "\n".format(i,
                               start[i + 0], start[i + 1], start[i + 2], start[i + 3],
                               start[i + 4], start[i + 5], start[i + 6], start[i + 7],
                               start[i + 8], start[i + 9], start[i + 10], start[i + 11],
                               start[i + 12], start[i + 13], start[i + 14], start[i + 15],
                               printable_char(start[i + 0]), printable_char(start[i + 1]),
                               printable_char(start[i + 2]), printable_char(start[i + 3]),
                               printable_char(start[i + 4]), printable_char(start[i + 5]),
                               printable_char(start[i + 6]), printable_char(start[i + 7]),
                               printable_char(start[i + 8]), printable_char(start[i + 9]),
                               printable_char(start[i + 10]),
                               printable_char(start[i + 11]),
                               printable_char(start[i + 12]),
                               printable_char(start[i + 13]),
                               printable_char(start[i + 14]),
                               printable_char(start[i + 15])))
        i += 16

    file.write("{:#010x}\n".format(size))
