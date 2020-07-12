#!/usr/bin/python
import requests
from test_utils import *
API = 'http://localhost:5000/todo/api/v1.0'

def start_server():
    app.start_server()

@test
def server_init():
    resp = requests.get(API + '/tasks')
    assert_true(resp.status_code, 200)

@test
def empty_list():
    resp = requests.get(API + '/tasks')
    assert_true(resp.status_code, 200)
    assert_true(resp.json(), {'tasks':[]} )

@test
def create_new_task():
    task = {
        'title':'Python',
        'description':'Finish todo api',
        'done':'false'
    }
    resp = requests.post(API + '/tasks', json=task)
    created_task = resp.json()['task']

    assert_true(resp.status_code, 201)
    assert_true(created_task['title'], 'Python')
    assert_true(created_task['description'], 'Finish todo api')
    assert_true(created_task['done'], 'false')
    assert_true(created_task['id'] == 0)

@test
def update_task():
    create_task = {
        'title':'Python',
        'description':'Finish todo api',
        'done': False
    }
    create_resp = requests.post(API + '/tasks', json=create_task)
    task_id = create_resp.json()['task']['id']

    create_task['title'] = 'Java'
    create_task['description'] = 'Learn spark java'
    create_task['done'] = True
    update_resp = requests.put(API + '/tasks/' + str(task_id), json=create_task)
    updated_task = update_resp.json()['task']
    assert_true(updated_task['id'] == task_id)
    assert_true(updated_task['title'] == 'Java')
    assert_true(updated_task['description'] == 'Learn spark java')
    assert_true(updated_task['done'] == True)

def print_test_statistics():
    print()
    passed_cnt = len([k for k in test_results.keys() if test_results[k]])
    print(str(passed_cnt) + ' test' +  ('s' if passed_cnt == 0 or passed_cnt > 1 else '') + ' passed')
    failed_cnt = len(test_results) - passed_cnt
    print(str(failed_cnt) + ' test' +  ('s' if failed_cnt == 0 or failed_cnt > 1 else '') + ' failed')

def start_tests():
    # start_server() # won't work in this way because start_server() is blocking
    print('*** Tests started ***\n')
    server_init()
    empty_list()
    create_new_task()
    update_task()

    print_test_statistics()

if __name__ == '__main__':
    if __package__ is None:
        #'Tests executed directly - classic way!'
        import sys
        from os import path
        todoApiDirPath = path.dirname(path.dirname( path.abspath(__file__) ))
        sys.path.insert(0,  todoApiDirPath)
        import api.app
        # from api import App
        # from api.App import *
    else:
        # 'Tests executed with -m param!'
        from ..api.app import *
    start_tests()
