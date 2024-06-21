#В файле input.txt определите, какие числа повторяются. Выведите все повторяющиеся числа в input.txt.
f = open('input.txt','r')
matr = []
for i in f:
    a = list(map(int,i.split()))
    matr.append(a)
print(matr)
f.close()
f = open('output.txt','w')
analiz = {}
for i in matr:
    for j in i:
        analiz[j] = 0
for i in matr:
    for j in i:
        analiz[j] += 1
for key,value in analiz.items():
    if value >= 2:
        f.write(f'{key} - povtor {value} raz(a)\n')
f.close()