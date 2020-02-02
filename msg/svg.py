from random import randint, uniform
from math import floor, pi
from .menu import menu
from .sprites import *
from .utils import *
import pygame

class SVG(object):
    def __init__(self):
        self.keys = keys()
        self.mainMenu = menu({
            'Start': {
                'heightdelta': 25,
                'size': 48,
                'args': '',
                'func': self.start
            },
            'Quit': {
                'heightdelta': -25,
                'size': 48,
                'args': pygame.event.Event(pygame.QUIT),
                'func': pygame.event.post
            }
        }, ['Start', 'Quit'], 0)
        self.started = False
        self.player = sprite(player, width/2, height-75)
        self.sprites = []

    def start(self):
        if not self.started:
            entry = self.mainMenu.entries.pop('Start')
            self.mainMenu.order.remove('Start')
            self.mainMenu.entries['Continue'] = entry
            self.mainMenu.order.insert(0, 'Continue')
            self.mainMenu.entry = 'Continue'
            self.started = True
        self.mainMenu.active = False

    def eventsAndDraw(self, surface, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.mainMenu.active:
                        pygame.quit()
                        exit()
                    else:
                        self.mainMenu.active = True
        self.keys.update(events)

        if self.mainMenu.active:
            self.mainMenu.events(events)
            text('MxG, not TxK', surface, {'x':width/2,'y':175}, (225, 75, 225), 60)
            self.mainMenu.draw(surface, (width/2, height/2))
        else:
            self.update(self.keys)
            self.draw(surface)

    def draw(self, surface):
        for sprite in self.sprites:
            sprite.draw(surface)
        self.player.draw(surface)

    def update(self, keys):
        for sprite in self.sprites:
            sprite.update(sprite)
        self.player.update(self.player, keys)

class sprite(object):
    def __init__(self, sprite, x, y):
        self.polygons = []
        self.colors = []
        self.sizes = []
        for poly in sprite.template:
            self.polygons.append(poly['points'])
            self.colors.append(poly['color'])
            self.sizes.append(poly['size'])
        self.alive = True
        self.update = sprite.update
        self.x = x
        self.y = y

    def draw(self, surface):
        if self.alive:
            for i in range(len(self.polygons)):
                polygon = []
                for point in self.polygons[i]:
                    polygon.append((self.x+point[0], self.y+point[1]))
                pygame.draw.polygon(surface, self.colors[i],
                    polygon, self.sizes[i])

# --- Fun ---
rndcolor = lambda rgb: (
    randint(rgb['rm'], rgb['rx']),
    randint(rgb['gm'], rgb['gx']),
    randint(rgb['bm'], rgb['bx'])
)

def loadingarchs(surface):
    rndcolordat = {
        'rm': 125, 'rx': 175,
        'gm': 75, 'gx': 150,
        'bm': 125, 'bx': 175
    }
    arcrectgen = lambda: [
        randint(floor(width/10), floor(width/6)),
        randint(floor(height/10), floor(height/6)),
        randint(floor(width/1.5), floor(width-width/4)),
        randint(floor(height/1.5), floor(height-height/4))
    ]
    rndarcangles = lambda: (uniform(pi/2, pi), uniform(pi/2, pi))

    for _ in range(13):
        rekt = arcrectgen()
        sangle, eangle = rndarcangles()
        pygame.draw.arc(surface, rndcolor(rndcolordat), rekt, sangle, eangle)
        sangle, eangle = rndarcangles()
        pygame.draw.arc(surface, rndcolor(rndcolordat), rekt, sangle, eangle)

