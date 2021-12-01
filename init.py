from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sslify import SSLify
from sqlalchemy.sql.elements import Null

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



class Map(db.Model):
    map_id = db.Column(db.Integer, primary_key=True)
    grid=db.Column(db.String(100))
    name = db.Column(db.String(20))
    pin = db.Column(db.Integer, nullable=True)

    def __init__(self, grid, name):
        self.grid=grid
        self.name = name
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Map %r>' % self.map_id

    def setPIN(self, pin: int) -> bool:
        self.pin = pin
        return True
    def clearPIN(self):
        self.pin = Null

    def clearChallenge(self) -> bool:
        self.pin = Null
        return True

db.create_all()