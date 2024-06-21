#В файле input.txt матрица размером N x N. 
#Выпишите все повторяющиеся числа в матрице, и то сколько раз они повторились в файл output.txt
from generate import generate
generate(7)
matr = [list(map(int,i.split())) for i in open('input.txt')]
analiz = {}
for i in matr:
    for j in i:
        analiz[j] = 0
for i in matr:
    for j in i:
        analiz[j] += 1
f = open('output.txt','w',encoding='utf-8')
for key, value in analiz.items():
    if value >= 2:
        f.write(f'{key} повторено -> {value}')
        f.write('\n')