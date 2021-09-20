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

        self.last_coord = None
        self.save_last_coord()

    def update(self, *args, **kwargs) -> None:
        self.rect.x += 1
        if self.rect.left == WIDTH - self.width:
            self.rect.x = 0

    def save_last_coord(self):
        self.last_coord = (self.rect.x, self.rect.y)

    def is_border(self):
        return self.rect.x == 0 or self.rect.y == 0 or self.rect.x == WIDTH - self.width or
