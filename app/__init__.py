from flask import Flask
from config import Config

# initializing flask
from flask_login import LoginManager

# flask-SQLAlchemy 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import logging
from logging.handlers import SMTPHandler 

from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__,template_folder='../templates')
app.config.from_object(Config)

# flask_login
login = LoginManager(app)
login.login_view= 'login'

# Flask-migrate initialization objects that represent migration egine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models, errors

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None

        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth =(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        
        secure = None

        if app.config['MAIL_USE_TLS']:
            secure = ()

        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr= 'no-reply@' + app.config['MAIL_SERVER'],
            toaddrs= app.config["ADMINS"], subject= 'Microblog Failer',
            credentials= auth, secure=secure)
        
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

        if not os.path.exits('logs'):
            os.mkdir('logs')

        file_handler = RotatingFileHandler('log/microblog.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Microblog startup')
