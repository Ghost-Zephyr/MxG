
class flipper:
    template = [{
        #'color': (79, 2, 137),
        'color': (250,0,250),
        'size': 2,
        'points': [
                (0,0),
                (20,20),
                (-20,20)
        ]
    }]
    def init(flipper):
        flipper.deltax = 1
    def update(flipper):
        flipper.y += 1
        if flipper.x > flipper.startx-50:
            if flipper.deltax > -10:
                flipper.deltax -= 1
        if flipper.x < flipper.startx+50:
            if flipper.deltax < 10:
                flipper.deltax += 1
        flipper.x += flipper.deltax


''',{
        'color': (239, 31, 211),
        'size': 2,
        'points': [
                (,),
                (,),
                (,)
        ]
    }'''

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

class bomber:
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
