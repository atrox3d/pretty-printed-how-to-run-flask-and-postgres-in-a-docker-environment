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
                "format": "%(name)-10s | %(message)s"
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


def print_app_env(app:Flask, *names:str):
    for name in names:
        app.logger.info(f'{name} = {app.config.get(name)}')


def create_app():
    setup_logging()

    app = Flask(__name__)
    app.logger.info('create_app')

    app.config.from_prefixed_env()
    print_app_env(
        app,
        'FLASK_SQLALCHEMY_DATABASE_URI',
        'SQLALCHEMY_DATABASE_URI',
        'FLASK_PYTHONUNBUFFERD',
        'PYTHONUNBUFFERD',
    )

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(main)

    return app
