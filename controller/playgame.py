
class Instructions():
    def __init__(self, map_id, session_id):
        self.map_id = map_id
        self.session_id = session_id

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

class Student():
    def __init__(self, session_id):
        self.session_id = session_id