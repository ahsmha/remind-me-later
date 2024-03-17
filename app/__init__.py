from flask import Flask, request 
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
# def create_app():
    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app

def register_extensions(app):
    db.init_app(app)
    return

from app import models