from flask import Blueprint, render_template, request, redirect, url_for
import logging

from app.extensions import db
from app.models import Todo

logger = logging.getLogger(__name__)
main = Blueprint("main", __name__)

# @main.route("/", methods=["GET", "POST"])
@main.post("/")
def create_todo():
    logger.info('create--------------------')
    db.session.add(Todo(task=request.form["task"]))
    db.session.commit()
    
    return redirect(url_for("main.get_todos"))

@main.get("/")
def get_todos():
    logger.info('get--------------------')
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)