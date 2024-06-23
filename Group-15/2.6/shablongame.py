#Pygame шаблон - скелет для нового проекта Pygame
import pygame

WIDTH = 360 # Ширина игрового окна
HEIGHT = 480 # Высота игрового окна
FPS = 30 # частота кадров в секунду
COLOR_LIST = {
# Цвета (R, G, B)  
"чёрный":(0, 0, 0),
"белый":(255, 255, 255), 
"красный":(255, 0, 0), 
"зелёный":(0, 255, 0), 
"синий":(0, 0, 255),
"мокрый асфальт":(96,96,96), 
"изумрудный":(80,200,120) 
}
#Создаём игру и окно
pygame.init() # запускает Pygame
pygame.mixer.init() # для звука
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # окно программы размером WIDTHxHEIGHT
pygame.display.set_caption('Моя игра')
clock = pygame.time.Clock() # Контроллер частоты кадров
# после отрисовки всего, переворачиваем экран



#Цикл игры
running = True

while running:
    # Ввод процесса
    for event in pygame.event.get():
       # проверить закрытие окна
       if event.type == pygame.QUIT:
           running = False
    # Обновление
    clock.tick(FPS)
    # Визуализация
    screen.fill(COLOR_LIST["зелёный"])
    pygame.display.flip()

pygame.quit()

