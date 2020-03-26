import sys

from helpers import hexdump, how_to_read_mem_stack_table
from driver import machine_state


def ex_add(instruction):
    print("ADD")


def ex_addi(instruction):
    print("ADDI")


def ex_and(instruction):
    print("AND")


def ex_andi(instruction):
    print("ANDI")


def ex_b(instruction):
    print("B")


def ex_b_cond(instruction):
    print("B.cond")


def ex_bl(instruction):
    print("BL")


def ex_br(instruction):
    print("BR")


def ex_cbnz(instruction):
    print("CBNZ")


def ex_cbz(instruction):
    print("CBZ")


def ex_dump(start=0):
    machine_state.print_all_registers(include_conditional=True)
    how_to_read_mem_stack_table()
    print("Memory:\n")
    # hexdump(sys.stdout, start, machine_state.memory_size)

    print("Stack:\n")
    # hexdump(sys.stdout, start, machine_state.stack_size)

    machine_state.print_program()
    exit(1)


def ex_eor(instruction):
    print("EOR")


def ex_eori(instruction):
    print("EORI")


def ex_halt():
    print("HALT")
    ex_dump()
    exit()


def ex_ldur(instruction):
    print("LDUR")


def ex_ldurb(instruction):
    print("LDURB NOT IMPLEMENTED")


def ex_ldurh(instruction):
    print("LDURH NOT IMPLEMENTED")


def ex_ldursw(instruction):
    print("LDRSW NOT IMPLEMENTED")


def ex_lsl(instruction):
    print("LSL")


def ex_lsr(instruction):
    print("LSR")


def ex_mul(instruction):
    print("MUL")


def ex_orr(instruction):
    print("ORR")


def ex_orri(instruction):
    print("ORRI")


def ex_prnl():
    print("PRNL")
    print("\n")


def ex_prnt():
    print("PRNT")
    machine_state.print_all_registers(include_conditional=True)


def ex_sdiv(instruction):
    print("SDIV NOT IMPLEMENTED")


def ex_smulh(instruction):
    print("SMULH NOT IMPLEMENTED")


def ex_stur(instruction):
    print("STUR")


def ex_sturh(instruction):
    print("STURH NOT IMPLEMENTED")


def ex_sturw(instruction):
    print("STURW NOT IMPLEMENTED")


def ex_sturw(instruction):
    print("STURW NOT IMPLEMENTED")


def ex_sub(instruction):
    print("SUB")


def ex_subi(instruction):
    print("SUBI")


def ex_subis(instruction):
    print("SUBIS")


def ex_subs(instruction):
    print("SUBS")


def ex_udiv(instruction):
    print("UDIV NOT IMPLEMENTED")


def ex_umulh(instruction):
    print("UMULH NOT IMPLEMENTED")


def execute_assembly(binary_instructions, filename):
    machine_state.filename = filename
    machine_state.binary_instructions = binary_instructions

    # TODO - remove next 3 lines
    machine_state.print_program()
    ex_dump()
    exit(1)

    for instruction in binary_instructions:
        name = instruction.name
        if name == "ADD":
            ex_add(instruction)
        elif name == "ADDI":
            ex_addi(instruction)
        elif name == "AND":
            ex_and(instruction)
        elif name == "ANDI":
            ex_addi(instruction)
        elif name == "B":
            ex_b(instruction)
        elif name == "B.cond":
            ex_b_cond(instruction)
        elif name == "BL":
            ex_bl(instruction)
        elif name == "BR":
            ex_br(instruction)
        elif name == "CBNZ":
            ex_cbnz(instruction)
        elif name == "CBZ":
            ex_cbz(instruction)
        elif name == "DUMP":
            ex_dump()
        elif name == "EOR":
            ex_eor(instruction)
        elif name == "EORI":
            ex_eori(instruction)
        elif name == "HALT":
            ex_halt()
        elif name == "LDUR":
            ex_ldur(instruction)
        elif name == "LDURB":
            ex_ldurb(instruction)
        elif name == "LDURH":
            ex_ldurh(instruction)
        elif name == "LDURSW":
            ex_ldursw(instruction)
        elif name == "LSL":
            ex_lsl(instruction)
        elif name == "LSR":
            ex_lsr(instruction)
        elif name == "MUL":
            ex_mul(instruction)
        elif name == "ORR":
            ex_orr(instruction)
        elif name == "ORRI":
            ex_orri(instruction)
        elif name == "PRNL":
            ex_prnl()
        elif name == "PRNT":
            ex_prnt()
        elif name == "SDIV":
            ex_sdiv(instruction)
        elif name == "SMULH":
            ex_smulh(instruction)
        elif name == "STUR":
            ex_stur(instruction)
        elif name == "STURW":
            ex_sturw(instruction)
        elif name == "SUB":
            ex_sub(instruction)
        elif name == "SUBI":
            ex_subi(instruction)
        elif name == "SUBIS":
            ex_subis(instruction)
        elif name == "SUBS":
            ex_subs(instruction)
        elif name == "UDIV":
            ex_udiv(instruction)
        elif name == "UMULH":
            ex_umulh(instruction)
        else:
            print("'{}' not found".format(name))
        machine_state.PC += 4
    return machine_state
