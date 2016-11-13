import my_math as mm
import nose

def test_power():
    assert mm.f_power(2,3) == 8

def test_sqrt():
    assert mm.f_sqrt(4) == 2, 'reason why this failed'

if __name__ == "__main__":
    nose.runmodule()
