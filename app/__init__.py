from flask import Flask 

from app.extensions import db
from app.routes import main
from app.config import setup_logging, print_app_env

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

    app.logger.info('init SQLAlchemy app')
    db.init_app(app)

    app.logger.info('create tables')
    with app.app_context():
        db.create_all()

    app.logger.info('register blueprint')
    app.register_blueprint(main)

    return app
