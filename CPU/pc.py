class PC:
    def __init__(self, numBits):
        self.numBits = numBits
        self.max_value = int("1" * numBits, 2)
        self.value = "0" * numBits

    def increment(self):
        int_value = int(self.value, 2)
        int_value = (int_value + 1) % (self.max_value + 1)
        self.value = format(int_value, f'0{self.numBits}b')

    def setValue(self, value):
        if len(value) == self.numBits:
            self.value = value
        else:
            raise ValueError(f"Input data must be a {self.numBits}-bit binary string.")

    def read(self):
        return self.value

    def reset(self):
        self.value = "0" * self.numBits

    def step(self, jumpCondition, jumpTo = None,reset = 0):
        if reset == 1:
            self.reset()
        elif jumpCondition == True:
            self.setValue(jumpTo)
        else:
            self.increment()

