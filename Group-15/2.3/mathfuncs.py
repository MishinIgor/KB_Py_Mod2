import random

def fact(n):
    if n>1:
        return n*fact(n-1)
    if n<=1:
        return 1

def pmatr(matr):
    for i in matr:
       print(*i)

def mcreate(row,column,type='random',left=0,right=10):
    matr = []
    if type == 'random':
        for i in range(row):
            matr.append([random.randrange(left,right) for i in range(column)])
    elif type == 'hleb':
        myhleb = "🍔 🌭 🍕 🥪 🥙 🌮 🌯 🥐 🍞 🥖 🥨".split()
        for i in range(row):
            matr.append([random.choice(myhleb) for i in range(column)])
    elif type == 'int':
        for i in range(row):
            matr.append([int(input(f'Введите [{i+1},{j+1}]: ')) for j in range(column)])
    elif type == 'float':
        for i in range(row):
            matr.append([float(input(f'Введите [{i+1},{j+1}]: ')) for j in range(column)])
    elif type == 'str':
        for i in range(row):
            matr.append([input(f'Введите [{i+1},{j+1}]: ') for j in range(column)])
    elif type == 'solo':
        solo = input('Чем заполним: ')
        matr = [[solo]*column for j in range(row)]
    return matr