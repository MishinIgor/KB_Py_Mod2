from utils import randcell
import os
class Helicopter():

    def __init__(self, w, h):
        rc  = randcell(w,h)
        rx,ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lives = 10
        self.mxlives = 10

    def move(self,dx,dy):
        nx, ny = dx + self.x, dy + self.y
        if(nx >=0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny
    

    def print_stats(self): #Функция будет выводить количество воды, жизни
        print('💦 :', self.tank, "/", self.mxtank, sep='', end=' | ')
        print('🏆 :', self.score, end=' | ')
        print('❤️ :', self.lives, "/", self.mxlives, sep='')

    def game_over(self):
        c = '          GAME OVER, YOUR SCORE IS: '+str(self.score)
        os.system("cls")
        print('🥵'*(len(c)-13))
        print('🤜',c,'     🤛')
        print('🤕'*(len(c)-13))
        exit(0)

    def export_data(self):
        return{
            'score': self.score,
            'lives': self.lives, 'mxlives': self.mxlives,
            'x': self.x, 'y': self.y,
            'tank': self.tank, 'mxtank': self.mxtank
        }
    
    def import_data(self,data):
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.tank = data['tank'] or 0
        self.mxtank = data['mxtank'] or 1
        self.lives = data['lives'] or 0
        self.mxlives = data['mxlives'] or 10
        self.score = data['score'] or 0