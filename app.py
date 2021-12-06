from flask import render_template, url_for, request, redirect
from flask.helpers import send_from_directory
from init import app

from controller.userManagement import userLogin, isTeacher , redirectTeacher
from controller.challengeControl import makeChallenge, stopChallenge, getChallenge
from controller.mapControl import createMap, deleteMap, getGrid, isValidMap, makeChallenge
from controller.instructionControl import setInstruction, getInstruction
from controller.scoreControl import setHighscore, getHighscore, checkHighscore
from currentMap import getCurrentMap
from controller.apiManagement import getCarInstruction, getCarData, setCarData

import sqlite3

@app.route('/')
def index():
    return render_template("landing.html")

@app.route('/createMap', methods=['GET', 'POST'])
def createNewMap():
    
     if request.method == 'GET':
        return createMap(0)
     elif request.method == 'POST':
        form = request.form

        if(isValidMap(form)):
            return createMap(form)
        else:
            redirect(url_for('createNewMap'))
 
# Routing Background Sounds 
@app.route('/media/<path:filename>')
def download_file(filename):
    return send_from_directory("media/",filename)

@app.route('/teacher', methods=['GET', 'POST'])
def teacherdashboard():
    if isTeacher():
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("select * from map")

        maps = cur.fetchall()
        return render_template("teacherdashboard.html", maps=maps)
    else:
        return render_template("landing.html")

@app.route('/getCarInstructions', methods = ['POST', 'GET'])
def getCarNewInstructions():
    if 'map_id' in request.args:
        map_id = int(request.args['map_id'])
    else:
        return "Error: No id field provided. Please specify an id."
    return getCarInstruction(map_id)

@app.route('/getCarDatas', methods = ['POST', 'GET'])
def getCarDataRouting():
    return getCarData()

@app.route('/setCarStatus', methods = ['GET', 'POST'])
def setCarStatus():
    if 'car_id' in request.args:
        car_id = int(request.args['car_id'])
    else:
        return "Error: No id field provided. Please specify an id."
    if 'distance' in request.args:
            distance = int(request.args['distance'])
    else:
        return "Error: No id field provided. Please specify an id."
    print(type(distance))
    return setCarData(distance)

@app.route('/deleteMap/<id>')
def delMap(id):
    return deleteMap(id)

@app.route('/createChallenge', methods = ['POST', 'GET'])
def createChallenge():
    try:
        map_id = request.form['map_id']
        pin = request.form['pin']
    except:
        return redirect(url_for('teacherdashboard'))
    return makeChallenge(map_id, pin)

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'GET':
        return render_template("studentdashboard.html")
    else:
        pin = request.form['pin']
        if pin != '':
            return redirect(url_for('gameLobby'))
        return render_template("studentdashboard.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        if userLogin(request.form['username'], request.form['password']):
            return redirect(url_for('teacher'))
        return render_template("login.html")

@app.route('/game/<game_id>')
def game(game_id):
    return render_template("game_map.html", game_map=getGrid(game_id))

@app.route('/api/currentmap/<id>')
def currMap(id):
    return getCurrentMap(id)

@app.route('/createInstructions', methods = ['POST'])
def createNewInstruction():
    if request.method == 'POST':
        try:
                print('createInstructions', request.json['map_id'])
                map_id = request.json['map_id']
                executed = request.json['executed']
                command = request.json['command']
                session_id = request.json['session_id']

        except:
                return redirect(url_for('dashboard'))
        return setInstruction(map_id, executed, command, session_id)

@app.route('/getInstructions', methods = ['POST'])
def getNewInstructions():
    if request.method == 'POST':
        try:
                print('getInstructions', request.json['map_id'])
                print('getInstructions', request.json['session_id'])
                map_id = request.json['map_id']
                session_id = request.json['session_id']
                print("Type of map_id", type(map_id))
                print("Type of map_id", type(session_id))

        except:
                return redirect(url_for('dashboard'))
        return getInstruction(map_id, session_id )

@app.route('/game_start')
def gameStart():
    return render_template("game/game_start.html")

@app.route('/game_lobby')
def gameLobby():
    return render_template("game/game_lobby.html")

@app.route('/start_game_lobby')
def start_gameLobby():
    return render_template("game/start_game_lobby.html")

def currMap(id):
    return getCurrentMap(id)

@app.route('/endgame', methods = ['GET', 'POST'])
def endgame():
    if request.method == 'POST':
        score = 3000
        mapId = 4
        detailsTable = getHighscore(mapId)
        if checkHighscore(score,detailsTable):
            redirect(url_for('challengeCompleted'))
        else:
            redirect(url_for('challengeCompleted'))

@app.route('/addHighscore', methods = ['GET'])
def addHighscore():
    detailsTable = getHighscore(4)
    return render_template('addhighscore.html', detailsTable = detailsTable)

@app.route('/sethighscore', methods = ['POST'])
def sethighscore():
    mapId = 4
    score = 3000
    if request.method == 'POST':
        name = request.form['username']
        setHighscore(mapId, name, score)
        # detailsTable = getHighscore(mapId)
        return redirect(f'viewhighscore/{mapId}')

@app.route('/viewhighscore/<mapId>', methods = ['GET'])
def viewhighscore(mapId):
    mapId = 4
    detailsTable = getHighscore(mapId)
    return render_template("viewhighscore.html", detailsTable = detailsTable)

@app.route('/challengeCompleted')
def challengeCompleted():
    return render_template('challengeCompleted.html') # render_template("challengeCompleted.html")

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(ssl_context=context, debug=True)
    app.run(debug=True, host="0.0.0.0", port="5000")
