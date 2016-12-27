#!/usr/bin/python
from flask import Flask, jsonify, request, abort, make_response

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
PATCH = 'PATCH'
DELETE = 'DELETE'

API = '/todo/api/v1.0'

tasks = {} #current active tasks
last_task_id = -1;

app = Flask(__name__)

def start_server():
    app.run(debug=True)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error':'Bad Request'}), 400)

@app.route(API + '/tasks', methods=[GET])
def get_tasks():
    return jsonify({'tasks': [tasks[k] for k in sorted(tasks.keys())] })

@app.route(API + '/tasks/<int:task_id>', methods=[GET])
def get_task(task_id):
    task = tasks.get(task_id)
    if not task:
        abort(404)
    return jsonify({'task':task})

@app.route(API + '/tasks', methods=[POST])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    global last_task_id
    last_task_id = last_task_id + 1

    task = {
        'id':last_task_id,
        'title': request.json['title'],
        'description':request.json.get('description', ''),
        'done': request.json.get('done', False)
    }
    tasks[last_task_id] = task
    return jsonify({'task':task}), 201

@app.route(API + '/tasks/<int:task_id>', methods=[PUT])
def update_task(task_id):
    if not request.json:
        abort(400)

    old_task = tasks.get(task_id, None)
    if not old_task:
        abort(400)

    modified_task = request.json
    if 'title' in modified_task and type(modified_task['title']) != unicode:
        abort(400)
    if 'description' in modified_task and type(modified_task['description']) != unicode:
        abort(400)
    if 'done' in modified_task and type(modified_task['done']) != bool:
        abort(400)

    old_task['title'] = modified_task.get('title', old_task['title'])
    old_task['description'] = modified_task.get('description', old_task['description'])
    old_task['done'] = modified_task.get('done', old_task['done'])
    return jsonify({'task':old_task})

if __name__ == '__main__':
    start_server()
