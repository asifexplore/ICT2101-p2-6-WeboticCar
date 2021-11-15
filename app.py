from flask import render_template, url_for, request, redirect
from init import app
from controller.userManagement import isTeacher
from controller.mapControl import createMap, isValidMap, makeChallenge

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


db.create_all()


@app.route('/')
def index():
    return render_template("landing.html")


@app.route('/createMap', methods=['GET', 'POST'])
def createNewMap():
    # comment out this line if testing without teacher account
    if not isTeacher():
        return render_template('login.html')

    if request.method == 'GET':
        return createMap(0)
    elif request.method == 'POST':
        form = request.form
        if(isValidMap(form)):
            return createMap(form)
        else:
            redirect(url_for('createNewMap'))


@app.route('/createChallenge', methods=['POST'])
def createNewChallenge():
    try:
        map_id = request.form['map_id']
        pin = request.form['pin']
    except:
        return redirect(url_for('teacherdashboard'))
    return makeChallenge(map_id, pin)


@app.route('/game')
def game():
    return render_template("game.html")


if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(ssl_context=context, debug=True)
