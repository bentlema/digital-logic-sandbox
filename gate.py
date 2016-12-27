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
    
class andGate():
    def __init__(self):
        
        # An AND gate has two input connections
        self.inputConnection = {}
        self.inputConnection['IN_0'] = inputConnection('Input 0')
        self.inputConnection['IN_1'] = inputConnection('Input 1')

        # An AND gate has one output connection
        self.outputConnection = {}
        self.outputConnection['OUT_0'] = outputConnection('Output')
        
    def updateState(self):
        self.outputConnection['OUT_0'].state = self.inputConnection['IN_0'].state and self.inputConnection['IN_1'].state
        
    def toggleInputState(self,conn):
        self.conn.state = not self.conn.state

    def toggleInputStateByName(self,connName):
        self.inputConnection[connName].state = not self.inputConnection[connName].state

    def setInputState(self,conn,state):
        self.conn.state = state

    def setInputStateByName(self,connName,state):
        self.inputConnection[connName].state = state
        
    # Need to re-write this in a general/generic way, without any knowledge of the input/output names
    def printState(self):
        print("IN_0 = {} AND IN_1 = {}, OUT_0 = {}".format(self.inputConnection['IN_0'].state, self.inputConnection['IN_1'].state, self.outputConnection['OUT_0'].state))
