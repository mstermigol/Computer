class ROM:
    def __init__(self, address_bits, program):
        self.address_bits = address_bits
        self.size = 2 ** address_bits
        if len(program) > self.size:
            raise ValueError("Program size exceeds ROM capacity")
        self.memory = program + [0] * (self.size - len(program))

    def read(self, address):
        if 0 <= address < self.size:
            return self.memory[address]
        else:
            raise IndexError("Memory address out of range")
