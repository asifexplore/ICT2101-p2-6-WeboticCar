from flask import session
from flask.templating import render_template
from init import db, User
from passlib.hash import pbkdf2_sha256



    
def userLogin(username, password):
    found = User.query.filter_by(username=username).first()
    if found:
        if pbkdf2_sha256.verify(password, found.password):
            session['role'] = found.role
            session['logged_in'] = found.username
            return True
    else:
        return False

def isLoggedIn():
    return session.get('logged_in')

def redirectDashboard():
    if not isLoggedIn():
        return render_template("index.html")
    else:
        return render_template("dashboard.html")

def addStudent(username, password):
    newStudent = User(username=username, password=pbkdf2_sha256.hash(password), role=0)
    db.session.add(newStudent)
    db.session.commit()
    return True