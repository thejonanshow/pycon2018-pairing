import sys
import random
import time

SEED = int(sys.argv[-1]) if sys.argv[-1] != 'conway.py' else 7

random.seed(SEED)
LIFE_DIVISOR = 40
START_MAX = 25

class Board():
    def __init__(self):
        self.cells = []

    def __iter__(self):
        for cell in self.cells:
            yield cell

    def render(self):
        for row in range(self.max_height()):
            new_row = ["💀"] * self.max_width()
            for cell in self:
                if cell.y == row:
                    if cell.state == 'alive':
                        new_row[cell.x] = "😍"
            print(''.join(new_row))


    def max_height(self):

        v = 0
        for cell in self:
            if cell.y > v:
                v = cell.y
        return v + 1


    def max_width(self):
        v = 0
        for cell in self:
            if cell.x > v:
                v = cell.x
        return v + 1

    # Live with < 2 : die
    # Live with 2 or 3 : live
    # Dead 8with == 3 : live
    # Live with > 3 : die
    def next(self):
        life_row, death_row = [], []

        for cell in self:
            count = self.living_neighbor_count(cell)

            if (count <  2) or (count > 3):
                death_row.append(cell)
            elif not cell.alive and count == 3:
                life_row.append(cell)

        for doomed in death_row:
            doomed.alive = False

        for chosen in life_row:
            chosen.alive = True

        return self

    def living_neighbor_count(self, cell):
        cells = {(cell.x, cell.y): cell for cell in self}

        neighbors = []
        for x_offset in [-1, 0, 1]:
            for y_offset in [-1, 0, 1]:
                target_x = cell.x + x_offset
                target_y = cell.y + y_offset

                try:
                    neighbors.append(cells[(target_x, target_y)])
                except KeyError:
                    pass

        return len([cell for cell in neighbors if cell.state == 'alive'])

board = Board()


class Cell():
    def __init__(self, *, x=None, y=None, board):
        self.x = x if x else random.randint(0, START_MAX)
        self.y = y if x else random.randint(0, START_MAX)
        self.alive = random.random() < LIFE_DIVISOR
        board.cells.append(self)

    @property
    def state(self):
        return 'alive' if self.alive else 'dead'

for i in range(40):
    c = Cell(board = board)

count = 0
while True:
    count += 1
    print(chr(27) + "[2J")
    board.render()
    print(count)
    board.next()
    time.sleep(1)
