# Live with < 2 : die
# Live with 2 or 3 : live
# Dead with == 3 : live
# Live with > 3 : die


class Molecule():
    def __init__(self, neighbours = []):
        self._neighbours = neighbours

    @property
    def neighbours(self):
        return self._neighbours
