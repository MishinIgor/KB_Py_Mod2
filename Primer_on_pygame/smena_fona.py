import pygame

pygame.init()
pygame.display.set_caption('Измени цвет фона')
window_surface = pygame.display.set_mode((300, 300))
background = pygame.Surface((300, 300))
background.fill(pygame.Color('#000000'))

color_list = [
    pygame.Color('#FF0000'),  # красный
    pygame.Color('#00FF00'),  # зеленый
    pygame.Color('#0000FF'),  # синий
    pygame.Color('#FFFF00'),  # желтый
    pygame.Color('#00FFFF'),  # бирюзовый
    pygame.Color('#FF00FF'),  # пурпурный
    pygame.Color('#FFFFFF')   # белый
]

current_color_index = 0

button_font = pygame.font.SysFont('Verdana', 15) # используем шрифт Verdana
button_text_color = pygame.Color("black")
button_color = pygame.Color("gray")
button_rect = pygame.Rect(100, 115, 100, 50)
button_text = button_font.render('Нажми!', True, button_text_color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                current_color_index = (current_color_index + 1) % len(color_list)
                background.fill(color_list[current_color_index])

        window_surface.blit(background, (0, 0))
        pygame.draw.rect(window_surface, button_color, button_rect)
        button_rect_center = button_text.get_rect(center=button_rect.center)
        window_surface.blit(button_text, button_rect_center)
        pygame.display.update()