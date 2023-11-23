class PC:
    def __init__(self, numBits):
        self.numBits = numBits
        self.max_value = int("1" * numBits, 2)
        self.value = "0" * numBits

#Metodo para incrementar en 1 el program counter
    def increment(self):
        int_value = int(self.value, 2)
        int_value = (int_value + 1) % (self.max_value + 1)
        self.value = format(int_value, f'0{self.numBits}b')

#Metodo para saltar
    def setValue(self, value):
        if len(value) == self.numBits:
            self.value = value
        else:
            raise ValueError(f"Input data must be a {self.numBits}-bit binary string.")

    def read(self):
        return self.value

#Metodo para resetear el program counter poniendolo en ceros
    def reset(self):
        self.value = "0" * self.numBits

#Metodo que engloba los anteriores. La jumpCondition es un bool. En caso de ser verdadero se salta a la posicion que se especifique
    def step(self, jumpCondition, jumpTo = None,reset = 0):
        if reset == 1:
            self.reset()
        elif jumpCondition == True:
            self.setValue(jumpTo)
        else:
            self.increment()

