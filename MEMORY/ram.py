class RAM:
    def __init__(self, address_bits, initial_values=None):
        self.address_bits = address_bits
        self.size = 2 ** address_bits
        self.data = ["0" * 16] * self.size

        if initial_values is not None:
            for address, data in initial_values.items():
                self.load(address, data, load=True)

    def load(self, address, data, load):
        if load:
            int_address = int(address, 2)
            if 0 <= int_address < self.size:
                if len(data) == 16:
                    self.data[int_address] = data
                else:
                    raise ValueError("Invalid data value")
            else:
                raise IndexError("data address out of range")

    def read(self, address):
        int_address = int(address, 2)
        if 0 <= int_address < self.size:
            return self.data[int_address]
        else:
            raise IndexError("data address out of range")