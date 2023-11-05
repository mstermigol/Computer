from MEMORY import ram
from MEMORY import rom
from CPU import register
from CPU import mux
from CPU import pc
from TOOLS.jumpCondition import jumpCondition


print(jumpCondition("010", 1, 1))

ram = ram.RAM(16)
rom = rom.ROM(16, ["0000000000000010", "0000000000000010", "0000000000000011"])
registerA = register.REGISTER(16)
registerA.load("0000000000000010", 1)


ram.load("000000000000000", "0000000000000011", 1)
data = ram.read("0000000000000000")
print(f"Data in BinaryRAM: {data}")

instruction = rom.read("0000000000000010")
print(f"This is the register: {registerA.read()}")
print(f"Instruction from BinaryROM: {instruction}")

mux1 = mux.MUX(16)
mux1.select("0000000010000000", "0000000000000011", 0)
print(f"This is what the mux chose: {mux1.data}")