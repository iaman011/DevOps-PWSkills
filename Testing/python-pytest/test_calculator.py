import pytest
from calculator import add, divide

def test_add():
    # Assert -> Asssertion(condition) => OutPut Result
    assert add(2,3) == 5

# The assert is a built-in Python keyword used to test if a condition is True.
# If it’s not true, Python (or pytest) will raise an AssertionError and mark the test as failed.

def test_add2():
        # False Case
        assert add(2,2) == 5

def test_divide():
    assert divide (2,2) == 1

def test_divide2():
    # False case
    assert divide (2,2) == 5

# to run : change the directory to desired directory : D:\DevOps-PWSkills\Testing\python-pytest> 
# python -m pytest test_calculator.py

# also try this using environment : python -m venv venv (create a folder any of drive, go to address bar select the cmnd then backspace then type this command venv created on your desired folder)
# to run this using environment: pytest test_calculator.py