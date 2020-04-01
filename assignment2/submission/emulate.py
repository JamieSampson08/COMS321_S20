import sys

from helpers import hexdump, how_to_read_mem_stack_table


NOT_REQUIRED = [
    "STURB", "STURW", "STURH",
    "LDURB", "LDURW", "LDURH",
    "SMULH", "UMULH",
    "UDIV", "SDIV"
]


def ex_add(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data
    new_value = rn_data + rm_data
    machine_state.registers[instruction.Rd].data = new_value


def ex_addi(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data + instruction.aluimm
    machine_state.registers[instruction.Rd].data = new_value


def ex_and(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data
    new_value = rn_data & rm_data
    machine_state.registers[instruction.Rd].data = new_value


def ex_andi(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data & instruction.aluimm
    machine_state.registers[instruction.Rd].data = new_value


def ex_b(instruction, machine_state):
    machine_state.PC += instruction.braddr
    machine_state.altered_pc = True
    return True


def ex_b_cond(instruction, machine_state):
    result = machine_state.get_conditional_value(instruction.Rt)

    if result:
        machine_state.PC += instruction.condaddr
        machine_state.altered_pc = True
        return True


def ex_bl(instruction, machine_state):
    machine_state.registers[30].data = machine_state.PC + 1
    ex_b(instruction, machine_state)
    return True


def ex_br(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    machine_state.PC = rn_data
    machine_state.altered_pc = True
    return True


def ex_cbnz(instruction, machine_state):
    rt_data = machine_state.registers[instruction.Rt].data
    if rt_data != 0:
        machine_state.PC += instruction.condaddr
        machine_state.altered_pc = True
        return True


def ex_cbz(instruction, machine_state):
    rt_data = machine_state.registers[instruction.Rt].data
    if rt_data == 0:
        machine_state.PC += instruction.condaddr
        machine_state.altered_pc = True
        return True


def ex_dump(machine_state):
    machine_state.print_all_registers(include_conditional=True)
    how_to_read_mem_stack_table()

    print("Stack:")
    hexdump(sys.stdout, machine_state.stack_size, machine_state)

    print("\nMain Memory:")
    hexdump(sys.stdout, machine_state.memory_size, machine_state)

    print("\n")
    machine_state.print_program()
    machine_state.print_stats()


def ex_eor(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data
    new_value = rn_data ^ rm_data
    machine_state.registers[instruction.Rd].data = new_value


def ex_eori(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data ^ instruction.aluimm
    machine_state.registers[instruction.Rd].data = new_value


def ex_halt(machine_state):
    ex_dump(machine_state)
    exit()


def ex_ldur(instruction, machine_state):
    machine_state.loads_issued += 1
    rn_data = machine_state.registers[instruction.Rn].data
    address = rn_data + instruction.dtaddr

    in_stack = False
    if instruction.Rn == 28:
        in_stack = True

    new_value = machine_state.get_value_at_address(address, in_stack)
    machine_state.registers[instruction.Rt].data = new_value


def ex_ldurb(instruction, machine_state):
    print("LDURB NOT IMPLEMENTED")
    machine_state.loads_issued += 1


def ex_ldurh(instruction, machine_state):
    print("LDURH NOT IMPLEMENTED")
    machine_state.loads_issued += 1


def ex_ldurw(instruction, machine_state):
    print("LDRSW NOT IMPLEMENTED")
    machine_state.loads_issued += 1


def ex_lsl(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data << instruction.shamt
    machine_state.registers[instruction.Rd].data = new_value


def ex_lsr(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data >> instruction.shamt
    machine_state.registers[instruction.Rd].data = new_value


def ex_mul(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data
    new_value = rn_data * rm_data
    machine_state.registers[instruction.Rd].data = new_value


def ex_orr(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data
    new_value = rn_data | rm_data
    machine_state.registers[instruction.Rd].data = new_value


def ex_orri(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data | instruction.aluimm
    machine_state.registers[instruction.Rd].data = new_value


def ex_prnl():
    print("\n")


def ex_prnt(instruction, machine_state):
    reg = machine_state.registers[instruction.Rd]
    reg.print_register()


def ex_sdiv(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data

    new_value = int(rn_data / rm_data)
    machine_state.registers[instruction.Rd].data = new_value


def ex_smulh(instruction, machine_state):
    print("SMULH NOT IMPLEMENTED")


def ex_stur(instruction, machine_state):
    machine_state.stores_issued += 1
    rt_data = machine_state.registers[instruction.Rt].data
    rn_data = machine_state.registers[instruction.Rn].data
    address = instruction.dtaddr + rn_data

    in_stack = False
    if instruction.Rn == 28:
        in_stack = True

    machine_state.set_value_at_address(address, rt_data, in_stack)


def ex_sturb(instruction, machine_state):
    print("STURB NOT IMPLEMENTED")
    machine_state.stores_issued += 1


def ex_sturh(instruction, machine_state):
    print("STURH NOT IMPLEMENTED")
    machine_state.stores_issued += 1


def ex_sturw(instruction, machine_state):
    print("STURW NOT IMPLEMENTED")
    machine_state.stores_issued += 1


def ex_sub(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data
    new_value = rn_data - rm_data
    machine_state.registers[instruction.Rd].data = new_value

    return new_value


def ex_subi(instruction, machine_state):
    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data - instruction.aluimm
    machine_state.registers[instruction.Rd].data = new_value

    return new_value


def ex_subis(instruction, machine_state):
    new_value = ex_subi(instruction, machine_state)
    machine_state.set_conditional_flags(new_value)


def ex_subs(instruction, machine_state):
    new_value = ex_sub(instruction, machine_state)
    machine_state.set_conditional_flags(new_value)


def ex_udiv(instruction, machine_state):
    sys.stderr.write("UDIV NOT TESTED")
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data

    # if negative numbers, make positive
    if rn_data < 0:
        rn_data *= -1
    if rm_data < 0:
        rm_data *= -1

    new_value = int(rn_data / rm_data)
    machine_state.registers[instruction.Rd].data = new_value


def ex_umulh(instruction, machine_state):
    print("UMULH NOT IMPLEMENTED")


def call_instructions(machine_state):
    """
    Determines what function to call based on the instruction name
    :param machine_state:
    :return:
    """
    pseudo_instructions = ["PRNL", "PRNT", "HALT", "DUMP"]

    # using the list of binary_instructions, handle branching by changing where the for loop
    # starts reading from by using the PC
    for instruction in machine_state.binary_instructions[machine_state.PC:]:
        machine_state.altered_pc = False
        machine_state.check_out_of_bounds()
        name = instruction.name

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
            func = ex_andi
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
        elif name == "LDURW":
            func = ex_ldurw
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
        elif name == "STURB":
            func = ex_sturb
        elif name == "STURH":
            func = ex_sturh
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

        # special instruction that don't require both instruction & machine state
        if name in pseudo_instructions:
            if name == "PRNL":
                ex_prnl()
            elif name == "PRNT":
                ex_prnt(instruction, machine_state)
            elif name == "HALT":
                ex_halt(machine_state)
            elif name == "DUMP":
                ex_dump(machine_state)

            if not progress_machine(machine_state):
                return
            continue

        set_new_index = False

        # return values of these two functions arn't needed
        if instruction.name in ["SUB", "SUBI"]:
            func(instruction, machine_state)
        else:
            set_new_index = func(instruction, machine_state) or False

            if set_new_index:
                break  # from for loop

        if not progress_machine(machine_state):
            return


def execute_assembly(binary_instructions, filename, machine_state):
    """
    Handles calling all lines of assembly decoded and ends program
    when appropriate
    :param binary_instructions: to execute
    :param filename: binary file name
    :param machine_state: state of machine (is more or less empty)
    :return:
    """
    machine_state.filename = filename
    machine_state.binary_instructions = binary_instructions

    while True:
        # [start index (inclusive) : end index (not inclusive)
        call_instructions(machine_state)
        if machine_state.PC >= len(machine_state.binary_instructions):
            break
    return machine_state


def progress_machine(machine_state):
    """
    Increases PC, instructions_executed, and resets XZR
    :param machine_state: current state of machine
    :return: bool, if reached end of program
    """
    if not machine_state.altered_pc:
        machine_state.PC += 1

    machine_state.instructions_executed += 1
    machine_state.registers[31].data = 0

    # when the PC exceeds the address of the last instruction, end program
    if machine_state.PC >= len(machine_state.binary_instructions):
        return False
    return True
