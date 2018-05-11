# Live with < 2 : die
# Live with 2 or 3 : live
# Dead with == 3 : live
# Live with > 3 : die


class Cell:
    alive = False

    def is_alive(self):
        return self.alive
    
    def is_dead(self):
        return not self.alive

    def enliven(self):
        self.alive = True

    def kill(self):
        self.alive = False

    def __repr__(self):
        if self.is_alive():
            return "🥞"
        else:
            return "💀"

    def __str__(self):
        return "🥞"


class Gridiverse:
    """
    This holds the cells, gently, lovingly.
    """
    grid = []

    def __init__(self, width):
        self.size = width * width
        self.grid = [Cell() for num in range(self.size)]

    def dead_cell_count(self):
        deadies = [cell for cell in self.grid if cell.is_dead()]
        return len(deadies)
