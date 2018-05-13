# Live with < 2 : die
# Live with 2 or 3 : live
# Dead with == 3 : live
# Live with > 3 : die

from random import randint

class Mundo:
    MINIMOS_XY = 0
    MAXIMOS_XY = 40

    def __init__(self, maximos_cuadro=200, porcentaje=0.1):
        self.lienzo = {}
        self.maximos_cuadro = maximos_cuadro
        self.porcentaje = porcentaje

    def populate(self):
        # add some Cuadros to lienzo
        numero_de_cuadros = self.maximos_cuadro * self.porcentaje
        for i in range(numero_de_cuadros):
            locacion = (randint(MINIMOS_XY, MAXIMOS_XY), randint(MINIMOS_XY, MAXIMOS_XY))
            self.lienzo[locacion] = Cuadro(cumpleanos=i)



class Cuadro:
    pass
