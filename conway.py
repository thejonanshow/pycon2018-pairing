# Live with < 2 : die
# Live with 2 or 3 : wake
# Dead with == 3 : wake
# Live with > 3 : die

from random import randint


class Square():
    def __init__(self):
        self.awake = True

    @property
    def is_awake(self):
        return self.awake

    @property
    def background(self):
        if self.is_awake:
            return 'grey'
        else:
            return 'black'

    def sleepify(self):
        self.awake = False

    def __str__(self):
        if self.is_awake:
            return "[O]"
        else:
            return "[X]"

class Board():
    def __init__(self, width = 25):
        self.spaces = [[Square() for i in range(width)] for j in range(width)]

        for row in self.spaces:
            for square in row:
                if randint(1, 2) == 2:
                    square.sleepify()

    def __str__(self):
        output = ""
        for row in self.spaces:
            for square in row:
                output = output + str(square)

            output = output + "\n"

        return output


board = Board()
print(board)
