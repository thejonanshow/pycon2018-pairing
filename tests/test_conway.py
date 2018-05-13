from .context import conway
from conway import Board

def test_default_board_dimensions():
    test_board = Board()
    assert test_board.width() == 25
    assert test_board.height() == 25

def test_board_has_given_dimensions():
    test_board = Board(width=30, height=30)
    assert test_board.width() == 30
    assert test_board.height() == 30

def test_board_internal_structure_created():
    test_board = Board()
    test_board._board

def test_board_internal_structure_dimensions():
    test_board = Board(width=35, height=40)
    assert len(test_board._board) == 35
    assert len(test_board._board[0]) == 40

