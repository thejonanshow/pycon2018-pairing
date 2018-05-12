# Look up Black for autoformatting

from pytest import fixture

import conway

@fixture()
def test_grid():
    return {
        (x, y): True
        for x in range(10)
        for y in range(10)
    }

def test_main():
    assert conway.grid[(0,0)]

def test_neighbors_finds_all_neighbors():
    start = (1, 1)
    expected = {
        (0, 0), (0, 1), (0, 2),
        (1, 0),         (1, 2),
        (2, 0), (2, 1), (2, 2),
    }

    assert expected == set(conway.get_neighbors(start))

def test_0_1_shouldnt_survive(test_grid):
    assert not conway.get_next_state((0, 1), test_grid)

def test_count_living_neighbors(test_grid):
    start = (1, 1)
    assert conway.count_living_neighbors(start, test_grid) == 8
    start = (0, 0)
    assert conway.count_living_neighbors(start, test_grid) == 3

def test_crowded_cells_die(test_grid):
    assert not conway.get_next_state((1, 1), test_grid)

def test_friendly_cells_breed(test_grid):
    test_grid[(0, 0)] = False
    assert conway.get_next_state((0, 0), test_grid)

def test_there_can_only_be_corners(test_grid):
    expected = {
        (0, 0), (0, 9),
        (9, 0), (9, 9),
    }
    for coordinates in conway.a_whole_new_world(test_grid):
        if test_grid[coordinates]:
            output_world(conway.a_whole_new_world)
            assert coordinates in expected


def output_world(grid):
    for x in  range(10):
        for y in range(10):
            print('\n', x, ' ,', y, ': ', grid[(x, y)])
