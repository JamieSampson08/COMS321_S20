import sys

from helpers import hexdump, how_to_read_mem_stack_table


def check_out_of_bounds(machine_state):
    if machine_state.registers[28].data < 8 or machine_state.PC > 4088:
        print("Error: Attempting to access out of bounds address")
        ex_dump(machine_state)


def ex_add(instruction, machine_state):
    print("ADD")


def ex_addi(instruction, machine_state):
    print("ADDI")
    current_value = machine_state.registers[instruction.Rn].data
    new_value = current_value + instruction.aluimm
    binary_rep = "{:08b}".format(new_value)
    address = machine_state.memory_location
    machine_state.registers[instruction.Rd].data = address


def ex_and(instruction, machine_state):
    print("AND")


def ex_andi(instruction, machine_state):
    print("ANDI")


def ex_b(instruction, machine_state):
    print("B")


def ex_b_cond(instruction, machine_state):
    print("B.cond")


def ex_bl(instruction, machine_state):
    print("BL")


def ex_br(instruction, machine_state):
    print("BR")


def ex_cbnz(instruction, machine_state):
    print("CBNZ")


def ex_cbz(instruction, machine_state):
    print("CBZ")


def ex_dump(machine_state, start=0):
    machine_state.print_all_registers(include_conditional=True)
    how_to_read_mem_stack_table()
    print("Memory:\n")
    # hexdump(sys.stdout, start, machine_state.memory_size)

    print("Stack:\n")
    # hexdump(sys.stdout, start, machine_state.stack_size)

    machine_state.print_program()
    exit(1)


def ex_eor(instruction, machine_state):
    print("EOR")


def ex_eori(instruction, machine_state):
    print("EORI")


def ex_halt(machine_state):
    print("HALT")
    ex_dump(machine_state)
    exit()


def ex_ldur(instruction, machine_state):
    print("LDUR")
    machine_state.loads_issued += 1


def ex_ldurb(instruction, machine_state):
    print("LDURB NOT IMPLEMENTED")
    machine_state.loads_issued += 1


def ex_ldurh(instruction, machine_state):
    print("LDURH NOT IMPLEMENTED")
    machine_state.loads_issued += 1


def ex_ldursw(instruction, machine_state):
    print("LDRSW NOT IMPLEMENTED")
    machine_state.loads_issued += 1


def ex_lsl(instruction, machine_state):
    print("LSL")


def ex_lsr(instruction, machine_state):
    print("LSR")


def ex_mul(instruction, machine_state):
    print("MUL")


def ex_orr(instruction, machine_state):
    print("ORR")


def ex_orri(instruction, machine_state):
    print("ORRI")


def ex_prnl():
    print("PRNL")
    print("\n")


def ex_prnt(machine_state):
    print("PRNT")
    machine_state.print_all_registers(include_conditional=True)


def ex_sdiv(instruction, machine_state):
    print("SDIV NOT IMPLEMENTED")


def ex_smulh(instruction, machine_state):
    print("SMULH NOT IMPLEMENTED")


def ex_stur(instruction, machine_state):
    print("STUR")
    machine_state.stores_issued += 1


def ex_sturh(instruction, machine_state):
    print("STURH NOT IMPLEMENTED")
    machine_state.stores_issued += 1


def ex_sturw(instruction, machine_state):
    print("STURW NOT IMPLEMENTED")
    machine_state.stores_issued += 1


def ex_sturw(instruction, machine_state):
    print("STURW NOT IMPLEMENTED")
    machine_state.stores_issued += 1


def ex_sub(instruction, machine_state):
    print("SUB")


def ex_subi(instruction, machine_state):
    print("SUBI")


def ex_subis(instruction, machine_state):
    print("SUBIS")


def ex_subs(instruction, machine_state):
    print("SUBS")


def ex_udiv(instruction, machine_state):
    print("UDIV NOT IMPLEMENTED")


def ex_umulh(instruction, machine_state):
    print("UMULH NOT IMPLEMENTED")


def execute_assembly(binary_instructions, filename, machine_state):
    pseudo_instructions = ["PRNL", "PRNT", "HALT", "DUMP"]

    machine_state.filename = filename
    machine_state.binary_instructions = binary_instructions

    # machine_state.print_program()
    # exit(1)

    for instruction in binary_instructions:
        check_out_of_bounds(machine_state)
        name = instruction.name

        # special instruction that don't require both instruction & machine state
        if name in pseudo_instructions:
            if name == "PRNL":
                ex_prnl()
            elif name == "PRNT":
                ex_prnt(machine_state)
            elif name == "HALT":
                ex_halt(machine_state)
            elif name == "DUMP":
                ex_dump(machine_state)
            continue

        # since all the functions require the instruction & machine state
        # create a variable to hold what function to call and then make
        # one call with necessary parameters
        func = None

        if name == "ADD":
            func = ex_add
        elif name == "ADDI":
            func = ex_addi
        elif name == "AND":
            func = ex_and
        elif name == "ANDI":
            func = ex_addi
        elif name == "B":
            func = ex_b
        elif name == "B.cond":
            func = ex_b_cond
        elif name == "BL":
            func = ex_bl
        elif name == "BR":
            func = ex_br
        elif name == "CBNZ":
            func = ex_cbnz
        elif name == "CBZ":
            func = ex_cbz
        elif name == "EOR":
            func = ex_eor
        elif name == "EORI":
            func = ex_eori
        elif name == "LDUR":
            func = ex_ldur
        elif name == "LDURB":
            func = ex_ldurb
        elif name == "LDURH":
            func = ex_ldurh
        elif name == "LDURSW":
            func = ex_ldursw
        elif name == "LSL":
            func = ex_lsl
        elif name == "LSR":
            func = ex_lsr
        elif name == "MUL":
            func = ex_mul
        elif name == "ORR":
            func = ex_orr
        elif name == "ORRI":
            func = ex_orri
        elif name == "SDIV":
            func = ex_sdiv
        elif name == "SMULH":
            func = ex_smulh
        elif name == "STUR":
            func = ex_stur
        elif name == "STURW":
            func = ex_sturw
        elif name == "SUB":
            func = ex_sub
        elif name == "SUBI":
            func = ex_subi
        elif name == "SUBIS":
            func = ex_subis
        elif name == "SUBS":
            func = ex_subs
        elif name == "UDIV":
            func = ex_udiv
        elif name == "UMULH":
            func = ex_umulh
        else:
            print("Error: '{}' not found".format(name))
            exit(1)
        func(instruction, machine_state)
        machine_state.instructions_executed += 1
        machine_state.PC += 1
    return machine_state
