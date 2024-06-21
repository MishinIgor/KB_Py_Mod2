from board import Board
from piece import *
pole = Board(5)
k = Knight('white',pole.w)

while True:
    pole.createpiece(k.x,k.y)
    pole.outmap()
    print(f'Позиция Коня: Б y={k.x+1}, Б x={k.y+1}')
    k.moove(int(input('y='))-1,int(input('x='))-1)
    