from flask import render_template, url_for, request, redirect
from flask.helpers import send_from_directory
from init import app
from controller.userManagement import isTeacher
from controller.mapControl import createMap, isValidMap, makeChallenge
from controller.instructionControl import createInstruction, getInstruction, getCarData


@app.route('/')
def index():
    return render_template("landing.html") 

@app.route('/createMap', methods = ['GET', 'POST'])
def createNewMap():
    #comment out this line if testing without teacher account
    if not isTeacher(): return render_template('login.html')

@app.route('/game_start')
def gameStart():
    return render_template("game/game_start.html")
@app.route('/game_lobby')
def gameLobby():
    return render_template("game/game_lobby.html")

@app.route('/start_game_lobby')
def start_gameLobby():
    return render_template("game/start_game_lobby.html")

# Routing Background Sounds 
@app.route('/media/<path:filename>')
def download_file(filename):
    return send_from_directory("media/",filename)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return createMap(0)
    elif request.method == 'POST':
        form = request.form
        if(isValidMap(form)):
            return createMap(form)
        else:
            redirect(url_for('createNewMap'))

@app.route('/createChallenge', methods = ['POST'])
def createNewChallenge():
    try:
        map_id = request.form['map_id']
        pin = request.form['pin']
    except:
        return redirect(url_for('teacherdashboard'))
    return makeChallenge(map_id, pin)

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
        return createInstruction(map_id, executed, command, session_id)

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

@app.route('/getCarDatas', methods = ['POST'])
def getCarDataRouting():
    return getCarData()

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(ssl_context = context, debug = True)