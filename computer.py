from tryte import *

class Computer:
    funclist = [self.terminate,self.read,self.write]
    
    def __init__(self):
        self.memory = [tryte(0) for i in range(19683)]

    def interpret(bytecode):
        cursor = 0
        while 

    def read(self,loc):
        assert(isinstance(loc,tryte))
        return self.memory[int(loc)%19683]

    def write(self,loc,val):
        assert(isinstance(loc,tryte))
        assert(isinstance(val,tryte))
        self.memory[int(loc)%19683] = val

c = Computer()
