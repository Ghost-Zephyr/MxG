#!/usr/bin/env python3
try:
    import pygame
    import msg
except ImportError as err:
    print(f'\nMissing module!\n{err}')
    exit()

def main():
    # Init
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((msg.width, msg.height))
    pygame.display.set_caption('MxG: Mæhd Space Game, not TxK')
    # Fyll bakgrunn og lag overflater
    background = pygame.Surface(screen.get_size())
    surface = pygame.Surface(screen.get_size())
    background = surface.convert()
    surface = surface.convert()
    surface.fill((0, 0, 0))
    msg.loadingarchs(surface)
    msg.text('MxG', surface, {'x':msg.width/2,'y':msg.height/2}, (175, 75, 175), 60)
    # Sett alt sammen for tegning til bildet
    screen.blit(surface, (0, 0))
    pygame.display.flip()
    # Spill loop
    try:
        game = msg.SVG()
        #msg.init()
        clock = pygame.time.Clock()
        while 'spillet er bra':
            clock.tick(120)
            #background.fill((0, 0, 0))
            surface.fill((0, 0, 0))
            game.eventsUpdatesAndDraw(surface, pygame.event.get())
            if game.started:
                msg.drawbg(surface, game.score)
            #background.blit(surface, (0, 0))
            screen.blit(surface, (0, 0))
            pygame.display.flip()
    except KeyboardInterrupt:
        print('\nlol\nsoft exit on keyboard interrupt')

if __name__ == '__main__':
    main()

