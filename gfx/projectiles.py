
class laser:
    template = [{
        'color': (221, 37, 59),
        'size': 3,
        'points': [ # Red laser
            (0,0),(0,1)
        ]
    }]
    def update(laser):
        if laser.polygons[0][1][1] < 20:
            laser.polygons[0][1] = (0,
                laser.polygons[0][1][1]+1)
        laser.y -= 3

