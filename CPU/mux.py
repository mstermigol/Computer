class MUX16:
    def __init__(self):
        self.data = 0b0000000000000000 

    def select(self, a, b, sel):
        if 0 <= a < 2**16 and 0 <= b < 2**16:
            if(sel == 0):
                self.data = a
            else:
                self.data = b
        else:
            raise ValueError("Input data must be a 16-bit binary number")

    def read(self):
        return self.data
