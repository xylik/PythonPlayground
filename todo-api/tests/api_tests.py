#!/usr/bin/python
import requests
from test_utils import *
API = 'http://localhost:5000/todo/api/v1.0'

def start_server():
    App.start_server()

@test
def server_init():
    resp = requests.get(API + '/tasks')
    assert_true(resp.status_code, 200)

@test
def empty_todo_list():
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

def print_test_statistics():
    print
    passed_cnt = len([k for k in passed_tests.keys() if passed_tests[k]])
    print str(passed_cnt) + ' test' +  ('s' if passed_cnt == 0 or passed_cnt > 1 else '') + ' passed'
    failed_cnt = len(failed_tests)
    print str(failed_cnt) + ' test' +  ('s' if failed_cnt == 0 or failed_cnt > 1 else '') + ' failed'

def start_tests():
    # start_server()
    print '*** Tests started ***\n'
    server_init()
    empty_todo_list()
    create_new_task()

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
