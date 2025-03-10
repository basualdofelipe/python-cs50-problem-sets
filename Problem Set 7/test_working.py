from working import convert
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:45 AM to 5 PM") == "09:45 to 17:00"
    assert convert("9 AM to 5:52 PM") == "09:00 to 17:52"
    assert convert("9 PM to 5 PM") == "21:00 to 17:00"
    assert convert("9 AM to 5 AM") == "09:00 to 05:00"

def test_convert_value_error():
    with pytest.raises(ValueError, match="input not accepted"):
        convert("123")
    with pytest.raises(ValueError, match="input not accepted"):
        convert("9 to 5")
