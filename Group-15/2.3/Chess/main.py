from board import board
from piece import *
pole = board(8,8)
pole.createboard()
knight1 = Knight('white')
knight2 = Knight('black')
while True:
    pole.createpiece(knight1.x,knight1.y,knight1.color)
    pole.createpiece(knight2.x,knight2.y,knight2.color)
    pole.outmap()
    print(f'Координаты Белого коня: y:{knight1.x+1} x:{knight1.y+1}')
    print(f'Координаты Чёрного коня: y:{knight2.x+1} x:{knight2.y+1}')
    knight1.move(int(input('Б y='))-1,int(input('Б x='))-1)
    if pole.flag == False:
        break
    knight2.move(int(input('Ч y='))-1,int(input('Ч x='))-1)
    if pole.flag == False:
        break