from seasons import calc_minutes
from datetime import date

def test_minutes():
    assert calc_minutes("1995-7-27", date(2024,1,17)) == "Fourteen million, nine hundred and seventy-seven thousand, four hundred and forty minutes"
    assert calc_minutes("2023-1-17", date(2024,1,17)) == "Five hundred and twenty-five thousand, six hundred minutes"
    assert calc_minutes("2022-1-17", date(2024,1,17)) == "One million, fifty-one thousand, two hundred minutes"