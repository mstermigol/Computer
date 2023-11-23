class REGISTER:
    def __init__(self, numBits):
        if numBits <= 0:
            raise ValueError("Number of bits must be greater than 0")
        self.numBits = numBits
        self.data = "0" * numBits

#Metodo para cargar un dato. Donde le ingresamos el valor y si lo guardamos o no
    def load(self, new_data, c):
        if c == 1:
            if len(new_data) == self.numBits:
                self.data = new_data
            else:
                raise ValueError(f"Input data must be a {self.numBits}-bit binary number")

    def read(self):
        return self.data
