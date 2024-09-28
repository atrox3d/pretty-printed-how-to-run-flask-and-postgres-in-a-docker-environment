from flask import Blueprint, render_template, request, redirect, url_for

from app.extensions import db
from app.models import Todo

main = Blueprint("main", __name__)

# @main.route("/", methods=["GET", "POST"])
@main.post("/")
def create_todo():
    db.session.add(Todo(task=request.form["task"]))
    db.session.commit()
    
    return redirect(url_for("main.get_todos"))

@main.get("/")
def get_todos():
        todos = Todo.query.all()
        return render_template("index.html", todos=todos)