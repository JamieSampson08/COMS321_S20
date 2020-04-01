TYPES = {
    "GREATER": ["GE", "GT", "HI", "HS", "NE", "PL"],
    "LESSER": ["LE", "LO", "LS", "LT", "MI", "NE"],
    "EQUALS": ["EQ", "GE", "HS", "LE", "LS", "PL"],
}

# B.cond condition extensions mapping
CONDITIONS = {
    '0x0': "EQ",
    '0x1': "NE",
    '0x2': "HS",
    '0x3': "LO",
    '0x4': "MI",
    '0x5': "PL",
    '0x6': "VS",
    '0x7': "VC",
    '0x8': "HI",
    '0x9': "LS",
    '0xa': "GE",
    '0xb': "LT",
    '0xc': "GT",
    '0xd': "LE",
}


class Conditional:
    def __init__(self, condition):
        self.flag = 0
        self.name = condition
        self.type = None

        self._set_type()

    def _set_type(self):
        for condition_type, conditions in TYPES.items():
            if self.name in conditions:
                self.type = condition_type
                return
        # print("{} is always 0".format(self.name))  # DEBUG

    def reset_flag(self):
        self.flag = 0

    def set_flag(self):
        self.flag = 1

    def print_condition(self):
        print("({}) {} : {}".format(self.type, self.name, self.flag))

