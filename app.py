from flask import render_template, url_for, request, redirect
from init import app
from controller.userManagement import redirectTeacher
from controller.challengeControl import makeChallenge, stopChallenge
from controller.mapControl import createMap, isValidMap, deleteMap, getGrid
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

@app.route('/deleteMap/<id>')
def delMap(id):
    return deleteMap(id)

@app.route('/createChallenge/<id>')
def createChallenge(id):
    return makeChallenge(id)

@app.route('/stopChallenge/<id>')
def delChallenge(id):
    return stopChallenge(id)

@app.route('/game/<game_id>')
def game(game_id):
    return render_template("game_map.html", game_map=getGrid(game_id))
    
@app.route('/api/currentmap/<id>')
def currMap(id):
    return getCurrentMap(id)

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(ssl_context=context, debug=True)
