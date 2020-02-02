from .svg import sprite
from gfx import explosion
import pygame

width, height = 1024, 768

def text(msg, surface, centerpos, color=(250, 250, 250), size=24, font=None):
    font = pygame.font.Font(font, size)
    text = font.render(msg, 1, color)
    textpos = text.get_rect()
    textpos.centerx = centerpos['x']
    textpos.centery = centerpos['y']
    surface.blit(text, textpos)

def die(dead):
    return sprite(explosion, dead.x, dead.y)

class keys(object):
    def __init__(self):
        self.down = []
    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_TAB, 308): # 308 = left alt, for allowing alt tab
                    return
                self.down.append(pygame.key.name(event.key))
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_TAB, 308):
                    return
                self.down.remove(pygame.key.name(event.key))

