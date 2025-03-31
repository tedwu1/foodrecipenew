from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# this is the user_loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # assuming you have a User model

from app import routes
