from secrets import token_bytes
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sslify import SSLify
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.operators import nullsfirst_op

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
    map_id = db.column(db.Integer, primary_key=True)
    rank = db.column(db.Integer)
    name = db.column(db.String(10))
    commands = db.Column(db.Integer)
    time = db.Column(db.Numeric)

db.create_all()