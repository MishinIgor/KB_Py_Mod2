#В файле input.txt дана матрица. Найдите все числа которые повторяются в матрице и запишите их и кол. повторений в output.txt
f = open('input.txt','r')
out = open('output.txt','w',encoding='utf-8')
matr = []
for i in f:
    a = list(map(int,i.split()))
    matr.append(a)
f.close()
analiz = {}
for i in matr:
    for j in i:
        analiz[j] = 0
for i in matr:
    for j in i:
        analiz[j] += 1
print(analiz)
for key,value in analiz.items():
    if value >= 2:
        out.write(f'Число {key} повторилось {value} раз(а)\n')
print(out.closed)
out.close()
