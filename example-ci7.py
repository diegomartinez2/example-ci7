from pytest import approx

def add(a, b):
    return a + b
    #print("0.3 with approx", approx(0.3))

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    assert add(0.001, 0.002) == approx(0.003)
    #test = add(0.1, 0.2)-0.3
    #assert test < 1.0e-7

