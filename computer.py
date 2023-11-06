from MEMORY import ram
from MEMORY import rom
from CPU import register
from CPU import mux
from CPU import pc
from CPU import alu
from TOOLS.jumpCondition import jumpCondition

initial_values = {
    "0000000000000000": "1111111111111111",
    "0000000000000001": "0000000000000000",
    "0000000000000010": "0101010101010101"
}

#Initialize components
alu = alu.ALU()

pc = pc.PC(16)

ram = ram.RAM(16, initial_values)

rom = rom.ROM(16, ["0000000000000101", "1110011111010111"])

registerA = register.REGISTER(16)
registerD = register.REGISTER(16)

mux1 = mux.MUX(16)
mux2 = mux.MUX(16)

#start
i = 0
while i < 2:
    currentInstructionAdress = pc.read()
    instruction = rom.read(currentInstructionAdress)

    opCode = int(instruction[0])
    a = int(instruction[3])
    comp = instruction[4:10]
    dest1 = int(instruction[10])
    dest2 = int(instruction[11])
    dest3 = int(instruction[12])
    jump = instruction[13:]

    #Check if it is an A-instruction or a C-instruction
    if(opCode == 0):
        mux1.select(instruction, alu.read()[0], opCode)
        registerA.load(mux1.read(), 1)
        pc.step(False)
    else:
        mux2.select(registerA.read(), ram.read(registerA.read()), a)
        alu.operate(registerD.read(), mux2.read(), comp)

        print(alu.read()[0])
        registerA.load(alu.read()[0], dest1)
        registerD.load(alu.read()[0], dest2)
        ram.load(registerA.read(), alu.read()[0], dest3)

        jumpCondition = jumpCondition(jump, alu.read()[1], alu.read()[2])
        pc.step(jumpCondition, registerA.read())
    
    print(ram.data[i])
    print(rom.memory[i])
    print(registerA.read())
    print(registerD.read())

    i += 1








