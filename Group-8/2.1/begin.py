#Вводится десятичное число. Оно переводится в двоичный код. Из числа убирают левую единичку и все нули после неё.
#Например: 100010101 => 10101
#Затем находится десятичная запись результата, и вычисляется разность изначального с результатом.
#Сколько разлинчых записей можно получить если брать числа от 10 до 1000
rezult = set()
for i in range(10,1001):
    chislo = bin(i)[2:]
    #print(chislo)
    schet = 1
    for j in chislo[1:]:
        if j == '0':
            schet += 1
        else:
            break
    chislo = chislo[schet:]
    if not(chislo):
        chislo = '0'
    #print(chislo)
    chislo = int(chislo,2)
    #print(chislo)
    chislo = i - chislo
    rezult.add(chislo)
print(rezult)
print(len(rezult))