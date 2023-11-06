from MEMORY import ram
from MEMORY import rom
from CPU import register
from CPU import mux
from CPU import pc
from CPU import alu
from TOOLS.jumpCondition import jumpCondition

alu = alu.ALU()

alu.operate("0000000000000010", "0000000000000111", "000111")
print(alu.read())

programCounter = pc.PC(16)
programCounter.step(False)
print(f"This is the program counter: {programCounter.read()}")


print(jumpCondition("010", 1, 1))


initial_values = {
    "0000000000000000": "1111111111111111",
    "0000000000000001": "0000000000000000",
    "0000000000000010": "0101010101010101"
}

ram = ram.RAM(16, initial_values)

print(ram.read("0000000000000000"))
print(ram.read("0000000000000001")) 
print(ram.read("0000000000000010")) 

rom = rom.ROM(16, ["0000000000000010", "0000000000000010", "0000000000000011"])
registerA = register.REGISTER(16)
registerA.load("0000000000000010", 1)

ram.load("0000000010000000", "0000000000000011", 1)
data = ram.read("0000000000000000")
print(f"Data in BinaryRAM: {data}")

instruction = rom.read("0000000010000000")
print(f"This is the register: {registerA.read()}")
print(f"Instruction from BinaryROM: {instruction}")

mux1 = mux.MUX(16)
mux1.select("0000000010000000", "0000000000000011", 0)
print(f"This is what the mux chose: {mux1.data}")