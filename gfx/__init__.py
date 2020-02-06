from .player import player
from .sprites import *

class explosion:
    template = [{
        'color': (250, 250, 250),
        'size': 2,
        'points': [
                (0,0),
                (10,10),
                (-10,10)
        ]
    }]
    def init(exp):
        exp.alive = False
        exp.explodeing = True
        exp.iter = 0
    def update(exp, *args):
        col = exp.colors[0]
        exp.colors[0] = (col[0]-1, col[1]-1, col[2]-1)
        exp.iter += 1

