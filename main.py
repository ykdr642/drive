import pytest
from testTool import Drive


def makeMatrix(column:int,row:int,init):
    r = [init for i in range(column)]
    m = [r[:] for i in range(row)]
    return m


def getNumList(stdin):
    out = stdin.split()
    return list(map(lambda x:int(x), out))


def getStrList(stdin):
    return stdin.split()

class testProgram(Drive):
    def test(self):
        print(self.input())