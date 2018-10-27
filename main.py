import pytest
from testTool import Drive


def getNumList(stdin):
    out = stdin.split()
    return list(map(lambda x:int(x), out))


def getStrList(stdin):
    return stdin.split()

class testProgram(Drive):
    def test(self):
        print(self.input())