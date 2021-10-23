from flask import render_template, url_for, request, redirect
from init import app
import UserManagement
from UserManagement import currentUser, userLogin, addStudent



@app.route('/')
def index():
    return UserManagement.redirectDashboard() 

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("dashboard.html")
    else:
        if userLogin(request.form['username'], request.form['password']):
            return render_template("dashboard.html")
        return render_template("login.html")

@app.route('/addStudent', methods = ['GET', 'POST'])
def addStudent():
    UserManagement.addStudent(request.form['username'], request.form['password'])
    return UserManagement.redirectDashboard()

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(ssl_context = context, debug = True)