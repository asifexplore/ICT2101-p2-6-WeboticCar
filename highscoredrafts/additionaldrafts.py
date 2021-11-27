  
# -------JS Pop-up with highscore table [addHighscore(commands, time)]-------


from operator import itemgetter
import json

try:
    with open('highscore.txt', 'r') as f:
        highscores = json.load(f)
except FileNotFoundError:
    # If the file doesn't exist, use your default values
    highscores = [
        ('Luke', 0),
        ('Dalip', 0),
        ('Andrew', 0),
        ]

playerName = input("what is your name? ")
playerScore = int(input('Give me a score? '))

highscores.append((playerName, playerScore))
highscores = sorted(highscores, key = itemgetter(1), reverse = True)[:10]

with open('highscore.txt', 'w') as f:
    json.dump(highscores, f)

    

# # @app.route('/setHighscore', methods = ['GET', 'POST'])
# def setHighscore(score, highscoreTable):
#         #sort highscore table
#     username = request.username
#     commands, time = score
#     Highscore # "INSERT INTO Highscore'map_id' WHERE map_id = ? VALUES (?,?,?)"

# class Score():
#     def __init__(self, map_id, commands, time):
#         self.map_id = map_id
#         self.commands = commands
#         self.time = time

#     def setUsername(self, name):
#         self.name = name
    
#     def getUsername(self):
#         return self.name

#     def checkHighscore(self,score):
#         commands, time = score
#         if (time <= self.highscoreTime & commands < self.highscoreCommands):
#             return True
#         else:
#             return False

# class HighscoreTable():
#     def __init__(self):
#     # store highscore in file json
#         detailsTable =  (["andrew","james","adam"], [9,10,11], [33,45,52])#   SELECT * FROM HighscoreTable ---- db
#         self.nameList, self.commandsList, self.timeList = detailsTable

#     def getHighscoreTable(self):
#         return self.nameList, self.commandsList, self.timeList

#     def setHighscore(self, name, score):
#         self.commands, self.time = score
#         self.name = name
    

#     def displayHighscore(self,HSTable,UHS):
#         return

#     def setminHighscore(self):
#         self.minHighscore = min(self.nameList)# mintime(details)

