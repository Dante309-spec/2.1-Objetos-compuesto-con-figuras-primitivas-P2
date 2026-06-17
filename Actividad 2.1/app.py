from p5 import *
from classes.clases import *
from models.models import Ventana

MAX_WIDTH = 800
MAX_HEIGHT = 700
ventana1 = None

def setup():
    global ventana1
    size(MAX_WIDTH, MAX_HEIGHT)
    ventana1 = Ventana(1.0)

def draw():
    background(220)
    ventana1.dibujar()

run()