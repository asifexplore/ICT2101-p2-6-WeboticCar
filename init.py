from enum import unique
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

class Map(db.Model):
    map_id = db.Column(db.Integer, primary_key=True)
    one = db.Column(db.String(10))
    two = db.Column(db.String(10))
    three = db.Column(db.String(10))
    four = db.Column(db.String(10))
    five = db.Column(db.String(10))
    six = db.Column(db.String(10))
    seven = db.Column(db.String(10))
    eight = db.Column(db.String(10))
    nine = db.Column(db.String(10))
    ten = db.Column(db.String(10))
    name = db.Column(db.String(20))
    pin = db.Column(db.Integer, nullable=True)

    def __init__(self, one, two, three, four, five, six, seven, eight, nine, ten, name):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six
        self.seven = seven
        self.eight = eight
        self.nine = nine
        self.ten = ten
        self.name = name
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Map %r>' % self.map_id

    def setPIN(self, pin: int) -> bool:
        self.pin = pin
        return True

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
    score_id = db.Column(db.Integer, primary_key=True, unique=True)
    map_id = db.Column(db.Integer)
    name = db.Column(db.String(10))
    score = db.Column(db.Integer)

db.create_all()
