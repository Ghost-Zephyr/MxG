from random import randint

oneposorneg = lambda x: 1 if x == 1 else -1

class explosion:
    template = [{
        'color': (225, 201, 41),
        'size': 1,
        'points': [
            (0,0),
            (3,3),
            (0,6),
            (-3,3)
        ]
    }]
    def init(exp):
        exp.alive = False
        exp.explodeing = True
        exp.maxiter = 200
        n = randint(4,7)
        for i in range(n):
            size = randint(1,3)
            npoly = []
            offsetx = randint(-25,25)
            offsety = randint(-25,25)
            for point in exp.polygons[0]:
                npoly.append((point[0]+offsetx, point[1]+offsety))
            exp.addpoly(npoly, exp.colors[0], size)
    def update(exp, *args):
        n = len(exp.polygons)
        for i in range(n):
            col = exp.colors[i]
            exp.colors[i] = (col[0]-1, col[1]-1, col[2])
            exp.iter += 1

class flipper:
    template = [{
        #'color': (79, 2, 137), (239, 31, 211)
        'color': (250,0,250),
        'size': 2,
        'points': [
                (0,0),
                (20,20),
                (-20,20)
        ]
    }]
    def init(flipper):
        flipper.points = 1
        flipper.deltax = 1
    def update(flipper):
        if flipper.x > flipper.startx-50:
            if flipper.deltax > -10:
                flipper.deltax -= 1
        if flipper.x < flipper.startx+50:
            if flipper.deltax < 10:
                flipper.deltax += 1
        flipper.x += flipper.deltax
        flipper.y += 1

class bomber:
    template = [{
        'color': (250, 250, 250),
        'size': 2,
        'points': [
                (0,0),
                (20,20),
                (0,40),
                (-20,20)
        ]
    }]
    def init(bomber):
        bomber.points = 6
        bomber.deltax = oneposorneg(randint(0,1))*randint(1,2)
    def update(bomber):
        if randint(0,199) < 1:
            bomber.deltax = bomber.deltax*-1
        bomber.x += bomber.deltax
        bomber.y += 1

'''
class fighter:
    template = [{
        'color': (250, 250, 250),
        'size': 2,
        'points': [
                (,),
                (,),
                (,)
        ]
    }]
'''
