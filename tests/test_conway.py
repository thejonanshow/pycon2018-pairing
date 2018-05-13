from .context import conway
from conway import Cell

def test_main():
    assert True

def test_cell_can_be_enlivened():
    test_cell = Cell()
    test_cell.state = Cell.DEAD
    
    test_cell.enliven()
    assert test_cell.state == Cell.ALIVE
