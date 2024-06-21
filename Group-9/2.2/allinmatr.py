import random

def generate(row=3,column=3,type='random',element=0):
    matr = []
    if type == 'random':
        for i in range(row):
            matr.append([random.randint(0,10) for j in range(column)])
    elif type == 'int':
        for i in range(row):
            matr.append([int(input(f'Введите [{i+1},{j+1}]: ')) for j in range(column)])
    elif type == 'element':
        for i in range(row):
            matr.append([random.choice(element) for j in range(column)])
    return matr

def out(matr):
    for i in matr:
        print(*i)

def analiz(a):
    t={}
    for i in a:
        for j in i:
            t[j] = 0
    for i in a:
        for j in i:
            t[j] += 1