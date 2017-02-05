#!/usr/bin/env python3

import math
from gate import logicGate, andGate, orGate, xorGate, notGate, bufferGate, wire

#
# How would we define a 2-bit full adder?  Let's cascade the 1-bit full
# adder we already built
#
# We need the following gates:
#
#     - 4 x AND Gate
#     - 4 x XOR Gate
#     - 2 x OR Gate
#
# We also need 3 toggle switches for inputs
# And two LEDs/Lamps for outputs
#
# Note:
#
#     - Inputs can only ever receive a single wire connection
#     - Outputs can have multiple wires attached to them
#     - wire can be connected to any number of things
#
# We will need 12 x 2 wires to connect the various parts
#
# For the first 1-bit full adder
#
and1a = andGate()
and2a = andGate()
xor1a = xorGate()
xor2a = xorGate()
or1a = orGate()
wire1a = wire()
wire2a = wire()
wire3a = wire()
wire4a = wire()
wire5a = wire()
wire6a = wire()
wire7a = wire()
wire8a = wire()
wire9a = wire()
wire10a = wire()
wire11a = wire()
wire12a = wire()
#
# For the second 1-bit full adder
#
and1b = andGate()
and2b = andGate()
xor1b = xorGate()
xor2b = xorGate()
or1b = orGate()
wire1b = wire()
wire2b = wire()
wire3b = wire()
wire4b = wire()
wire5b = wire()
wire6b = wire()
wire7b = wire()
wire8b = wire()
wire9b = wire()
wire10b = wire()
wire11b = wire()
wire12b = wire()

# Since we dont have switches or lamps yet, I'm using a buffer gate
# which will allow me to set a state manually and test
switchA0 = bufferGate() # input A0
switchA1 = bufferGate() # input A1
switchB0 = bufferGate() # input B0
switchB1 = bufferGate() # input B1
switchC1 = bufferGate() # input  Carry_IN on first 1-bit adder
lampC2 = bufferGate() # output Carry_OUT on second 1-bit adder
switchCC = bufferGate() # used to cascade Carry_OUT --> Carry_IN
lampS0   = bufferGate() # sum S0
lampS1   = bufferGate() # sum S1

# later on we will create the circuit class, but for now let's just do this...
circuit1 = (
	switchCC,
	and1a,   and1b,
	and2a,   and2b,
	xor1a,   xor1b,
	xor2a,   xor2b,
	or1a,    or1b,
	wire1a,  wire1b,
	wire2a,  wire2b,
	wire3a,  wire3b,
	wire4a,  wire4b,
	wire5a,  wire5b,
	wire6a,  wire6b,
	wire7a,  wire7b,
	wire8a,  wire8b,
	wire9a,  wire9b,
	wire10a, wire10b,
	wire11a, wire11b,
	wire12a, wire12b)

# first 1-bit adder - connect all the wires to the gates to make a full adder with carry
wire1a.connect(switchA0.outputConnection['OUT_0'],  xor1a.inputConnection['IN_0'])
wire2a.connect(switchB0.outputConnection['OUT_0'],  xor1a.inputConnection['IN_1'])
wire3a.connect(xor1a.outputConnection['OUT_0'],     xor2a.inputConnection['IN_0'])
wire4a.connect(switchC1.outputConnection['OUT_0'],  xor2a.inputConnection['IN_1'])
wire5a.connect(xor2a.outputConnection['OUT_0'],     lampS0.inputConnection['IN_0'])
wire6a.connect(switchA0.outputConnection['OUT_0'],  and1a.inputConnection['IN_0'])
wire7a.connect(switchB0.outputConnection['OUT_0'],  and1a.inputConnection['IN_1'])
wire8a.connect(and1a.outputConnection['OUT_0'],     or1a.inputConnection['IN_1'])
wire9a.connect(xor1a.outputConnection['OUT_0'],     and2a.inputConnection['IN_0'])
wire10a.connect(switchC1.outputConnection['OUT_0'], and2a.inputConnection['IN_1'])
wire11a.connect(and2a.outputConnection['OUT_0'],    or1a.inputConnection['IN_0'])

