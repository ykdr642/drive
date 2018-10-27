import main
import pytest
from testTool import getTestCase

inputMessage = "testCase,expected"
testcase = []

detabase = getTestCase()

@pytest.mark.xfail()
@pytest.mark.parametrize(inputMessage,detabase)
def test_Paiza(testCase,expected,capsys):
    test_obj = main.testProgram(testCase)
    test_obj.test()
    out,err = capsys.readouterr()
    assert out == expected