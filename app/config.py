import logging.config
from flask import Flask

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
