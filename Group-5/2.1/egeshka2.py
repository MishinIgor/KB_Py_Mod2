# Автомат обрабатывает натуральное число N по следующему алгоритму:
# 1.Строится двоичная запись числа N.
# 2.Запись «переворачивается», то есть читается справа налево. Если при этом появляются ведущие нули, они отбрасываются.
# 3.Полученное число переводится в десятичную запись и выводится на экран.
# Какое наибольшее число, не превышающее 100, после обработки автоматом даёт результат 13?
schet = 0
for N in range(100):
    chislo = bin(N)[:1:-1]
    nechislo = int(chislo,2)
    if nechislo == 13:
        schet += 1
        print(N)
print(schet)