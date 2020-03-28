from formatting import format_values


class Instruction:
    def __init__(self):
        # store all variations of opcode combinations (in binary)
        self.opcode6 = None
        self.opcode8 = None
        self.opcode9 = None
        self.opcode10 = None
        self.opcode11 = None

        self.opcode_len = None

        self.name = None  # key from instruct_dir
        self.assembly = None
        self.branch_name = None

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
            setattr(self, key, value)

    def set_format_values(self, master_opcode, values):
        """
        Sets all format values in the given array of values
        If get=True, return a list of values corresponding to the given format names
        :param master_opcode: all 32 bits read in from file
        :param values: list of format values to get or set
        :return: list if get=True, else None
        """
        start_offset = self.opcode_len  # start location in 32 bits

        for val in values:
            if "opcode" in val:
                continue

            byte_len = format_values[val]  # length of format value
            offset = start_offset + byte_len  # end location in 32 bits
            binary_val = master_opcode[start_offset:offset]  # take the bits between the two values
            start_offset = offset  # set the new start point to the end point

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
            elif val == "braddr":  # signed
                self.braddr = binary_val
            elif val == "dtaddr":  # signed
                self.dtaddr = binary_val
            elif val == "condaddr":  # signed
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
