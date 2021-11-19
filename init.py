from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sslify import SSLify

app = Flask(__name__)
app.secret_key = "wow_so_secret!"

context = ('cert.pem', 'key.pem')
sslify = SSLify(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
db.app = app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    role = db.Column(db.Integer)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.id

class Instruction(db.Model):
    instruction_id = db.Column(db.Integer, primary_key=True)
    executed = db.Column(db.Boolean)
    command = db.Column(db.Integer(10))
    map_id = db.Column(db.Integer(10))
    session_id = db.Column(db.String(10))

    def __init__(self, instruction_id, executed, command, map_id, session_id):
        self.instruction_id = instruction_id
        self.executed = executed
        self.command = command
        self.map_id = map_id
        self.session_id = session_id
        
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
    


    
    
db.create_all()