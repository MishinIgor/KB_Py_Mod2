#Число переводится в двоичный код, затем пишется справа на лево. Если число стало начинаться с нуля, нужно добавить 1.
#Затем найти разность начального числа и результата в десятичном виде. Сколько будет результатов равных 0 среди чисел от 8 до 128?
schet = 0
for i in range(8,129):
    chislo = bin(i)[:1:-1]
    if chislo[0] == '0':
        chislo = '1'+chislo
    chislo = int(chislo,2)
    if i-chislo == 0:
        schet += 1
print(schet)
    