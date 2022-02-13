from flask import Flask
from .config import Development
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config.from_object(Development)

bootstrap = Bootstrap(app)
db.init_app(app)


from app import views


