from MEMORY import ram
from MEMORY import rom
from CPU import register

# Create BinaryRAM and BinaryROM instances with 16-bit addresses
ram = ram.RAM(16)
rom = rom.ROM(16, [0b0000000000000010, 0b0000000000000010, 0b0000000000000011])
registerA = register.REGISTER()
registerA.load(0b0000000000000010, 1)


# Read and write 16-bit binary data to BinaryRAM using 16-bit binary addresses
ram.operate(1, 0b0000000000000001, 0b0000000000000011)
data = ram.operate(0, 0b0000000000000001)
print(f"Data in BinaryRAM: {data}")

# Read 16-bit binary instructions from BinaryROM using 16-bit binary addresses
instruction = rom.read(0b0000000000000000)
print(f"This is the register: {registerA.read()}")
print(f"Instruction from BinaryROM: {instruction}")