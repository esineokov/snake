import pygame

from constant import WIDTH, HEIGHT, FPS, DIRECTION_UP, DIRECTION_DOWN, DIRECTION_LEFT, DIRECTION_RIGHT
from constant.color import BLACK
from sprites.fruit import Fruit
from sprites.snake import Snake

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake - SsSsSsss....')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Snake()
fruit = Fruit()
all_sprites.add(player)
all_sprites.add(fruit)

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Если нажата клаивша
        if event.type == pygame.KEYDOWN:

            # Какая клавиша нажата. Меняем направление
            if event.key == pygame.K_DOWN:
                player.direction = DIRECTION_DOWN
            if event.key == pygame.K_UP:
                player.direction = DIRECTION_UP
            if event.key == pygame.K_LEFT:
                player.direction = DIRECTION_LEFT
            if event.key == pygame.K_RIGHT:
                player.direction = DIRECTION_RIGHT

    # Обновление спрайтов
    all_sprites.update()

    # Отрисовка
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

