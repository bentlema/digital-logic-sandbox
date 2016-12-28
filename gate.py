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


class simpleGate():

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


class andGate(simpleGate):

    def __init__(self):

        # Dictionaries to keep track of inputs and outputs
        self.inputConnection = {}
        self.outputConnection = {}

        # An AND gate has two input connections and one output connection
        self.inputConnection['IN_0'] = inputConnection('Input 0')
        self.inputConnection['IN_1'] = inputConnection('Input 1')
        self.outputConnection['OUT_0'] = outputConnection('Output')

    def updateState(self):
        self.outputConnection['OUT_0'].state = self.inputConnection['IN_0'].state and self.inputConnection['IN_1'].state

    #
    # Need to re-write this in a general/generic way, without any knowledge of the input/output names
    # so that we can "promote" this method up to to the simpleGate class
    #
    def printState(self):
        print()
        print("IN_0      IN_1    OUT_0")
        print("-----     -----   -----")
        print("{!r:<5} AND {!r:<5} = {!r:<5}".format(self.inputConnection['IN_0'].state,self.inputConnection['IN_1'].state,self.outputConnection['OUT_0'].state))
        print()


class orGate(simpleGate):

    def __init__(self):

        # Dictionaries to keep track of inputs and outputs
        self.inputConnection = {}
        self.outputConnection = {}

        # An OR gate has two input connections and one output connection
        self.inputConnection['IN_0'] = inputConnection('Input 0')
        self.inputConnection['IN_1'] = inputConnection('Input 1')
        self.outputConnection['OUT_0'] = outputConnection('Output')

    def updateState(self):
        self.outputConnection['OUT_0'].state = self.inputConnection['IN_0'].state or self.inputConnection['IN_1'].state

    #
    # Need to re-write this in a general/generic way, without any knowledge of the input/output names
    # so that we can "promote" this method up to to the simpleGate class
    #
    def printState(self):
        print()
        print("IN_0      IN_1    OUT_0")
        print("-----     -----   -----")
        print("{!r:<5} OR {!r:<5} = {!r:<5}".format(self.inputConnection['IN_0'].state,self.inputConnection['IN_1'].state,self.outputConnection['OUT_0'].state))
        print()

