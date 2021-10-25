import MathFunc
import pytest
setupState = 'none'

''' 
Pytest fixture is basically analogus to the function in general programming.
Once the fixture is defined. it can be passed as a paramerter to to the test function.
After which the fixture function can be called. It is very useful feature as
repetion of same code in multiple places can be avoided.

By making the scope Modular, the fixture
automatically called by every test function and no need to pass an argument


cd C:\Projects\Github\Python-Test-Work\PyTest
pytest -v -s Test_Pyfixture_mpdule.py

'''

setupState = 'None'

@pytest.fixture(scope='module')
def setupState(): #Afer scoping for module. Only supposed to be executed onec.
    print ("******************Setup*****************")
    global setupState
    #code that Intitialises the setup or Hware
    setupState = "Setup Done"
    yield setupState
    setupState = "No Setup Done"
@pytest.mark.number #option to only run seleted test marked by number
def test_add():
    assert MathFunc.add(7,3) == 10
    assert MathFunc.add(7) == 9    # second is given default in function as 2   
    global setupState
    print (setupState) 
@pytest.mark.number
def test_product():
     assert MathFunc.product(7,3) == 21
     assert MathFunc.product(7) == 14
     print (setupState) 
#instead of == we can also use <,>,=>. != etc
#@pytest.mark.skip(reason = "do not run the test")
#Skipif can also be used if conditonal skip is required
def test_Junk():
    assert MathFunc.product(7,3) == 21
    print(MathFunc.product (7,3),'Testing of print')# use -s to capture print
    print (setupState) 
     
@pytest.mark.string #option to only run seleted test marked by number
def test_add_Strings():
    result = MathFunc.add('Hello', 'World')
    assert result == 'HelloWorld'
    assert type(result) is str
    assert 'Hello' in result                            
    assert 'Helllo'not in result
    print (setupState) 
      
@pytest.mark.string 
def test_product_Strings():
    assert MathFunc.product( 'Hello ', 3 ) == 'Hello Hello Hello '
    result  = MathFunc.product('Hello')
    assert result == 'HelloHello'
    assert type(result)is str
    assert 'Hello' in result
    print (setupState)




