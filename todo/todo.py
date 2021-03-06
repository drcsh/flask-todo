import os
from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(app)
db = mongo.db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/todo')
def todo():
    _todos = db.todo.find()

    todos = []
    for todo_obj in _todos:
        item = {
            'id': str(todo_obj['_id']),
            'title': todo_obj['title'],
            'details': todo_obj['details'],
        }
        todos.append(item)

    return render_template('todos.html', todos=todos)


@app.route('/todo', methods=['POST'])
def create_todo():
    data = request.get_json(force=True)
    item = {
        'todo': data['todo']
    }
    db.todo.insert_one(item)

    return jsonify(
        status=True,
        message='To-do saved successfully!'
    ), 201


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
