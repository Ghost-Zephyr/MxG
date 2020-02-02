#!/usr/bin/env python3
try:
    import pygame
    #from pygame.locals import *
    from msg import *
    from gfx import *
except ImportError as err:
    print(f'\nMissing module!\n{err}')
    exit()

loadSprites = [
    {
        's': player,
        'x': width/2,
        'y': height-75
    }
]
sprites = []
for s in loadSprites:
    sprites.append(sprite(
        s['s'], s['x'], s['y']
    ))

keys = utils.keys()

def update(sprites, events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    keys.update(events)
    for sprite in sprites:
        sprite.update(sprite, keys)

def draw(surface, sprites):
    for sprite in sprites:
        sprite.draw(surface)

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('MxG: Spriter')
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    surface.fill((0, 0, 0))
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    try:
        clock = pygame.time.Clock()
        while 'testing sprites':
            clock.tick(60)
            surface.fill((0, 0, 0))
            update(sprites, pygame.event.get())
            draw(surface, sprites)
            screen.blit(surface, (0, 0))
            pygame.display.flip()
    except KeyboardInterrupt:
        print('\nlol\nstopping spriter sprite tester')

if __name__ == '__main__':
    main()

