from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from init import Highscore
from flask.globals import session
from init import commit

# -------JS Pop-up with highscore table [addHighscore(commands, time)]-------


def getHighscore(mapId):
    highscoreTable = Highscore.query.filter_by(map_id=mapId).all()
    # lst = len(highscoreTable) 
    # for i in range(lst): 
    #     for j in range(lst-i-1): 
    #         if (highscoreTable[j][3] > highscoreTable[j + 1][3]): 
    #             temp = highscoreTable[j] 
    #             highscoreTable[j]= highscoreTable[j + 1] 
    #             highscoreTable[j + 1]= temp 
    # if lst > 10: 
    #     b = highscoreTable.pop
        # Highscore.query.filter_by(map_id=b[0]).delete()
        # commit()   
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
    Highscore(map_id=mapId, name = username, score = uscore)

