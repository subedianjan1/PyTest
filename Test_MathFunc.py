import MathFunc

def test_add():
    assert MathFunc.add(7,3) == 10
    assert MathFunc.add(7) == 9    # second is given default in function as 2

def test_product():
    assert MathFunc.product(7,3) == 21
    assert MathFunc.product(7) == 14
