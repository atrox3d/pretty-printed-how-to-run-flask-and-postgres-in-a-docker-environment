from flask import Flask 
import logging.config
from app.extensions import db
from app.routes import main

def setup_logging():
    logging.config.dictConfig({
        "version": 1,
        "formatters": {
            "default": {
                # "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                "format": "%(name)s | %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            }
        },
        "root": {"level": "DEBUG", "handlers": ["console"]},
    })


def print_app_env(app:Flask):
    app.logger.info(f'FLASK_SQLALCHEMY_DATABASE_URI = {app.config.get('FLASK_SQLALCHEMY_DATABASE_URI')}')
    app.logger.info(f'SQLALCHEMY_DATABASE_URI = {app.config.get('SQLALCHEMY_DATABASE_URI')}')

    app.logger.info(f'FLASK_PYTHONUNBUFFERD = {app.config.get('FLASK_PYTHONUNBUFFERD')}')
    app.logger.info(f'PYTHONUNBUFFERD = {app.config.get('PYTHONUNBUFFERD')}')


def create_app():
    setup_logging()

    app = Flask(__name__)
    app.config.from_prefixed_env()

    app.logger.info('create_app')
    print_app_env(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(main)

    return app
