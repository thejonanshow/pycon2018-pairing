from .context import conway
from conway import Cell, Board

def test_main():
    assert True

def test_creating_cell():
    assert Cell()

def test_new_cells_are_dead():
    assert Cell().is_dead()

def test_cells_can_live():
    test_cell = Cell()
    test_cell.resurrect()
    assert test_cell.is_alive()

def test_murder():
    test_cell = Cell()
    test_cell.murder()
    assert test_cell.is_dead()

def test_board_is_twenty_five_bigness():
    test_board = Board()
    assert test_board.get_width() == 25

def test_get_cell():
    test_board = Board()
    assert type(test_board.get_cell()) == Cell

def test_that_cells_contain_turtles():
    test_cell = Cell()
    assert "turtle" in test_cell

def test_draw_board():
    test_board = Board()
    assert "💀" in str(test_board)

