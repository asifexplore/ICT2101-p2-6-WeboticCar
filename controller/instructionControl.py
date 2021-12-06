from flask import jsonify
from flask.globals import session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from init import Instruction
import sqlite3


# Get Instruction
def getInstruction(map_id: int, session_id: str) -> Instruction:
    print("Instruction Obtained")
    # testing = Instruction.query.filter_by(map_id=map_id, session_id=session_id).first()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    print(map_id)
    c.execute("SELECT * FROM instruction WHERE map_id = ? ORDER BY instruction_id DESC", (map_id,) )
    testing = c.fetchone()
    print(testing[0])

    
    # return jsonify({"Result": "Success", "InstructionID":testing.getInstructionID(), "SessionID":testing.getSesson_id(), 
    #                 "mapID": testing.getMap_id(), "instruction":testing.getCommand(), "executed":testing.getExecued()})
    return jsonify({"Result":"Success", "InstructionID":testing[0], "SessionID":testing[4], 
                     "mapID": testing[3], "instruction":testing[2], "executed":testing[1]})
    

# Set Instruction
def setInstruction(map_id, executed, command, session_id):
    if map_id == None or executed == None or command == None or session_id == None:
        return render_template("dashboard.html")
    
    # Create new Instruction object, auto stores in db
    Instruction(executed,command,map_id,session_id)
    print("Instruction Created")

    #display dashboard, maybe can include argv to show banner saying map craeted
    # return render_template("dashboard.html")
    # return render_template("login.html")
    # Return Json Object Here. 
    return jsonify({"Result": "Success"})

# Get CarData
def getCarData():
    print(" Car Data Function ")
    # testing = Instruction.query.filter_by(map_id=map_id, session_id=session_id).first()
    carDataConn = sqlite3.connect('database.db')
    carDataCursor = carDataConn.cursor()
    carDataCursor.execute("SELECT * FROM car_data")
    testing = carDataCursor.fetchall()
    print(testing)
    print(testing[0])

    return jsonify({"Result":"Success", "car_id":testing[0][0], "distance":testing[0][1], "speed": testing[0][2] })
