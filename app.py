import pandas as pd
import sqlite3
from flask import render_template, url_for, request, redirect
from flask.helpers import send_from_directory
from init import app
from controller.userManagement import userLogin, isTeacher , redirectTeacher
from controller.challengeControl import makeChallenge, stopChallenge
from controller.mapControl import createMap, deleteMap, getGrid, isValidMap, makeChallenge
from controller.instructionControl import createInstruction, getInstruction
from api.currentMap import getCurrentMap

@app.route('/')
def index():
    return render_template("landing.html")

@app.route('/teacherdashboard')
def teacherdashboard():
    return redirectTeacher()

@app.route('/createMap', methods=['GET', 'POST'])
def createNewMap():
    # comment out this line if testing without teacher account
    # if not isTeacher():
    #     return render_template('login.html')

     if request.method == 'GET':
        return createMap(0)
     elif request.method == 'POST':
        form = request.form

        if(isValidMap(form)):
            return createMap(form)
        else:
            redirect(url_for('createNewMap'))

@app.route('/teacher', methods=['GET', 'POST'])
def teacher():
    if isTeacher():
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute("select * from map")

        maps = cur.fetchall()
        return render_template("teacherdashboard.html", maps=maps)
    else:
        return render_template("landing.html")

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

# insert code for play challenge here
@app.route('/playChallenge')
def playChallenge():
    return render_template("playchallenge.html")

     
@app.route('/student')
def student():
    # con = sqlite3.connect("database.db")
    # con.row_factory = sqlite3.Row
    #
    # cur = con.cursor()
    # cur.execute("SELECT * FROM challenges WHERE pin IS NOT NULL")
    #
    # rows = cur.fetchall();
    # return render_template("studentdashboard.html", rows=rows)
    return render_template("studentdashboard.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        if userLogin(request.form['username'], request.form['password']):
            return redirect(url_for('teacher'))
        return render_template("login.html")

@app.route('/game_start')
def gameStart():
    return render_template("testing/game_start.html")
@app.route('/game_lobby')
def gameLobby():
    return render_template("testing/game_lobby.html")
    
# Routing Background Sounds 
@app.route('/media/<path:filename>')
def download_file(filename):
    return send_from_directory("media/",filename)
    if request.method == 'GET':
        return createMap(0)
    elif request.method == 'POST':
        form = request.form
        if(isValidMap(form)):
            return createMap(form)
        else:
            redirect(url_for('createNewMap'))


@app.route('/game/<game_id>')
def game(game_id):
    return render_template("game_map.html", game_map=getGrid(game_id))
 
@app.route('/api/currentmap/<id>')
def currMap(id):
    return getCurrentMap(id)
    
@app.route('/createInstructions', methods = ['POST', 'GET'])
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

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(ssl_context=context, debug=True)
