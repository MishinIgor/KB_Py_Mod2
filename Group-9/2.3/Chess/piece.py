import random

class Piece:
    def __init__(self,color):
        self.color = color
class Knight(Piece):
    def __init__(self, color,w):
        super().__init__(color)
        self.w = w
        self.x = random.randint(0,w-1)
        self.y = random.randint(0,w-1)
    def moove(self,x,y):
        x1, y1 = self.x, self.y
        dopustim = [(x1+2,y1+1),(x1+2,y1-1),(x1-2,y1+1),(x1-2,y1-1),(x1+1,y1+2),(x1-1,y1+2),(x1+1,y1-2),(x1-1,y1-2)]
        if ((x,y) in dopustim) and 0<=x<=self.w and 0<=x<=self.w:
            self.x = x
            self.y = y
        else:
            print('Координаты не верны')