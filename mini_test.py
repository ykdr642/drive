import main

def test_1():
    out = main.get_field("2 2 2")
    assert out == ["2","2","2"]

def test_2():
    out = main.get_field("1")
    assert out == "1"

def test_3():
    game1 = main.game("2 2 2")
    assert game1.hight == 2
    assert game1.width == 2
    assert game1.people == 2
    assert type(game1.card_list) == list
    assert type(game1.score_board) == list
    assert game1.score_board == [0,0]

def test_4():
    game1 = main.game("2 2 2")
    game1.get_card("1 2")
    assert game1.card_list == [["1","2"]]
    game1.add_score()
    assert game1.score_board == [2,0]
    game1.next()
    game1.add_score()
    assert game1.score_board == [2,2]

def test_5(capsys):
    game1 = main.game("2 2 2")
    game1.get_card("1 2")
    game1.get_card("2 1")
    game1.turn("1 1 2 1")
    game1.turn("1 1 2 2")
    game1.output()
    out,err = capsys.readouterr()
    assert out == "0\n2\n"

def test_6():
    game1 = main.game("2 2 2")
    game1.get_card("1 2")
    game1.get_card("2 1")
    game1.turn("1 1 2 1")
    assert game1.player == 1
    game1.turn("1 1 2 1")
    assert game1.player == 0
    game1.turn("1 1 2 1")
    game1.turn("1 1 2 1")
    assert game1.player == 0
    game1.turn("1 1 1 1")
    assert game1.player == 1

def test_7():
    game1 = main.game("2 2 2")
    game1.get_card("1 2")
    game1.get_card("2 1")
    game1.turn("1 1 1 1")
    assert game1.player == 1