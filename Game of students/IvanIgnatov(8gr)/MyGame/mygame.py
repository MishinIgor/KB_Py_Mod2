# Передвижение на стрелочки
# Прыжок на Space
# Цель игры набрать 15 очков

import pygame
clock = pygame.time.Clock()
pygame.init()  # init() - инициализация окна
screen = pygame.display.set_mode((600, 360))
pygame.display.set_caption('My Game')  # set_caption - определение имени
icon = pygame.image.load('MyGame/images/icon-game-controller-b-64.webp').convert_alpha()
pygame.display.set_icon(icon)  # set_icon - определение иконки

game_score = 0
background = pygame.image.load('MyGame/images/background.jpg').convert_alpha()
player_anim_count = 0
bg_x = 0

background_music = pygame.mixer.Sound('MyGame/sounds/music.mp3.mp3')  # музыка на заднем фоне
background_music.set_volume(0.3)
background_music.play(-1)
jump_sound = pygame.mixer.Sound('MyGame/sounds/jump.mp3.mp3')
jump_sound.set_volume(1)
victory_sound = pygame.mixer.Sound('MyGame/sounds/win.mp3.mp3')
victory_sound.set_volume(0.3)

ghost = pygame.image.load('MyGame/images/free-icon-ghost-706023.png').convert_alpha()
ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 3500)  # таймер появления призраков
ghost_list_in_game = []

label = pygame.font.Font('MyGame/TLHeader-Regular-RUS.otf', 40)
lose_label = label.render('Game Over', True, (125, 22, 22))
restart = label.render('Press To Restart', True, (125, 22, 22))
restart_rect = restart.get_rect(topleft= (160, 150))
win_label = pygame.font.Font('MyGame/TLHeader-Regular-RUS.otf', 80)
win123 = win_label.render('You Win',True, (10,10,10))
gamescore = label.render(f'Game Score: {game_score}',True, (125, 22, 22))
score_label = pygame.font.Font('MyGame/TLHeader-Regular-RUS.otf', 20)
score = score_label.render(f'Game Score: {game_score}',True, (10,10,10))

player_speed = 8
player_x = 200
player_y = 210
is_jump = False
jump_count = 7

walk_right= [
    pygame.image.load('MyGame/images/player_right/player1_right.png').convert_alpha(),
    pygame.image.load('MyGame/images/player_right/player2_right.png').convert_alpha(),
    pygame.image.load('MyGame/images/player_right/player3_right.png').convert_alpha(),
    pygame.image.load('MyGame/images/player_right/player4_right.png').convert_alpha()
]
# convert_alfa() - конвертация изображения
walk_left = [
    pygame.image.load('MyGame/images/player_left/player1_left.png').convert_alpha(),
    pygame.image.load('MyGame/images/player_left/player2_left.png').convert_alpha(),
    pygame.image.load('MyGame/images/player_left/player3_left.png').convert_alpha(),
    pygame.image.load('MyGame/images/player_left/player4_left.png').convert_alpha()
]

win = False
gameplay = True
running = True  
    
while running:
    if not win:
        if gameplay:
            screen.blit(background, (bg_x, 0))
            screen.blit(background, (bg_x + 600, 0))  # анимация заднего фона
                
            player_rect = walk_right[0].get_rect(topleft= (player_x, player_y))
                
            if ghost_list_in_game:  # появление призраков
                for (i, el) in enumerate(ghost_list_in_game):
                    screen.blit(ghost, el)
                    el.x -= 10
                        
                    if el.x <= -9:
                        game_score += 1
                        if game_score == 15:
                            win =True
                        score = score_label.render(f'Game Score: {game_score}',True, (10,10,10))
                        gamescore = label.render(f'Game Score: {game_score}',True, (125, 22, 22))
                           
                    if el.x < -10:
                        ghost_list_in_game.pop(i)  # удаление призрака, если тот выйдет за пределы игры
                        
                    if player_rect.colliderect(el):  # отслеживание соприкосновений
                        gameplay = False
                        is_jump = False
            
            screen.blit(score,(5,5))   
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                screen.blit(walk_left[player_anim_count], (player_x, player_y))  # анимация и передвижение игрока
            else:
                screen.blit(walk_right[player_anim_count], (player_x, player_y))
                    
            if keys[pygame.K_LEFT] and player_x > 50:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_x  < 500:
                player_x += player_speed
                
            if player_anim_count == 3:
                player_anim_count = 0
            else:
                player_anim_count += 1
                
            bg_x -= 2
            if bg_x == -600:
                bg_x = 0  # анимация заднего фона
                
            if not is_jump:  # реализация прыжка
                if keys[pygame.K_SPACE]:
                    is_jump = True
            else:
                if jump_count >= -7:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1                      
                else:
                    is_jump = False
                    jump_count = 7
                    jump_sound.play()
                    player_y = 210
                        
            pygame.display.update()
        else:  # экран проигрыша
            screen.fill((10, 10, 10))  # fill - заливка экрана
            screen.blit(lose_label, (200, 100))  # blit - добавление изображений
            screen.blit(restart, restart_rect)
            screen.blit(gamescore, (175, 200))
            background_music.stop()
            victory_sound.play()    
            mouse = pygame.mouse.get_pos()
            if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                
                gameplay = True
                player_x = 200
                player_y = 210
                ghost_list_in_game.clear()
                victory_sound.stop()
                background_music.play(-1)
                
        pygame.display.update()              

    else:  # экран победы
        screen.blit(background, (bg_x, 0))
        screen.blit(background, (bg_x + 600, 0))
        bg_x -= 2
        if bg_x == -600:
            bg_x = 0
        screen.blit(win123,(150,150))
        background_music.stop()
        victory_sound.play()
        pygame.display.update()
        
    for event in pygame.event.get():  # выход
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()
            exit(0)
        if event.type == ghost_timer:  # появление призраков
            ghost_list_in_game.append(ghost.get_rect(topleft= (605, 212)))
    clock.tick(12)