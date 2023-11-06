class ALU:
    def __init__(self):
        self.zero = False
        self.result = ""
        self.zr = 0
        self.ng = 0

    def operate(self, x, y, c):
        if len(c) != 6:
            raise ValueError("Control bits (c) must be a 6-bit binary string.")

        zx, nx, zy, ny, f, no = map(int, c) 

        if zx:
            x = "0" * 16
        if zy:
            y = "0" * 16

        if nx:
            x = ''.join(['1' if bit == '0' else '0' for bit in x])
        if ny:
            y = ''.join(['1' if bit == '0' else '0' for bit in y])

        if f:
            self.result = bin(int(x, 2) + int(y, 2))[2:].zfill(16)
        else:
            self.result = ''.join(['1' if (bit_x == '1' and bit_y == '0') else '0' for bit_x, bit_y in zip(x, y)])

        if no:
            self.result = ''.join(['1' if bit == '0' else '0' for bit in self.result])

        self.zero = all(bit == '0' for bit in self.result)

        self.zr = 1 if self.zero else 0
        self.ng = 1 if self.result[0] == '1' else 0
    
    def read(self):
        return [self.result, self.zr, self.ng]


    