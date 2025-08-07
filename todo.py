from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Todo {self.id}: {self.task} - {self.done}>"
        

@app.route('/')
def index():
    return 'OM NAMO MOOKAMBIKE'

@app.route('/todos')
def get_todo():
    todos = Todo.query.all()
    output = []
    for todo in todos:
        todo_data = {"id": todo.id, "task": todo.task, "done": todo.done}
        output.append(todo_data)
    return {'todo': output}

@app.route('/todos/<id>')
def get_todos(id):
    todo = Todo.query.get_or_404(id)
    return {"id": todo.id, "task": todo.task, "done": todo.done}


@app.route('/todos', methods=['POST'])
def add_todo():
    todo = Todo(task=request.json['task'],done=request.json['done'])
    db.session.add(todo)
    db.session.commit()
    return {'id':todo.id}


@app.route('/todos/<id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get(id)
    if todo is None:
        return {"error": "not found"}
    db.session.delete(todo)
    db.session.commit()
    return {"message": "yeet!@"}

@app.route('/todos/<id>',methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get(id)
    if todo is None:
        return {"error":"Not found!"}
    todo.task=request.json['task']
    todo.done=request.json['done']
    db.session.commit()
    return{"message":"updated!"}

@app.route('/todos/<id>',methods=['PATCH'])
def patch_todos(id):
    todo = Todo.query.get(id)
    if todo is None:
        return{"error":"Not found!"}
    if "task" in request.json:
        todo.task = request.json['task']
    if "done" is request.json:
        todo.done = request.json['done']
    db.session.commit()
    return{"message":"patched!"}




