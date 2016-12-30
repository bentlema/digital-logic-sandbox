#!/usr/bin/env python3

from gate import logicGate, andGate, orGate, xorGate, notGate

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



