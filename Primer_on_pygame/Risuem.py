import pygame
import math

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Геометрические фигуры")

#Описываем цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
pink = (255, 192, 203)

# рисуем прямоугольник
rect_x = 50
rect_y = 50
rect_width = 100
rect_height = 50
pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))

# рисуем круг
circle_x = 200
circle_y = 75
circle_radius = 30
pygame.draw.circle(screen, green, (circle_x, circle_y), circle_radius)

# рисуем треугольник
triangle_x = 350
triangle_y = 50
triangle_width = 100
triangle_height = 100
triangle_points = [(triangle_x, triangle_y), (triangle_x + triangle_width, triangle_y),
                   (triangle_x + triangle_width / 2, triangle_y + triangle_height)]
pygame.draw.polygon(screen, blue, triangle_points)

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
pygame.draw.polygon(screen, white, pent_points)

# рисуем эллипс
ellipse_x = 100
ellipse_y = 275
ellipse_width = 150
ellipse_height = 60
pygame.draw.ellipse(screen, red, (ellipse_x, ellipse_y, ellipse_width, ellipse_height))

# горизонтальная линия
horiz_line_y = 400
pygame.draw.line(screen, blue, (50, horiz_line_y), (590, horiz_line_y), 5)

# вертикальная линия
vert_line_x = 320
pygame.draw.line(screen, green, (vert_line_x, 50), (vert_line_x, 430), 5)

# рисуем желтую звезду
yellow_star_points = [(260 - 50, 250 - 70), (310 - 50, 250 - 70), (325 - 50, 200 - 70),
                      (340 - 50, 250 - 70), (390 - 50, 250 - 70), (350 - 50, 290 - 70),
                      (365 - 50, 340 - 70), (325 - 50, 305 - 70), (285 - 50, 340 - 70),
                      (300 - 50, 290 - 70)]
pygame.draw.polygon(screen, yellow, yellow_star_points)

# рисуем окружность с квадратом внутри
circle2_x = 490
circle2_y = 350
circle2_radius = 80
pygame.draw.circle(screen, white, (circle2_x, circle2_y), circle2_radius)
square_side = 60
square_x = circle2_x - square_side / 2
square_y = circle2_y - square_side / 2
pygame.draw.rect(screen, pink, (square_x, square_y, square_side, square_side))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()