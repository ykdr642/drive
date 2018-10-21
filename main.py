import pytest
from testTool import Drive

def get_field(input_stdin):
    out = input_stdin.split()
    if len(out) > 1:
        return out
    else:
        return out[0]

class game:
    def __init__(self,field_inf):
        field = get_field(field_inf)
        self.hight = int(field[0])
        self.width = int(field[1])
        self.people = int(field[2])
        self.card_list = []
        self.score_board = []
        for hoge in range(self.people):
            self.score_board.append(0)
        self.player = 0

    def get_card(self,stdin):
        input = get_field(stdin)
        self.card_list.append(input)

    def add_score(self):
        self.score_board[self.player] += 2

    def next(self):
        self.player += 1
        if self.player == self.people:
            self.player = 0

    def check_card(self,stdin):
        input_list = get_field(stdin)
        hw = list(map(lambda x: int(x) - 1,input_list))
        if self.card_list[hw[0]][hw[1]] == self.card_list[hw[2]][hw[3]] and \
            self.card_list[hw[0]][hw[1]] is not None and \
            not (hw[0] == hw[2] and hw[1] == hw[3]):
            self.card_list[hw[0]][hw[1]] = None
            self.card_list[hw[2]][hw[3]] = None
            return True
        else:
            return False

    def turn(self,stdin):
        judge = self.check_card(stdin)
        if judge:
            self.add_score()
        else:
            self.next()

    def output(self):
        for _score in self.score_board:
            print(_score)
    


class testProgram(Drive):
    def test(self):
        game1 = game(self.input())
        for num in range(game1.hight):
            game1.get_card(self.input())
        num = int(self.input())
        for i in range(num):
            game1.turn(self.input())
        game1.output()