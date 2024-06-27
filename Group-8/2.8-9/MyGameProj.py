import pygame, random

#Задаем размер игрового окна
HEIGHT = 550
#Добавим словарь цветов
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
'Изумрудный':(80,200,120),
'Аквамариновый': (127,255,212),
"Бирюзово-Голубой": (119,221,231)
}
#Дополнительные переменные
INDENT = 1
SIZE_RECT = 20 #размер клетки
COUNT_RECTS = 20 # кол. полей по горизонтали
WIDTH = SIZE_RECT * COUNT_RECTS + 2*SIZE_RECT+INDENT*SIZE_RECT  #Ширина в зависимости от создания квадратов
HEADER_RECT = 70
POTOM_UBEREM = 0 # Она пока за очки отвечает, но временно. Нужно поменять
#Функция для вывода текста
pygame.font.init()
def display_text(text,font_size,x,y,color):
    font = pygame.font.Font(None,font_size)
    text_surface = font.render(text,True,color)
    app.blit(text_surface,(x,y))
#Рисуем окно
app = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(f'Длинна вашей змеи: {POTOM_UBEREM} попугаев')
#Подключаем звук
pygame.mixer.init()
#Загружаем музыку
pygame.mixer.music.load('брыньбрынь.mp3')
#Игровой цикл
time = pygame.time.Clock()
play_game = True
#начинаем проигрывать музыку в бесконечном цикле
pygame.mixer.music.play(-1)
while play_game:
    #Создаём обработчик закрытия окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play_game = False
    app.fill(COLOR_LIST["Бирюзово-Голубой"])
    pygame.draw.rect(app,COLOR_LIST["Изумрудный"],[0,0,WIDTH,HEADER_RECT])
    for row in range(COUNT_RECTS):
        for column in range(COUNT_RECTS):
            if (column+row) % 2 == 0:
                pygame.draw.rect(app,COLOR_LIST["Мокрый асфальт"],[SIZE_RECT+column*SIZE_RECT+INDENT*(column+1),HEADER_RECT+SIZE_RECT+row*SIZE_RECT+INDENT*(row+1),SIZE_RECT,SIZE_RECT])
            else:
                pygame.draw.rect(app,COLOR_LIST["Серый"],[SIZE_RECT+column*SIZE_RECT+INDENT*(column+1),HEADER_RECT+SIZE_RECT+row*SIZE_RECT+INDENT*(row+1),SIZE_RECT,SIZE_RECT])
    time.tick(2)
    POTOM_UBEREM += 10
    if POTOM_UBEREM == 100:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load("Поражение.mp3")
        pygame.mixer.music.play()
        time.tick(0.5)
        play_game = False
    #Выводим текст на экран
    pygame.display.set_caption(f'Длинна вашей змеи: {POTOM_UBEREM} попугаев')
    display_text('Игру выполнил: Мишин Игорь и его команда студентов',20,20,HEIGHT-30,COLOR_LIST["Чёрный"])
    pygame.display.update()


pygame.quit()