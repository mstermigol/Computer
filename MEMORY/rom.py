class ROM:
    def __init__(self, address_bits, program):
        self.address_bits = address_bits
        self.size = 2 ** address_bits
        if len(program) > self.size:
            raise ValueError("Program size exceeds ROM capacity")
        self.memory = program + ["0" * 16] * (self.size - len(program))

    def read(self, address):
        if len(address) == 16:
            address_int = int(address, 2)
            if 0 <= address_int < self.size:
                return self.memory[address_int]
            else:
                raise IndexError("Memory address out of range")
        else:
            raise ValueError("Invalid address value")