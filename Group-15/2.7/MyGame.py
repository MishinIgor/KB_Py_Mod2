import pygame
import random

pygame.init()

#Определим цвета
COLOR_LIST = {
    "Белый": (255,255,255),
    "Красный": (255,0,0),
    "Зелёный": (0,255,0),
    "Синий": (0,0,255)
}
BLACK = (0,0,0)
#Задаём размер игрового окна
WIDTH = 400
HEIGHT = 600

#Создаём окно игры
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Догони меня буханка')

#Контроллер ФПС
clock = pygame.time.Clock()

#Границы поля
top_boundary = 0
bottom_boundary = HEIGHT
right_boundary = WIDTH

#Определяем размеры игрока и препятсвия
player_width = 50
player_height = 50
obstacle_width = 50
obstacle_height = 50

#Определяем скорость игрока и препятсвия
player_speed = 10
obstacle_speed = 7
score = 0 # Очки за каждый пропущенный объект
level = 1 # Уровни игры

#Определение начальных позиций игрока и препятсвия
player_x = WIDTH-2*player_width
player_y = HEIGHT/2 - player_height/2
obstacle_x = 0
obstacle_y = random.randint(0,HEIGHT-obstacle_height)
obstacle2_x = random.randint(0,WIDTH-obstacle_width)
obstacle2_y = 0
#Функцию для отображения текста
def display_text(text,font_size,x,y,color=COLOR_LIST["Белый"]):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text,True,color)
    screen.blit(text_surface,(x,y))

#Игровой цикл
game_over = False

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
    if keys[pygame.K_LEFT] and player_x > top_boundary:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < right_boundary - player_width:
        player_x += player_speed
    #Движение препятсвия
    obstacle_x += obstacle_speed
    obstacle2_y += obstacle_speed
    if obstacle2_y + obstacle_height >= HEIGHT:
        obstacle2_x = random.randint(0,WIDTH-obstacle_width)
        obstacle2_y = 0
        score += 1
    #Если препятсвие пересекло границу
    if obstacle_x + obstacle_width >= WIDTH:
        obstacle_x = 0
        obstacle_y = random.randint(0,HEIGHT-obstacle_height)
        score += 1
        if score % 5 == 0: # Каждые 5 очков увеличивается уровень
            level += 1
            obstacle_speed += 1
    #Проверка столкновений игрока с препятсвием
    if player_x + player_width > obstacle_x and player_x < obstacle_x + obstacle_width and player_y + player_height > obstacle_y and player_y < obstacle_y + obstacle_height:
        player_speed = 0
        obstacle_speed = 0
    if player_x + player_width > obstacle2_x and player_x < obstacle2_x + obstacle_width and player_y + player_height > obstacle2_y and player_y < obstacle2_y + obstacle_height:
        player_speed = 0
        obstacle_speed = 0
    #Обновляем чёрный фон после каждой прорисовки объектов
    screen.fill(BLACK)
    
    #Отрисовка игрока и препятсвия
    pygame.draw.rect(screen,COLOR_LIST["Зелёный"],(player_x,player_y,player_width,player_height))
    pygame.draw.rect(screen,COLOR_LIST['Красный'],(obstacle_x,obstacle_y,obstacle_width,obstacle_height))
    pygame.draw.rect(screen,COLOR_LIST["Синий"],(obstacle2_x,obstacle2_y,obstacle_width,obstacle_height))
    #Отображем информацию на экране
    display_text(f'Очки: {score}',25,10,10)
    display_text(f'Уровень: {level}',25,10,40)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
    