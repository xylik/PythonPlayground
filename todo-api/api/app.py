#!/usr/bin/python
from flask import Flask, jsonify, request, abort, make_response

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
PATCH = 'PATCH'
DELETE = 'DELETE'

API_VERSION = 'v1.0'

tasks = {} #current active tasks
last_task_id = -1;

app = Flask(__name__)

def start_server():
    app.run(debug=True)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}), 404)

@app.route('/todo/api/' + API_VERSION + '/tasks', methods=[GET])
def get_tasks():
    return jsonify({'tasks': [tasks[k] for k in sorted(tasks.keys())] })

@app.route('/todo/api/' + API_VERSION + '/tasks/<int:task_id>', methods=[GET])
def get_task(task_id):
    task = tasks.get(task_id)
    if not task:
        abort(404)
    return jsonify({'task':task})

@app.route('/todo/api/' + API_VERSION + '/tasks', methods=[POST])
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

if __name__ == '__main__':
    start_server()
