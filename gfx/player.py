from .projectiles import *
import msg

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
    def init(player):
        player.xdelta = 0
        player.lastshot = 0
        player.shotiter = 0
        player.speediter = 0
        #player.leftpadding = 0
        #player.rightpadding = 0
        #player.lastpoly = player.polygons
    def update(player, keys):
        if player.alive:
            startdelta = player.xdelta
            for key in keys.down:
                if key in ('a', 'left') and player.xdelta > -4:
                    player.xdelta += -1
                elif key in ('d', 'right') and player.xdelta < 4:
                    player.xdelta += 1
                if 'space' in key and player.shotiter == 0:
                    if player.lastshot == 0:
                        x = player.x - 43
                        player.lastshot = 1
                    else:
                        x = player.x + 43
                        player.lastshot = 0
                    player.projectiles.append(
                        msg.projectile(laser, x, player.y-28))
                    player.shotiter = 1
            if player.xdelta == startdelta and player.speediter > 6:
                if player.xdelta < 0:
                    player.xdelta += 1
                if player.xdelta > 0:
                    player.xdelta += -1
                player.speediter = 0
            player.speediter += 1
            if player.shotiter > 0:
                player.shotiter += 1
                if player.shotiter > 40:
                    player.shotiter = 0
            if player.x < -50:
                player.x = 1024+50
            if player.x > 1024+50:
                player.x = -50
            player.x += player.xdelta

