import pytest

def testEqual():
    assert 2*2 == 4

def testNotEqual():
    assert 2*2 != 5

def testLessthan():
    assert 2*2 < 5

# Can print in the traceback with the error message
def testMorethan():
    assert 2*2 < 3, "2*2 should be larger; Expected failure"    

def testInstring():
    assert "uu" in "pluubh"
#if we are expectig a exception and we want to ingnore and pass it
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# for actual exception info
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert "maxim" in str(excinfo.value)

