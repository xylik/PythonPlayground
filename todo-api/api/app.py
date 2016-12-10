#!/usr/bin/python
from flask import Flask, jsonify

GET = 'GET'
POST = 'POST'
PUT = 'PUT'
PATCH = 'PATCH'
DELETE = 'DELETE'

tasks = {} #current active tasks
finished_tasks = {} #old finished tasks

app = Flask(__name__)

def start_server():
    app.run(debug=True)

@app.route('/todo/api/v1.0/tasks', methods=[GET])
def get_tasks():
    return jsonify()

if __name__ == '__main__':
    start_server()
