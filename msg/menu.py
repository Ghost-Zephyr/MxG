from pygame import *
from . import utils

class menu(object):
    def __init__(self, title, entries, order, activeEntry, active=True):
        self.title = title
        self.active = active
        self.entry = order[activeEntry]
        self.order = order
        self.entries = entries

    def draw(self, surface, whc):
        utils.text(self.title, surface, {'x':whc[0],'y':175}, (225, 75, 225), 60)
        for entry in self.entries:
            color = (200, 200, 200)
            if entry == self.entry:
                color = (200, 50, 200)
            utils.text(entry, surface, {
                    'x': whc[0],
                    'y': whc[1]-self.entries[entry]['heightdelta']
                },
                color,
                self.entries[entry]['size'])

    def events(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if key.name(event.key) in ('return', 'space'):
                    self.entries[self.entry]['func'](self.entries[self.entry]['args'])

                elif key.name(event.key) in ('up', 'w'):
                    try: self.entry = self.order[self.order.index(self.entry)+1]
                    except IndexError: self.entry = self.order[0]
                elif key.name(event.key) in ('down', 's', 'tab'):
                    try: self.entry = self.order[self.order.index(self.entry)-1]
                    except IndexError: self.entry = self.order[len(self.order)]

