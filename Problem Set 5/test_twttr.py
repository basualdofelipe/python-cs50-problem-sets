from twttr import shorten

def test_shorten():
    assert shorten("amapola") == "mpl"
    assert shorten("cangrejo hermitaño") == "cngrj hrmtñ"

def test_shorten_all_caps():
    assert shorten("AMAPOLA") == "MPL"
    assert shorten("CANGREJO HERMITAÑO") == "CNGRJ HRMTÑ"