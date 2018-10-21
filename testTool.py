class Drive:
    def __init__(self,testcase):
        self.ls = testcase

    def input_testCase(self,testcase):
        self.ls = testcase

    def input(self):
        out = self.ls[0]
        self.ls.pop(0)
        return out
#main
    def test(self):
        pass