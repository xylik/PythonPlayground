import sys

test_name = ''
test_results = {}

def test(func):
    global test_name
    test_name = func.__name__
    test_results[test_name] = True
    return func

def assert_true(actual, expected=True):
    if actual != expected:
        print(test_name + ' failed. Expected: ' + str(expected) + ' found: ' + str(actual))
        test_results[test_name] = False
