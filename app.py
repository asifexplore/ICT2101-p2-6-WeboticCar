from flask import render_template, url_for, request, redirect, jsonify
from init import app
from UserManagement import userLogin, addStudent, redirectDashboard

@app.route('/')
def index():
    return redirectDashboard() 

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

@app.route('/getCarInstruction', methods = ['GET', 'POST'])
def getCarInstruction():
    return "123"

@app.route('/setCarStatus', methods = ['GET', 'POST'])
def setCarStatus():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    return str(id)

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(debug=True, host="0.0.0.0", port="5000")
    # app.run(ssl_context = context, debug = True)