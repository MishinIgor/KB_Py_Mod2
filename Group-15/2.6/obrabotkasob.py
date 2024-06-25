import pygame
import random
WINDOW_SIZE = (300,300)
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
pygame.init()
pygame.display.set_caption(f'Ваш фон: {keycolor}')
screen = pygame.display.set_mode(WINDOW_SIZE)
background = pygame.Surface(WINDOW_SIZE)
background.fill(pygame.Color(COLOR_LIST[keycolor]))

button_font = pygame.font.SysFont('Verdana',15) #используем шрифт Verdana и размер 15 для текста кнопки
button_text_color = pygame.Color(COLOR_LIST["мокрый асфальт"])
button_color = pygame.Color('gray')
button_rect = pygame.Rect(100,115,100,50)
button_text = button_font.render('Смена!', True, button_text_color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                keycolor = random.choice(list(COLOR_LIST.keys()))
                background.fill(COLOR_LIST[keycolor])
        
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,button_color,button_rect)
    button_rect_center = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text,button_rect_center)
    pygame.display.update()
                