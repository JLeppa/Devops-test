def test_1:
    assert 1+1 == 2

def test_2:
    assert 2*4 == 8

def test_3:
    from src.project import multiplier
    assert 2*3 == multiplier(2,3)
