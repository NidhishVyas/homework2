from calculator import add, subtract

def test_addition():
    assert add(3,3) == 6

def test_subtraction():
    assert subtract(3,2) == 1
    