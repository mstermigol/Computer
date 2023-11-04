def checkBit(binary_number, bit_position):
    bit_mask = 1 << bit_position
    
    bit_value = (binary_number & bit_mask) >> bit_position
    
    return bit_value
