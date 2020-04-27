from formatting import FormatType


"""
key = instruction name
value: 
    opcode = unique instruction code
    format_type = determine how to read in bits
    operation = list of format values to fill
    assembly = <instruction> assembly (ie. how the actual assembly looks like)
"""
instruct_dir = {
    "ADD":
    {
        "opcode": b'10001011000',  # ADD
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn + Rm
        "assembly": "Rd, Rn, Rm",
    },
    "ADDI": {
        "opcode": b'1001000100',  # ADD Immediate
        "format_type": FormatType.I,
        "operation": ["Rd", "Rn", "aluimm"],  # Rd = Rn + ALUImm
        "assembly": "Rd, Rn, aluimm",
    },
    "AND": {
        "opcode": b'10001010000',  # AND
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn & Rm
        "assembly": "Rd, Rn, Rm",
    },
    "ANDI": {
        "opcode": b'1001001000',  # AND Immediate
        "format_type": FormatType.I,
        "operation": ["Rd", "Rn", "aluimm"],  # Rd = Rn & ALUImm
        "assembly": "Rd, Rn, aluimm",
    },
    "B": {
        "opcode": b'000101',  # Branch
        "format_type": FormatType.B,
        "operation": ["braddr"],  # PC = PC + BranchAddr
        "assembly": "braddr",
    },
    "B.cond": {
        "opcode": b'01010100',  # Branch Conditionally
        "format_type": FormatType.CB,
        "operation": ["condaddr", "Rt"],  # if (FLAGS == cond) -> PC = PC + CondBranchAddr
        "assembly": "condaddr",
    },
    "BL": {
        "opcode": b'100101',  # Branch with Link
        "format_type": FormatType.B,
        "operation": ["braddr"],  # R[30] = PC + 4; PC = PC + BranchAddr
        "assembly": "braddr",
    },
    "BR": {
        "opcode": b'11010110000',  # Branch to Register
        "format_type": FormatType.R,
        "operation": ["Rn"],  # PC = Rn
        "assembly": "Rn",
    },
    "CBNZ": {
        "opcode": b'10110101',  # Compare & Branch if Not Zero
        "format_type": FormatType.CB,
        "operation": ["Rt", "condaddr"],  # if(Rt != 0) -> PC = PC + CondBranchAddr + 4
        "assembly": "Rt, condaddr"
    },
    "CBZ": {
        "opcode": b'10110100',  # Compare & Branch if Zero
        "format_type": FormatType.CB,
        "operation": ["Rt", "condaddr"],  # if (Rt == 0) -> PC = PC + CondBranchAddr + 4
        "assembly": "Rt, condaddr",
    },
    "DUMP": {
        "opcode": b'11111111110',  # print all regs, mem, stack, program
        "format_type": FormatType.R,
        "operation": [],
        "assembly": "",
    },
    "EOR": {
        "opcode": b'11001010000',  # Exclusive OR
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn ^ Rm
        "assembly": "Rd, Rn, Rm",
    },
    "EORI": {
        "opcode": b'1101001000',  # Exclusive OR Immediate
        "format_type": FormatType.I,
        "operation": ["Rd", "Rn", "aluimm"],  # Rd = Rn ^ ALUImm
        "assembly": "Rd, Rn, aluimm",
    },
    "HALT": {
        "opcode": b'11111111111',  # Trigger DUMP & Terminate
        "format_type": FormatType.R,
        "operation": [],
        "assembly": "",
    },
    "LDUR": {
        "opcode": b'11111000010',  # Load Register Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rt", "Rn", "dtaddr"],  # Rt = [Rn + DTAddr]
        "assembly": "Rt, [Rn, dtaddr]",
    },
    "LDURB": {
        "opcode": b'00111000010',  # Load Byte Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rt", "Rn", "dtaddr"],  # Rt = [Rn + DTAddr]
        "assembly": "Rt, [Rn, dtaddr]",
        "required": False,
    },
    "LDURH": {
        "opcode": b'01111000010',  # Load Half Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rt", "Rn", "dtaddr"],  # Rt = [Rn + DTAddr]
        "assembly": "Rt, [Rn, dtaddr]",
        "required": False,
    },
    "LDURSW": {
        "opcode": b'10111000100',  # Load Signed Word Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rt", "Rn", "dtaddr"], # Rt = [Rn + DTAddr]
        "assembly": "Rt, [Rn, dtaddr]",
        "required": False,
    },
    "LSL": {
        "opcode": b"11010011011",  # Logical Shift Left
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "shamt"],  # Rd = Rn << shamt
        "assembly": "Rd, Rn, shamt",
    },
    "LSR": {
        "opcode": b"11010011010",  # Logical Shift Right
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "shamt"],  # Rd = Rn >>> shamt
        "assembly": "Rd, Rn, shamt",
    },
    "MUL": {
        "opcode": b"10011011000",  # Multiply
        "format_type": FormatType.R,
        "shamt": b"011111",
        "operation": ["Rd", "Rn", "Rm"],  # Rd = (Rn * Rm)
        "assembly": "Rd, Rn, Rm",
    },
    "ORR": {
        "opcode": b"10101010000",  # Inclusive OR
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn | Rm
        "assembly": "Rd, Rn, Rm",
    },
    "ORRI": {
        "opcode": b"1011001000",  # Inclusive OR Immediate
        "format_type": FormatType.I,
        "operation": ["Rd", "Rn", "aluimm"],  # Rd = Rn | ALUImm
        "assembly": "Rd, Rn, aluimm",
    },
    "PRNL": {
        "opcode": b"11111111100",  # Prints a blank line
        "format_type": FormatType.R,
        "operation": [],
        "assembly": "",
    },
    "PRNT": {
        "opcode": b"11111111101",  # Prints Register Name & Contents in Hex & Decimal
        "format_type": FormatType.R,
        "operation": ["Rd"],
        "assembly": "Rd",
    },
    "SDIV": {
        "opcode": b"10011010110",  # Signed Divide
        "format_type": FormatType.R,
        "shamt": b"000010",
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn / Rm
        "assembly": "Rd, Rn, Rm",
        "required": False,
    },
    "SMULH": {
        "opcode": b"10011011010",  # Signed Multiply High
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = (Rn * Rm)
        "assembly": "Rd, Rn, Rm",
        "required": False,
    },
    "STUR": {
        "opcode": b"11111000000",  # Store Register Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rn", "dtaddr", "Rt"],  # [Rn + DTAddr] = Rt
        "assembly": "Rt, [Rn, dtaddr]",
    },
    "STURB": {
        "opcode": b'00111000000',  # Store Byte Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rn", "dtaddr", "Rt"],  # [Rn + DTAddr] = Rt
        "assembly": "Rt, [Rn, dtaddr]",
        "required": False,
    },
    "STURH": {
        "opcode": b'01111000000',  # Store Half Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rt", "dtaddr", "Rn"],  # [Rn + DTAddr] = Rt
        "assembly": "Rt, [Rn, dtaddr]",
        "required": False,
    },
    "STURW": {
        "opcode": b"10111000000",  # Store Word Unscaled Offset
        "format_type": FormatType.D,
        "operation": ["Rn", "dtaddr", "Rt"],  # [Rn + DTAddr] = Rt
        "assembly": "Rt, [Rn, dtaddr]",
        "required": False,

    },
    "SUB": {
        "opcode": b"11001011000",  # Subtract
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn - Rm
        "assembly": "Rd, Rn, Rm",
    },
    "SUBI": {
        "opcode": b"1101000100",  # Subtract Immediate
        "format_type": FormatType.I,
        "operation": ["Rd", "Rn", "aluimm"],  # Rd = Rn - ALUImm
        "assembly": "Rd, Rn, aluimm",
    },
    "SUBIS": {
        "opcode": b"1111000100",  # Subtract Immediate & Set Flags
        "format_type": FormatType.I,
        "operation": ["Rd", "Rn", "aluimm"],  # Rd, FLAGS = Rn - ALUImm
        "assembly": "Rd, Rn, aluimm",
    },
    "SUBS": {
        "opcode": b"11101011000",  # Subtract & Set Flags
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd, FLAGS = Rn - Rm
        "assembly": "Rd, Rn, Rm",
    },
    "UDIV": {
        "opcode": b"10011010110",  # Unsigned Divide
        "format_type": FormatType.R,
        "shamt": b"000011",
        "operation": ["Rd", "Rn", "Rm"],  # Rd = Rn / Rm
        "assembly": "Rd, Rn, Rm",
        "required": False,
    },
    "UMULH": {
        "opcode": b"10011011110",  # Unsigned Multiply High
        "format_type": FormatType.R,
        "operation": ["Rd", "Rn", "Rm"],  # Rd = (Rn * Rm)
        "assembly": "Rd, Rn, Rm",
        "required": False,
    },
}