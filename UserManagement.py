from flask import session
from flask.templating import render_template
from init import db
from passlib.hash import pbkdf2_sha256


currentUser = None

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    role = db.Column(db.Integer)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.id
    
def userLogin(username, password):
    found = User.query.filter_by(username=username)
    if found:
        if found.password is pbkdf2_sha256.verify(password):
            currentUser = found
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