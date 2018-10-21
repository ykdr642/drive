import main
import pytest
"""
detabase = [
    (["2 2 2","1 2","2 1","2","1 2 2 1","1 1 2 2"],"4\n0\n"),
    (["2 4 4","1 2 1 3","2 1 1 3","6","1 2 2 1","1 3 1 4","2 1 2 3","1 4 2 4","1 1 1 3","2 2 2 3"],"2\n0\n6\n0\n")
]
"""
inputMessage = "testCase,expected"
testcase = []

#@pytest.fixture()
def getTestCase():
    f = open("testcase.txt","r")
    testcase = f.readlines()
    f.close()
    testcase = list(map(lambda x: x.replace("\n",""),testcase))
    return testcase

g = getTestCase()

def makeCase():
    return [(["2 2 2","1 2","2 1","2","1 2 2 1","1 1 2 2"],"4\n0\n"),(["2 4 4","1 2 1 3","2 1 1 3","6","1 2 2 1","1 3 1 4","2 1 2 3","1 4 2 4","1 1 1 3","2 2 2 3"],"2\n0\n6\n0\n")]

detabase = makeCase()

@pytest.mark.parametrize(inputMessage,detabase)
def test_Paiza(testCase,expected,capsys):
    test_obj = main.testProgram(testCase)
    test_obj.test()
    out,err = capsys.readouterr()
    assert out == expected

def test_1():
    assert g == ["1 2 3","1 2","1","","12 13","1"]