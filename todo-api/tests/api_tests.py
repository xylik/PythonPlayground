#!/usr/bin/python
import requests
from test_utils import *
API_BASE_URL = 'http://localhost:5000/todo/api/v1.0'

def start_server():
    App.start_server()

@test
def server_init():
    resp = requests.get(API_BASE_URL + '/tasks')
    assert_true(resp.status_code, 200)

def start_tests():
    # start_server()
    server_init()

if __name__ == '__main__':
    if __package__ is None:
        print 'Tests executed directly - classic way!'
        import sys
        from os import path
        todoApiDirPath = path.dirname(path.dirname( path.abspath(__file__) ))
        sys.path.insert(0,  todoApiDirPath)
        import api.App
        # from api import App
        # from api.App import *
    else:
        print 'Tests executed with -m param!'
        from ..api.App import *
    start_tests()
