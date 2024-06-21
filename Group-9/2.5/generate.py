#Сгенерируйте матрицу и поместите её в файл input.txt
import random
def generate(n):
    matrix = [[str(random.randint(0,9)) for i in range(n)] for i in range(n)]
    with open('input.txt','w') as f:
        for i in matrix:
            for j in i:
                f.write(j)
                f.write(' ')
            f.write('\n')

