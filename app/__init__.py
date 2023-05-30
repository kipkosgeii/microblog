from flask import Flask
from config import Config

# initializing flask
from flask_login import LoginManager

# flask-SQLAlchemy 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__,template_folder='../templates')
app.config.from_object(Config)

# flask_login
login = LoginManager(app)
login.login_view= 'login'

# Flask-migrate initialization objects that represent migration egine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
