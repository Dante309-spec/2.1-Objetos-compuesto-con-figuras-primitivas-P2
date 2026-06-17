from p5 import *
from classes.clases import *
import copy

class Ventana(Figura):

    def __init__(self, escala=1.0):
        self.escala = escala
        self.figuras: list[Figura] = []

        self.figuras.append(
            Cuadrado(
                borde_color="#000000", borde_grosor=2,
                width=50, height=60,
                x=0, y=0,
                relleno="#E0E30B"
            )
        )

        self.vidrio1 = Cuadrado(
            borde_color="#000000", borde_grosor=2,
            width=15, height=15,
            x=5, y=5,
            relleno="#45E30B"
        )
        self.figuras.append(
            Cuadrado(
                borde_color="#000000", borde_grosor=2,
                width=15, height=15,
                x=5, y=5,
                relleno="#45E30B"
            )
        )

        self.vidrio2 = copy.deepcopy(self.vidrio1)
        self.vidrio2.posicion.coord_x = 30
        self.vidrio2.posicion.coord_y = 5
        self.figuras.append(self.vidrio2)

        self.vidrio3 = copy.deepcopy(self.vidrio1)
        self.vidrio3.posicion.coord_x = 5
        self.vidrio3.posicion.coord_y = 30
        self.figuras.append(self.vidrio3)

        self.vidrio4 = copy.deepcopy(self.vidrio1)
        self.vidrio4.posicion.coord_x = 30
        self.vidrio4.posicion.coord_y = 30
        self.figuras.append(self.vidrio4)

        self.base = Cuadrado(
            borde_color="#000000", borde_grosor=2,
            width=50, height=10,
            x=0, y=50,
            relleno="#0BBFE3"
        )
        self.figuras.append(self.base)

    def dibujar(self):
        push_matrix()

        scale(self.escala)

        for figura in self.figuras:
            figura.dibujar()

        pop_matrix()