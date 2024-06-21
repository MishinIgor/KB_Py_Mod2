# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
# 1) Строится двоичная запись числа N.
# 2) К этой записи дописываются справа ещё два разряда по следующему правилу:
# а) складываются все цифры двоичной записи числа N, и остаток от деления суммы на 2 дописывается в конец числа (справа). 
# Например, запись 11100 преобразуется в запись 111001;
# б) над этой записью производятся те же действия – справа дописывается остаток от деления суммы её цифр на 2.
# Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N) является двоичной записью искомого числа R.
# Укажите минимальное число R, которое превышает число 83 и может являться результатом работы данного алгоритма. 
# В ответе это число запишите в десятичной системе счисления.
for N in range(1000):
    chislo = bin(N)[2:] # 1011100 - 4
    if chislo.count('1') % 2 == 0:
        chislo += '00'
    else:
        chislo += '10'
    R = int(chislo,2)
    if R > 83:
        print(f'R={R},N={N}')
        break
    
    
    