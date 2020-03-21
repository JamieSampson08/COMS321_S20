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
        # convert binary to string (1s and 0s)
        temp_line = temp_line.decode("utf-8")
        # remove all the spaces
        temp_line = temp_line.replace(" ", "")
        # append to final binary string
        final_line += temp_line

    # return binary string to binary
    return str.encode(final_line)
