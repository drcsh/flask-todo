
def get_todos(db):
    _todos = db.todo.find()

    todos = []
    for todo_obj in _todos:
        item = {
            'id': str(todo_obj['_id']),
            'title': todo_obj['title'],
            'details': todo_obj['details'],
        }
        todos.append(item)

    return todos