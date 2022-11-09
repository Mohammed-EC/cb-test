def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def test_add():
    result = add(1, 2)
    assert result == 4


def test_subtract():
    result = subtract(2, 1)
    assert result == 1
