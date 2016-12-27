import sys

test_name = ''
passed_tests = {}
failed_tests = {}

def test(func):
    global test_name, passed_tests
    test_name = func.__name__
    passed_tests[test_name] = True
    return func

def assert_true(actual, expected=True):
    if actual != expected:
        print test_name + ' failed. Expected: ' + str(expected) + ' found: ' + str(actual)
        global passed_tests, failed_tests
        passed_tests[test_name] = False
        failed_tests[test_name] = True

    # else: print 'Test passed: ' + test_name
