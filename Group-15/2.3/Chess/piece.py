import random

class Piece:
    def __init__(self,color):
        self.color = color
class Knight(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.x = random.randint(0,7)
        self.y = random.randint(0,7)
    def move(self,x,y):
        x1,y1 = self.x,self.y #Начальная позиция коня
        dopustimo = [(x1+2,y1+1),(x1+2,y1-1),(x1-2,y1+1),(x1-2,y1-1),(x1+1,y1+2),(x1+1,y1-2),(x1-1,y1+2),(x1-1,y1-2)]
        if (x,y) in dopustimo and 0<x<7 and 0<y<7:
            self.x = x
            self.y = y
        else:
            print('Введены некорректные данные')