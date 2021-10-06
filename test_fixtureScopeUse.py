'''
Here using the fixture scope to the module with autouse, the fixture gets invoked
in every test function with out bieing have to pass the fixture return/yield Value as argument

Use: pytest -s -v test_fixtureScopeUse.py
'''


import pytest
Apple = "None"

@pytest.fixture (scope ='module', autouse= True)
def Runfirst():
    global Apple
    print ("fixture run")
    Apple = 1
    yield Apple

    
def test001_DoNotUseFixture():
    global Apple
    assert 2 ==2
    print (Apple)
    

def test002_printApple():
    global Apple
    print (Apple)
  


def test01_AppleState(Runfirst):
    global Apple
    assert 1 == 1
    print (Apple)



    

