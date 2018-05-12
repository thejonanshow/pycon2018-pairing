grid = {
    (0, 0): True,
    (0, 1): True,
}

def get_neighbors(coordinates):
    x, y = coordinates

    for x_offset in [-1, 0, 1]:
        for y_offset in [-1, 0, 1]:
            target = (x + x_offset, y + y_offset)

            # don't count self as its neighbor
            if target == coordinates:
                continue

            yield target

def count_living_neighbors(coordinates, grid):
    return sum(
        1 if grid.get(neighbor, False) else 0 
        for neighbor in get_neighbors(coordinates)
    )

def get_next_state(coordinates, grid):
    count = count_living_neighbors(coordinates, grid)
    live = grid[coordinates]

    # Live with < 2 : die
    if live and count < 2:
        return False

    # Live with 2 or 3 : live
    if live and (1 < count < 4):
        return True

    # Dead with == 3 : live
    if not live and count == 3:
        return True
    
    # Live with > 3 : die
    if live and count > 3:
        return False

    return False

def a_whole_new_world(grid):
    return {
        coordinates: get_next_state(coordinates, grid)
        for coordinates in grid
    }
