'''
Created on Dec 26, 2016

@author: bentlema
'''

import math

class inputConnection():
    def __init__(self,label):
        self.state = bool(False)
        self.label = label

class outputConnection():
    def __init__(self,label):
        self.state = bool(False)
        self.label = label



class logicGate():

    def printTruthTable(self):
        numberOfInputs = len(self.inputConnection)
        # Think of number of inputs as a binary string of bits
        # 1 input requires 1 bit
        # 2 inputs requires 2 bits
        # 3 inputs requires 3 bits, etc.
        inputPermutations = int(math.pow(2, numberOfInputs))  # all possible input combinations
        formatString = "{:0" + str(numberOfInputs) + "b}"     # binary number stringified
        for i in range(inputPermutations):
            myBits = formatString.format(i)
            '''
                take a look at http://stackoverflow.com/questions/1679384/converting-python-dictionary-to-list
                we have the input values being generated now, but still need to set those input values and
                calculate the output value, and print.  Since we refer the inputConnections by name, we need
                to create a mapping of connection names to connection number or something...either that, or
                we need to reconsider storing the connection names as a dict, and maybe a list/array would
                be more convenient...not sure yet. Maybe there's a way to store it both ways?
            '''
            if (numberOfInputs == 1):
                print(myBits[0], outputValue)
            elif (numberOfInputs == 2):
                print(myBits[0], myBits[1], outputValue)
            elif (numberOfInputs == 3):
                print(myBits[0], myBits[1], myBits[2], outputValue)
            print()


    def printState(self):
        for i in self.inputConnection.keys():
            print("{} = {}".format(self.inputConnection[i].label,self.inputConnection[i].state))
        for o in self.outputConnection.keys():
            print("{} = {}".format(self.outputConnection[o].label,self.outputConnection[o].state))

    def toggleInputState(self,conn):
        self.conn.state = not self.conn.state
        self.updateState()

    def toggleInputStateByName(self,connName):
        self.inputConnection[connName].state = not self.inputConnection[connName].state
        self.updateState()

    def setInputState(self,conn,state):
        self.conn.state = state
        self.updateState()

    def setInputStateByName(self,connName,state):
        self.inputConnection[connName].state = state
        self.updateState()



class notGate(logicGate):

    def __init__(self):

        # Dictionaries to keep track of inputs and outputs
        self.inputConnection = {}
        self.outputConnection = {}

        # A NOT gate has a single input and a single output connection
        self.inputConnection['IN_0'] = inputConnection('Input')
        self.outputConnection['OUT_0'] = outputConnection('Output')

        # Ensure initial value of output is correct
        self.updateState()

    def updateState(self):
        self.outputConnection['OUT_0'].state = not self.inputConnection['IN_0'].state



class andGate(logicGate):

    def __init__(self):

        # Dictionaries to keep track of inputs and outputs
        self.inputConnection = {}
        self.outputConnection = {}

        # An AND gate has two input connections and one output connection
        self.inputConnection['IN_0'] = inputConnection('Input 0')
        self.inputConnection['IN_1'] = inputConnection('Input 1')
        self.outputConnection['OUT_0'] = outputConnection('Output')

        # Ensure initial value of output is correct
        self.updateState()

    def updateState(self):
        self.outputConnection['OUT_0'].state = self.inputConnection['IN_0'].state and self.inputConnection['IN_1'].state



class orGate(logicGate):

    def __init__(self):

        # Dictionaries to keep track of inputs and outputs
        self.inputConnection = {}
        self.outputConnection = {}

        # An OR gate has two input connections and one output connection
        self.inputConnection['IN_0'] = inputConnection('Input 0')
        self.inputConnection['IN_1'] = inputConnection('Input 1')
        self.outputConnection['OUT_0'] = outputConnection('Output')

        # Ensure initial value of output is correct
        self.updateState()

    def updateState(self):
        self.outputConnection['OUT_0'].state = self.inputConnection['IN_0'].state or self.inputConnection['IN_1'].state



class xorGate(logicGate):

    def __init__(self):

        # Dictionaries to keep track of inputs and outputs
        self.inputConnection = {}
        self.outputConnection = {}

        # An XOR gate has two input connections and one output connection
        self.inputConnection['IN_0'] = inputConnection('Input 0')
        self.inputConnection['IN_1'] = inputConnection('Input 1')
        self.outputConnection['OUT_0'] = outputConnection('Output')

        # Ensure initial value of output is correct
        self.updateState()

    def updateState(self):
        # Python does not implement a logical XOR operator, but because we are storing
        # state using the Boolean type, we can use the Bitwise XOR operator here
        self.outputConnection['OUT_0'].state = self.inputConnection['IN_0'].state ^ self.inputConnection['IN_1'].state



