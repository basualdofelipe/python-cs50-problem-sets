from fuel import convert, gauge

def test_convert_zero_division():
    assert convert("1/0") == None
    assert convert("13/0") == None
    assert convert("3/0") == None

def test_convert_value_error():
    assert convert("") == None
    assert convert("hola") == None
    assert convert("8+8") == None
    assert convert("8") == None
    assert convert("2.7") == None
    

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/5") == 20
    assert convert("10/10") == 100
    assert convert("2/1") == 200
    assert convert("99/100") == 99
    assert convert("0/2") == 0
    assert convert("1/8") == 12

def test_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_gauge_perc():
    assert gauge(80) == "80%"
    assert gauge(30) == "30%"
    assert gauge(88) == "88%"
    assert gauge(24) == "24%"
    assert gauge(25) == "25%"

def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"