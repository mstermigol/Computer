from MEMORY import ram
from MEMORY import rom
from CPU import register
from CPU import mux
from CPU import pc
from CPU import alu
from TOOLS.jumpCondition import jumpCondition

initial_values = {
    "0000000000000000": "0000000000000001",
    "0000000000000001": "0000000000000010"
}

#Initialize components
alu1 = alu.ALU()

pc1 = pc.PC(16)

ram1 = ram.RAM(16, initial_values)

rom1 = rom.ROM(16, ["0000000000000000", "1111110000010000", "0000000000000001", "1111000010010000", "0000000000010001", "1110000010010000", "0000000000000010", "1110001100001000"])

registerA = register.REGISTER(16)
registerD = register.REGISTER(16)

mux1 = mux.MUX(16)
mux2 = mux.MUX(16)

#start
i = 0
while i < 2**16:
    currentInstructionAdress = pc1.read()
    instruction = rom1.read(currentInstructionAdress)

    opCode = int(instruction[0])
    a = int(instruction[3])
    comp = instruction[4:10]
    dest1 = int(instruction[10])
    dest2 = int(instruction[11])
    dest3 = int(instruction[12])
    jump = instruction[13:]

    #Check if it is an A-instruction or a C-instruction
    if(opCode == 0):
        mux1.select(instruction, alu1.read()[0], opCode)
        registerA.load(mux1.read(), 1)
        pc1.step(False)
    else:
        mux2.select(registerA.read(), ram1.read(registerA.read()), a)
        alu1.operate(registerD.read(), mux2.read(), comp)

        registerA.load(alu1.read()[0], dest1)
        registerD.load(alu1.read()[0], dest2)
        ram1.load(registerA.read(), alu1.read()[0], dest3)

        

        jumpConditionCheck = jumpCondition(jump, alu1.read()[1], alu1.read()[2])
        pc1.step(jumpConditionCheck, registerA.read())

    
    i += 1

print("------------RAM------------")
for i in range(10):
    print(ram1.data[i])
print("------------ROM------------")
for i in range(10):
    print(rom1.memory[i])
print(f"El registro A: {registerA.read()}")
print(f"El registro D: {registerD.read()}")









