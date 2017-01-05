#!/usr/bin/env python3

from gate import logicGate, andGate, orGate, xorGate, notGate, bufferGate, wire

foo = andGate()
bar = orGate()
lah = xorGate()
dee = notGate()

print()
print("AND Gate")
foo.printState()
print()
foo.toggleInputStateByName('IN_0')
foo.printState()
print()
foo.toggleInputStateByName('IN_1')
foo.printState()
print()
foo.toggleInputStateByName('IN_0')
foo.printState()
print()
foo.toggleInputStateByName('IN_1')
foo.printState()
print()
print("OR Gate")
bar.printState()
print()
bar.toggleInputStateByName('IN_0')
bar.printState()
print()
bar.toggleInputStateByName('IN_1')
bar.printState()
print()
bar.toggleInputStateByName('IN_0')
bar.printState()
print()
bar.toggleInputStateByName('IN_1')
bar.printState()
print()
print("XOR Gate")
lah.printState()
print()
lah.toggleInputStateByName('IN_0')
lah.printState()
print()
lah.toggleInputStateByName('IN_1')
lah.printState()
print()
lah.toggleInputStateByName('IN_0')
lah.printState()
print()
lah.toggleInputStateByName('IN_1')
lah.printState()
print()
print("NOT Gate")
dee.printState()
print()
dee.toggleInputStateByName('IN_0')
dee.printState()
print()
dee.toggleInputStateByName('IN_0')
dee.printState()
print()

'''
Wouldn't it be cool to write a method that would print out the truth table for the gate?
Let's do that next...
'''

print('AND Gate Truth Table')
foo.printTruthTable()

print('OR Gate Truth Table')
bar.printTruthTable()

print('XOR Gate Truth Table')
lah.printTruthTable()

print('NOT Gate Truth Table')
dee.printTruthTable()

print()


#
# How would we define a full adder?
#
# We need the following gates:
#
#     - 3 x AND Gate
#     - 2 x XOR Gate
#     - 2 x OR Gate (or a single 3-input OR Gate)
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

#switchA = circuitInput('IN_A', 'toggle') # input A
#switchB = circuitInput('IN_B', 'toggle') # input B
#switchC = circuitInput('IN_C', 'toggle') # input Carry

#lampS = circuitOutput('OUT_S') # shown in GUI as a lamp/LED
#lampC = circuitOutput('OUT_C') # shown in GUI as a lamp/LED

xor1.connectByName('IN_0', wire1.outputConnection['OUT_0']) # Connect xor1 IN_0 to wire1 output
xor1.connectByName('IN_1', wire2.outputConnection['OUT_0']) # Connect xor1 IN_1 to wire2 output

wire3.connectByName('IN_0', xor1) # connecte wire3 IN_0 to xor1 output

xor2.connectByName('IN_0', wire3) # Connect xor2 IN_0 to wire3
xor2.connectByName('IN_1', wire4) # Connect xor2 IN_1 to wire4

wire5.connectByName('IN_0', xor2) # connecte wire3 IN_0 to xor1 output


print()
print("xor1")
xor1.printState()

print()
print("wire1")
wire1.printState()

print()
print("wire2")
wire2.printState()

print()
print("toggle wire1")
wire1.toggleInputStateByName('IN_0')
wire1.printState()

print()
print("xor1")
xor1.printState()

print()
print("toggle wire2")
wire2.toggleInputStateByName('IN_0')
wire2.printState()

print()
print("xor1")
xor1.printState()

print()
print("toggle wire1")
wire1.toggleInputStateByName('IN_0')
wire1.printState()

print()
print("xor1")
xor1.printState()

