from flask import Blueprint, render_template, request, redirect, url_for
from flask import current_app

from app.extensions import db
from app.models import Todo

main = Blueprint("main", __name__)

# @main.route("/", methods=["GET", "POST"])
@main.post("/")
def create_todo():
    todo = Todo(task=request.form["task"])
    current_app.logger.info(f'create {todo=}')
    db.session.add(todo)
    db.session.commit()
    
    return redirect(url_for("main.get_todos"))

@main.get("/")
def get_todos():
    current_app.logger.info(f'get todos')
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)