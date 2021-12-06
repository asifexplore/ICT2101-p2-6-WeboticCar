from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from init import Highscore
# -------JS Pop-up with highscore table [addHighscore(commands, time)]-------


def getHighscore(mapId):
    # try:
    highscoreTable = Highscore.query.filter_by(map_id=mapId).all()
    #     lst = len(highscoreTable) 
    #     for i in range(0, lst): 
    #         for j in range(0, lst-i-1): 
    #             if (highscoreTable[j][3] > highscoreTable[j + 1][3]): 
    #                 temp = highscoreTable[j] 
    #                 highscoreTable[j]= highscoreTable[j + 1] 
    #                 highscoreTable[j + 1]= temp 
    # except:
    #     return "empty table"
    return highscoreTable

def checkHighscore(score, highscoreTable):
    try:
        scoreList = list(map(lambda x: x[3], highscoreTable))
    except:
        return True
    if (score > max(scoreList)):
        return True
    else:
        return False

def setHighscore(mapId, username, uscore):
    # try:
    #     b = highscoreTable.pop
    #     highscoreTable.append(a)
    #     Highscore.query.filter_by(map_id=b[0]).delete()
    # except:
    #     highscoreTable = []
    Highscore(map_id=mapId, name = username, score = uscore)
    # detailsTable = getHighscore(mapId)
    # return detailsTable
    # return render_template("addhighscore.html", detailsTable = detailsTable)

