#!/usr/bin/env python3

import math
from gate import logicGate, andGate, orGate, xorGate, notGate, bufferGate, wire

#
# How would we define a 1-bit full adder?
#
# We need the following gates:
#
#     - 2 x AND Gate
#     - 2 x XOR Gate
#     - 1 x OR Gate
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
# We will need 12 wires to connect the various parts

and1 = andGate()
and2 = andGate()
xor1 = xorGate()
xor2 = xorGate()
or1 = orGate()
wire1 = wire()
wire2 = wire()
wire3 = wire()
wire4 = wire()
wire5 = wire()
wire6 = wire()
wire7 = wire()
wire8 = wire()
wire9 = wire()
wire10 = wire()
wire11 = wire()
wire12 = wire()

# later on we will create the circuit class, but for now let's just do this...
circuit1 = (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12)

# Since we dont have switches or lamps yet, I'm using a buffer gate
# which will allow me to set a state manually and test
#switchA = circuitInput('IN_A', 'toggle') # input A
switchA = bufferGate()
#switchB = circuitInput('IN_B', 'toggle') # input B
switchB = bufferGate()
#switchC = circuitInput('IN_C', 'toggle') # input Carry IN
switchC = bufferGate()
#lampS = circuitOutput('OUT_S') # shown in GUI as a lamp/LED
lampS = bufferGate()
#lampC = circuitOutput('OUT_C') # shown in GUI as a lamp/LED
lampC = bufferGate()

# connect all the wires to the gates to make a full adder with carry
wire1.connect(switchA.outputConnection['OUT_0'],  xor1.inputConnection['IN_0'])
wire2.connect(switchB.outputConnection['OUT_0'],  xor1.inputConnection['IN_1'])
wire3.connect(xor1.outputConnection['OUT_0'],     xor2.inputConnection['IN_0'])
wire4.connect(switchC.outputConnection['OUT_0'],  xor2.inputConnection['IN_1'])
wire5.connect(xor2.outputConnection['OUT_0'],     lampS.inputConnection['IN_0'])
wire6.connect(switchA.outputConnection['OUT_0'],  and1.inputConnection['IN_0'])
wire7.connect(switchB.outputConnection['OUT_0'],  and1.inputConnection['IN_1'])
wire8.connect(and1.outputConnection['OUT_0'],     or1.inputConnection['IN_1'])
wire9.connect(xor1.outputConnection['OUT_0'],     and2.inputConnection['IN_0'])
wire10.connect(switchC.outputConnection['OUT_0'], and2.inputConnection['IN_1'])
wire11.connect(and2.outputConnection['OUT_0'],    or1.inputConnection['IN_0'])
wire12.connect(or1.outputConnection['OUT_0'],     lampC.inputConnection['IN_0'])

# Try toggling these 3 inputs, and you'll see that this full adder works
#switchA.toggleInputStateByName('IN_0')
#switchB.toggleInputStateByName('IN_0')
#switchC.toggleInputStateByName('IN_0')

switchA.setInputStateByName('IN_0', bool(0))
switchB.setInputStateByName('IN_0', bool(0))
switchC.setInputStateByName('IN_0', bool(0))

print('--------------------------------------------------------------------------------')

numberOfInputs = 3                                    # The full adder with carry has 3 inputs
inputPermutations = int(math.pow(2, numberOfInputs))  # all possible input combinations
formatString = "{:0" + str(numberOfInputs) + "b}"     # binary number stringified
for i in range(inputPermutations):
    myBits = formatString.format(i)
    a = bool(int(myBits[0])) # take single character out of string (which will be a 0 or 1
    b = bool(int(myBits[1])) # and convert to an int, and then convert to a boolean
    c = bool(int(myBits[2]))
    print("SwitchA {},  SwitchB {},  SwitchC {}".format(a, b, c))
    switchA.setInputStateByName('IN_0', a)
    switchB.setInputStateByName('IN_0', b)
    switchC.setInputStateByName('IN_0', c)

    # we call updateState() enough times to propagate the signal through the entire circuit
    counter = 100
    while counter > 0:
        for obj in circuit1:
            obj.updateState()
        counter -= 1

    print()
    print("lampS (Sum)")
    lampS.printState()

    print()
    print("lampC (Carry)")
    lampC.printState()
    print()

print('--------------------------------------------------------------------------------')


#
# Next, let's work on making the circuit() class, so that we can easily copy a circuit
# object, and then link together multiple 1-bit full adders to make an 8-bit full adder
#
