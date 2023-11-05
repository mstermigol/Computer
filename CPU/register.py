class REGISTER:
    def __init__(self, num_bits):
        if num_bits <= 0:
            raise ValueError("Number of bits must be greater than 0")
        self.num_bits = num_bits
        self.data = "0" * num_bits

    def load(self, new_data, c):
        if c:
            if len(new_data) == self.num_bits:
                self.data = new_data
            else:
                raise ValueError(f"Input data must be a {self.num_bits}-bit binary number")
        else:
            return self.data

    def read(self):
        return self.data
