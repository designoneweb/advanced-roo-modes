from utils.temperature import c_to_f, f_to_c

def test_c_to_f_freezing():
    assert c_to_f(0) == 32

def test_c_to_f_boiling():
    assert c_to_f(100) == 212

def test_f_to_c_freezing():
    assert f_to_c(32) == 0

def test_f_to_c_boiling():
    assert f_to_c(212) == 100