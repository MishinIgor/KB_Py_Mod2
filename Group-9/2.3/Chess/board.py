import random
CELL_TYPES = '⬜🟫🦄'
class Board:
    def __init__(self,w):
        self.w = w
        self.h = w
        self.cells = [[0 for i in range(w)] for j in range(w)]
        self.createmap()
        
    def createmap(self):
        flag = False
        for i in range(self.h):
            for j in range(self.w):
                self.cells[i][j] = int(flag)
                flag = not(flag)
            if self.w % 2 == 0:
                flag = not(flag)
                
    def createpiece(self,x,y):
        self.cells[x][y] = 2
        
    def outmap(self):
        namepole = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
        for i in range(self.h):
            print(i+1,end=' ')
            for j in range(self.w):
                cell = self.cells[i][j]
                print(CELL_TYPES[cell],end='')
            print()
        print(f'   {namepole[:self.w*2]}   ')
    