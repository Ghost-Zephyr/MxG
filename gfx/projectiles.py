
class laser:
    template = [{
        'color': (221, 37, 59),
        'size': 3,
        'points': [ # Red laser
            (0,0),(0,1)
        ]
    }]
    def init(laser):
        return
    def update(laser):
        if laser.polygons[0][1][1] < 20:
            laser.polygons[0][1] = (0,
                laser.polygons[0][1][1]+1)
        laser.y -= 3

class bomb:
    template = [{
        'color': (175, 21, 49),
        'size': 3,
        'points': [ # Red bomb
            (0,0),
            (5,5),
            (0,10),
            (-5,5)
        ]
    }]
    def init(bomb):
        bomb.ydelta = 0
    def update(bomb):
        bomb.ydelta += 2
        bomb.y += 2

class shrapnel:
    template = [{
        'color': (175, 21, 49),
        'size': 3,
        'points': [ # Red shrapnel
            (0,0),
            (5,5),
            (0,10),
            (-5,5)
        ]
    }]
    def init(shrapnel, i):
        shrapnel.iter = 0
        if i == 0:
            x, y = 0.75, 0.75
        elif i == 1:
            x, y = 0, 1
        elif i == 2:
            x, y = -0.75, 0.75
        elif i == 3:
            x, y = -1, 0
        elif i == 4:
            x, y = -0.75, -0.75
        elif i == 5:
            x, y = 0, -1
        elif i == 6:
            x, y = 0.75, -0.75
        elif i == 7:
            x, y = 1, 0
        shrapnel.xdelta = x
        shrapnel.ydelta = y
    def update(shrapnel):
        shrapnel.iter += 1
        shrapnel.x += shrapnel.xdelta
        shrapnel.y += shrapnel.ydelta

