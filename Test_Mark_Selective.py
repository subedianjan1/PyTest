import MathFunc
import pytest
'''
With the use of decorator "@pytest.mark.*", only selected test cases can
be executed. The selection is done in the commandline giving the argument * 
in pytest command
E.g  "  pytest -v  -m  number Test_mark_Selective"   if we want to run only test functions def test_add()
and def test_product():
Read other red comments that provide important selective test functions or wathch the video lesson 2

Note: There are also options to execute the selected tests with tetcase strings in
by passing the arguments in command line.

To Execute:
cd C:\Projects\Github\Python-Test-Work\PyTest
pytest -v -s Test_Mark_Selective.py

'''


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
    print(MathFunc.product (7,3),'Testing of print')# use -s to capture print
    #assert 'ii' == MathFunc.add ( 'i')
   
     
    
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

