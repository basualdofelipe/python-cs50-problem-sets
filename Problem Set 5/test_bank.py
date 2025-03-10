from bank import value

def test_bank_hello():
    assert value("hello") == 0

def test_bank_h():
    assert value("hi") == 20
    assert value("halwdknawad") == 20
    assert value("hell o") == 20

def test_bank_other():
    assert value("") == 100
    assert value("djfgwejf") == 100
    assert value("morning") == 100
    assert value("sir") == 100