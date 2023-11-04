class REGISTER:
    def __init__(self):
        self.data = 0b0000000000000000

    def load(self, new_data, c):
        if c:
            if 0 <= new_data < 2**16:
                self.data = new_data
            else:
                raise ValueError("Input data must be a 16-bit binary number")

    def read(self):
        return self.data
