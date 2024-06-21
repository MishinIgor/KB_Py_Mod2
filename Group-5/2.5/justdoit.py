#В файле input.txt дана матрица N x N. Определите сколько и каких чисел повторяется в матрице и выведите их в output.txt
matr = [list(map(int,i.split())) for i in open('input.txt')]
#matr1 = []
# for i in open('input.txt'):
#     a = list(map(int,i.split()))
#     matr1.append(a)
#print(matr1)
analiz = {}
for i in matr:
    for j in i:
        analiz[j] = 0
for i in matr:
    for j in i:
        analiz[j] += 1
f = open('output.txt','w',encoding='utf-8')
for key,value in analiz.items():
    if value >= 2:
        f.write(f'Число {key} было повторно написано в колличестве {value} раз(а)\n')