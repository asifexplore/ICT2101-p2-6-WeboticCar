# -------------End Game:------------- 

def getminHighscore():
    minHighscore = SELECT highscoreCommands, highscoreTime FROM HighscoreTable WHERE highscoreTime = MIN from db
    highscoreCommands, highscoreTime = minHighscore
    return highscoreCommands, highscoreTime

def addHighscore(commands, time):
#    @app.route('/addHighscore' (self.commands, self.time)

def backtoDashboard():
#    route to challengecompleted.html

def checkHighscore(commands, time, getminHighscore()):
    highscoreCommands, highscoreTime = getminHighscore()
    if (time <= highscoreTime & commands < highscoreCommands):
        return addHighscore(commands, time)
    else:
        return backtoDashboard()


if __name__ == "__main__":
   checkHighscore(commands, time, getminHighscore())