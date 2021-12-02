from flask import render_template, url_for, request, redirect
from init import app
from init import Highscore
import uuid
# -------JS Pop-up with highscore table [addHighscore(commands, time)]-------


def getHighscore(map_id):
    highscoreTable = Highscore.query("SELECT * FROM Highscore WHERE map_id = ?;", map_id)
    return highscoreTable

def checkHighscore(score, highscoreTable):
    scoreList = list(map(lambda x: x[3], highscoreTable))
    if (score > max(scoreList)):
        return True
    else:
        return False

def setHighscore(score, username, highscoreTable):
    lst = len(highscoreTable) 
    a = tuple([uuid.uuid4(), highscoreTable[0][1], score, username])
    lst.append(a)
    for i in range(0, lst): 
        for j in range(0, lst-i-1): 
            if (highscoreTable[j][3] > highscoreTable[j + 1][3]): 
                temp = highscoreTable[j] 
                highscoreTable[j]= highscoreTable[j + 1] 
                highscoreTable[j + 1]= temp 
    b = lst.pop
    Highscore.query("DELETE FROM Highscore WHERE score_id = ?", b[0])
    Highscore.query("INSERT INTO Highscore VALUES {?,?,?,?}", a[0], a[1], a[2], a[3])

    # score_id, map_id, name, score, 
    # insertsort and rerank

