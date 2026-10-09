# test_app.py: an automated test (the TEST stage)
from app import add     # import the function we want to check

def test_add():         # pytest runs any function starting with "test_"
    assert add(4, 2) == 6   # if this is false, the test fails and the pipeline stops
    assert add(5, 7) == 12  # if this is false, the test fails and the pipeline stops
