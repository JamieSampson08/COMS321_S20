from formatting import format_values
from helpers import remove_spaces


class Instruction:
    def __init__(self, opcode6):
        self.opcode6 = opcode6

        # store all variations of opcode combinations (in binary)
        self.opcode8 = None
        self.opcode9 = None
        self.opcode10 = None
        self.opcode11 = None

        self.name = None  # key from instruct_dir
        self.assembly = None

        # values for x type of format
        self.shamt = None
        self.Rn = None
        self.Rd = None
        self.Rt = None
        self.Rm = None
        self.aluimm = None
        self.braddr = None
        self.op = None
        self.dtaddr = None
        self.condaddr = None

        self.format_type = None  # FormatType Enum

    def add_properties(self, **kwargs):
        for key, value in kwargs.items():
            # print("{0} = {1}".format(key, value))
            setattr(self, key, value)

    def set_format_values(self, file, values):
        """
        Sets all format values in the given array of values
        If get=True, return a list of values corresponding to the given format names
        :param file: that is being read
        :param values: list of format values to get or set
        :return: list if get=True, else None
        """

        for val in values:
            if "opcode" in val:
                continue

            byte_len = format_values[val]
            binary_val = remove_spaces(file, byte_len)

            if val == "shamt":
                self.shamt = binary_val
            elif val == "Rn":
                self.Rn = binary_val
            elif val == "Rd":
                self.Rd = binary_val
            elif val == "Rt":
                self.Rt = binary_val
            elif val == "Rm":
                self.Rm = binary_val
            elif val == "aluimm":
                self.aluimm = binary_val
            elif val == "braddr":
                self.braddr = binary_val
            elif val == "dtaddr":
                self.dtaddr = binary_val
            elif val == "condaddr":
                self.condaddr = binary_val
            elif val == "op":
                self.op = binary_val
            else:
                print("{} is not a valid format value".format(val))

    def get_format_value(self, value):
        """
        Returns the contents of an instruction's given value
        :param value: the value you are wanting from the instruction
        :return:
        """
        if value == "shamt":
            return self.shamt
        if value == "Rn":
            return self.Rn
        if value == "Rd":
            return self.Rd
        if value == "Rt":
            return self.Rt
        if value == "Rm":
            return self.Rm
        if value == "aluimm":
            return self.aluimm
        if value == "braddr":
            return self.braddr
        if value == "dtaddr":
            return self.dtaddr
        if value == "condaddr":
            return self.condaddr
        if value == "op":
            return self.op

        print("Invalid Instruction Attribute")
        return -1
