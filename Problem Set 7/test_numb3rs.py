from numb3rs import validate

def test_validate_correct():
    assert validate("1.1.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("100.100.100.100") == True
    assert validate("255.255.255.255") == True
    assert validate("123.123.123.123") == True
    assert validate("15.81.91.140") == True
    assert validate("13.12.18.14") == True
    assert validate("135.0.182.0") == True

def test_validate_incorrect():
    assert validate("1.1.1") == False
    assert validate("1.1..1") == False
    assert validate("1.156.1") == False
    assert validate("259.2.3.0") == False
    assert validate("1.1.1.1.1") == False
    assert validate("cat") == False
    assert validate("ipv4") == False
