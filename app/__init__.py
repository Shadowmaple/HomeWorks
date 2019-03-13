from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from .api import app as api_app
app.register_blueprint(api_app, url_prefix="/api")
