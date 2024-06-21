# В каждой строке электронной таблицы записаны шесть натуральных чисел. 
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
# — в строке встречается ровно четыре различных числа; два из них по два раза,два  — по одному;
# — сумма повторяющихся чисел (без учёта повторений, то есть каждое число входит в сумму один раз) меньше суммы неповторяющихся.
# В ответе запишите число  — количество строк, для которых выполнены эти условия.
schet = 0
for i in open('09.csv'):
    a = list(map(int,i.split(';')))
    analiz = {}
    for i in a:
        analiz[i] = 0
    for i in a:
        analiz[i] += 1
    povtor = []
    nepovtor = []
    for key,value in analiz.items():
        if value==1:
            nepovtor.append(key)
        elif value==2:
            povtor.append(key)
    if len(povtor) == 2 and sum(povtor)<sum(nepovtor):
        schet+=1
print(schet)
     