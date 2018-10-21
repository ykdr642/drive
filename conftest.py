import pytest

@pytest.fixture()
def getTestCase():
    f = open("testcase.txt","r")
    testcase = f.readlines()
    f.close()
    return testcase