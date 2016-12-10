import sys

test_name = ''

def test(func):
    global test_name
    test_name = func.__name__
    return func

def assert_true(actual, expected):
    if actual != expected: print 'Test failed: ' + test_name
    else: print 'Test passed: ' + test_name
