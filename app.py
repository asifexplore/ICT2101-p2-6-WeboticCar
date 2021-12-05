from flask import render_template, url_for, request, redirect, jsonify
from init import app
from controller.UserManagement import userLogin, addStudent, redirectDashboard
from controller.instructionControl import createInstruction
from controller.apiManagement import getCarInstruction, getCarData, setCarData

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

@app.route('/getCarInstructions', methods = ['POST', 'GET'])
def getNewInstructions():
    if 'map_id' in request.args:
        map_id = int(request.args['map_id'])
    else:
        return "Error: No id field provided. Please specify an id."
    return getCarInstruction(map_id)

@app.route('/getCarDatas', methods = ['POST', 'GET'])
def getCarDataRouting():
    return getCarData()

@app.route('/setCarStatus', methods = ['GET', 'POST'])
def setCarStatus():
    if 'car_id' in request.args:
        car_id = int(request.args['car_id'])
    else:
        return "Error: No id field provided. Please specify an id."
    if 'distance' in request.args:
            distance = int(request.args['distance'])
    else:
        return "Error: No id field provided. Please specify an id."
    print(type(distance))
    return setCarData(distance)

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(debug=True, host="0.0.0.0", port="5000")
    # app.run(ssl_context = context, debug = True)