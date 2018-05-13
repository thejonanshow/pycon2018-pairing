from .context import conway
from conway import Matrix
from conway import Cell

def test_matrix_can_be_created():
    assert Matrix()

def test_matrix_size():
    assert Matrix().width == 50
    assert Matrix().height == 25

def test_matrix_starts_with_cells():
    assert type(Matrix().grid[0]) == Cell

def test_cell_can_be_dead():
    assert Matrix().grid[0].dead

def test_cell_can_be_killed():
    test_cell = Cell()
    test_cell.live()
    assert not test_cell.dead

    test_cell.die()
    assert test_cell.dead
