import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '3622cda657037e0dcc040b1918d21b84'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.sqlite3'
# app.config['SQLALCHEMY_DATABASE_URI'] = create_engine("sqlite3:///salaries.db")
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
#  send reset password mail
# app.config['MAIL_SERVER'] ='smtp.googlemail.com'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
# app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = 'xxx@gmail.com'
app.config['MAIL_PASSWORD'] = 'xxxxx'
mail = Mail(app)
#setting if you set username & password in environment variable
# app.config['MAIL_USERNAME'] = os.environ.get('Email_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

from app import routes
