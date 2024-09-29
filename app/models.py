from .extensions import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)

    def __str__(self) -> str:
        return self.task
    
    def __repr__(self) -> str:
        return f'Todo({self.task!r})'