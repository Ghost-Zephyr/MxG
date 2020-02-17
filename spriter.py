#!/usr/bin/env python3
try:
    import pygame
    #from pygame.locals import *
    from msg import *
    from msg import sprite as nsprite
    from gfx import *
except ImportError as err:
    print(f'\nMissing module!\n{err}')
    exit()

loadSprites = [
    {
        's': flipper,
        'x': width/2,
        'y': 10
    },
    {
        's': bomber,
        'x': width-75,
        'y': 10
    }
]

sprites = []
explosions = []
for s in loadSprites:
    sprites.append(nsprite(
        s['s'], s['x'], s['y']
    ))
player = nsprite(player, width/2, height-75)
keys = utils.keys()

def update(sprites, events, player, score):
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
        if sprite.x < -50:
            sprite.x = 1024+50
        if sprite.x > 1024+50:
            sprite.x = -50
        if player.alive and player.hitbox.colliderect(sprite.hitbox):
            player = utils.die(player)
            sprites[sprites.index(sprite)] = utils.die(sprite)
        if sprite.explodeing:
            if sprite.iter > sprite.maxiter:
                sprites.remove(sprite)
    for projectile in player.projectiles:
        if projectile.y < 0:
            player.projectiles.remove(projectile)
        projectile.update(projectile)
        for sprite in sprites:
            if sprite.alive and projectile.hitbox.colliderect(sprite.hitbox):
                score += sprite.points
                sprites[sprites.index(sprite)] = utils.die(sprite)
    if player.explodeing:
        if player.iter > player.maxiter:
            player.explodeing = False
    if player.alive or player.explodeing:
        player.update(player, keys)
    return player, score

def draw(surface, sprites, player):
    for sprite in sprites:
        sprite.draw(surface)
    for projectile in player.projectiles:
        projectile.draw(surface)
    if player.alive or player.explodeing:
        player.draw(surface)
    else:
        utils.text('DED', surface,
            {'x':350, 'y':250}, (200, 200, 200), 48)

def main(player, score):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('MxG: Spriter')
    background = pygame.Surface(screen.get_size())
    surface = pygame.Surface(screen.get_size())
    background = surface.convert()
    surface = surface.convert()
    surface.fill((0, 0, 0))
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    try:
        clock = pygame.time.Clock()
        while 'testing sprites':
            clock.tick(120)
            background.fill((0, 0, 0))
            surface.fill((0, 0, 0))
            player, score = update(sprites, pygame.event.get(), player, score)
            drawbg(background, score)
            surface.blit(background, (0, 0))
            draw(surface, sprites, player)
            screen.blit(surface, (0, 0))
            pygame.display.flip()
    except KeyboardInterrupt:
        print('\nlol\nstopping spriter sprite tester')

if __name__ == '__main__':
    main(player, 0)

