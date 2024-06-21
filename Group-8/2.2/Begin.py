import random
def printmatr(matr):
    for i in range(len(matr)):
        print()
        for j in range(len(matr[i])):
            print(matr[i][j],end=' ')
    print()

def creatematr(row,column,type='random',left=0,right=10):
    matr = []
    if type == 'random':
        for mrow in range(row):
            matr.append([random.randrange(left,right) for i in range(column)])
    else:
        if type == 'int':
            for mrow in range(row):
                matr.append([int(input(f'Введие значение[{mrow+1},{i+1}]: ')) for i in range(column)])
        elif type == 'emoji':
            for mrow in range(row):
                matr.append(['🍞' for i in range(column)])
    return matr

matr2 = creatematr(2,2)
printmatr(matr2)
print()
matr4 = creatematr(4,4,'random',3,15)
printmatr(matr4)
print(f"Вторая строка: {matr4[1]}")
print(f'В первой строке, второй элемент: {matr4[0][1]}')