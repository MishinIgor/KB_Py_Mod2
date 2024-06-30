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
"Бирюзово-Голубой": (119,221,231),
"Малиновый":(220,20,60)
}
#Дополнительные переменные
points = 0
#Дополнительные константы
SIZE_TEXT = 25
INDENT = 1 #Отступ между секторами
SIZE_SECTOR = 25 # размер сектора карты
COUNT_SECTOR = 20 # количество секторов в одной строке
HEADER = SIZE_SECTOR*COUNT_SECTOR // 10 # Размер хедера 10% от размера карты
FOOTER = SIZE_SECTOR*COUNT_SECTOR // 10 # Размер футера 10% от размера карты
SOUND_PLAY = 0
TICK = 5
FLAG = True
VEKTOR = ''
START = False
#Создаём змейку и еду
class Snake:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __eq__(self, other):
        return isinstance(other,Snake) and self.x == other.x and self.y == other.y
    def inside(self):
        return 0 <= self.x < COUNT_SECTOR and 0 <= self.y < COUNT_SECTOR
def generate_food():
    x = random.randint(0,COUNT_SECTOR-1)
    y = random.randint(0,COUNT_SECTOR-1)
    food_block = Snake(x,y)
    return food_block
food = generate_food()
snake_rect = [Snake(9,9),Snake(9,10)]
move_x = 0
move_y = 0
#Задаём размеры игрового окна
WIDTH = 2*SIZE_SECTOR+COUNT_SECTOR*(INDENT+SIZE_SECTOR)
HEIGHT = SIZE_SECTOR*2+HEADER+FOOTER+COUNT_SECTOR*(INDENT+SIZE_SECTOR)
def display_text(text, font_size,x,y,color=COLOR_LIST["Чёрный"]):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text,True,color)
    screen.blit(text_surface,(x,y))
def draw_obj(color,row,column):
    pygame.draw.rect(screen,color,[SIZE_SECTOR+column*SIZE_SECTOR+INDENT*(column+1),HEADER+SIZE_SECTOR+row*SIZE_SECTOR+INDENT*(row+1),SIZE_SECTOR,SIZE_SECTOR])

#Создаём игровое окно
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(f'Питон размером {points} попугаев')
#Подключаем звуковые эффекты
pygame.mixer.music.load('брыньбрынь.mp3')
pygame.mixer.music.play(-1)

#Игровой цикл
time = pygame.time.Clock() #контроллер фпс
python_live = True
while python_live:
    #Цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            python_live = False
        if event.type == pygame.KEYDOWN and FLAG == True:
            START = True
            if event.key in (pygame.K_w,pygame.K_UP) and VEKTOR != 'DOWN': # Вверх
                VEKTOR = 'UP'
                move_x = -1
                move_y = 0
            if event.key in (pygame.K_s,pygame.K_DOWN) and VEKTOR != 'UP': # Вниз
                VEKTOR = 'DOWN'
                move_x = 1
                move_y = 0
            if event.key in (pygame.K_a,pygame.K_LEFT) and VEKTOR != 'RIGHT': # Влево
                VEKTOR = 'LEFT'
                move_x = 0
                move_y = -1
            if event.key in (pygame.K_d,pygame.K_RIGHT) and VEKTOR != 'LEFT': # Вправо
                VEKTOR = 'RIGHT'
                move_x = 0
                move_y = 1
    #отрисовка фона
    screen.fill(COLOR_LIST['Аквамариновый'])
    #Отрисовка карты
    for row in range(COUNT_SECTOR):
        for column in range(COUNT_SECTOR):
            if (row+column) % 2 == 0:
                color = COLOR_LIST['Серый']
            else:
                color = COLOR_LIST['Мокрый асфальт']
            draw_obj(color,row,column)
    pygame.display.set_caption(f'Питон размером {points} попугаев')
    #Отрисовка хедера
    pygame.draw.rect(screen,COLOR_LIST['Белый'],[0,0,WIDTH,HEADER])
    
    #ОТРИСОВКА ЗМЕИ И ЕДЫ
    draw_obj(COLOR_LIST["Малиновый"],food.x,food.y)
    for snake in snake_rect:
        draw_obj(COLOR_LIST["Тёмно-зелёный"],snake.x,snake.y)
    head = snake_rect[-1]
    new_head = Snake(head.x+move_x,head.y+move_y)
    #Проверка врезания в стену
    if not head.inside():
        #FLAG = False
        if new_head.x == -1:
            new_head.x = COUNT_SECTOR-1
        elif new_head.x == COUNT_SECTOR:
            new_head.x = 0
        elif new_head.y == -1:
            new_head.y = COUNT_SECTOR-1
        elif new_head.y == COUNT_SECTOR:
            new_head.y = 0
    if snake_rect.count(new_head) >= 2:
        FLAG = False
    else:
        if START == True:
            snake_rect.append(new_head)
            snake_rect.pop(0)
        if head == food:
            snake_rect.append(food)
            food = generate_food()
            points += 50
            #TICK += 1
    ######################
    if FLAG == False:
        move_x = 0
        move_y = 0
        if SOUND_PLAY == 0:
            pygame.mixer.music.load('Поражение.mp3')
            pygame.mixer.music.play()
        SOUND_PLAY += 1
        display_text(f'Питон был размером {points} попугаев!', SIZE_TEXT,SIZE_SECTOR,0)
        display_text(f'Но не хватило на маленькое крылышко', SIZE_TEXT,SIZE_SECTOR,SIZE_TEXT+5)
    #Отрисовка футера
    pygame.draw.rect(screen,COLOR_LIST['Белый'],[0,HEIGHT-FOOTER,WIDTH,FOOTER])
    display_text(f'Проект разработан Мишиным Игорем и его студентами', SIZE_TEXT,SIZE_SECTOR,HEIGHT-FOOTER)
    display_text(f'Заливай сюда своё: https://github.com/MishinIgor/KB_Py_Mod2', SIZE_TEXT,SIZE_SECTOR,HEIGHT-FOOTER+SIZE_TEXT+5)
    #Обновление дисплея и контроль фпс
    time.tick(TICK+2)
    pygame.display.update()
pygame.quit()
    