#Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import math

WIDTH = 800 # Ширина игрового окна
HEIGHT = 800 # Высота игрового окна
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
keycolor = random.choice(list(COLOR_LIST.keys()))
randcolor = COLOR_LIST[keycolor]
#Создаём игру и окно
pygame.init() # запускает Pygame
pygame.mixer.init() # для звука
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # окно программы размером WIDTHxHEIGHT
pygame.display.set_caption('Графические фигуры')
clock = pygame.time.Clock() # Контроллер частоты кадров
# после отрисовки всего, переворачиваем экран


# рисуем прямоугольник рандомного цвета
rect_x = 50
rect_y = 50
rect_width = 100
rect_height = 50
pygame.draw.rect(screen, randcolor, (rect_x, rect_y, rect_width, rect_height))

# рисуем круг
circle_x = 200
circle_y = 75
circle_radius = 30
pygame.draw.circle(screen, randcolor, (circle_x, circle_y), circle_radius)

# рисуем треугольник
triangle_x = 350
triangle_y = 50
triangle_width = 100
triangle_height = 100
triangle_points = [(triangle_x, triangle_y), (triangle_x + triangle_width, triangle_y),
                   (triangle_x + triangle_width / 2, triangle_y + triangle_height)]
pygame.draw.polygon(screen, randcolor, triangle_points)

# рисуем пятиугольник
pent_x = 500
pent_y = 100
radius = 40
sides = 5
pent_points = []
for i in range(sides):
    angle_deg = 360 * i / sides
    angle_rad = math.radians(angle_deg)
    x = pent_x + radius * math.sin(angle_rad)
    y = pent_y - radius * math.cos(angle_rad)
    pent_points.append((x, y))
pygame.draw.polygon(screen, randcolor, pent_points)

# вертикальная линия
vert_line_x = 320
pygame.draw.line(screen, (0,255,0), (vert_line_x, 50), (vert_line_x, 430), 5)

# рисуем желтую звезду
yellow_star_points = [(260 - 50, 250 - 70), (310 - 50, 250 - 70), (325 - 50, 200 - 70),
                      (340 - 50, 250 - 70), (390 - 50, 250 - 70), (350 - 50, 290 - 70),
                      (365 - 50, 340 - 70), (325 - 50, 305 - 70), (285 - 50, 340 - 70),
                      (300 - 50, 290 - 70)]
pygame.draw.polygon(screen, (255,255,0), yellow_star_points)

# рисуем окружность с квадратом внутри
circle2_x = 490
circle2_y = 350
circle2_radius = 80
pygame.draw.circle(screen, (0,255,0), (circle2_x, circle2_y), circle2_radius)
square_side = 60
square_x = circle2_x - square_side / 2
square_y = circle2_y - square_side / 2
pygame.draw.rect(screen, (255,0,0), (square_x, square_y, square_side, square_side))

pygame.display.update()

#Цикл игры
running = True

while running:
    # Ввод процесса
    for event in pygame.event.get():
       # проверить закрытие окна
       if event.type == pygame.QUIT:
           running = False

pygame.quit()