# cascade Carry_OUT of first adder to Carry_IN of second adder
wire12a.connect(or1a.outputConnection['OUT_0'],     switchCC.inputConnection['IN_0'])

# second 2-bit adder - connect all the wires to the gates to make a full adder with carry
wire1b.connect(switchA1.outputConnection['OUT_0'],  xor1b.inputConnection['IN_0'])
wire2b.connect(switchB1.outputConnection['OUT_0'],  xor1b.inputConnection['IN_1'])
wire3b.connect(xor1b.outputConnection['OUT_0'],     xor2b.inputConnection['IN_0'])
wire4b.connect(switchCC.outputConnection['OUT_0'],  xor2b.inputConnection['IN_1'])
wire5b.connect(xor2b.outputConnection['OUT_0'],     lampS1.inputConnection['IN_0'])
wire6b.connect(switchA1.outputConnection['OUT_0'],  and1b.inputConnection['IN_0'])
wire7b.connect(switchB1.outputConnection['OUT_0'],  and1b.inputConnection['IN_1'])
wire8b.connect(and1b.outputConnection['OUT_0'],     or1b.inputConnection['IN_1'])
wire9b.connect(xor1b.outputConnection['OUT_0'],     and2b.inputConnection['IN_0'])
wire10b.connect(switchCC.outputConnection['OUT_0'], and2b.inputConnection['IN_1'])
wire11b.connect(and2b.outputConnection['OUT_0'],    or1b.inputConnection['IN_0'])
wire12b.connect(or1b.outputConnection['OUT_0'],     lampC2.inputConnection['IN_0'])

# init all inputs
switchA0.setInputStateByName('IN_0', bool(0))
switchA1.setInputStateByName('IN_0', bool(0))
switchB0.setInputStateByName('IN_0', bool(0))
switchB1.setInputStateByName('IN_0', bool(0))
switchC1.setInputStateByName('IN_0', bool(0))
switchCC.setInputStateByName('IN_0', bool(0)) # cascaded carry

print('----------------------------------------------------------------------------------')

numberOfInputs = 5                                    # The full adder with carry has 3 inputs
inputPermutations = int(math.pow(2, numberOfInputs))  # all possible input combinations
formatString = "{:0" + str(numberOfInputs) + "b}"     # binary number stringified
print("C1 B1 B0 A1 A0 | C2 S1 S0")
print("-- -- -- -- -- | -- -- --")
for i in range(inputPermutations):
    myBits = formatString.format(i)
    c1 = bool(int(myBits[0]))
    b1 = bool(int(myBits[1])) # take single character out of string (which will be a 0 or 1
    b0 = bool(int(myBits[2])) # and convert to an int, and then convert to a boolean
    a1 = bool(int(myBits[3])) # take single character out of string (which will be a 0 or 1
    a0 = bool(int(myBits[4])) # and convert to an int, and then convert to a boolean
    print("{:<2} {:<2} {:<2} {:<2} {:<2}".format(c1, b1, b0, a1, a0), end="")
    switchC1.setInputStateByName('IN_0', c1)
    switchB1.setInputStateByName('IN_0', b1)
    switchB0.setInputStateByName('IN_0', b0)
    switchA1.setInputStateByName('IN_0', a1)
    switchA0.setInputStateByName('IN_0', a0)

    # we call updateState() enough times to propagate the signal through the entire circuit
    counter = 500
    while counter > 0:
        for obj in circuit1:
            obj.updateState()
        counter -= 1

    print(" | {:<2} {:<2} {:<2}".format(lampC2.getOutputState(),lampS1.getOutputState(),lampS0.getOutputState()))

print('----------------------------------------------------------------------------------')

