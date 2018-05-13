# Live with < 2 : die
# Live with 2 or 3 : live
# Dead with == 3 : live
# Live with > 3 : die
WIDTH_DEFAULT=25
HEIGHT_DEFAULT=25
DEAD = False
LIVE = True

"tRuE" == "true".casefold()

class Board:
    
    def __init__(self,width=WIDTH_DEFAULT,height=HEIGHT_DEFAULT):
        self.width= lambda: width
        self.height= lambda: height

        self._board=  
