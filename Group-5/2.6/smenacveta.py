# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 300
HEIGHT = 300
FPS = 30
# Задаем цвета
COLOR_LIST = [
(255, 255, 255), #WHITE
(0, 0, 0), #BLACK
(255, 0, 0), #RED
(0, 255, 0), #GREEN
(0, 0, 255) #BLUE
]
current_color_index = 3
# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Изменить цвето фона")
background = pygame.Surface((WIDTH,HEIGHT))
background.fill(pygame.Color(COLOR_LIST[current_color_index]))

button_font = pygame.font.SysFont('Verdana',15) #используем шрифт Verbana
button_text_color = pygame.Color('black')
button_rect = pygame.Rect(100,115,100,50)
button_color = pygame.Color('gray')
button_text = button_font.render('Смена', True, button_color)

clock = pygame.time.Clock()

# Цикл игры
running = True
while running:
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                current_color_index = random.randint(0,4)
                background.fill(COLOR_LIST[current_color_index])
    # Держим цикл на правильной скорости
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen,button_color,button_rect)
    button_rect_center = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text,button_rect_center)
    pygame.display.update()
    # Ввод процесса (события)
    



pygame.quit()
