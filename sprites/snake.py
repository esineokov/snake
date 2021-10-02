import operator
import random

import pygame

from constant import HEIGHT, WIDTH, DIRECTION_RIGHT
from constant.color import GREEN, WHITE


class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super(Snake, self).__init__()
        self.size = 50
        self.width = self.height = self.size

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.direction = DIRECTION_RIGHT

    def update(self, *args, **kwargs) -> None:
        next_x = self.rect.x + self.direction[0] * self.size
        next_y = self.rect.y + self.direction[1] * self.size

        if next_x > WIDTH:
            next_x = 0
        elif next_x < 0:
            next_x = WIDTH - self.width
        else:
            next_x = self.rect.x + self.direction[0] * self.size

        if next_y > HEIGHT:
            next_y = 0
        elif next_y < 0:
            next_y = HEIGHT - self.height
        else:
            next_y = self.rect.y + self.direction[1] * self.size

        self.rect.x = next_x
        self.rect.y = next_y
