import pygame, random
pygame.init()
pygame.mixer.init() #Инициализируем подключение звука
#Словарь цветов
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
HEADER = 70
RECT_SIZE = 20 # размер единицы поля
COUNT_RECTS = 20 # кол. полей в строке
INDENT = 1 # размер отступа между полями
FOOTER = 70
TEXT_SIZE = 25
TRY_GAME = True
PLAY_SOUND = 0
ADD = 5
#Задаём размеры игрового окна
HEIGHT = RECT_SIZE*2+HEADER+FOOTER+COUNT_RECTS*(RECT_SIZE+INDENT)
WIDTH = RECT_SIZE*2+(RECT_SIZE+INDENT)*COUNT_RECTS # Ширина состоит из боковых отступов размером ед. поля и кол. полей умнож. на отпуступы+размер ед. поля.
#Создаём змейку и еду
class Snake:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def inside(self):
        return 0 <= self.x < COUNT_RECTS and 0 <= self.y < COUNT_RECTS
    def __eq__(self, other):
        return isinstance(other,Snake) and self.x == other.x and self.y == other.y
#Дополнительные переменные
vektor = 'вправо'
x_row = 0
y_col = 1
points = 0 # Подсчёт очков
snake_rect = [Snake(COUNT_RECTS//2,COUNT_RECTS//2)] #Список где хранится координаты змеи
#Функции
def generate_obj(color,row,column): #Функция генерирует координаты нового поля для цикла построения игровой карты
    return pygame.draw.rect(screen,color,[RECT_SIZE+column*RECT_SIZE+INDENT*(column+1), # координаты по x
            HEADER+RECT_SIZE/2+row*RECT_SIZE+INDENT*(row+1), # координаты по y
            RECT_SIZE,RECT_SIZE # Размеры клетки Ширина х Высота
            ])
def display_text(text,font_size,x,y,color=COLOR_LIST["белый"]): #Функция написания текста
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text,True,color)
    screen.blit(text_surface,(x,y))
def random_food_block():
    x = random.randint(0,COUNT_RECTS-1)
    y = random.randint(0,COUNT_RECTS-1)
    
    food_block = Snake(x,y)
    return food_block
food = random_food_block()  # Генерируем еду
#Рисуем окно
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(f'Питон длинной {points} попугаев') #Выводим в заголовке кол. очков
#Контроллер ФПС
time = pygame.time.Clock()
#Подключение звука
pygame.mixer.music.load('брыньбрынь.mp3') #Загружаем основную мелодию игры
pygame.mixer.music.play(-1) #Запускаем музыку в бесконечном цикле
#Цикл игры 
play_game = True
while play_game:
    #Создаём обработку событий нажатия
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play_game = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_w,pygame.K_UP) and vektor != 'вниз': #движение вверх
                vektor = 'вверх'
                x_row = -1
                y_col = 0
            if event.key in (pygame.K_s,pygame.K_DOWN) and vektor != 'вверх': #движение вниз
                vektor = 'вниз'
                x_row = 1
                y_col = 0
            if event.key in (pygame.K_a,pygame.K_LEFT) and vektor != 'вправо': #движение влево
                vektor = 'влево'
                x_row = 0
                y_col = -1
            if event.key in (pygame.K_d,pygame.K_RIGHT) and vektor != 'влево': #движение вправо
                vektor = 'вправо'
                x_row = 0
                y_col = 1
    screen.fill(COLOR_LIST["бирюзово-голубой"])
    #Цикл генерации игровой карты(по которой бегает змейка)
    for row in range(COUNT_RECTS):
        for column in range(COUNT_RECTS):
            if (column + row) % 2 == 0:
                color = COLOR_LIST["cерый"]
            else:
                color = COLOR_LIST["мокрый асфальт"]
            generate_obj(color,column,row)
    generate_obj(COLOR_LIST["синий"],food.x,food.y)
    for snake in snake_rect:
        generate_obj(COLOR_LIST["тёмно-зелёный"],snake.x,snake.y)
    head = snake_rect[-1]
    new_head = Snake(head.x+x_row,head.y+y_col)
    snake_rect.append(new_head)
    snake_rect.pop(0)
    if food == head:
        snake_rect.append(food)
        food = random_food_block()
        points += 50
    if not head.inside():
        TRY_GAME = False
    
    #Отрисовка Header
    pygame.draw.rect(screen,COLOR_LIST["изумрудный"],[0,0,WIDTH,HEADER])
    #Отрисовка Footer
    pygame.draw.rect(screen,COLOR_LIST["белый"],[0,HEIGHT-FOOTER,WIDTH,FOOTER])
    #Выводим текст в футер
    display_text(f'Программу выполнил Мишин Игорь и его студенты',TEXT_SIZE,
                 RECT_SIZE, # Координата х текста
                 HEIGHT-(FOOTER+TEXT_SIZE)/2, # Координата у текста
                 COLOR_LIST['чёрный'])
    #Подсчёт очков и действия с ними
    if TRY_GAME == True:
        pygame.display.set_caption(f'Питон длинной {points} попугаев') #Выводим в заголовке кол. очков  
    else: #Выводим в header текст при поражении.
        x_row = 0
        y_col = 0
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        if PLAY_SOUND == 0:
            pygame.mixer.music.load('Поражение.mp3')
            pygame.mixer.music.play(1)
            PLAY_SOUND += 1
        display_text(f'Вы съели {points} попугаев,и не хватило на крылышко', TEXT_SIZE ,RECT_SIZE,RECT_SIZE,COLOR_LIST["красный"])
        display_text(f'Попробуйте написать свою версию программы ', TEXT_SIZE ,RECT_SIZE,RECT_SIZE*2+1,COLOR_LIST["красный"])
    #Определяем кол. ФПС и обновляем
    time.tick(3)
    pygame.display.flip()
    pygame.display.update()

pygame.mixer.music.stop()
pygame.mixer.music.unload()
pygame.quit()