from test import checkNo

def test_even():
    assert checkNo(10) == "Even number"

def test_odd():
    assert checkNo(13) == "Odd number"