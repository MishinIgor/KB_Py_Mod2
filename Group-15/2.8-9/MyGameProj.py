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
TICK = 0
ADD = 5
#Задаём размеры игрового окна
HEIGHT = 620
WIDTH = RECT_SIZE*2+(RECT_SIZE+INDENT)*COUNT_RECTS # Ширина состоит из боковых отступов размером ед. поля и кол. полей умнож. на отпуступы+размер ед. поля.
#Дополнительные переменные
points = 0 # Подсчёт очков
#Функции
def generate_map(column,row): #Функция генерирует координаты нового поля для цикла построения игровой карты
    return [RECT_SIZE+column*RECT_SIZE+INDENT*(column+1), # координаты по x
            HEADER+RECT_SIZE/2+row*RECT_SIZE+INDENT*(row+1), # координаты по y
            RECT_SIZE,RECT_SIZE # Размеры клетки Ширина х Высота
            ]
def display_text(text,font_size,x,y,color=COLOR_LIST["белый"]): #Функция написания текста
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text,True,color)
    screen.blit(text_surface,(x,y))
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
        #Возможность остановить и запустить игру(пока не работает)
        if event.type == pygame.K_SPACE: # останавливаем падение звезд по клику
            ADD = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # возобновляем движение вниз, если нажат Enter
                ADD = 5
    screen.fill(COLOR_LIST["бирюзово-голубой"])
    #Цикл генерации игровой карты(по которой бегает змейка)
    for row in range(COUNT_RECTS):
        for column in range(COUNT_RECTS):
            if (column + row) % 2 == 0:
                pygame.draw.rect(screen,COLOR_LIST["cерый"],generate_map(column,row))
            else:
                pygame.draw.rect(screen,COLOR_LIST["мокрый асфальт"],generate_map(column,row))
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
        points += ADD
        pygame.display.set_caption(f'Питон длинной {points} попугаев') #Выводим в заголовке кол. очков
        if points >= 100: #Условие имитирующее столкновение(переделать при добав. объектов)
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load('Поражение.mp3')
            pygame.mixer.music.play()
            TRY_GAME = False
    else: #Выводим в header текст при поражении.
        display_text(f'Вы набрали {points} попугаев, но не хватило на крылышко', 22 ,RECT_SIZE,RECT_SIZE,COLOR_LIST["красный"])
        display_text(f'Попробуйте написать свою версию программы ', 22 ,RECT_SIZE,RECT_SIZE*2+1,COLOR_LIST["красный"])
        TICK += 1
        if TICK == 20:
            play_game = False
    #Определяем кол. ФПС и обновляем
    time.tick(2)
    pygame.display.update()

pygame.mixer.music.stop()
pygame.mixer.music.unload()
pygame.quit()