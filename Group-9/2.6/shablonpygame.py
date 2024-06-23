import pygame

WIN_SIZE = (360,480) # Размер игрового окна ширина x высота
FPS = 300 # частота кадров в секунду
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
'Изумрудный':(80,200,120)
}
colorkey = 'Чёрный'
# создаём игру и окно
pygame.init() # запускает pygame
pygame.mixer.init() # для звука
screen = pygame.display.set_mode(WIN_SIZE) #окно программы
pygame.display.set_caption('Титульная фиговинка') #титульная фиговинка
clock = pygame.time.Clock() #контролирует частоту кадров

#Цикл игры
running = True

while running:
    # Ввод процесса
    for event in pygame.event.get():
        #Проверяем закрытие окна
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    # Обновления
    clock.tick(FPS/10)
    # Визуализация
    screen.fill(COLOR_LIST["Изумрудный"])
    pygame.display.flip()
