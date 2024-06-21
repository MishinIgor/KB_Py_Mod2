import random
def pmatr(matr):
    for i in matr:
        print()
        for j in i:
            print(j,end=' ')
    print()

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
matr = [[1,2,3],[4,5,6],[7,8,9]]
matr2 = mcreate(3,3)
pmatr(matr2)
matr3 = mcreate(3,3)
pmatr(matr3)
delete = matr3[2].pop(1)
matr3[2].insert(1,' ')
print(f'{matr3},Удалено: {delete}')
matr4 = mcreate(3,3,'solo')
pmatr(matr4)
matr5 = mcreate(int(input('row=')),int(input('column=')),input('type='))
pmatr(matr5)