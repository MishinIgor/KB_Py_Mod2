import pygame
import random
#Запускаем pygame
pygame.init()

#Определяем цвета
COLOR_LIST = {
    "Белый": (255,255,255),
    "Красный": (255,0,0),
    "Зелёный": (0,255,0),
    "Синий": (0,0,255)
}

#Определяем размер игрового окна
WIDTH = 900
HEIGHT = 800

#Создаём игровое окно
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Догони меня батон')
clock = pygame.time.Clock()
#Функция для вывода текста
def display_text(text, font_size,x,y,color=COLOR_LIST["Белый"]):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text,True,color)
    screen.blit(text_surface,(x,y))
# Запуск игры как вызов функции
def play_game():
    #Определяем границы поля
    zero_boundary = 0
    right_boundary = WIDTH
    bottom_boudary = HEIGHT

    #Определяем размеры игрока и препятвия
    player_width = 50
    player_height = 50
    obstacle_width = 50
    obstacle_height = 50

    #Определяем доп. переменные
    player_speed = 10 # Скорость движения игрока
    obstacle_speed = 5 # Скорость движения препятсвия
    points = 0 # Очки за каждый кубик
    level = 5 # уровень

    #Определим начальное положение игрока и препятсвия
    player_x = WIDTH/2 - player_width/2
    player_y = 2*player_height
    player2_x = WIDTH/2 - player_width/2
    player2_y = HEIGHT/2 - player_height/2
    obstacle_x = random.randint(zero_boundary,right_boundary-obstacle_width)
    obstacle_y = HEIGHT
    obstacle2_x = -obstacle_width
    obstacle2_y = random.randint(zero_boundary,bottom_boudary-obstacle_height)
    #Цикл игры
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #Обработка нажатий клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_y > zero_boundary:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < bottom_boudary - player_height:
            player_y += player_speed
        if keys[pygame.K_RIGHT] and player_x < right_boundary - player_width:
            player_x += player_speed
        if keys[pygame.K_LEFT] and player_x > zero_boundary:
            player_x -= player_speed
        #Управление для второго игрока
        if keys[pygame.K_w] and player2_y > zero_boundary:
            player2_y -= player_speed
        if keys[pygame.K_s] and player2_y < bottom_boudary - player_height:
            player2_y += player_speed
        if keys[pygame.K_d] and player2_x < right_boundary - player_width:
            player2_x += player_speed
        if keys[pygame.K_a] and player2_x > zero_boundary:
            player2_x -= player_speed
        #Движение препятсвия
        obstacle_y -= obstacle_speed
        #Генерируем слева на права препятсвия при уровне 3+
        if level >= 3:
            obstacle2_x+= obstacle_speed
            if obstacle2_x-obstacle_width>right_boundary:
                obstacle2_x = 0
                obstacle2_y = random.randint(zero_boundary,bottom_boudary-obstacle_height)
                points += 1
                
        #Если препятсвие вышло за границу генерируем новое
        if obstacle_y< 0:
            obstacle_x = random.randint(zero_boundary,right_boundary-obstacle_width)
            obstacle_y = HEIGHT
            points += 1
            if points % 5 == 0:
                level += 1
                obstacle_speed += 1
        
        #Проверка столкновений двух игроков
        if player_x + player_width > obstacle_x and player_x < obstacle_x + obstacle_width and player_y + player_height > obstacle_y and player_y < obstacle_y + obstacle_height:
            player_speed = 0
            obstacle_speed = 0
            
        if player_x + player_width > obstacle2_x and player_x < obstacle2_x + obstacle_width and player_y + player_height > obstacle2_y and player_y < obstacle2_y + obstacle_height:
            player_speed = 0
            obstacle_speed = 0
            
        if player2_x + player_width > obstacle_x and player2_x < obstacle_x + obstacle_width and player2_y + player_height > obstacle_y and player2_y < obstacle_y + obstacle_height:
            player_speed = 0
            obstacle_speed = 0
            
        if player2_x + player_width > obstacle2_x and player2_x < obstacle2_x + obstacle_width and player2_y + player_height > obstacle2_y and player2_y < obstacle2_y + obstacle_height:
            player_speed = 0
            obstacle_speed = 0
            
        #Отрисовка чёрного фона
        screen.fill((0,0,0))
        
        #Отрисовка игрока и препятсвия
        pygame.draw.rect(screen,COLOR_LIST['Зелёный'],(player_x,player_y,player_width,player_height))
        pygame.draw.rect(screen,COLOR_LIST["Белый"],(player2_x,player2_y,player_width,player_height))
        pygame.draw.rect(screen,COLOR_LIST["Красный"],(obstacle_x,obstacle_y,obstacle_width,obstacle_height))
        pygame.draw.rect(screen,COLOR_LIST["Синий"],(obstacle2_x,obstacle2_y,obstacle_width,obstacle_height))
        display_text(f'Очки: {points}',25,10,10)
        display_text(f'Уровень: {level}',25,10,40)
        pygame.display.update()
        clock.tick(60)
play_game()
pygame.quit()
