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

def getTestCase():
    f = open("testcase.txt","r")
    testCaseList = f.readlines()
    f.close()
    tmp = []
    test = []
    for _case in testCaseList:
        if _case is not "\n":
            tmp.append(_case)
        else:
            test.append(tmp[:])
            tmp = []
    test.append(tmp[:])
    testcase = test[0::2]
    _tmpexpected = test[1::2]
    testCase = []
    for oneTestcase in testcase:
        testCase.append((list(map(lambda x:x.replace("\n",""),oneTestcase))))
    onexpected = ""
    expected = []
    for _etmp in _tmpexpected:
        for t in _etmp:
            onexpected += t
        expected.append(onexpected)
        onexpected = ""
    detabase = []
    for t,e in zip(testCase, expected):
        detabase.append((t,e))
    return detabase