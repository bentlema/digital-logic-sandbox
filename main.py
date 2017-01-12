#!/usr/bin/env python3

from gate import logicGate, andGate, orGate, xorGate, notGate, bufferGate, wire

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

# later on we will create the circuit class, but for now let's just do this...
circuit1 = (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12)

# Since we dont have switches or lamps yet, I'm using a buffer gate
# which will allow me to set a state manually and test
#switchA = circuitInput('IN_A', 'toggle') # input A
switchA = bufferGate()
#switchB = circuitInput('IN_B', 'toggle') # input B
switchB = bufferGate()
#switchC = circuitInput('IN_C', 'toggle') # input Carry
switchC = bufferGate()

#lampS = circuitOutput('OUT_S') # shown in GUI as a lamp/LED
lampS = bufferGate()
#lampC = circuitOutput('OUT_C') # shown in GUI as a lamp/LED
lampC = bufferGate()

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
switchA.toggleInputStateByName('IN_0')
switchB.toggleInputStateByName('IN_0')
switchC.toggleInputStateByName('IN_0')

print()
print("switchA")
switchA.printState()

print()
print("switchB")
switchB.printState()

print()
print("switchC")
switchC.printState()

for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
for obj in (and1, and2, xor1, xor2, or1, wire1, wire2, wire3, wire4, wire5, wire6, wire7, wire8, wire9, wire10, wire11, wire12):
    obj.updateState()
    
print()
print("lampS")
lampS.printState()

print()
print("lampC")
lampC.printState()




