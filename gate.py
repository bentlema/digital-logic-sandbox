'''
Created on Dec 26, 2016

@author: bentlema
'''

class inputConnection():
    def __init__(self,label):
        self.state = bool(False)
        self.label = label

class outputConnection():
    def __init__(self,label):
        self.state = bool(False)
        self.label = label



class logicGate():

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



