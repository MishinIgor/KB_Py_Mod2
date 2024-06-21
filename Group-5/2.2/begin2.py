from allinmatr import *
matr = []
row = 3
column = 3
left = 1
right = 9
for i in range(row):
    matr.append([random.randrange(left,right+1) for t in range(column)])
for i in matr:
    print(*i)
print(*matr[1])
print(matr[2][2])
    