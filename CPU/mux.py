class MUX:
    def __init__(self, numBits):
        if numBits <= 0:
            raise ValueError("Number of bits must be greater than 0")
        self.numBits = numBits
        self.data = "0" * numBits

    def select(self, a, b, sel):
        if len(a) == self.numBits and len(b) == self.numBits:
            if sel == 0:
                self.data = a
            elif sel == 1:
                self.data = b
            else:
                raise ValueError("sel must be 0 or 1")
        else:
            raise ValueError(f"Input data must be a {self.numBits}-bit binary number")

    def read(self):
        return self.data