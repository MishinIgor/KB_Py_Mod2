from piece import *
CELLS_TYPE = '⬜🟫🦄🐴'

class Board:
    def __init__(self):
        self.w = 8
        self.h = 8
        self.cells = [[0 for i in range(8)] for j in range(8)]
    def createboard(self):
        flag = False
        for i in range(8):
            for j in range(8):
                self.cells[i][j] = int(flag)
                flag = not(flag)
            flag = not(flag)
            
    def outboard(self):
        for i in range(8):
            for j in range(8):
                cell = self.cells[i][j]
                print(CELLS_TYPE[cell],end='')
            print()
    def createpiece(self,w,h):
        self.cells[w][h] = 2
    