# test_app.py: an automated test (the TEST stage)
from app import add     # import the function we want to check

def test_add():         # pytest runs any function starting with "test_"
    assert add(2, 3) == 6   # if this is false, the test fails and the pipeline stops
