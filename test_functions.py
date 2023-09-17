"""
    The file name which we have to tun for pytest should start with test_ or end with _test
    pytest will run all the files which start with test_ or end with _test
    Also the function name should start with test_ or end with _test
    pytest will run all the functions which start with test_ or end with _test
"""
from utils import add, subtract

def test_add_function():
    assert add(10, 20) == 40
    assert add(10, 20) != 50

def test_subtract_function():
    assert subtract(20, 10) == 30
    
"""
run "pytest <file name>" to run the test and look for the errors
"""