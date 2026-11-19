from calculator import add, subtract, multiply, divide, CircleArea

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(6, 2) == 3

def test_subtract():
    assert subtract(7,3) == 4

def test_multiply():
    assert multiply(6,5) == 30

def test_divide_uneven():
    a, b = 5, 2
    result = divide(a,b)
    assert result == 2.5

def test_circleArea():
    assert CircleArea(-4) == "Error"