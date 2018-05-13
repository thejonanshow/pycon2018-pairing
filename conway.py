# Live with < 2 : die
# Live with 2 or 3 : live
# Dead with == 3 : live
# Live with > 3 : die

class Cell:

    ALIVE = 'alive'
    DEAD = 'dead'
    
    def __init__(self):
        self.state = self.DEAD

    def enliven(self):
        self.state = self.ALIVE
    
def main():
    pass
