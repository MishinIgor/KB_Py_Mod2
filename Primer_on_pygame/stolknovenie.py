import pygame
import math

pygame.init()
screen_width = 400
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Драматическое столкновение")

# размеры и позиция окружности
circle_pos = [screen_width/2, 50]
circle_radius = 20

# размеры и позиция прямоугольника
rect_pos = [screen_width/2, screen_height-50]
rect_width = 100
rect_height = 50

# цвета окружности и прямоугольника
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# скорость движения окружности
speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # окружность движется вниз
    circle_pos[1] += speed

    # проверяем (используя формулу расстояния),
    # столкнулась ли окружность с прямоугольником
    circle_x = circle_pos[0]
    circle_y = circle_pos[1]
    rect_x = rect_pos[0]
    rect_y = rect_pos[1]
    distance_x = abs(circle_x - rect_x)
    distance_y = abs(circle_y - rect_y)
    if distance_x <= (rect_width/2 + circle_radius) and distance_y <= (rect_height/2 + circle_radius):
        circle_color = red # изменяем цвет фигур
        rect_color = green # в момент столкновения
    else:
        circle_color = green
        rect_color = black

    # рисуем окружность и прямоугольник на экране
    screen.fill(white)
    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
    pygame.draw.rect(screen, rect_color, (rect_pos[0]-rect_width/2, rect_pos[1]-rect_height/2, rect_width, rect_height))

    pygame.display.update()

    # останавливаем движение окружности, если она
    # столкнулась с прямоугольником
    if circle_pos[1] + circle_radius >= rect_pos[1] - rect_height/2:
        speed = 0

    # задаем частоту обновления экрана
    pygame.time.Clock().tick(60)