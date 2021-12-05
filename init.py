from enum import unique
from secrets import token_bytes
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sslify import SSLify
import sqlalchemy
from sqlalchemy.sql.elements import Null
<<<<<<< HEAD
from sqlalchemy.sql.operators import nullsfirst_op
=======
from random import randint
>>>>>>> Development-Integration-(Marven-and-Kok-Hwee)

app = Flask(__name__)
app.secret_key = "wow_so_secret!"

context = ('cert.pem', 'key.pem')
sslify = SSLify(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
db.app = app

def commit():
    db.session.commit()
    return

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    role = db.Column(db.Integer)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.id

<<<<<<< HEAD
class Cars(db.Model):
    car_id = db.Column(db.Integer, primary_key=True)
    car_pass = db.Column(db.String(80))
    ip_addr = db.Column(db.String(15), nullable = True)
    token = db.Column(db.String(32), nullable = True)

    def __init__(self, car_id, car_pass):
        self.car_id = car_id
        self.car_pass = car_pass
        self.ip_addr = Null
        self.token = Null

class Highscore(db.Model):
    score_id = db.column(db.Integer, primary_key=True, unique=True)
    map_id = db.column(db.Integer)
    name = db.column(db.String(10))
    score = db.Column(db.Integer)
=======
class carData(db.Model):
    car_id = db.Column(db.Integer, primary_key=True)
    distance = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    
    def __init__(self, distance, speed):
        self.distance = distance
        self.speed = speed
    
    def getDistance(self):
        return self.distance

    def getSpeed(self):
        return self.speed
    
    def setDistance(self, distance:int):
        self.distance = distance
        return True

    def setSpeed(self, speed:int):
        self.speed = speed
        return True

class Instruction(db.Model):
    instruction_id = db.Column(db.Integer, primary_key=True)
    executed = db.Column(db.Boolean)
    command = db.Column(db.Integer)
    map_id = db.Column(db.Integer)
    session_id = db.Column(db.String)

    def __init__(self, executed, command, map_id, session_id):
        self.executed = executed
        self.command = command
        self.map_id = map_id
        self.session_id = session_id
        db.session.add(self)
        db.session.commit()
        
    def getSesson_id(self):
        return self.session_id
    
    def getCommand(self):
        return self.command

    def setCommand(self, commands:int) -> bool:
        self.command = commands 
        return True 

    def getMap_id(self):
        return self.map_id

    def getExecued(self):
        return self.executed
    
    def setExecuted(self, executed:bool) -> bool:
        self.executed = executed 
        return True 
    
    def getInstructionID(self):
            return self.instruction_id
>>>>>>> Development-Integration-(Marven-and-Kok-Hwee)

class Map(db.Model):
    map_id = db.Column(db.Integer, primary_key=True)
    grid=db.Column(db.String(100))
    name = db.Column(db.String(20))
    pin = db.Column(db.Integer, nullable=True)

    def __init__(self, grid, name):
        self.grid=grid
        self.name = name
        self.pin = None
        db.session.add(self)
        db.session.commit()
s
    def __repr__(self):
        return '<Map %r>' % self.map_id

    def setPIN(self) -> bool:
        self.pin = randint(1000,9999)        
        db.session.commit()
        return True
<<<<<<< HEAD
    def clearPIN(self):
        self.pin = Null

    def clearChallenge(self) -> bool:
        self.pin = Null
        return Trues
=======

    def clearPIN(self) -> bool:
        self.pin = sqlalchemy.null()
        db.session.commit()
        return True
>>>>>>> Development-Integration-(Marven-and-Kok-Hwee)

db.create_all()