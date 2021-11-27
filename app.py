import sqlite3

import pandas as pd
from flask import render_template, url_for, request, redirect, session
from init import app
from controller.userManagement import isTeacher, userLogin
from controller.mapControl import createMap, isValidMap, makeChallenge


@app.route('/')
def index():
    return render_template("landing.html") 

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

# insert code for play challenge here
@app.route('/playChallenge')
def playChallenge():
    return render_template("playchallenge.html")

@app.route('/createMap', methods = ['GET', 'POST'])
def createNewMap():
    #comment out this line if testing without teacher account
    if not isTeacher():
        return render_template('login.html')

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