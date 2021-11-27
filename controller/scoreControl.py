from flask import render_template, url_for, request, redirect
from init import app
from init import Highscore
# -------JS Pop-up with highscore table [addHighscore(commands, time)]-------


def getHighscoretable(map_id):
    detailsTable = Highscore.query("SELECT * FROM Highscore WHERE map_id = ?;", map_id)
    return detailsTable

def checkHighscore(score, highscoreTable):
    commands, time = score
    mapidList, nameList, commandsList, timeList = highscoreTable
    if (time <= max(timeList) & commands < max(commandsList)):
        return True
    else:
        return False

def setHighscore(score, username, map_id):
    commands, time = score
    detailsTable = Highscore.query("SELECT * FROM Highscore WHERE map_id = ?;", map_id)
    for (tableMapid, tableName, tableCommands, tableTime, tableRank) in detailsTable:

    # insertsort and rerank

