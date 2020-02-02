#!/usr/bin/env python3
from msg import *
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
        's': flipper,
        'x': width/2,
        'y': 10
    }
]

sprites = []
for s in loadSprites:
    sprites.append(sprite(
        s['s'], s['x'], s['y']
    ))
player = sprite(player, width/2, height-75)

keys = utils.keys()

def update(sprites, events, player):
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
        sprite.update(sprite)
        if sprite.y > 768:
            sprite.y = 0
        if player.alive and player.hitbox.colliderect(sprite.hitbox):
            player = utils.die(player)
            sprite = utils.die(sprite)
    player.update(player, keys)
    return player

def draw(surface, sprites):
    for sprite in sprites:
        sprite.draw(surface)
    player.draw(surface)

def main(player):
    pygame.init()
    pygame.mouse.set_visible(False)
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
            clock.tick(120)
            surface.fill((0, 0, 0))
            player = update(sprites, pygame.event.get(), player)
            draw(surface, sprites)
            screen.blit(surface, (0, 0))
            pygame.display.flip()
    except KeyboardInterrupt:
        print('\nlol\nstopping spriter sprite tester')

if __name__ == '__main__':
    main(player)

