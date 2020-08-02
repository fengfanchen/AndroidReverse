from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
manager = Manager( app )
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:xxxx@xxxx.xxxx.xxxx.xxxx/xxxx"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
