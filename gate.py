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

    # Class variable: truthTable (shared by all instances)
    # Key will be type of gate (such as 'AND', 'OR', 'NOT', etc.)
    # Value will be a 2-dimensional list of lists
    # We index into the list of lists with 2 indecies corresponding to the binary input values
    # The output is stored as the actual value within the matrix
    # We initialize the dictionary here, but the more specific gate objects will
    # define the actual truth table
    truthTable = {}

    def printTruthTable(self, gateName):
        numberOfInputs = len(self.inputConnection)
        # Think of number of inputs as a binary string of bits
        # 1 input requires 1 bit
        # 2 inputs requires 2 bits
        # 3 inputs requires 3 bits, etc.
        inputPermutations = int(math.pow(2, numberOfInputs))  # number of possible input combinations
        formatString = "{:0" + str(numberOfInputs) + "b}"     # format to convert decimal to binary
        for i in range(inputPermutations):
            myBits = formatString.format(i)
            if (numberOfInputs == 1):
                print(myBits[0], self.truthTable[gateName][int(myBits[0])])
            elif (numberOfInputs == 2):
                print(myBits[0], myBits[1], self.truthTable[gateName][int(myBits[0])][int(myBits[1])] )


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
        # List to store truth table inputs and outputs
        # The NOT gate only has 1 input, so it's just a list, but for
        # gates with 2 inputs, we'd have a list of lists
        # Rather than dynamically generating the truth table, let's just
        # define it statically for now.  We can get fancy later on.
        self.myTruth = [0 for x in range(2)]
        self.myTruth[0] = 1
        self.myTruth[1] = 0
        logicGate.truthTable['NOT'] = self.myTruth

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

    def printTruthTable(self):
        logicGate.printTruthTable(self, 'NOT')



class andGate(logicGate):

    def __init__(self):
        # List of Lists to store truth table inputs and outputs
        # Rather than dynamically generating the truth table, let's just
        # define it statically for now.  We can get fancy later on.
        self.myTruth = [[0 for x in range(2)] for y in range(2)]
        self.myTruth[0][0] = 0
        self.myTruth[0][1] = 0
        self.myTruth[1][0] = 0
        self.myTruth[1][1] = 1
        logicGate.truthTable['AND'] = self.myTruth

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

    def printTruthTable(self):
        logicGate.printTruthTable(self, 'AND')



class orGate(logicGate):

    def __init__(self):
        # List of Lists to store truth table inputs and outputs
        # Rather than dynamically generating the truth table, let's just
        # define it statically for now.  We can get fancy later on.
        self.myTruth = [[0 for x in range(2)] for y in range(2)]
        self.myTruth[0][0] = 0
        self.myTruth[0][1] = 1
        self.myTruth[1][0] = 1
        self.myTruth[1][1] = 1
        logicGate.truthTable['OR'] = self.myTruth

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

    def printTruthTable(self):
        logicGate.printTruthTable(self, 'OR')



class xorGate(logicGate):

    def __init__(self):
        # List of Lists to store truth table inputs and outputs
        # Rather than dynamically generating the truth table, let's just
        # define it statically for now.  We can get fancy later on.
        self.myTruth = [[0 for x in range(2)] for y in range(2)]
        self.myTruth[0][0] = 0
        self.myTruth[0][1] = 1
        self.myTruth[1][0] = 1
        self.myTruth[1][1] = 0
        logicGate.truthTable['XOR'] = self.myTruth

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

    def printTruthTable(self):
        logicGate.printTruthTable(self, 'XOR')


