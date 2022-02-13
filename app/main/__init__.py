from flask import Flask
from ...config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



bootstrap = Bootstrap()

def create_app(Development):
    app = Flask(__name__)
    app.config.from_object(config_options[Development])
    db.init_app(app)
    return app

from app.main import views


