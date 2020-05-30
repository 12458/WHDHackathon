import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from myproject.eldery.views import elderly_blueprints
from myproject.helpers.views import helpers_blueprint

app.register_blueprint(elderly_blueprints,url_prefix='/elderly')
app.register_blueprint(helpers_blueprint,url_prefix='/helpers')
