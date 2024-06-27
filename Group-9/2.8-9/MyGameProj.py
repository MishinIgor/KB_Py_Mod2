import random,pygame
pygame.init()
pygame.mixer.init()
#Словарь цветов
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
points = 0
add = 0 # кол. добавляемых очков
#Дополнительные константы
SIZE_TEXT = 25
INDENT = 1 #Отступ между секторами
SIZE_SECTOR = 25 # размер сектора карты
COUNT_SECTOR = 20 # количество секторов в одной строке
HEADER = SIZE_SECTOR*COUNT_SECTOR // 10 # Размер хедера 10% от размера карты
FOOTER = SIZE_SECTOR*COUNT_SECTOR // 10 # Размер футера 10% от размера карты
TICK = 0
FLAG = True
X_SNAKE, Y_SNAKE = random.randint(0,COUNT_SECTOR), random.randint(0,COUNT_SECTOR)
#Задаём размеры игрового окна
WIDTH = 2*SIZE_SECTOR+COUNT_SECTOR*(INDENT+SIZE_SECTOR)
HEIGHT = SIZE_SECTOR*2+HEADER+FOOTER+COUNT_SECTOR*(INDENT+SIZE_SECTOR)
#Функции
def generate_sector(row,column):
    return [SIZE_SECTOR+column*SIZE_SECTOR+INDENT*(column+1), # координата по х
            HEADER+SIZE_SECTOR+row*SIZE_SECTOR+INDENT*(row+1), # координата по у
            SIZE_SECTOR,SIZE_SECTOR] #Размеры Ширины и Высоты
def display_text(text, font_size,x,y,color=COLOR_LIST["Чёрный"]):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text,True,color)
    screen.blit(text_surface,(x,y))
#Создаём игровое окно
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(f'Питон размером {points} попугаев')
#Подключаем звуковые эффекты
pygame.mixer.music.load('брыньбрынь.mp3')
pygame.mixer.music.play(-1)
def draw_snake(color,row,column):
    pygame.draw.rect(screen,color,[SIZE_SECTOR+column*SIZE_SECTOR+INDENT*(column+1),HEADER+SIZE_SECTOR+row*SIZE_SECTOR+INDENT*(row+1),SIZE_SECTOR,SIZE_SECTOR])

#Игровой цикл
time = pygame.time.Clock() #контроллер фпс
python_live = True
while python_live:
    #Цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            python_live = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # Пауза по клавише Enter
                add = 0
            if event.key == pygame.K_SPACE: # Старт по клавише Space
                add = 5
    #отрисовка фона
    screen.fill(COLOR_LIST['Аквамариновый'])
    #Отрисовка карты
    for row in range(COUNT_SECTOR):
        for column in range(COUNT_SECTOR):
            if column % 2 == 0:
                pygame.draw.rect(screen,COLOR_LIST['Серый'],generate_sector(row,column))
            else:
                pygame.draw.rect(screen,COLOR_LIST["Мокрый асфальт"],generate_sector(row,column))
            
            draw_snake(COLOR_LIST["Синий"],X_SNAKE,Y_SNAKE)
    pygame.display.set_caption(f'Питон размером {points} попугаев')
    #Отрисовка хедера
    points += add
    pygame.draw.rect(screen,COLOR_LIST['Белый'],[0,0,WIDTH,HEADER])
    if points >= 50 and FLAG == True:
        pygame.mixer.music.load('Поражение.mp3')
        pygame.mixer.music.play()
        FLAG = False
        add = 0
    if FLAG == False:
        display_text(f'Питон был размером {points} попугаев!', SIZE_TEXT,SIZE_SECTOR,0)
        display_text(f'Но не хватило на маленькое крылышко', SIZE_TEXT,SIZE_SECTOR,SIZE_TEXT+5)
    #Отрисовка футера
    pygame.draw.rect(screen,COLOR_LIST['Белый'],[0,HEIGHT-FOOTER,WIDTH,FOOTER])
    display_text(f'Проект разработан Мишиным Игорем и его студентами', SIZE_TEXT,SIZE_SECTOR,HEIGHT-FOOTER)
    display_text(f'Заливай сюда своё: https://github.com/MishinIgor/KB_Py_Mod2', SIZE_TEXT,SIZE_SECTOR,HEIGHT-FOOTER+SIZE_TEXT+5)
    #Обновление дисплея и контроль фпс
    time.tick(2)
    pygame.display.update()
pygame.quit()
    