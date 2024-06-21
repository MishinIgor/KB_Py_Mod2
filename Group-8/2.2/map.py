from utils import randbool
from utils import randcell
from utils import randcell2

# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-шоп
# 5 - огонь

CELL_TYPES = "🟩🌲🌊🚑🎇🔥"
TREE_BONUS = 200
UPGRADE_COST = 300
LIVE_COST = 100
OVER = 5

class Map:
    
    def __init__(self,w,h): # h - высота, w - ширина
        self.w = w
        self.h = h
        self.cells= [[0 for i in range(w)]for j in range(h)]
        self.generate_forest(3, 10)
        self.generate_rivers(10)
        self.generate_rivers(10)
        self.generate_upgrade_shop()
        self.generate_lives_shop()

    def check_bounds(self,x,y): #Проверка принадлежности клетки полю
        if(x<0 or y<0 or x>= self.h or y>=self.w):
            return False
        return True
    
    def print_map(self, helico, clouds): #Вывод карты
        print('🟥'*(self.w+2))
        for ri in range(self.h):
            print('🟥',end='')
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if(clouds.cells[ri][ci] == 1):
                    print('⚪', end='')
                elif(clouds.cells[ri][ci] == 2):
                    print('🌀', end='')
                elif (helico.x == ri and helico.y == ci):
                    print('🚁', end='')
                elif (cell>=0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end='')
            print('🟥')
        print('🟥'*(self.w+2))

    def generate_forest(self, r, mxr): #Генерирует лес
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r,mxr):
                    self.cells[ri][ci] = 1

    def generate_tree(self): #Генерирует дерево
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx,cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1

    def generate_upgrade_shop(self):#Генерирует магазин апгрейда
        c = randcell(self.w,self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def generate_lives_shop(self):#Генерирует магазин здоровья
        c = randcell(self.w,self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.generate_lives_shop()

    def generate_rivers(self,l): #Генерируют реку
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx,ry)
            rx2, ry2 = rc2[0], rc2[1]
            if(self.check_bounds(rx2,ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l-=1

    def add_fire(self): #Создаёт огонь
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    def update_fires(self,helico): #Обновляет огонь
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
                    if helico.score >= OVER:
                        helico.score -= OVER
        for i in range(10):
            self.add_fire()
    
    def process_helicopter(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]
        if(c == 2):
            helico.tank = helico.mxtank

        if(c == 5 and helico.tank > 0):
            helico.tank -= 1
            helico.score += TREE_BONUS
            self.cells[helico.x][helico.y] = 1

        if(c == 4 and helico.score >= UPGRADE_COST):
            helico.mxtank +=1
            helico.score -= UPGRADE_COST

        if(c == 3 and helico.score >= UPGRADE_COST):
            helico.mxlives += 15
            helico.lives = helico.mxlives
            helico.score -= LIVE_COST

        if(d==2):
            helico.lives -= 1
            if(helico.lives == 0):
                helico.game_over()

    def export_data(self):
        return{'cells': self.cells}
    
    def import_data(self,data):
        self.cells = data['cells'] or [[0 for i in range(self.w)] for j in range(self.h)]