from .context import conway
from conway import (Cell, Gridiverse)

def test_main():
    assert True

def test_cell_can_be_created():
    assert Cell()

def test_cell_starts_dead():
    cell = Cell()
    assert cell.is_dead()

def test_enliven():
    cell = Cell()
    cell.enliven()
    assert cell.is_alive()

def test_kill():
    cell = Cell()
    cell.kill()
    assert cell.is_dead()

def test_gridiverse():
    width = 20
    grid = Gridiverse(width)
    assert grid.size == width * width

def test_gridiverse_has_cells():
    grid = Gridiverse(10)
    assert grid.dead_cell_count() == 100
