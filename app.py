from flask import render_template, url_for, request, redirect
from flask.helpers import send_from_directory
from init import app
from controller.userManagement import isTeacher
from controller.mapControl import createMap, isValidMap, makeChallenge


@app.route('/')
def index():
    return render_template("landing.html") 

@app.route('/createMap', methods = ['GET', 'POST'])
def createNewMap():
    #comment out this line if testing without teacher account
    if not isTeacher(): return render_template('login.html')

@app.route('/game_start')
def gameStart():
    return render_template("testing/game_start.html")
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

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(ssl_context = context, debug = True)