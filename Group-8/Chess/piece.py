import random
class Piece:
    def __init__(self,color):
        self.color = color
class Knight(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.w = random.randint(0,8)
        self.h = random.randint(0,8)
    def move(self,w,h):
        self.w, self.h = w,h
        