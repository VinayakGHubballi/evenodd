from test import addit

def test_pos():
    assert addit(10, 20) == 30

def test_zero():
    assert addit(10,0) == 10
