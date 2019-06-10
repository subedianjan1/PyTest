import MathFunc
import pytest

@pytest.mark.number #option to only run seleted test marked by number
def test_add():
    assert MathFunc.add(7,3) == 10
    assert MathFunc.add(7) == 9    # second is given default in function as 2

@pytest.mark.number
def test_product():
    assert MathFunc.product(7,3) == 21
    assert MathFunc.product(7) == 14
        #instead of == we can also use <,>,=>. != etc

#@pytest.mark.skip(reason = "do not run the test")
#Skipif can also be used if conditonal skip is required
def test_Junk():
    #assert 'ii' == MathFunc.add ( 'i')
    print  = (MathFunc.product (7,3),'Testing of print')# use -s to capture print
     
    
@pytest.mark.string #option to only run seleted test marked by number
def test_add_Strings():
    result = MathFunc.add('Hello', 'World')
    assert result == 'HelloWorld'
    assert type(result) is str
    assert 'Hello' in result                            
    assert 'Helllo'not in result
      
@pytest.mark.string 
def test_product_Strings():
    assert MathFunc.product( 'Hello ', 3 ) == 'Hello Hello Hello '
    result  = MathFunc.product('Hello')
    assert result == 'HelloHello'
    assert type(result)is str
    assert 'Hello' in result 

