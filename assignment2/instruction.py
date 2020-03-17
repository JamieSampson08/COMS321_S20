class Instruction:
    def __init__(self, opcode6):
        self.opcode6 = opcode6

        # store all variations of opcode combinations (in binary)
        self.opcode8 = None
        self.opcode9 = None
        self.opcode10 = None
        self.opcode11 = None

        self.name = None  # key from instruct_dir

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

        self.execute = None # what format type function to call to execute assembly
        self.assembly = None  # actual assembly instruction

    def add_properties(self, **kwargs):
        for key, value in kwargs.items():
            # print("{0} = {1}".format(key, value))
            setattr(self, key, value)
