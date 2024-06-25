import pygame
import random

pygame.init()
#Определяем цвета
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
#Определяем размер игрового окна
WIDTH = 800
HEIGHT = 600
WIN_SIZE = (WIDTH,HEIGHT)
#Создаём окно игры и запись в title
screen = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('My first game')
#Контроллер фпс
clock = pygame.time.Clock()
#Определяем границы экрана

top_boundary = 0
bottom_boundary = HEIGHT
left_boundary = 0
right_boundary = WIDTH
#Определение размеров игрока и препятсвий
player_width = 50
player_height = 50
obstacle_width = 50
obstacle_height = 50

#Определение скорости движения игрока и препятсвий
player_speed = 10
obstacle_speed = 5
score = 0
level = 1
# Определение начальных позиций игрока и препятсвий
player_x = WIDTH/2 - player_width/2
player_y = HEIGHT/2 - player_height/2
obstacle_x = WIDTH
obstacle_y = random.randint(top_boundary,bottom_boundary - obstacle_height)

#Переменная флажок для проигрыша
game_over = False
#Функция для отображения текста на экране
def display_text(text,font_size,x,y,color):
    font = pygame.font.Font(None,font_size)
    text_surface = font.render(text,True,color)
    screen.blit(text_surface,(x,y))

#Основной игровой цикл
while not(game_over):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    #Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > top_boundary:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < bottom_boundary - player_height:
        player_y += player_speed
    if keys[pygame.K_LEFT] and player_x > left_boundary:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < right_boundary-player_width:
        player_x += player_speed
    #Движение препятсвия
    obstacle_x -= obstacle_speed
    
    #Если препятсвие вышло за пределы экрана, генерируется новое препятсвие
    if obstacle_x + obstacle_width <0:
        obstacle_x = WIDTH
        obstacle_y = random.randint(top_boundary,bottom_boundary - obstacle_height)
        score += 1
        if score % 5 == 0: #Повышение уровня каждые 10 очков
            level += 1
            obstacle_speed += 1
    
    #Проверка столкновения игрока с препятствием
    if player_x + player_width > obstacle_x and player_x < obstacle_x + obstacle_width and player_y + player_height > obstacle_y and player_y < obstacle_y + obstacle_height:
        game_over = True
    screen.fill(BLACK)
    
    #Отрисовка игрока и препятсвия
    pygame.draw.rect(screen,RED,(player_x,player_y,player_width,player_height))
    pygame.draw.rect(screen,WHITE,(obstacle_x,obstacle_y,obstacle_width,obstacle_height))
    
    #Отображем на экране информацию
    display_text(f'Score: {score}', 25, 10, 10, BLUE)
    display_text(f'LeveL {level}', 25,10,40,BLUE)

    pygame.display.update()
    clock.tick(60)

pygame.quit()