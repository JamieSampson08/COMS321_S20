from formatting import FormatType


def print_directory():
    for name, data in instruct_dir:
        print("Name: {} Data: {}".format(name, data))


# format value with corresponding byte length
format_values = {
    "shamt": 6,
    "Rn": 5,
    "Rd": 5,
    "Rt": 5,
    "Rm": 5,
    "aluimm": 12,
    "braddr": 26,
    "dtaddr": 9,
    "condaddr": 16,
    "op": 2,
}


# key = instruction name
instruct_dir = {
    "ADD":
    {
        "opcode": b'10001011000',
        "format_type": FormatType.R,
    },
    "ADDI": {
        "opcode": b'1001000100',
        "format_type": FormatType.I,
    },
    "AND": {
        "opcode": b'10001010000',
        "format_type": FormatType.R,
    },
    "ANDI": {
        "opcode": b'1001001000',
        "format_type": FormatType.I,
    },
    "B": {
        "opcode": b'000101',
        "format_type": FormatType.B,
    },
    "B.cond": {
        "opcode": b'01010100',
        "format_type": FormatType.CB,
    },
    "BL": {
        "opcode": b'100101',
        "format_type": FormatType.B,
    },
    "BR": {
        "opcode": b'11010110000',
        "format_type": FormatType.R,
    },
    "CBNZ": {
        "opcode": b'10110101',
        "format_type": FormatType.CB,
    },
    "CBZ": {
        "opcode": b'10110100',
        "format_type": FormatType.CB,
    },
    # DONT CHECK
    "DUMP": {
        "opcode": b'11111111110',
        "format_type": FormatType.R,
    },
    "EOR": {
        "opcode": b'11001010000',
        "format_type": FormatType.R,
    },
    "EORI": {
        "opcode": b'1101001000',
        "format_type": FormatType.I,
    },
    # DO NOT DO
    "HALT": {
        "opcode": b'11111111111',
        "format_type": FormatType.R,
    },
    "LDUR": {
        "opcode": b'11111000010',
        "format_type": FormatType.D,
    },
    "LDURB": {
        "opcode": b'00111000010',
        "format_type": FormatType.D,
    },
    "LDURH": {
        "opcode": b'01111000010',
        "format_type": FormatType.D,
    },
    "LDURSW": {
        "opcode": b'10111000100',
        "format_type": FormatType.D,
    },
    "LSL": {
        "opcode": b"11010011011",
        "format_type": FormatType.R,
    },
    "LSR": {
        "opcode": b"11010011010",
        "format_type": FormatType.R,
    },
    "MUL": {
        "opcode": b"10011011000",
        "format_type": FormatType.R,
        "shamt": b"011111"
    },
    "ORR": {
        "opcode": b"10101010000",
        "format_type": FormatType.R,
    },
    "ORRI": {
        "opcode": b"1011001000",
        "format_type": FormatType.I,
    },
    "PRNL": {
        "opcode": b"11111111100",
        "format_type": FormatType.R,
    },
    "PRNT": {
        "opcode": b"11111111101",
        "format_type": FormatType.R,
    },
    "SDIV": {
        "opcode": b"10011010110",
        "format_type": FormatType.R,
        "shamt": b"000010"
    },
    "SMULH": {
        "opcode": b"10011011010",
        "format_type": FormatType.R,
    },
    "STUR": {
        "opcode": b"11111000000",
        "format_type": FormatType.D,
    },
    "STURW": {
        "opcode": b"10111000000",
        "format_type": FormatType.D,
    },
    "SUB": {
        "opcode": b"11001011000",
        "format_type": FormatType.R,
    },
    "SUBI": {
        "opcode": b"1101000100",
        "format_type": FormatType.I,
    },
    "SUBIS": {
        "opcode": b"1111000100",
        "format_type": FormatType.I,
    },
    "SUBS": {
        "opcode": b"11101011000",
        "format_type": FormatType.R,
    },
    "UDIV": {
        "opcode": b"10011010110",
        "format_type": FormatType.R,
        "shamt": b"000011",
    },
    "UMULH": {
        "opcode": b"10011011110",
        "format_type": FormatType.R,
    },
}

# B.cond condition extensions
conditions = {
    "EQ": 0x0,
    "NE": 0x1,
    "HS": 0x2,
    "LO": 0x3,
    "MI": 0x4,
    "PL": 0x5,
    "VS": 0x6,
    "VC": 0x7,
    "HI": 0x8,
    "LS": 0x9,
    "GE": 0x10,
    "LT": 0x11,
    "GT": 0x12,
    "LE": 0x13,
}