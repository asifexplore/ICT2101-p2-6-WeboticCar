from flask import jsonify
from flask.globals import session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from init import Instruction
import sqlite3

# API point for car to get instructions to execute 
def getCarInstruction(map_id: int) -> Instruction:
    print("Instruction Obtained")
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM instruction WHERE map_id = ? ORDER BY instruction_id DESC", (map_id,) )
    data = c.fetchone()
    return str(data[2])

# API point to retrieve information sent by the car. 
def getCarData():
    carDataConn = sqlite3.connect('database.db')
    carDataCursor = carDataConn.cursor()
    carDataCursor.execute("SELECT * FROM car_data")
    testing = carDataCursor.fetchall()
    return jsonify({"Result":"Success", "car_id":testing[0][0], "distance":testing[0][1], "speed": testing[0][2] })

# API point for car to send data to 
def setCarData(distance:int):
    carDataConn = sqlite3.connect('database.db')
    carDataCursor = carDataConn.cursor()
    print(type(distance))
    print(distance)
    if (carDataCursor.execute("UPDATE car_data SET distance = ? WHERE car_id = 1", (distance,)) ):
        return "True"
    else:
        return "False"