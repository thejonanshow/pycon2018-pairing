# Live with < 2 : die
# Live with 2 or 3 : live
# Dead with == 3 : live
# Live with > 3 : die
import random


class Matrix:

    def __init__(self, width=50, height=25):
        self.width = width
        self.height = height
        self.grid = []
        for column in range(self.height * self.width):
            self.grid.append(Cell())

    def __str__(self):
        for cell in self.grid:
            print(cell)

class Cell:

    def __init__(self):
        dead_chance = random.randint(1, 100)
        if dead_chance > 50:
            self.dead = True
        else:
            self.dead = False
    def die(self):
        self.dead = True
        # if you wanna do other things here

    def live(self):
        self.dead = False

    def __str__(self):
        if self.dead:
            return "💀"
        else:
            return "😀"

print(Matrix())
