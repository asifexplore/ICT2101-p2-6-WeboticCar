from enum import unique
from secrets import token_bytes
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sslify import SSLify
import sqlalchemy
from sqlalchemy.sql.elements import Null
from random import randint


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

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.id

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

    def __init__(self, instruction_id, executed, command, map_id, session_id):
        self.instruction_id = instruction_id
        self.executed = executed
        self.command = command
        self.map_id = map_id
        self.session_id = session_id
        db.session.add(self)
        db.session.commit()

    def getSesson_id(self):
        return self.session_id

        
    def getSesson_id(self):
        return self.session_id
    
    def getCommand(self):
        return self.command

    def setCommand(self, commands:int) -> bool:
        self.command = commands
        return True
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

    def __repr__(self):
        return '<Map %r>' % self.map_id

    def setPIN(self) -> bool:
        self.pin = randint(1000,9999)
        db.session.commit()
        return True

    def clearPIN(self) -> bool:
        self.pin = sqlalchemy.null()
        db.session.commit()
        return True


class Highscore(db.Model):
    score_id = db.Column(db.Integer, primary_key=True)
    map_id = db.Column(db.Integer)
    name = db.Column(db.String(10))
    score = db.Column(db.Integer)

    def __init__(self, map_id, name, score):
        self.map_id = map_id
        self.name = name
        self.score = score
        db.session.add(self)
        db.session.commit()

db.create_all()
