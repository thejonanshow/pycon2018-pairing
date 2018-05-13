from .context import conway
from conway import Grid

def test_grid_has_size():
    grid = Grid()
    assert grid.width == 50
    assert grid.height == 25
