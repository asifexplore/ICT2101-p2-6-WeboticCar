from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sslify import SSLify

app = Flask(__name__)

context = ('cert.pem', 'key.pem')
sslify = SSLify(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
db.app = app
db.create_all()