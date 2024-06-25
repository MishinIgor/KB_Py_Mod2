import pygame
import random

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Звезды падают вниз")

black = (0, 0, 0)
white = (255, 255, 255)
pink = (255, 192, 203)

font = pygame.font.SysFont("Verdana", 15)

star_list = []
for i in range(50):
    x = random.randrange(screen_width)
    y = random.randrange(-200, -50)
    speed = random.randrange(1, 9)
    star_list.append([x, y, speed])
score = 0

freeze = False # флаг для определения момента остановки

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN: # останавливаем падение звезд по клику
            freeze = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # возобновляем движение вниз, если нажат Enter
                freeze = False

    if not freeze: # если флаг не активен,
        # звезды падают вниз
        for star in star_list:
            star[1] += star[2]
            if star[1] > screen_height:
                star[0] = random.randrange(screen_width)
                star[1] = random.randrange(-200, -50)
                score += 1

    # рисуем звезды, выводим результаты подсчета
    screen.fill(black)
    for star in star_list:
        pygame.draw.circle(screen, pink, (star[0], star[1]), 3)
    score_text = font.render("Упало звезд: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    # устанавливаем частоту обновления экрана
    pygame.time.Clock().tick(60)