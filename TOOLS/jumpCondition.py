def jumpCondition(jump_bits, zr, ng):
    jump_conditions = {
        "000": "null",
        "001": "JGT",
        "010": "JEQ",
        "011": "JGE",
        "100": "JLT",
        "101": "JNE",
        "110": "JLE",
        "111": "JMP"
    }
    
    if jump_bits in jump_conditions:
        code = jump_conditions[jump_bits]
        if (
            (code == "JGT" and ng == 0 and zr == 0) or
            (code == "JEQ" and zr == 1) or
            (code == "JGE" and (zr == 1 or ng == 0)) or
            (code == "JLT" and ng == 1 and zr == 0) or
            (code == "JNE" and zr == 0) or
            (code == "JLE" and (zr == 1 or ng == 1)) or
            code == "JMP"):
            return True
    
    return False