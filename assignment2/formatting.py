from enum import Enum


class FormatType(Enum):
    R = {
        "order": ["opcode11", "Rm", "shamt", "Rn", "Rd"],
    }
    I = {
        "order": ["opcode10", "aluimm", "Rn", "Rd"],
    }
    D = {
        "order": ["opcode11", "dtaddr", "op", "Rn", "Rt"],
    }
    B = {
        "order": ["opcode6", "braddr"],
    }
    CB = {
        "order": ["opcode8", "condaddr", "Rt"],
    }


# all possible format values with corresponding byte length
format_values = {
    "shamt": 6,  # unsigned (64 bits)
    "Rn": 5,  # unsigned
    "Rd": 5,  # unsigned
    "Rt": 5,  # unsigned
    "Rm": 5,  # unsigned
    "aluimm": 12,
    "braddr": 26,  # signed
    "dtaddr": 9,  # signed
    "condaddr": 19,  # signed
    "op": 2,
}
