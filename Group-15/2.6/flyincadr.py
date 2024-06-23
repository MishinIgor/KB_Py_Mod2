import pygame

pygame.init()

window_size = (640, 480)
screen = pygame.display.set_mode(window_size)
color = (216, 233, 243)
screen.fill(color)
pygame.display.flip()
pygame.display.set_caption("Покадровая анимация")
clock = pygame.time.Clock()

# загружаем кадры
frame_images = []
for i in range(1, 9):
    frame_images.append(pygame.image.load(f"frame{i}.png"))

# параметры анимации
animation_length = len(frame_images)
animation_speed = 15  # кадры в секунду
current_frame_index = 0
animation_timer = 0
frame_position = [0, 0]

# вычисляем позицию для вывода кадров в зависимости от высоты окна
window_height = screen.get_height()
frame_height = frame_images[0].get_height()
frame_position[1] = int(window_height * 0.45) - int(frame_height / 2)

# запускаем основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # обновление состояния
    time_delta = clock.tick(60) / 1000.0
    animation_timer += time_delta
    if animation_timer >= 1.0 / animation_speed:
        current_frame_index = (current_frame_index + 1) % animation_length
        animation_timer -= 1.0 / animation_speed

    frame_position[0] += 1  # сдвигаем кадр вправо

    # выводим кадры, обновляем экран
    current_frame = frame_images[current_frame_index]
    screen.blit(current_frame, frame_position)
    pygame.display.flip()

pygame.quit()