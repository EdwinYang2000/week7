from flask import Flask,render_template

from simpledu.config import configs
from simpledu.models import db, Course
from .handlers import front, course, admin, user


def register_blueprints(app):
    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)
    app.register_blueprint(user)

def create_app(config):
    """load different config according to imported config settings"""
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    register_blueprints(app)
    return app






