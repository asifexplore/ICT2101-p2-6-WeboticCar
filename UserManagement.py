import secrets
from flask import session
from flask.templating import render_template
from init import db, User, Cars
from passlib.hash import pbkdf2_sha256



    
def userLogin(username, password):
    user_found = User.query.filter_by(username=username).first()
    if user_found:
        if pbkdf2_sha256.verify(password, user_found.password):
            session['role'] = user_found.role
            session['logged_in'] = user_found.username
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

def carSync(car_id, car_pass, ip_addr):
    car_found = Cars.query.filter_by(car_id=car_id).first()
    if car_found:
        if pbkdf2_sha256.verify(car_pass, car_found.car_pass):
            car_found.ip_addr = ip_addr
            token = secrets.token_hex(16)
            car_found.token = token
            db.session.commit()
            return token
    return False