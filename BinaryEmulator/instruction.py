from formatting import format_values, FormatType


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

        for attribute in values:
            if "opcode" in attribute:
                continue

            byte_len = format_values[attribute]  # length of format value
            offset = start_offset + byte_len  # end location in 32 bits
            binary_val = master_opcode[start_offset:offset]  # take the bits between the two values
            start_offset = offset  # set the new start point to the end point

            if attribute == "shamt":
                self.shamt = binary_val
            elif attribute == "Rn":
                self.Rn = binary_val
            elif attribute == "Rd":
                self.Rd = binary_val
            elif attribute == "Rt":
                self.Rt = binary_val
            elif attribute == "Rm":
                self.Rm = binary_val
            elif attribute == "aluimm":
                self.aluimm = binary_val
            elif attribute == "braddr":  # signed
                self.braddr = binary_val
            elif attribute == "dtaddr":  # signed
                self.dtaddr = binary_val
            elif attribute == "condaddr":  # signed
                self.condaddr = binary_val
            elif attribute == "op":
                self.op = binary_val
            else:
                print("{} is not a valid format value".format(attribute))

    def get_value(self, attribute):
        """
        Returns the contents of an instruction's given value
        :param attribute: the value you are wanting from the instruction
        :return:
        """
        if attribute == "shamt":
            return self.shamt
        if attribute == "Rn":
            return self.Rn
        if attribute == "Rd":
            return self.Rd
        if attribute == "Rt":
            return self.Rt
        if attribute == "Rm":
            return self.Rm
        if attribute == "aluimm":
            return self.aluimm
        if attribute == "braddr":
            return self.braddr
        if attribute == "dtaddr":
            return self.dtaddr
        if attribute == "condaddr":
            return self.condaddr
        if attribute == "op":
            return self.op

        print("Invalid Instruction Attribute")
        return -1

    def update_value(self, attribute, value):
        """
        Updates one attribute of instruction
        :param attribute: to update
        :param value: to change to
        :return:
        """
        if attribute == "shamt":
            self.shamt = value
        if attribute == "Rn":
            self.Rn = value
        if attribute == "Rd":
            self.Rd = value
        if attribute == "Rt":
            self.Rt = value
        if attribute == "Rm":
            self.Rm = value
        if attribute == "aluimm":
            self.aluimm = value
        if attribute == "braddr":
            self.braddr = value
        if attribute == "dtaddr":
            self.dtaddr = value
        if attribute == "condaddr":
            self.condaddr = value
        if attribute == "op":
            self.op = value

    def print_values(self):
        format_obj = FormatType(self.format_type)
        fill_values = format_obj.value["order"]
        instruction = "{}:\n".format(self.name)
        for attribute in fill_values:
            if "opcode" in attribute:
                continue
            val = self.get_value(attribute)
            attribute_info = "{}({})".format(attribute, str(val))
            instruction += attribute_info + ' '
        print(instruction)

