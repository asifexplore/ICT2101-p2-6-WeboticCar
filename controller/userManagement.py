from flask import session
from flask.templating import render_template
from init import User
from passlib.hash import pbkdf2_sha256
from controller.mapControl import getMaps
from controller.challengeControl import getChallenge

    
def userLogin(username, password):
    user_found = User.query.filter_by(username=username).first()
    if user_found:
        if pbkdf2_sha256.verify(password, user_found.password):
            session['logged_in'] = True
            return True
    else:
        return False

def isTeacher():
    return session.get('logged_in')

def redirectTeacher():
    if isTeacher():
        return render_template("teacherdashboard.html")
    return render_template("teacherdashboard.html", maps = getMaps(), challenge = getChallenge())