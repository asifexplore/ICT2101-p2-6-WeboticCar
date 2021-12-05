from flask import render_template, url_for, request, redirect
from init import app
from flask import session
from controller.userManagement import isTeacher
from controller.mapControl import createMap, isValidMap, makeChallenge
from controller.scoreControl import *


@app.route('/')
def index():
    return render_template("landing.html")

@app.route('/createMap', methods = ['GET', 'POST'])
def createNewMap():
    #comment out this line if testing without teacher account
    if not isTeacher(): return render_template('login.html')

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

@app.route('/playgame')
def playgame():
    session['my_var'] = 'my_value'
    return render_template('Game.html')

@app.route('/endgame', methods = ['GET', 'POST'])
def endgame():
    if request.method == 'POST':
        score = 3000
        mapId = 3
        detailsTable = getHighscore(mapId)
        if checkHighscore(score,detailsTable):
            redirect(url_for('challengeCompleted'))
        else:
            redirect(url_for('challengeCompleted'))

@app.route('/addHighscore', methods = ['GET'])
def addHighscore():
    return render_template('addhighscore.html')

@app.route('/sethighscore', methods = ['POST'])
def sethighscore():
    mapId = 3
    score = 3000
    if request.method == 'POST':
        name = request.form['username']
        setHighscore(mapId, name, score)
        # detailsTable = getHighscore(mapId)
        return redirect(f'viewhighscore/{mapId}')

@app.route('/viewhighscore/<mapId>', methods = ['GET'])
def viewhighscore(mapId):
    mapId = 1
    detailsTable = getHighscore(mapId)
    return render_template("viewhighscore.html", detailsTable = detailsTable)

@app.route('/challengeCompleted')
def challengeCompleted():
    return render_template('challengeCompleted.html') # render_template("challengeCompleted.html")

@app.route('/gameOver')
def gameOver():
    # score_id, map_id, name, score= getHighscore(1)
    return getHighscore(1)# render_template("gameOver.html")

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(ssl_context = context, debug = True)
