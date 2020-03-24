from directory import instruct_dir


def remove_spaces(file, read_length):
    """
    Reads from the file 1 bit at a time, converts to a string & removes spaces
    :param file: to read from
    :param read_length: expected length of binary
    :return: binary of length read_length
    """
    final_line = ""
    while len(final_line) != read_length:
        temp_line = file.read(1)
        if temp_line == b'\n':
            continue
        # convert binary to string (1s and 0s)
        temp_line = temp_line.decode("utf-8")
        # remove all the spaces
        temp_line = temp_line.replace(" ", "")
        # append to final binary string
        final_line += temp_line

    # return binary string to binary
    return str.encode(final_line)


def print_directory():
    """
    Prints all the key value pairs from the dictionary
    :return:
    """
    for name, data in instruct_dir:
        print("Name: {} Data: {}".format(name, data))


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

    :param file: to write to
    :param start: address location
    :param size:
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
