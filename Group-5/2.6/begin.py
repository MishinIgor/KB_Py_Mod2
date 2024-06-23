# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 400
HEIGHT = 400
FPS = 30
# Задаем цвета
COLOR_LIST = [
(255, 255, 255), #WHITE
(0, 0, 0), #BLACK
(255, 0, 0), #RED
(0, 255, 0), #GREEN
(0, 0, 255) #BLUE
]

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Изменить цвето фона")
background = pygame.Surface((WIDTH,HEIGHT))
background.fill(pygame.Color(COLOR_LIST[0]))
clock = pygame.time.Clock()

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False



pygame.quit()
