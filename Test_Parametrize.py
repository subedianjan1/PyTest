import MathFunc
import pytest

''' Instead of calling the same function many times as in "Test_Mark_Selective.py"
This time we parametrize it so that the function is call only once but with many
input variables '''

@pytest.mark.parametrize('Add1,Add2,AddResult',
                            [            #List the input variables
                                (3,7,10), #Intgers
                                (2.5,3.5, 6),#Float
                                ('Hello','World','HelloWorld'), #String
                                (-5, 1, -4)# -ve Numbers
                                ]
                         )
def test_add(Add1,Add2,AddResult):
    assert MathFunc.add(Add1,Add2) == AddResult
     

@pytest.mark.parametrize('prd1,prd2,prdResult',
                         [
                             ('aaa',1, 'aaa'), 
                             ('aaa',5,'aaaaaaaaaaaaaaa' ),
                             (6,8,48)
                             ]
                         )
def test_product(prd1,prd2,prdResult):
    assert MathFunc.product(prd1,prd2) == prdResult

# Not sure how do the default product with only one parameter in the parametrize above.
#Let us do it manually with the Extra tes cases.
def test_add_Extra():
    assert MathFunc.add(3) == 5

def test_product_Extra():
    assert MathFunc.product(6)== 12

   


