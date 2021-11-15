from flask import session
from init import User
from passlib.hash import pbkdf2_sha256


    
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