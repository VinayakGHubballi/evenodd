from test import addit

def test_pos():
    assert addit(10, 20) == 30

def test_zero():
    assert check_even_odd(10,0) == 10
