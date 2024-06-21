import random
def fact(n):
    if n>1:
        return n*fact(n-1)
    if n<=1:
        return 1
def kvur(a,b,c):
    D = b**2 - 4*a*c
    if D<0:
        return 'Нет корректного решения на множестве действительных чисел'
    if D>= 0:
        x = ((-b+D**0.5)/2*a,(-b-D**0.5)/2*a)
        return x
    if D==0:
        x = -b/2*a
        return x
def createspisok(length=5,left=0,right=10):
    return [random.randint(left,right) for i in range(length)]
def creatematr(row,column,type='random',left=0,right=10):
    matr = []
    hleb = '🍔🌭🍕🥪🥙🌮🌯🥐🍞🥖🥨'
    smile = '😀😃😄😁😆😅😂🤣😇🙂🙃😉😌'
    if type == 'random':
        for i in range(row):
            matr.append([random.randrange(left,right+1) for t in range(column)])
    elif type == 'hleb':
        for i in range(row):
            matr.append([random.choice(hleb) for j in range(column)])
    elif type == 'smile':
        for i in range(row):
            matr.append([random.choice(smile) for j in range(column)])
    elif type == 'int':
        for i in range(row):
            matr.append([int(input(f'Введите значение [{i+1},{j+1}]: ')) for j in range(column)])
    elif type == 'float':
        for i in range(row):
            matr.append([float(input(f'Введите значение [{i+1},{j+1}]: ')) for j in range(column)])
    elif type == 'str':
        for i in range(row):
            matr.append([input(f'Введите значение [{i+1},{j+1}]: ') for j in range(column)])
    elif type == 'solo':
        solo = input('Введите элемент которым заполните матрицу: ')
        matr = [[solo]*row for j in range(column)]
    return matr
def printmatr(matr):
    for i in matr:
        print(*i)
