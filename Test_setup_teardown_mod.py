import MathFunc
import pytest

''' Instead of calling the same codes over and over again to setup e.g
to connect and disconnect hardware or intialize a object or database..
This feature(Setup) will help to do it only once before the test. While teardown
will help to release the setup at the end of the test.
)
If 'function' parameter is not given to the setup and teardown functions the socpe
of thier executeion is module


cd C:\Projects\Github\Python-Test-Work\PyTest
pytest -v -s Test_setup_teardown.py
'''
setupState =  None  #Global Variable 

def setup_module():
   
    #code that Intitialises the setup or Hware ( do the action of setup)
    print(" Initialed the database or HWare")
    print( "Connected to Hardware")
  
def teardown_module():
    print(" Disconnect Hardware or close the databae")
    # do the action of releasing here
   
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

