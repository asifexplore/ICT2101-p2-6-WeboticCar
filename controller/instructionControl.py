# Command and executed should be stack/queue
def setExecuted(self, executed):
    self.executed += executed

def getExecuted(self):
        return self.executed
    
def setCommand(self):
    self

def getCommand(self):
    return self.commands, self.time

def setScore(self, commands, time):
    self.commands = commands
    self.time = time
    # self.score = calculate score with commands and time
        
def getScore(self):
    return self.commands, self.time