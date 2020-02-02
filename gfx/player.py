
class player:
    template = [{
        'color': (228, 234, 51),
        'size': 2,
        'points': [ # Yellow body
            (0,20),
            (-40,4),(-46,-16),(-36,-4),
            (0,4),
            (36,-4),(46,-16),(40,4)
        ]
    },{
        'color': (221, 59, 37),
        'size': 2,
        'points': [ # Red outline
            (0,25),
            (-43,7),(-53,-28),(-34,-7),
            (0,0),
            (34,-7),(53,-28),(43,7)
        ]
    }]
    def update(player, keys):
        if player.alive:
            xdelta = 0
            for key in keys.down:
                if key in ('a', 'left'):
                    if player.x > 0:
                        xdelta = -3
                if key in ('d', 'right'):
                    if player.x < 1024:
                        xdelta = 3
            player.x += xdelta

