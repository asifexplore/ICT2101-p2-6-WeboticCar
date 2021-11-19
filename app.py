from flask import render_template, url_for, request, redirect
from flask.helpers import send_from_directory
from init import app
from UserManagement import userLogin, addStudent, redirectDashboard



@app.route('/')
def index():
    return redirectDashboard() 

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
        return render_template("login.html")
    else:
        if userLogin(request.form['username'], request.form['password']):
            return render_template("dashboard.html")
        return render_template("login.html")

@app.route('/addStudent', methods = ['GET', 'POST'])
def register():
    addStudent(request.form['username'], request.form['password'])
    return redirectDashboard()

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(ssl_context = context, debug = True)