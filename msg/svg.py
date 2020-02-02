from random import randint, uniform
from math import floor, pi
from .menu import menu
from .utils import *
from gfx import *
import pygame

class SVG:
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

    def eventsUpdatesAndDraw(self, surface, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if not self.mainMenu.active and event.key == pygame.K_ESCAPE:
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
            if sprite.alive:
                sprite.update(sprite)
                if sprite.y > 768:
                    sprite.y = 0
                if self.player.alive and self.player.hitbox.colliderect(sprite.hitbox):
                    self.player = die(self.player)
                    sprite = die(sprite)
            elif len(sprite.projectiles) == 0 and sprite.iter > 180:
                self.sprites.remove(sprite)
        if self.player.alive:
            self.player.update(self.player, self.keys, self.sprites)

class drawable:
    def init(self, sprite, x, y):
        self.__name__ = sprite.__name__
        self.polygons = []
        self.colors = []
        self.sizes = []
        for poly in sprite.template:
            self.polygons.append(poly['points'])
            self.colors.append(poly['color'])
            self.sizes.append(poly['size'])
        self.alive = True
        self.update = sprite.update
        self.hitbox = pygame.Rect((0,0),(0,0))
        self.x = x
        self.y = y

    def draw(self, surface):
        if self.alive:
            for i in range(len(self.polygons)):
                polygon = []
                for point in self.polygons[i]:
                    polygon.append((self.x+point[0], self.y+point[1]))
                if i == 0: # TODO: Doing; REKT
                    rect = pygame.draw.polygon(surface, self.colors[i],
                        polygon, self.sizes[i])
                    self.hitbox = rect
                else:
                    pygame.draw.polygon(surface, self.colors[i],
                        polygon, self.sizes[i])

class sprite(drawable):
    def __init__(self, sprite, x, y):
        self.init(sprite, x, y)
        if not sprite.__name__ == 'player':
            self.startx = x
            self.starty = y
            self.deltax = 0
            self.deltay = 0
            sprite.init(self)
        self.projectiles = []

class projectile(drawable):
    def __init__(self, sprite, x, y):
        self.init(sprite, x, y)

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

