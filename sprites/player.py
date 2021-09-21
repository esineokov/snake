import collections

import pygame

from constant import HEIGHT, WIDTH
from constant.color import GREEN


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.width = self.height = 50

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

        self.coord_history  = collections.deque(maxlen=2)
        self.save_last_coord()

    def update(self, *args, **kwargs) -> None:
        if not self.coord_history:
            self.rect.x += 1

        # if self.is_border():
        #     # сменить направление
        # else:
        #
        #
        # self.save_last_coord()
        # self.rect.x += 1
        # if self.is_border():
        #     test = 1

    def save_last_coord(self):
        self.coord_history.append((self.rect.x, self.rect.y))

    def is_border(self):
        return (0 in (self.rect.x, self.rect.y)
                or self.rect.x == WIDTH - self.width
                or self.rect.y == HEIGHT - self.height)

    def is_direct_direction(self):

