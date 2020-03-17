from enum import Enum


def calculate_R():
    print("Calculating R instruction")


def calculate_I():
    print("Calculating I instruction")


def calculate_D():
    print("Calculating D instruction")


def calculate_B():
    print("Calculating B instruction")


def calculate_CB():
    print("Calculating CB instruction")


class FormatType(Enum):
    R = {
        "order": ["opcode11", "Rm", "shamt", "Rn", "Rd"],
        "execute": calculate_R,
    }
    I = {
        "order": ["opcode10", "aluimm", "Rn", "Rd"],
        "execute": calculate_I,
    }
    D = {
        "order": ["opcode11", "dtaddr", "op", "Rn", "Rt"],
        "execute": calculate_D,
    }
    B = {
        "order": ["opcode6", "braddr"],
        "execute": calculate_B,
    }
    CB = {
        "order": ["opcode11", "condaddr", "Rt"],
        "execute": calculate_CB,
    }


def printable_char(c):
    return c if c.isprintable() else '.'


def hexdump(file, start, size):
    print("Hexdump")
