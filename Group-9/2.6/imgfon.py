import pygame

pygame.init()

WIN_SIZE = (400,400)
screen = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('Свинка на картинке')

#Загрузка изображения
background_image = pygame.image.load('background.png')

#Подгоняем масштаб под размер окна
background_image = pygame.transform.scale(background_image, WIN_SIZE)

#Накладываем изображение на поверхность
screen.blit(background_image,(0,0))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        #Проверяем закрытие окна
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()