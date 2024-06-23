#Программа меняет цвет фона при нажатии на кнопку
import pygame
import random

def randcolor():
    return random.choice(list(COLOR_LIST.keys()))

COLOR_LIST = {
# Цвета (R, G, B)
'Чёрный':(0, 0, 0),
'Белый':(255, 255, 255),
'Касный':(255, 0, 0),
'Зелёный':(0, 255, 0),
'Синий':(0, 0, 255),
'Мокрый асфальт':(96,96,96),
'Серый':(128,128,128),
'Тёмно-зелёный':(0,69,36),
'Изумрудный':(80,200,120)
}
colorkey = 'Белый'

WIN_SIZE = (300,300)
pygame.init()
pygame.display.set_caption('обработка событий')
screen = pygame.display.set_mode(WIN_SIZE)
background = pygame.Surface(WIN_SIZE)
background.fill(pygame.Color(COLOR_LIST[randcolor()]))

button_font = pygame.font.SysFont('Verdana', 15) # Шрифт и размер шрифта
button_text_color = pygame.Color('black')
button_color = pygame.Color('gray')
button_rect = pygame.Rect(100,115,100,50)
button_text = button_font.render('Сменить!', True, button_text_color)

while True:
    for event in pygame.event.get():
        #Проверяем закрытие окна
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Обрабатываем событие нажатия на кнопку
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):#Если столкновение нажатия на мышку в позиции кнопки
                background.fill(COLOR_LIST[randcolor()]) #Сменить цвет фона на рандомный
    
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,button_color,button_rect) #Прорисовка фона, цвет кнопки, отступы кнопки
    button_rect_center = button_text.get_rect(center=button_rect.center) #По центру внутри кнопки
    screen.blit(button_text,button_rect_center)
    pygame.display.update()
    
    
