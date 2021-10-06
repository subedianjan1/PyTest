import pytest

@pytest.fixture


def setupWallet():
    wallet  = [2,5,8]
    # Hello
    return wallet
'''
def test01_Wallet(setupWallet):
    assert setupWallet == [2,5]
'''
    
def test02_Wallet(setupWallet):
    assert setupWallet == [2,5,8]
 

 
