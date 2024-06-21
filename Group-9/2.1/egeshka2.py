# Определите количество четырехзначных чисел, записанных в десятичной системе счисления, 
# в записи которых все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
import itertools
alph = '0123456789'
chet = '02468'
nechet = '13579'
rezult = []
for i in itertools.permutations(alph, 4):
    if i[0] != '0' and (i[0] in chet and i[1] in nechet and i[2] in chet and i[3] in nechet) or (i[0] in nechet and i[1] in chet and i[2] in nechet and i[3] in chet):
        rezult.append(i)
print(len(rezult))

    