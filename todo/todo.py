import os
from flask import Flask, request, jsonify, render_template, flash, session, redirect, url_for
from flask_pymongo import PyMongo

from todo import db_functions

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

mongo = PyMongo(app)
db = mongo.db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/todo')
def todo():
    todos = db_functions.get_todos(db)
    return render_template('todos.html', todos=todos)


@app.route('/create')
def create_todo():
    return render_template('new_todo.html')


@app.route('/create', methods=['POST'])
def create_todo_submit():
    print(request.form)

    title = request.form.get('title')
    details = request.form.get('details')
    if title:
        item = {
            'title': title,
            'details': details
        }
        db.todo.insert_one(item)
        flash("Added new ToDo!")
        return redirect(url_for('todo'))

    else:
        flash("Error: you need to add a title at least to create a ToDo!")
        return redirect(url_for('create_todo'))




if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
