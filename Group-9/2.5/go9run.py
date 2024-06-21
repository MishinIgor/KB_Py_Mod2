# Определите количество строк таблицы, 
# в которых квадрат суммы максимального и минимального чисел в строке больше суммы квадратов трёх оставшихся.
f = open('107_9.csv')
newf = open('107_9_new.csv','w')
schet = 0
rezult = []
for i in f:
    a = list(map(int,i.split(';')))
    a.sort()
    if (a[0]+a[4])**2 > a[1]**2 + a[2]**2 + a[3]**2:
        newf.writelines(i)
        #newf.write('\n')

    
        

    