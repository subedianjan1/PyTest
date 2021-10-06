import pytest

@pytest.fixture
def verCheckList():
    #CheckList = [swVer,fwVer,devFwVer,modFwVer]
    CheckList = [1.0,1.1,1.2,1.3]
    return CheckList

def test01_CheckVersions(verCheckList):
	assert [1.0,1.1,1.2,1.3] == verCheckList
