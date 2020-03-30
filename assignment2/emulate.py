import sys

from helpers import hexdump, how_to_read_mem_stack_table


NOT_REQUIRED = [
    "STURB", "STURW", "STURH",
    "LDURB", "LDURW", "LDURH",
    "SMULH", "UMULH",
    "UDIV", "SDIV"
]


def ex_add(instruction, machine_state):
    print("ADD")

    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data
    new_value = rn_data + rm_data
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_addi(instruction, machine_state):
    print("ADDI")  # Rd = Rn + ALUImm

    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data + instruction.aluimm
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_and(instruction, machine_state):
    print("AND")
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data
    new_value = rn_data & rm_data
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_andi(instruction, machine_state):
    print("ANDI")

    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data & instruction.aluimm
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_b(instruction, machine_state):
    print("B")
    machine_state.PC += instruction.braddr
    return True


def ex_b_cond(instruction, machine_state):
    print("B.cond")
    result = machine_state.conditional_registers[instruction.Rt].data

    if result:
        machine_state.PC += instruction.condaddr
        return True


def ex_bl(instruction, machine_state):
    print("BL")
    machine_state.registers[30] = machine_state.PC + instruction.braddr
    ex_b(instruction, machine_state)
    return True


def ex_br(instruction, machine_state):
    print("BR")
    rn_data = machine_state.registers[instruction.Rn].data
    machine_state.PC = rn_data
    return True


def ex_cbnz(instruction, machine_state):
    print("CBNZ")
    rt_data = machine_state.registers[instruction.Rt].data
    if rt_data != 0:
        machine_state.PC += instruction.condaddr + 1
        return True


def ex_cbz(instruction, machine_state):
    print("CBZ")
    rt_data = machine_state.registers[instruction.Rt].data
    if rt_data == 0:
        machine_state.PC += instruction.condaddr + 1
        return True


def ex_dump(machine_state, start=0):
    machine_state.print_all_registers(include_conditional=True)
    how_to_read_mem_stack_table()
    print("Memory:\n")
    # hexdump(sys.stdout, start, machine_state.memory_size)

    print("Stack:\n")
    # hexdump(sys.stdout, start, machine_state.stack_size)

    machine_state.print_program()
    machine_state.print_stats()
    exit(1)


def ex_eor(instruction, machine_state):
    print("EOR")
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data
    new_value = rn_data ^ rm_data
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_eori(instruction, machine_state):
    print("EORI")

    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data ^ instruction.aluimm
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_halt(machine_state):
    print("HALT")
    ex_dump(machine_state)
    exit()


def ex_ldur(instruction, machine_state):
    print("LDUR")
    machine_state.loads_issued += 1
    rn_data = machine_state.registers[instruction.Rn].data
    address = rn_data + instruction.dtaddr
    new_value = machine_state.get_value_at_address(address)
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
    print("LSL")

    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data << instruction.shamt
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_lsr(instruction, machine_state):
    print("LSR")

    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data >> instruction.shamt
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_mul(instruction, machine_state):
    print("MUL")

    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data
    new_value = rn_data * rm_data
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_orr(instruction, machine_state):
    print("ORR")
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data
    new_value = rn_data | rm_data
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_orri(instruction, machine_state):
    print("ORRI")
    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data | instruction.aluimm
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_prnl():
    print("PRNL")
    print("\n")


def ex_prnt(machine_state):
    print("PRNT")
    machine_state.print_all_registers(include_conditional=True)


def ex_sdiv(instruction, machine_state):
    print("SDIV NOT REQUIRED")
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data

    # TODO - need to convert rn_data & rm_data to binary, take two's compliment and then divide

    new_value = rn_data / rm_data
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_smulh(instruction, machine_state):
    print("SMULH NOT IMPLEMENTED")


def ex_stur(instruction, machine_state):
    print("STUR")
    machine_state.stores_issued += 1
    rt_data = machine_state.registers[instruction.Rt].data
    rn_data = machine_state.registers[instruction.Rn].data
    address = instruction.dtaddr + rn_data

    machine_state.set_value_at_address(address, rt_data)


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
    print("SUB")

    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data
    new_value = rn_data - rm_data
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)
    return new_value


def ex_subi(instruction, machine_state):
    print("SUBI")

    rn_data = machine_state.registers[instruction.Rn].data
    new_value = rn_data - instruction.aluimm
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)
    return new_value


def ex_subis(instruction, machine_state):
    print("SUBIS")
    new_value = ex_subi(instruction, machine_state)
    machine_state.set_conditional_flags(new_value)


def ex_subs(instruction, machine_state):
    print("SUBS")
    new_value = ex_sub(instruction, machine_state)
    machine_state.set_conditional_flags(new_value)


def ex_udiv(instruction, machine_state):
    print("UDIV NOT REQUIRED")
    rn_data = machine_state.registers[instruction.Rn].data
    rm_data = machine_state.registers[instruction.Rm].data

    new_value = rn_data / rm_data
    machine_state.registers[instruction.Rd].data = new_value

    machine_state.shift_memory(new_value)


def ex_umulh(instruction, machine_state):
    print("UMULH NOT IMPLEMENTED")


def execute_assembly(binary_instructions, filename, machine_state):
    pseudo_instructions = ["PRNL", "PRNT", "HALT", "DUMP"]

    machine_state.filename = filename
    machine_state.binary_instructions = binary_instructions

    start_index = machine_state.PC
    prev_instruction = None

    while True:
        # [start index (inclusive) : end index (not inclusive)
        for instruction in binary_instructions[start_index:]:
            machine_state.check_out_of_bounds()
            name = instruction.name
            prev_instruction = instruction

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
            set_new_index = func(instruction, machine_state) or False
            machine_state.instructions_executed += 1

            if set_new_index:
                start_index = machine_state.PC
                break

            machine_state.PC += 1

        if prev_instruction == binary_instructions[-1]:
            break

    return machine_state
