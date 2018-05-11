# Live with < 2 : die
# Live with 2 or 3 : live
# Dead with == 3 : live
# Live with > 3 : die

def main():
    pass


class Cell():
    def __init__(self):
        self.live = False

    def is_alive(self):
        return self.live == True

    def is_dead(self):
        return self.live == False

    def murder(self):
        self.live = False

    def resurrect(self):
        self.live = True

    def __iter__(self):
        yield "turtle"

    def next(self):
        pass

    def __str__(self):
        return "💀" if self.is_dead() else "😇"

    def __repr__(self):
        return "🤖" if self.is_dead() else "👻"


class Board():
    def __init__(self):
        self.width = 25
        self.cells = [[Cell() for i in range(self.width)] for j in range(self.width)]

    def get_width(self, mykeyword):
        return self.width

    def get_cell(self, xpos = 0, ypos = 0):
        return self.cells[xpos][ypos] 

    def __str__(self):
        result = ""

        for row in self.cells:
            for cell in row:
                result = result + str(cell)

            result = result + "\n"

        return result

    def __repr__(self):
        return "<Board - width: {width}>".format(width=self.width, height=2)

print(Board())
