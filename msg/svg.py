from random import randint, uniform
from math import floor, pi
from .menu import menu
from . import utils
from gfx import *
import pygame

width, height = 1024, 768

class SVG:
    def __init__(self):
        self.keys = utils.keys()
        self.mainMenu = menu('MxG, not TxK', {
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
        self.score = 0
        self.explosions = []
        self.sprites = []

    def start(self, *args):
        if not self.started:
            entry = self.mainMenu.entries.pop('Start')
            self.mainMenu.order.remove('Start')
            self.mainMenu.entries['Continue'] = entry
            self.mainMenu.order.insert(0, 'Continue')
            self.mainMenu.entry = 'Continue'
            self.started = True
        self.mainMenu.active = False

    def restart(self, *args):
        keys = self.keys
        self.__init__()
        self.keys = keys
        self.start()

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
            self.mainMenu.draw(surface, (width/2, height/2))
        else:
            self.update(self.keys)
            self.draw(surface)

    def draw(self, surface):
        for sprite in self.sprites:
            sprite.draw(surface)
        for projectile in self.player.projectiles:
            projectile.draw(surface)
        if self.player.alive or self.player.explodeing:
            self.player.draw(surface)
        else:
            self.mainMenu = menu('Game Over', {
                'Restart': {
                    'heightdelta': 25,
                    'size': 48,
                    'args': '',
                    'func': self.restart
                },
                'Quit': {
                    'heightdelta': -25,
                    'size': 48,
                    'args': pygame.event.Event(pygame.QUIT),
                    'func': pygame.event.post
                }
            }, ['Restart', 'Quit'], 0)

    def update(self, keys):
        self.spawner()
        for sprite in self.sprites:
            sprite.update(sprite)
            if sprite.y > 768:
                sprite.y = 0
            if sprite.x < -50:
                sprite.x = 1024+50
            if sprite.x > 1024+50:
                sprite.x = -50
            if self.player.alive and sprite.hitbox.colliderect(self.player.hitbox):
                self.player = utils.die(self.player)
                self.sprites[self.sprites.index(sprite)] = utils.die(sprite)
            if sprite.explodeing:
                if sprite.iter > sprite.maxiter:
                    self.sprites.remove(sprite)
        for projectile in self.player.projectiles:
            if projectile.y < 0:
                self.player.projectiles.remove(projectile)
            projectile.update(projectile)
            for sprite in self.sprites:
                if sprite.alive and projectile.hitbox.colliderect(sprite.hitbox):
                    self.sprites[self.sprites.index(sprite)] = utils.die(sprite)
                    self.score += sprite.points
        if self.player.explodeing:
            if self.player.iter > self.player.maxiter:
                self.player.explodeing = False
        if self.player.alive or self.player.explodeing:
            self.player.update(self.player, self.keys)

    def spawner(self):
        chance = 100
        if len(self.sprites) > 0:
            chance = floor(
                100 / len(self.sprites*3)
            )-1
        if randint(0,99) < chance:
            self.sprites.append(sprite(bomber, randint(0, width), 0))

class drawable:
    def init(self, sprite, x, y, kwargs):
        self.__name__ = sprite.__name__
        self.polygons = []
        self.colors = []
        self.sizes = []
        for poly in sprite.template:
            self.polygons.append(poly['points'])
            self.colors.append(poly['color'])
            self.sizes.append(poly['size'])
        self.alive = True
        self.explodeing = False
        self.update = sprite.update
        try:
            self.hitbox = kwargs['oldhitbox']
            self.projectiles = kwargs['projectiles']
            self.maxiter = 249
            self.iter = 0
        except:
            self.hitbox = pygame.Rect((0,0),(0,0))
        self.x = x
        self.y = y

    def addpoly(self, points, color=(250,250,250), size=2):
        self.polygons.append(points)
        self.colors.append(color)
        self.sizes.append(size)

    def draw(self, surface):
        for i in range(len(self.polygons)):
            polygon = []
            for point in self.polygons[i]:
                polygon.append((self.x+point[0], self.y+point[1]))
            if i == 0:
                self.hitbox = pygame.draw.polygon(surface, self.colors[i],
                    polygon, self.sizes[i]) # Function returns pygame Rect
            else:
                pygame.draw.polygon(surface, self.colors[i],
                    polygon, self.sizes[i])

class sprite(drawable):
    def __init__(self, sprite, x, y, **kwargs):
        self.init(sprite, x, y, kwargs)
        if not sprite.__name__ == 'player':
            self.startx = x
            self.starty = y
            self.deltax = 0
            self.deltay = 0
        sprite.init(self)
        if len(kwargs) < 1:
            self.projectiles = []

class projectile(drawable):
    def __init__(self, sprite, x, y):
        self.init(sprite, x, y, {})

# --- Fun stuff ---
def drawbg(surface, score):
    pygame.draw.polygon(surface, (250,250,250),
        [(100,100),(50,150),(100,200),(150,150)], 2)

    utils.text(f'Score: {score}', surface,
        {'x':100,'y':45}, (225, 75, 225), 48)

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
    width, height = 1024, 768
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

