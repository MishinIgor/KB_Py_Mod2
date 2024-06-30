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
PLAY_SOUND = 0
TIME = 5
#Создаём змейку и еду
class Snake:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def inside(self):
        return 0<= self.x < COUNT_RECT and 0<= self.y < COUNT_RECT
    def __eq__(self, other):
        return isinstance(other,Snake) and self.x == other.x and self.y == other.y
    
snake_rect = [Snake(7,7),Snake(7,8)]
move_x = 1
move_y = 0
def generate_food():
    x = random.randint(0,COUNT_RECT-1)
    y = random.randint(0,COUNT_RECT-1)
    new_food = Snake(x,y)
    
    while new_food in snake_rect:
        x = random.randint(0,COUNT_RECT-1)
        y = random.randint(0,COUNT_RECT-1)
    return new_food
food = generate_food()
#Дополнительные переменные
vektor = ""
points = 0 # Подсчёт очков
tick = 0
#Задаём размеры окна
WIDTH = SIZE_RECT*2+(SIZE_RECT+INDENT)*COUNT_RECT # Ширина окна зависит от кол. полей в строке и их размера
HEIGHT = HEADER+SIZE_RECT*2+FOOTER+COUNT_RECT*(SIZE_RECT+INDENT) # Высота окна зависит от кол. полей в столбце и из размера
#Рисуем игровое окно
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(f'Питон размером {points} попугаев')
#Функции
def generate_pole(color,row,column): #Функция возвращает координаты для каждого поля при генерировании в цикле
    return pygame.draw.rect(screen,color,[SIZE_RECT+column*SIZE_RECT+INDENT*(column+1),HEADER+SIZE_RECT+SIZE_RECT*row+INDENT*(row+1),SIZE_RECT,SIZE_RECT])
def display_text(text,font_size,x,y,color=COLOR_LIST["чёрный"]):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text,True,color)
    screen.blit(text_surface,(x,y))
#Подключаем музыку
pygame.mixer.music.load('брыньбрынь.mp3')
pygame.mixer.music.play(-1)
#Цикл игры
clock = pygame.time.Clock()
play_game = True
while play_game:
    #Цикл обработки событий
    for event in pygame.event.get():
        #Условие завершения игры при нажатии на крестик
        if event.type == pygame.QUIT:
            play_game = False
        if event.type == pygame.KEYDOWN and PYTHON_LIVE == True:
            if event.key == pygame.K_w and vektor != 'DOWN': #Вверх
                vektor = 'UP'
                move_x = -1
                move_y = 0
            if event.key == pygame.K_s and vektor != 'UP': #Вниз
                vektor = 'DOWN'
                move_x = 1
                move_y = 0
            if event.key == pygame.K_a and vektor != 'RIGHT': #Влево
                vektor = 'LEFT'
                move_x = 0
                move_y = -1
            if event.key == pygame.K_d and vektor != 'LEFT': #Вправо
                vektor = 'RIGHT'
                move_x = 0
                move_y = 1   
    
    #Отрисовка фона
    screen.fill(COLOR_LIST['бирюзово-голубой'])
    #Отрисовка игровой карты
    for row in range(COUNT_RECT):
        for column in range(COUNT_RECT):
            if (row+column) % 2 == 0:
                color = COLOR_LIST['cерый']
            else:
                color = COLOR_LIST["мокрый асфальт"]
            generate_pole(color,row,column)
    #Отрисовка змейки и еды
    for snake in snake_rect:
        generate_pole(COLOR_LIST["тёмно-зелёный"],snake.x,snake.y)
    head = snake_rect[-1]
    new_head = Snake(head.x + move_x, head.y + move_y)
    if snake_rect.count(new_head) >= 2:
        PYTHON_LIVE = False
        display_text(f'Питон был размером {points} попугаев',SIZE_TEXT,SIZE_RECT,10)
        display_text(f'но не хватило места для маленького крылышка',SIZE_TEXT,SIZE_RECT,35)
    else:
        snake_rect.append(new_head)
        snake_rect.pop(0)
    if food == head:
        snake_rect.append(food)
        food = generate_food()
        points += 50
        TIME += 1
    generate_pole(COLOR_LIST['синий'],food.x,food.y)
    #Условие набора очков и действия с ними
    pygame.display.set_caption(f'Питон размером {points} попугаев')
    if not head.inside():
            PYTHON_LIVE = False
            move_x = 0
            move_y = 0
            display_text(f'Питон был размером {points} попугаев',SIZE_TEXT,SIZE_RECT,10)
            display_text(f'но не хватило места для маленького крылышка',SIZE_TEXT,SIZE_RECT,35)
    if PYTHON_LIVE == False:
        if PLAY_SOUND == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load('Поражение.mp3')
            pygame.mixer.music.play()
            PLAY_SOUND += 1   
            tick += 1
        if tick == 20:
            play_game == False
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.quit()
    #Отрисовка футера
    pygame.draw.rect(screen,COLOR_LIST["белый"],[0,HEIGHT-FOOTER,WIDTH,FOOTER])
    display_text(f'Проект подготовили {AUTOR}',SIZE_TEXT,SIZE_RECT,HEIGHT-FOOTER/2-SIZE_TEXT-5)
    display_text(f'Гитхаб: https://github.com/MishinIgor/KB_Py_Mod2',SIZE_TEXT,SIZE_RECT,HEIGHT-FOOTER/2)
    #Контроль фпс и обновление дисплея
    clock.tick(5)
    pygame.display.update()
pygame.mixer.music.stop()
pygame.mixer.music.unload()
pygame.quit()
