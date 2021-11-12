  
# -------JS Pop-up with highscore table [addHighscore(commands, time)]-------


class UserHighscore:
    def __init__(self)

    def setScore(self, commands, time):
        self.commands = commands
        self.time = time

    def setUsername(self, name):
        self.name = name

    def getScore(self):
        return self.commands, self.time

    def getUsername(self):
        return self.name

class HighscoreTable:
    def __init__(self)
    def getHighscoreTable(db):
    #    return SELECT * FROM HighscoreTable from db
    def setHighscore(name, score):
        commands, time = score
    #    UPDATE {name, commands, time} to db
    def displayHighscore(HSTable, UHS):
    #    return JS popup window with setHighscore


if __name__ == "__main__":
    # Fields: setUsername() = name, setScore() = [getCommands(), getTime()]
    user = UserHighscore()
    user.setUsername(name)
    user.getCommands(commands)
    user.getTime(time)
    getHighscoreTable()
    # Display Highscore Table: Sort by Time Ranking {name,commands,time} with new Highscore
    displayHighscore(getHighscoreTable(), getScore())
    # Submit button
    setHighscore(getUsername(), getScore())
