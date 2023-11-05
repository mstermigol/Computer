class PC:
    def __init__(self, max_value):
        self.max_value = max_value  
        self.value = 0  

    def increment(self):
        self.value = (self.value + 1) % (self.max_value + 1)

    def set_value(self, address):
        if 0 <= address <= self.max_value:
            self.value = address
        else:
            raise ValueError("Invalid address value")

    def get_value(self):
        return self.value

    def reset(self):
        self.value = 0

    def step(self, jumpCondition, reset):
        if reset == 1:
            self.reset()
        elif jumpCondition == 1:
            self.set_value(self.max_value) 
        else:
            self.increment()