import pytest
from testTool import Drive

def get_field(input_stdin,Number=False):
    out = input_stdin.split()
    if len(out) > 1:
        if Number:
            try:
                return list(map(lambda x:int(x), out))
            except:
                return out
        else:
            return out
    else:
        if Number:
            try:
                return int(out[0])
            except:
                return out[0]
        else:
            return out[0]

class testProgram(Drive):
    def test(self):
        print(self.input())