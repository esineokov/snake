import os

import pygame

from constant import WIDTH, HEIGHT
from constant.color import BLACK


class Fruit(pygame.sprite.Sprite):

    def __init__(self):
        super(Fruit, self).__init__()
        self.size = 50
        self.width = self.height = self.size

        # image_object = pygame.image.load(os.path.join('./img/' 'fruits.png')).convert_alpha()
        # image_object = pygame.transform.scale(image_object, (self.width*10, self.height*10))
        #
        # self.image = pygame.Surface((self.width, self.height))
        # self.image.blit(image_object, (0, 0), (60, 0, 50, 50))
        # self.image.set_colorkey(BLACK)
        # self.rect = self.image.get_rect()
        # self.rect.x, self.rect.y = 0, 0

        image_object = pygame.image.load(os.path.join('./img/' 'banana.png')).convert_alpha()
        image_object = pygame.transform.scale(image_object, (self.width, self.height))

        self.image = pygame.Surface((self.width, self.height))
        self.image.blit(image_object, (0, 0))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
