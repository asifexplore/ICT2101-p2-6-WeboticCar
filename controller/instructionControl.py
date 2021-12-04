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
    testing = Instruction.query.filter_by(map_id=map_id, session_id=session_id).first()
    print(testing)
    print(testing.getSesson_id())
    print(testing.getInstructionID())
    
    return jsonify({"Result": "Success", "InstructionID":testing.getInstructionID(), "SessionID":testing.getSesson_id(), 
                    "mapID": testing.getMap_id(), "instruction":testing.getCommand(), "executed":testing.getExecued()})

    
    

# Set Instruction
def createInstruction(map_id, executed, command, session_id):
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

# isValid()
