import random
def outmatr(matr): # def NameFunc(arguments)
    for row in matr: 
        print(*row)
    print()

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