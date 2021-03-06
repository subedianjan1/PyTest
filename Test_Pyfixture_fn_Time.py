import MathFunc
import pytest
import time

''' Instead of calling the same codes over and over again to setup e.g
to connect and disconnect hardware or initialize a object or database..
This feature(Setup) will help to do it only once before the test. While teardown
will help to release the setup at the end of the test.

If something has to be run each time before each test function can use fixture.
No need to type code each time for function.

after the execution of each function setupState changed to 0. However as we run
setupState fixture each time a test function is executed makes setupState to 1 as it
prints.
)


'''

@pytest.fixture
def setupState():
    #code that Intitialises the setup or Hware
    print('*****Setup******Runs beore each fn')
    start = time.time()
    setupState  = 1
    yield setupState
    print('*****tear down******Runs after each fn')
    end = time.time()
    setupState  = 0
    print ("time taken for the test is " + str ((end-start)*1000) + ' msescs')


    
@pytest.mark.number #option to only run seleted test marked by number
def test_add(setupState):
    if setupState == 1:
        print("Initialed the database or HWare")
    assert MathFunc.add(7,3) == 10
    assert MathFunc.add(7) == 9    # second is given default in function as 2
    setupState = 0
    
    
@pytest.mark.number
def test_product(setupState):
     if setupState == 1:
        print("Initialed the database or HWare")
     assert MathFunc.product(7,3) == 21
     assert MathFunc.product(7) == 14
     setupState = 0
    
 #instead of == we can also use <,>,=>. != etc

#@pytest.mark.skip(reason = "do not run the test")
#Skipif can also be used if conditonal skip is required
def test_Junk(setupState):
    if setupState == 1:
        print("Initialed the database or HWare")
    assert MathFunc.product(7,3) == 21
    print(MathFunc.product (7,3),'Testing of print')# use -s to capture print
    setupState = 0
    
     
@pytest.mark.string #option to only run seleted test marked by number
def test_add_Strings(setupState):
    if setupState == 1:
        print("Initialed the database or HWare")
    result = MathFunc.add('Hello', 'World')
    assert result == 'HelloWorld'
    assert type(result) is str
    assert 'Hello' in result                            
    assert 'Helllo'not in result
    setupState = 0
      
@pytest.mark.string 
def test_product_Strings(setupState):
    if setupState == 1:
        print("Initialed the database or HWare")
    assert MathFunc.product( 'Hello ', 3 ) == 'Hello Hello Hello '
    result  = MathFunc.product('Hello')
    assert result == 'HelloHello'
    assert type(result)is str
    assert 'Hello' in result
    setupState = 0

