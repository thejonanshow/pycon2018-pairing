from .context import conway
from conway import Square

def test_main():
    assert True

def test_square__initial_state():
    assert Square().is_awake

def test_square__background__awake_state():
    assert Square().background == 'grey'

def test_square__background__sleep_state():
    square = Square()
    square.sleepify()
    assert square.background == 'black'
