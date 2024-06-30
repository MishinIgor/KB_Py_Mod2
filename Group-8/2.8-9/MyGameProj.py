import pygame, random
pygame.init()
#Подключаем звук
pygame.mixer.init()
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
#Дополнительные константы
INDENT = 1
SIZE_RECT = 20 #размер клетки
COUNT_RECTS = 20 # кол. полей по горизонтали и вертикали
HEADER_RECT = 50
FOOTER = 50
POINTS = 0
TIME = 5
SOUND_LOOZ = False
#Объект змейка и еда
class Snake:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def out_snake(self):
        return 0<= self.x < COUNT_RECTS and 0 <= self.y < COUNT_RECTS
    def __eq__(self, other):
        return isinstance(other,Snake) and self.x == other.x and self.y == other.y
def random_food_block():
    x = random.randint(0,COUNT_RECTS-1)
    y = random.randint(0,COUNT_RECTS-1)
    
    food_block = Snake(x,y)
    while food_block in snake_rect:
        food_block.x = random.randint(0,COUNT_RECTS-1)
        food_block.y = random.randint(0,COUNT_RECTS-1)
    return food_block
snake_rect = [Snake(9,10),Snake(10,10)]
food = random_food_block()
x_row =  0
y_col = 1
#Задаем размер игрового окна
HEIGHT = HEADER_RECT + SIZE_RECT*2+COUNT_RECTS*(SIZE_RECT+INDENT)+FOOTER #Высота в зависимости от создания квадратов
WIDTH =  2*SIZE_RECT+COUNT_RECTS*(SIZE_RECT+INDENT)  #Ширина в зависимости от создания квадратов
#Функции
def display_text(text,font_size,x,y,color):#Функция для вывода текста
    font = pygame.font.Font(None,font_size)
    text_surface = font.render(text,True,color)
    screen.blit(text_surface,(x,y))
def draw_rect(color,row,column):
    return pygame.draw.rect(screen,color,[SIZE_RECT+column*SIZE_RECT+INDENT*(column+1),HEADER_RECT+SIZE_RECT+row*SIZE_RECT+INDENT*(row+1),SIZE_RECT,SIZE_RECT])

#Рисуем окно
screen = pygame.display.set_mode((WIDTH,HEIGHT)) #В старой версии было app, через ctr+f сделали замену на screen
pygame.display.set_caption(f'Длинна вашей змеи: {POINTS} попугаев')

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and y_col != 0: #Движение вверх
                x_row =  -1
                y_col = 0
            if event.key == pygame.K_s and y_col != 0: #Движение вниз
                x_row =  1
                y_col = 0
            if event.key == pygame.K_a and x_row != 0: #Движение влево
                x_row =  0
                y_col = -1
            if event.key == pygame.K_d and x_row != 0: #Движение вправо
                x_row =  0
                y_col = 1
    screen.fill(COLOR_LIST["Бирюзово-Голубой"])
    pygame.draw.rect(screen,COLOR_LIST["Изумрудный"],[0,0,WIDTH,HEADER_RECT])
    for row in range(COUNT_RECTS):
        for column in range(COUNT_RECTS):
            if (column+row) % 2 == 0:
                color = COLOR_LIST['Мокрый асфальт']
            else:
                color = COLOR_LIST["Серый"]
        draw_rect(color,row,column)
    draw_rect(COLOR_LIST['Синий'],food.x,food.y) #Рисуем еду
    for snake in snake_rect: 
        draw_rect(COLOR_LIST['Тёмно-зелёный'],snake.x,snake.y)
    head = snake_rect[-1]
    if not head.out_snake(): #Останавливаем игру в случае проигрыша
        x_row = 0
        y_col = 0
        
    new_head = Snake(head.x+x_row,head.y+y_col)
    snake_rect.append(new_head)
    snake_rect.pop(0)
    
    if food == head: #Функция проверки столкновения с едой
        snake_rect.append(food)
        food = random_food_block()
        POINTS += 1
        TIME += POINTS
    #Выводим текст на экран
    pygame.display.set_caption(f'Длинна вашей змеи: {POINTS} попугаев')
    display_text('Игру выполнил: Мишин Игорь',25,10,HEIGHT-55,COLOR_LIST["Чёрный"])
    display_text('и его команда студентов',25,10,HEIGHT-25,COLOR_LIST["Чёрный"])
    time.tick(TIME)
    if x_row == 0 and y_col == 0:
        display_text(f'Питон длинной {POINTS} попугая(ев/й)',25,10,5,COLOR_LIST["Чёрный"])
        display_text(f'и не хватило на маленькое крылышко',25,10,25,COLOR_LIST["Чёрный"])
        if SOUND_LOOZ == False:
            pygame.mixer.music.load('Поражение.mp3')
            pygame.mixer.music.play(1)
            SOUND_LOOZ = True
    pygame.display.update()
pygame.mixer.music.stop()
pygame.mixer.music.unload()
pygame.quit()