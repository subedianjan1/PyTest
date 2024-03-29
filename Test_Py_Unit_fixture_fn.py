import MathFunc
import pytest # Required for fixtures
import unittest # so that we can also mix Unit test 

''' Instead of calling the same codes over and over again to setup e.g
to connect and disconnect hardware or intialize a object or database..
This feature(Setup) will help to do it only once before the test.

If somethig has to be run each time before each test function can use fixture.
No need to type code each time for function.

after the execution of each function setupState changed to 0. However as we run
setupState fixture each time a test function is executed makes setupState to 1 as it
prints.
)

'''

@pytest.fixture
def setupState():
    #code that Intitialises the setup or Hware
    print('*****Setup******')
    setupState  = 1
    yield setupState
    print('*****Original State, SetupState is set to 0 ******')
    setupState  = 0
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

##Let us insert unit test in the middle of the pytest so that we can mix it up.

#class UnittestMix


class TestNumeric(unittest.TestCase):
    def test_add(self):
        self.assertEqual(MathFunc.add(1,2),3)
        
#below codes are not required if ran with pytest although causes no error if kept

'''
if __name__ == '__main__':
    unittest.main()
'''




    

