import random, pygame
pygame.init()
pygame.mixer.init()
#Задаём словарь цветов
COLOR_LIST = {
# Цвета (R, G, B)  
"чёрный":(0, 0, 0),
"белый":(255, 255, 255), 
"красный":(255, 0, 0), 
"зелёный":(0, 255, 0), 
"синий":(0, 0, 255),
"мокрый асфальт":(96,96,96), 
"изумрудный":(80,200,120),
'cерый':(128,128,128),
'тёмно-зелёный':(0,69,36),
'аквамариновый': (127,255,212),
"бирюзово-голубой": (119,221,231)
}
#Дополнительные константы
AUTOR = "Мишин Игорь и студенты"#Автор проекта
SIZE_TEXT = 25 #Размер текста
HEADER = 55 # Нижняя панель
FOOTER = 65 # Верхняя панель
INDENT = 1 # отступ между полями 
SIZE_RECT = 20 # Размер поля для генерирования карты
COUNT_RECT = 20 # Сколько у нас полей в линии
PYTHON_LIVE = True # переменная ВРЕМЕННАЯ, ПОТОМ ОТРЕДАКТИРОВАТЬ
ADD = 10
#Дополнительные переменные
points = 0 # Подсчёт очков
tick = 0
#Задаём размеры окна
WIDTH = SIZE_RECT*2+(SIZE_RECT+INDENT)*COUNT_RECT # Ширина окна зависит от кол. полей в строке и их размера
HEIGHT = HEADER+SIZE_RECT*2+FOOTER+COUNT_RECT*(SIZE_RECT+INDENT) # Высота окна зависит от кол. полей в столбце и из размера
#Рисуем игровое окно
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(f'Питон размером {points} попугаев')
#Функции
def generate_pole(column,row): #Функция возвращает координаты для каждого поля при генерировании в цикле
    return [SIZE_RECT+column*SIZE_RECT+INDENT*(column+1),HEADER+SIZE_RECT+SIZE_RECT*row+INDENT*(row+1),SIZE_RECT,SIZE_RECT]
def display_text(text,font_size,x,y,color=COLOR_LIST["чёрный"]):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text,True,color)
    screen.blit(text_surface,(x,y))
#Подключаем музыку
pygame.mixer.music.load('брыньбрынь.mp3')
pygame.mixer.music.play(-1)
#Цикл игры
time = pygame.time.Clock()
play_game = True
while play_game:
    #Цикл обработки событий
    for event in pygame.event.get():
        #Условие завершения игры при нажатии на крестик
        if event.type == pygame.QUIT:
            play_game = False
    #Отрисовка фона
    screen.fill(COLOR_LIST['бирюзово-голубой'])
    #Отрисовка игровой карты
    for row in range(COUNT_RECT):
        for column in range(COUNT_RECT):
            if (row+column) % 2 == 0:
                pygame.draw.rect(screen,COLOR_LIST["cерый"],generate_pole(column,row))
            else:
                pygame.draw.rect(screen,COLOR_LIST["мокрый асфальт"],generate_pole(column,row))
    #Отрисовка хедера
    pygame.draw.rect(screen,COLOR_LIST["белый"],[0,0,WIDTH,HEADER])
    #Условие набора очков и действия с ними
    pygame.display.set_caption(f'Питон размером {points} попугаев')
    if PYTHON_LIVE == True:
        points += ADD
    if points >= 100 and PYTHON_LIVE == True:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load('Поражение.mp3')
        pygame.mixer.music.play()    
        PYTHON_LIVE = False
    if PYTHON_LIVE == False:
        display_text(f'Питон был размером {points} попугаев',25,SIZE_RECT,10)
        display_text(f'но не хватило места для маленького крылышка',25,SIZE_RECT,35)
        tick += 1
        if tick == 10:
            play_game == False
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.quit()
    #Отрисовка футера
    pygame.draw.rect(screen,COLOR_LIST["белый"],[0,HEIGHT-FOOTER,WIDTH,FOOTER])
    display_text(f'Проект подготовили {AUTOR}',SIZE_TEXT,SIZE_RECT,HEIGHT-FOOTER/2-SIZE_TEXT-5)
    display_text(f'Скидывайте примеры в гитхаб: https://github.com/MishinIgor/KB_Py_Mod2',SIZE_TEXT-10,SIZE_RECT,HEIGHT-FOOTER/2)
    #Контроль фпс и обновление дисплея
    time.tick(2)
    pygame.display.update()
pygame.mixer.music.stop()
pygame.mixer.music.unload()
pygame.quit()
