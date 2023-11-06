class PC:
    def __init__(self, num_bits):
        self.num_bits = num_bits
        self.max_value = int("1" * num_bits, 2)
        self.value = "0" * num_bits

    def increment(self):
        int_value = int(self.value, 2)
        int_value = (int_value + 1) % (self.max_value + 1)
        self.value = format(int_value, f'0{self.num_bits}b')

    def setValue(self, value):
        if len(value) == self.num_bits:
            self.value = value
        else:
            raise ValueError(f"Input data must be a {self.num_bits}-bit binary string.")

    def read(self):
        return self.value

    def reset(self):
        self.value = "0" * self.num_bits

    def step(self, jumpCondition, jumpTo = None,reset = 0):
        if reset == 1:
            self.reset()
        elif jumpCondition == True:
            self.setValue(jumpTo)
        else:
            self.increment()

