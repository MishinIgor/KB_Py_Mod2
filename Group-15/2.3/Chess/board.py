CELL_TYPES = '🟫⬜🦄🐴'
class board:
    def __init__(self,w,h): #w - ширина, h - высота
        self.flag = True
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]
    def createboard(self): 
        flag = True
        for i in range(self.h):
            for j in range(self.w):
                self.cells[i][j] = int(flag)
                flag = not(flag)
            if self.h % 2 == 0:
                flag = not(flag)
    def createpiece(self,x,y,color):
        if self.cells[x][y] == 2:
            print('Победа белых')
            self.flag = False
        elif self.cells[x][y] == 3:
            print('Победа чёрных')
            self.flag = False
        if color == 'white':
            self.cells[x][y] = 2
        if color == 'black':
            self.cells[x][y] = 3
    def outmap(self):
        namepole = '123456789'
        print('   ',end='')
        for n in range(self.w):
            print(namepole[n],end=' ')
        print('   ')
        for i in range(self.h):
            print(i+1,end=' ')
            for j in range(self.w):
                cell = self.cells[i][j]
                print(CELL_TYPES[cell],end='')
            print(' ',i+1)
        print('   ',end='')
        for n in range(self.w):
            print(namepole[n],end=' ')
        print('   ')
    
    