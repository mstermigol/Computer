class ALU:
    def __init__(self):
        self.zero = False
        self.result = "0" * 16
        self.zr = 0
        self.ng = 0

# Se ingresa X y Y que son numeros y C que son 6 bits que corresponde a ZX, NX, ZY, NY, F y NO respectivamente
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
            self.result = '{0:016b}'.format(int(x, 2) + int(y, 2))
        else:
            self.result = ''.join(['1' if (bit_x == '1' and bit_y == '1') else '0' for bit_x, bit_y in zip(x, y)])

        if no:
            self.result = ''.join(['1' if bit == '0' else '0' for bit in self.result])

        if len(self.result) > 16:
            self.result = self.result[-16:]

        self.result = self.result

        self.zero = all(bit == '0' for bit in self.result)

        self.zr = 1 if self.zero else 0
        self.ng = 1 if self.result[0] == '1' else 0
    
    #Se devuelve el resultado y las flags de si es ceros o negativo
    def read(self):
        return [self.result, self.zr, self.ng]