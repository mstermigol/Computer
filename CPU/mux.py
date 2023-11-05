class MUX:
    def __init__(self, num_bits):
        if num_bits <= 0:
            raise ValueError("Number of bits must be greater than 0")
        self.num_bits = num_bits
        self.data = "0" * num_bits

    def select(self, a, b, sel):
        if len(a) == self.num_bits and len(b) == self.num_bits:
            if sel == 0:
                self.data = a
            elif sel == 1:
                self.data = b
            else:
                raise ValueError("sel must be 0 or 1")
        else:
            raise ValueError(f"Input data must be a {self.num_bits}-bit binary number")

    def read(self):
        return self.data