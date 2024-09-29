from flask import Flask 
import logging

from app.extensions import db
from app.routes import main

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def print_app_env(app:Flask):
    logger.info(f'FLASK_SQLALCHEMY_DATABASE_URI = {app.config.get('FLASK_SQLALCHEMY_DATABASE_URI')}')
    logger.info(f'SQLALCHEMY_DATABASE_URI = {app.config.get('SQLALCHEMY_DATABASE_URI')}')

    logger.info(f'FLASK_PYTHONUNBUFFERD = {app.config.get('FLASK_PYTHONUNBUFFERD')}')
    logger.info(f'PYTHONUNBUFFERD = {app.config.get('PYTHONUNBUFFERD')}')


def create_app():
    logger.info('create_app')

    app = Flask(__name__)
    app.config.from_prefixed_env()
    print_app_env(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(main)

    return app
