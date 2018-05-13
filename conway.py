# Live with < 2 : die
# Live with 2 or 3 : live
# Dead with == 3 : live
# Live with > 3 : die


class Grid():
    def __init__(self, width=50, height=25):
        self.layout = [[None for i in range(height)] for j in range(width)]

    @property
    def width(self):
        len(self.layout)

    @property
    def height(self):
        len(self.layout[0])
