from board import Board
from piece import *

pole = Board()
knight1 = Knight('белый')
pole.createboard()
pole.createpiece(knight1.w,knight1.h)
while True:
    pole.outboard()
    knight1.move(int(input('h=')),int(input('w=')))
    pole.createpiece(knight1.w,knight1.h)