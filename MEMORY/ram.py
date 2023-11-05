class RAM:
    def __init__(self, address_bits):
        self.address_bits = address_bits
        self.size = 2 ** address_bits - 1
        self.memory = ["0" * 16] * self.size

    def load(self, address, memory, load):
        if load:
            int_address = int(address, 2)
            if 0 <= int_address < self.size:
                if len(memory) == 16:
                    self.memory[int_address] = memory
                else:
                    raise ValueError("Invalid memory value")
            else:
                raise IndexError("Memory address out of range")

    def read(self, address):
        int_address = int(address, 2)
        if 0 <= int_address < self.size:
            return self.memory[int_address]
        else:
            raise IndexError("Memory address out of range")