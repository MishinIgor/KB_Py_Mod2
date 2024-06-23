import pygame
import random

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# цвета окружностей
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

# цвет, скорость, начальная позиция окружности
circle_radius = 30
circle_speed = 3
circle_color = random.choice([red, green, blue, yellow, white])
circle_pos = [screen_width//2, -circle_radius]
circle_landed = False

# список приземлившихся окружностей и их позиций
landed_circles = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # если окружность не приземлилась
    if not circle_landed:
        # меняем направление по нажатию клавиши
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            circle_pos[0] -= circle_speed
        if keys[pygame.K_RIGHT]:
            circle_pos[0] += circle_speed

        # проверяем, столкнулась ли окружность с другой приземлившейся окружностью
        for landed_circle in landed_circles:
            landed_rect = pygame.Rect(landed_circle[0]-circle_radius, landed_circle[1]-circle_radius, circle_radius*2, circle_radius*2)
            falling_rect = pygame.Rect(circle_pos[0]-circle_radius, circle_pos[1]-circle_radius, circle_radius*2, circle_radius*2)
            if landed_rect.colliderect(falling_rect):
                circle_landed = True
                collision_x = circle_pos[0]
                collision_y = landed_circle[1] - circle_radius*2
                landed_circles.append((collision_x, collision_y, circle_color))
                break

        # если окружность не столкнулась с другой приземлившейся окружностью
        if not circle_landed:
            # окружность движется вниз
            circle_pos[1] += circle_speed

            # проверяем, достигла ли окружность дна
            if circle_pos[1] + circle_radius > screen_height:
                circle_pos[1] = screen_height - circle_radius
                circle_landed = True
                # добавляем окружность и ее позицию в список приземлившихся окружностей
                landed_circles.append((circle_pos[0], circle_pos[1], circle_color))

    if circle_landed:
        # если окружность приземлилась, задаем параметры новой
        circle_pos = [screen_width//2, -circle_radius]
        circle_color = random.choice([red, green, blue, yellow, white])
        circle_landed = False

    # рисуем окружности
    screen.fill(black)
    for landed_circle in landed_circles:
        pygame.draw.circle(screen, landed_circle[2], (landed_circle[0], landed_circle[1]), circle_radius)
    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
    pygame.display.update()

    # частота обновления экрана
    pygame.time.Clock().tick(60)