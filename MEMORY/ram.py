class RAM:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("RAM size must be greater than 0")
        self.size = size
        self.data = [0 for _ in range(size)]

    def operate(self, load, address, data = 0):
        if 0 <= address < self.size:
            if load:
                if 0 <= data < 2**16:
                    self.data[address] = data
            else:
                return self.data[address]
        else:
            raise ValueError("Invalid address")
